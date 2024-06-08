from PyQt5 import QtWidgets
from PyQt5.QtCore import QObject, QThread, pyqtSignal, QTimer


import json
import time

# import hwSetup as hws
# import consoleWidget as cw


from datenerfassung.datamanager import DataManager
import datenerfassung.simulation

class ComBundle(QObject):
    
    """
    Beispiel für HWBundle
    
    Ziel: Gebündelte Organisation aller Hardware-Komponenten, dann nurnoch 1 DataManager im HWSetup
    
    - Einbindung von Sensor / Aktor Bündeln über einzelne Funktion 
    - Sammlung der Bündel in Dict und Ansprache über Bündel-ID

    - HWSetup
    - HWBundle
    - DataManager
    - DataGraphWidget
    - DataTableWidget
    - ConsoleWidget
    - csvDataLogger

    """
    
    TEST_MODE = False    # True setzen, um Verbindungstests zur Hardware zu umgehen
    EMULATION = False    # True setzen, um Virtuelle Daten zum Testen der Anzeige zu generieren
    
    DEFAULT_COM_TAKT = 1000 # [ms]
    
    CONNECT_STATUS_NONE = -1     # Verbindung zu keinem COM-Port aufgebaut
    CONNECT_STATUS_FAILURE = 0   # Verbindugn zu mindestems einem COM-Port erfolgreich
    CONNECT_STATUS_OK = 1        # Verbindungen zu allen Ports hergestellt.
    
    
    _sig_SetupConnect = pyqtSignal()
    _sig_SetupConnectFinished = pyqtSignal(int)

    _sig_pauseMessLoop = pyqtSignal(int)
    _sig_continueMessLoop = pyqtSignal()
    
    _sig_NewData = pyqtSignal(dict)

    _sig_closeConnection = pyqtSignal()
    
    
    def __init__(self, configURL):
        
        self.__configURL = configURL
        
        self._connecting = False
        self.connectStatus = self.HW_CONNECT_STATUS_FAILURE
        
        # Dict mit Infos aus Config File
        self._config = self._load_config()
        
        # Dict mit SerialConnections mit Bezeichner aus Config als Key  
        self._ports = {}
        
        # Datenmanager
        self.dm = dmgr.DataManager(self._config)
        
        # Verbinde Receiver für neue Daten
        self._sig_NewData.connect(self.dm.append_RawData)
        
        
        ##############
        # Messschleife

        self._interval = self.DEFAULT_COM_TAKT
        
        self._threadMessLoop = QThread()
        self._worker = ComSetupUpdateWorker(self, self._interval)
        self._worker.moveToThread(self._threadMessLoop)
        
        self._threadMessLoop.started.connect(self._worker._start_worker)
        self._worker._sig_finished.connect(self._threadMessLoop.quit)
        self._worker._sig_finished.connect(self._worker.deleteLater)
        self._threadMessLoop.finished.connect(self._threadMessLoop.deleteLater)
        
        self._sig_closeConnection.connect(self._worker._stop_worker)
        
        self._sig_pauseMessLoop.connect(self._worker._pause_worker)
        self._sig_continueMessLoop.connect(self._worker._continue_worker)
        
        
        ###################
        # Verbindungsthread
        self.__sct = ComSetupConnectThread(self)
        self._sig_SetupConnect.connect(self.__sct.start)
        
    
        
        

    def __load_config(self):
        """
        Liest Sensor-Konfiguration aus json-File
        """
        # TODO: Ausnahmebehandlung, wenn Config File nicht gefunden wurde oder File ungültiges Format hat!
        
        with open(self.__configURL) as f:
            return json.load(f)


    def _connect_ports(self):
        if(not self._connecting):
            self.__sig_SetupConnect.emit()
            


    def _connect_port(self, name):

        # Suche aktuelles Serial Objekt unter Namen
        ser = None
        connected = False
        if(name in self._ports):
            if("serial" in self._ports[name]):
                ser = self._ports[name]["serial"]
            if("connected" in self._ports[name]):
                connected = self._ports[name]["connected"]
        
        
        # Verbindungsversuch starten    
        try:
            
            if(ser == None or connected == False): 
            
                ser = serial.Serial(
                    port=self._config[name]["port"], 
                    baudrate = self._config[name]["baud"], 
                    parity=serial.PARITY_NONE, 
                    stopbits=serial.STOPBITS_ONE, 
                    bytesize=serial.EIGHTBITS, 
                    timeout=1
                )
                
                self._zuweisen_Port(name, ser)
                
                if(ser != None):
                    print (f"{name} ( {self._config[name]['port']} ) verbunden !")
                    self._ports[name]["connected"] = True
                    return True
        
            else:
                # Verbindung zum Port steht schon und wurde nur überprüft 
                return True
        
        except:
            
            print (f"{name} ( {self._config[name]['port']} ) konnte nicht verbunden werden!")

            if(ser != None):
                ser.close()
            self._ports[name]["serial"] = None
            self._ports[name]["connected"] = False
        
            return False              
        


    def _zuweisen_Port(self, name, portDriver):
        if(not name in self._ports):
            self._ports[name]["serial"] = portDriver  
        else:
            print (f"Fehler bei der Zuweisung des Ports: Port-Name {name} bereits vergeben!")
    
    
    
    def _start_MessSchleife(self):
        if(self.connectStatus == self.CONNECT_STATUS_OK):
            self._threadMessLoop.start()
        else:
            print("Warte auf Verbindung zur Hardware...")
    

    def _read_Messwerte(self):
        
        if(not self.TEST_MODE):
            # Versuche Verbindung neu aufzubauen, wenn Fehler vorliegt:
            if(self.connectStatus != self.CONNECT_STATUS_OK):
                self._connect_ports()
        
        
        if(not self.EMULATION):
        
            if(self.connectStatus == self.CONNECT_STATUS_OK):
                
                # Lese Messwerte aus Ports aus
                disconnectCount = 0
                data = dict()
                for name in self._ports:
                    
                    
                    # Messwerte
                    val = self._ports[p].get_ist()
                    
                    
                    if(val == None):
                        # Fehler beim Auslesen des Messwertes
                        print (name + ": Fehler beim Auslesen des Messwertes: val=" + str(val))
                        self.connectStatus = self.CONNECT_STATUS_FAILURE
                        disconnectCount = disconnectCount + 1
                    elif(val == "BUSY"):
                        # Keine Aktuellen Daten, weil busy!
                        print (name + ": Fehler beim Auslesen des Messwertes: val=" + str(val))
                        data[name] = "BUSY"
                    else: 
                        # Alles OK
                        data[name] = val
                        
                # Überprüfung, ob von allen Ports Daten empfangen wurden
                if (disconnectCount == len(self._ports)):
                    # Von KEINEM Port konnten Messwerte ausgelesen werden
                    print ("Fehler beim Auslesen der Messdaten: data=" + str(data))
                    self.connectStatus = self.CONNECT_STATUS_NONE
                    
                    return None
                
                return data
        
        
        else:
            return self._emulate_Messwerte()
                
        
        return None
    
    
    
    def _emulate_Messwerte(self):
        
        # Generiere Messwerte
        data = dict()
        for p in self._ports:
            data[p] = simulation.sim_flussMessung_sin(self.dm.get_currentTime(), 1, 2, 10)
            
        return data


    def _close_ComSetup(self):
        
        allClosed = False
        
        # Ports schließen
        cnt = 0
        print ("Closing COM Setup ...")
        while(not allClosed and cnt < 10):
            allClosed = True
            for name in self._ports:
                if(not self._close_port(name)):
                    allClosed = False
                    cnt += 1
                    break
            time.sleep(0.1)
            
        # Update Thread beenden    
        self.sig_closeConnection.emit()
        
        self.terminated = True
        print("COM-Setup geschlossen.")




    def _close_port(self, name):
        
        # Suche aktuelles Serial Objekt unter Namen
        ser = None
        connected = False
        if(name in self._ports):
            if("serial" in self._ports[name]):
                ser = self._ports[name]["serial"]
            if("connected" in self._ports[name]):
                connected = self._ports[name]["connected"]
        
        # Schließe Verbindung
        if(ser != None):
            if(ser.is_open):
                ser.close() 
                self._ports[name]["connected"] = False
                print(self.__port + " getrennt")
                
        return True
    
    
    
    
    # Zurücksetzen der Aufzeichnungen
    
    def reset(self):
        self.dm.reset()
        
        
    
    # Aufzeichnung von Messdaten

    def start_recordData(self):
        """
        Startet das externe Aufzeichnen von Messdaten in einer Log-Datei über den DataManager
        """
        
        self.dm.start_recordData()
                
    def stop_recordData(self):
        """
        Stoppt das externe Aufzeichnen von Messdaten in einer Log-Datei über den DataManager
        """
        
        self.dm.stop_recordData()

    
###########################################################################################################
# 
# Helferklassen           

class ComSetupUpdateWorker(QObject):
    """
    Enthält den Haupttask zum Update der Messungen
    """
    _sig_finished = pyqtSignal()
    _sig_progress = pyqtSignal(int)
    
    sig_paused_for = pyqtSignal(int)
    
    def __init__(self, setup, interval):
        super(ComSetupUpdateWorker, self).__init__()
        self.s = setup
        self._interval = interval
        self._readingData = False
        self._timer = QTimer()
        
        self._paused = False
        
        self._currentComTakt = -1
        
        
    def _start_worker(self):
        self._start_timer()
        

    def _pause_worker(self, forID=0):
        self._timer.stop()
        self._set_paused(True)
        
        self.sig_paused_for.emit(forID)
        
        
    def _continue_worker(self):
        self._start_timer()
        self._set_paused(False)
        

    def _stop_worker(self):
        self._timer.stop()
        self._sig_finished.emit()
        
        
    def _set_interval(self, interval):
        self._timer.disconnect()
        self._interval = interval
        
        
    def _start_timer(self):
        self._timer = QTimer()
        self._timer.setInterval(self._interval)
        self._timer.timeout.connect(self._executeComTakt)
        self._timer.start()
        
        
    def _set_paused(self, paused):
        self._paused = int(paused)


    def _executeComTakt(self):
        self._currentComTakt += 1
        if(self._currentComTakt == 0):
            self.updateData()
            
        self._currentComTakt = self._currentComTakt % 1

                

    def _dataUpdate(self):
        """
        Wenn Sensor vorhanden, wird Messung getriggert und Daten aktualisiert.
        """
        
        # Trigger Messung nur, wenn nicht gerade schon Messung läuft und HW nicht im Testmode ist.          
        if(not self._readingData):
                
            self._readingData = True		
            
            # Triggert Auslesen der Messwerte
            data = self.s._read_Messwerte()
    
            if(data != None):
                # Messung abgeschlossen
                self._readingData = False
                # Mappen der Daten auf Kanäle
                self.s._sig_NewData.emit(data)

            else:
                print ("Data Update: Fehler beim Auslesen der Messungen!")
                self._readingData = False

    
###############################################################################################    
    
class ComSetupConnectThread(QThread):
    
    _sig_finished = pyqtSignal()
    
    def __init__(self, setup: ComBundle):
        QThread.__init__(self)
        self.s = setup
        
    def run(self):
                
        lastStatus = self.s.connectStatus
                
        if(not self.s._connecting):
        
            print ("Verbinde Sesorik ...")
    
            self.s._connecting = True
                
            status = -1
            connected = 0
            self.s.connectStatus = ComSetup.CONNECT_STATUS_NONE # Noch kein COM-Port wurde verbunden
            for name in self.s._config:
                if(self.s._connect_port(name)):
                    connected += 1
                    self.s.connectStatus = ComSetup.CONNECT_STATUS_FAILURE # Zumindest 1 COM-Port wurde verbunden
            if(connected == len(self.s._config)):
                self.s.connectStatus = ComSetup.CONNECT_STATUS_OK # Alle COM-Ports wurden verbunden
                status = 1

            self.s._connecting = False
            
            if(self.s.connectStatus != lastStatus):
                self.s._sig_SetupConnectFinished.emit(status)
            
            # Neuen Verbindungsversuch starten, wenn vorheriger fehlschlägt
            if(status != 1):
                self.s._sig_HWSetupConnect.emit()