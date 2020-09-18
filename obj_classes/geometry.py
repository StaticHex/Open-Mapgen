# ================================================================================
# = Geometry Class                                                               =
# = ---------------------------------------------------------------------------- =
# = Written By: Joseph Bourque     Last Updated By: Joseph Bourque               =
# = Completed On: ----/--/--                                                     =
# = Last Updated: ----/--/--                                                     =
# = ---------------------------------------------------------------------------- =
# = description:                                                                 =
# = Used to create the visual vtk components i.e. meshes, mappers, and actors    =
# ================================================================================
# imports:
from   __future__        import print_function, division # Backwards compatibility
from   obj_classes.color import Color
import vtk

class Geometry:
    # ============================================================================
    # = Constructor                                                              =
    # = ------------------------------------------------------------------------ =
    # = description:                                                             =
    # = Used to construct a new geometry object with the passed in background    =
    # = color                                                                    =
    # ============================================================================
    def __init__(
        self,         # (Ref) Reference to class, required by all members
        col = Color() # (Color) A color object to set the background color to
    ):
        # Create new renderer
        self.renderer = vtk.vtkRenderer()

        # Add background color to color list
        self.__colors = vtk.vtkNamedColors()
        self.__colors.SetColor("SceneColor", *col.normalize())

        # Set renderer window background to our color
        self.renderer.SetBackground(self.__colors.GetColor3d("SceneColor"))

    # ============================================================================
    # = Create Cylinder                                                          =
    # = ------------------------------------------------------------------------ =
    # = description:                                                             =
    # = Creates a new cylinder and addes it to the renderer                      =
    # = ------------------------------------------------------------------------ =
    # = return:                                                                  =
    # = (vtkActor) An actor holding the mapping data for the newly created       =
    # = cylinder.                                                                =
    # ============================================================================    
    def createCylinder(
        self,               # (Ref) Reference to class, required by all members

        color = "Tomato",   # (String) The name of a previously added color

        resolution = 8,     # (Int) The number of vertices to use to create the
                            # face of the cylinder, more vertices equal a
                            # smoother appearance

        position = (0,0,0), # (Tuple) the xyz coordinates of the object in the
                            # scene

        rotation = (0,0,0)  # (Tuple) A rotation to apply to the object
    ):
        # Create a new cylinder mesh
        mesh  = vtk.vtkCylinderSource()
        mesh.SetResolution(resolution)
        mesh.SetCenter(*position)

        # Create a new data mapper out of the mesh
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(mesh.GetOutputPort())

        # Create a new actor from our mapper
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)
        actor.GetProperty().SetColor(self.__colors.GetColor3d(color))
        actor.RotateX(rotation[0])
        actor.RotateY(rotation[1])
        actor.RotateZ(rotation[2])

        # Add the actor to our scene and return a reference
        self.renderer.AddActor(actor)
        return actor

