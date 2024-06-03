from PyQt5.QtCore import QTimer

from PyQt5.QtWidgets import QGraphicsView, QOpenGLWidget
from PyQt5.QtGui import QSurfaceFormat


from mainFrame.sceneGameGraphics import SceneGameGraphics

class WeltGraphicsViewWidget(QGraphicsView):

    def __init__(self) -> None:
        super().__init__()

        # GraphicsScene
        self.wgs = SceneGameGraphics()
        self.setScene(self.wgs)

        #self.setFixedSize(1000, 600)

        # OPEN GL Widget
        self.oglw = QOpenGLWidget()
        
        sf = QSurfaceFormat()
        sf.setSamples(1)
        sf.setSwapInterval(1)
        self.oglw.setFormat(sf)
        self.setViewport(self.oglw)

        # self.setTransformationAnchor(QGraphicsView.NoAnchor)
        self.setViewportUpdateMode(1)

        # self.centerOn(self.wgs.centerItem())

        self.lastUpdate = 0






    def init_updateRoutine(self):
        """
        Initialisierung durch Main
        """
        self.updateTimer = QTimer()
        self.updateTimer.setTimerType(Qt.PreciseTimer)
        self.updateTimer.setInterval(0) # Wird durch vsync gesteuert
        self.updateTimer.timeout.connect(self.vlm.update_vlm, Qt.DirectConnection)
        self.updateTimer.timeout.connect(self.m.update_model)

        # StartUp Finished -> Start UpdateTimer
        if(CONTINOUS_UPDATE):
            window.init_updateRoutine()
            window.start_updateRoutine()


    def start_updateRoutine(self):
        """
        Start durch Main
        """
        self.updateTimer.start()


    def update_graphicsView(self):  
        self.wgs.update_graphicsScene()
        # self.centerOn(self.wgs.centerItem())

        # Update GL
        # self.oglw.update()