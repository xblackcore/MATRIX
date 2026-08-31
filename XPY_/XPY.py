#!/usr/bin/env python
#┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
#region    [M]  										   ┃
# __doc__
"""
    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    # [XPY.py]
    ## META-Python main entry point
    \n┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
    ## [+]
    - |
    \n┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
    ## [!]
    - |
    \n┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
    ## [?]
    - |
    \n┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
    ## [>]
    - |
    \n┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
"""
# __author__
__author__ = "Sir. Doyle; S.Class Astartes at BlackCoreΔ"
# __version__
__version__ = "1.0"
# __annotations__
DEBUG: bool = False
# import
try: from XPRINT import Error, Print, Box
except ImportError as E:
    print(f"\033[91m┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\033[0m")
    print(f"\033[91m[{__file__[0].upper() + __file__[1:]}] ImportError:{E}\033[0m")
    print(f"\033[91m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\033[0m")
#endregion [M]  										   ┃
#┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
#┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
#region    [D] 											   ┃
class D_:
    ...
def D():
    ...
#endregion [D] 											   ┃
#┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
#┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
#region    [B] 											   ┃
class B_:
    ...
def B():
    ...
#endregion [B] 											   ┃
#┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
#┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
#region    [F] 											   ┃
class F_:
    ...
def F():
    ...
#endregion [F] 											   ┃
#┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
#┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
#region    [X] 											   ┃
#endregion [X] 											   ┃
#┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
#┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
#┃ [.U] 												   ┃
"""
class XPY_:
    def __init__(self,
        Debug         = False,
        BoxStyle      = "Cyan",
        BoxTextStyle  = "White",
        XPYTextStyle  = "White",
        BoxTitle      = __file__
    ):
        self.Debug         = Debug

        self.BoxStyle      = BoxStyle
        self.BoxTextStyle  = BoxTextStyle
        self.BoxTitle      = BoxTitle

        self.XPYTextStyle  = XPYTextStyle
        self._CallsStack   = 0
    def Say(self, I):
        print(f"\033[96m[XPY]\033[0m {I}")
    def X(self,
        I,
        Sub = None,
        End = None
    ):
        if self._CallsStack == 0: # I == Main
            Box(
                Title = self.BoxTitle,
                Style = self.BoxStyle)

        elif self._CallsStack >= 1:
            Box(Style = self.BoxStyle, Section=1)

        if callable(I):
            self.Say(f"callable({I})")
            self._CallsStack +=1
            self.Say(f"_CallsStack = {self._CallsStack}")
            self.Say(f"try: {I}()")
            I()

"""
#┃ [.U] 												   ┃
#┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛