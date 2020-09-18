# ================================================================================
# = Main                                                                         =
# = ---------------------------------------------------------------------------- =
# = Written By: Joseph Bourque     Last Updated By: Joseph Bourque               =
# = Completed On: ----/--/--                                                     =
# = Last Updated: ----/--/--                                                     =
# = ---------------------------------------------------------------------------- =
# = description:                                                                 =
# = Driver file, works similar to C++ main file. Use this to run the program     =
# ================================================================================
# imports:
from __future__ import print_function, division # Backward compatibility
from obj_classes.ui import TerrainUI
from obj_classes.color import Color
from PyQt5 import QtWidgets

# Create a new pyqt application
app = QtWidgets.QApplication([])

# Create a new UI
ui = TerrainUI()

# Create objects here
# NOTE: This area is mainly for testing; when the real application is created
#       these will be created in the ui object itself
cylinder = ui.geometry.createCylinder()

# Start the application
ui.Start()
app.exec_()