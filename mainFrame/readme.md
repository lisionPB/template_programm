# MainFrame Template

## Kernklassen

### Main
* Initialisiert und hält MainFrame

### MainFrame
* Initialisiert ViewLayerManager
* Initialisiert ViewContainer
* Setzt ViewContainer als zentrales Widget von MainFrame
* Übergibt ViewContainer dem ViewLayerManager
* Übergibt KeyEvents dem ViewLayerManager

### ViewLayerManager (Template)
* Initialisiert die Views als Implementierung von Screen
* Fügt Views dem ViewContainer hinzu
* Verbindet Signale von Views

### ViewContainer
* Verwaltet die Views in dict `viewStructure`
* Hinzufügen neuer Views über `add_view(viewID, view: Screen)`
* Setzen der aktuellen View über `set_currentView(viewID)` 
* Inaktive Views werden unsichtbar gemacht
* Bei Aktivierung einer View wird `on_setActive()` aufgerufen
* Bei Deaktivierung einer View wird `on_setInactive()` aufgerufen

### Screen
* Interface für Views
* `on_setActive()` wird bei Aktivierung der View aufgerufen
* `on_setInactive()` wird bei Deaktivierung der View aufgerufen


### Process
* Implementiert Thread
* Mit `runProcess()` process starten  

<br>

# Spiel Template

## Screens

### Screen Classes

#### ScreenCredits

#### ScreenInit
#### ScreenIntro
#### ScreenLoad
#### ScreenMenu
#### ScreenPause
#### Screen Play

