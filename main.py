import sys

from PyQt5.QtGui import QSurfaceFormat 
from PyQt5.QtWidgets import QApplication

import mainFrame.mainFrame as mf


if __name__ == "__main__":

    # Starten der GUI Anwendung

    print ("Starte Anwendung ...")

    app = QApplication(sys.argv)

    # Render Format
    format = QSurfaceFormat()
    format.setDepthBufferSize(24)
    format.setStencilBufferSize(8)
    format.setVersion(3, 2)
    format.setProfile(QSurfaceFormat.CoreProfile)
    QSurfaceFormat.setDefaultFormat(format)


    # Init MainFrame
    window = mf.MainFrame()
    window.show()

    app.exec()


    # TODO: Single Open
    # TODO: Crash abfangen