# ================================================================================
# = Terrain User Interface Class                                                 =
# = ---------------------------------------------------------------------------- =
# = Written By: Joseph Bourque     Last Updated By: Joseph Bourque               =
# = Completed On: ----/--/--                                                     =
# = Last Updated: ----/--/--                                                     =
# = ---------------------------------------------------------------------------- =
# = description:                                                                 =
# = Used to create and manage the user interface components of the terrain       =
# = generator.                                                                   =
# ================================================================================
# imports:
from __future__                        import print_function, division
from PyQt5                             import QtCore, QtGui, Qt
from obj_classes.color                 import Color
from obj_classes.geometry              import Geometry
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

class TerrainUI(Qt.QMainWindow):
    # ============================================================================
    # = Constructor                                                              =
    # = ------------------------------------------------------------------------ =
    # = description:                                                             =
    # = Creates a new UI instance.                                               =
    # ============================================================================
    def __init__(
        self,             # (Ref) Reference to class, required by all members
        col    = Color(), # (Color) the color to set the vtk window background as
        parent = None     # (Ref) Reference to container object this object
                          # belongs to
    ):
        Qt.QMainWindow.__init__(self, parent)
        # Set window size and title
        self.resize(800,600)
        self.setWindowTitle("Open MapGen")

        # Create the embedded window
        self.__frame = Qt.QFrame()
        self.__layout = Qt.QHBoxLayout()
        self.__frame.setLayout(self.__layout)
        self.setCentralWidget(self.__frame)
        self.__interactor = QVTKRenderWindowInteractor(self.__frame)
        self.__interactor.Initialize()
        self.__layout.addWidget(self.__interactor)

        self.geometry = Geometry(col)

        self.__interactor.GetRenderWindow().AddRenderer(self.geometry.renderer)
        self.__iren = self.__interactor.GetRenderWindow().GetInteractor()

    # ============================================================================
    # = Start Method                                                             =
    # = ------------------------------------------------------------------------ =
    # = description:                                                             =
    # = Used to make the window visible to the user and start the graphics       =
    # = component rendering                                                      =
    # ============================================================================
    def Start(
        self
    ):
        self.show()
        self.__iren.Initialize()
        self.geometry.renderer.ResetCamera()
        self.geometry.renderer.GetActiveCamera().Zoom(1.5)
        self.__iren.Render()
        self.__iren.Start()
