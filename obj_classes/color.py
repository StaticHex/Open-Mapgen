# ================================================================================
# = Color Class                                                                  =
# = ---------------------------------------------------------------------------- =
# = Written By: Joseph Bourque     Last Updated By: Joseph Bourque               =
# = Completed On: 2020/09/18                                                     =
# = Last Updated: 2020/09/18                                                     =
# = ---------------------------------------------------------------------------- =
# = description:                                                                 =
# = Used to manage colors for the geometry class. Handles rgba color values as   =
# = well as web colors                                                           =
# ================================================================================
class Color:
    # ============================================================================
    # = Constructor                                                              =
    # = ------------------------------------------------------------------------ =
    # = description:                                                             =
    # = Used to construct a new color object from either rgba values or using a  =
    # = web color. It should be noted that alpha is 255 or fully opaque by       =
    # = default                                                                  =
    # ============================================================================
    def __init__(
        self,        # (Ref) Reference to class, required by all members
        web   = 0x0, # (Ord) A hex value in the format 0xRRGGBB or 0xRRGGBBAA
        red   = 0,   # (Int) The red channel for the color
        green = 0,   # (Int) The green channel for the color
        blue  = 0,   # (Int) The blue channel for the color
        alpha = 255  # (Int) The alpha (transparency) channel for the color

    ):
        # Initialize internal members using default values first
        self.red   = red
        self.blue  = blue
        self.green = green
        self.alpha = alpha

        # if we have a web color, convert it to rgba values and store
        if web > 0x0:
            # This is the max value without alpha; if our number is greater than
            # this it means we're using an alpha channel
            if web > 0xFFFFFF:
                self.alpha = (255 & web)
                web = (web >> 8)
            self.blue =  (255 & web)
            web = (web >> 8)
            self.green =  (255 & web)
            web = (web >> 8)
            self.red = web

    # ============================================================================
    # = To List                                                                  =
    # = ------------------------------------------------------------------------ =
    # = description:                                                             =
    # = Flattens class into a standard python list                               =
    # = ------------------------------------------------------------------------ =
    # = return:                                                                  =
    # = (List<Int>) Class contents as a python list in the format [r, g, b, a]   =
    # ============================================================================
    def toArray(
        self,          # (Ref) Reference to class, required by all members
        alphaOn = True # (Bool) Whether to return alpha channel or not
    ):
        col = [self.red, self.green, self.blue ]
        if alphaOn:
            col.append(self.alpha)
        return col

    # ============================================================================
    # = To List                                                                  =
    # = ------------------------------------------------------------------------ =
    # = description:                                                             =
    # = Flattens class into a standard python list with values scaled betwen 0.0 =
    # = and 1.0                                                                  =
    # = ------------------------------------------------------------------------ =
    # = return:                                                                  =
    # = (List<Float>) Class contents as a python list in the format [r, g, b, a] =
    # ============================================================================
    def normalize(
        self,          # (Ref) Reference to class, required by all members
        alphaOn = True # (Bool) Whether to return alpha channel or not
    ):
        return [ round( x / 255 * 100) / 100 for x in self.toArray(alphaOn) ]
        

    # ============================================================================
    # = String Convert Override                                                  =
    # = ------------------------------------------------------------------------ =
    # = description:                                                             =
    # = Handles how to display the color when it's converted to a string         =
    # = ------------------------------------------------------------------------ =
    # = return:                                                                  =
    # = (String) Class members r, g, b, and a as a string                        =
    # ============================================================================
    def __str__(
        self # (Ref) Reference to class, required by all members
    ):
        return f"(R: {self.red}, G: {self.green}, B: {self.blue}, A:{self.alpha})"
        