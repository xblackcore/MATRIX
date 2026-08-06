#!/usr/bin/env python
#┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
#region    [M] Meta-Logic                                  ┃
    #┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    #region    ["""__doc__"""]                                 ┃
"""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# []
\n┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
## []
\n┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
"""
    #endregion ["""__doc__"""]                                 ┃
    #┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
    #┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    #region    [import]                                        ┃
        #┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        #region    [from Python import *]                          ┃
        #endregion [from Python import *]                          ┃
        #┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        #┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        #region    [from . import *]                               ┃
from XPRINT import Error, Print, Box
        #endregion [from . import *]                               ┃
        #┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
    #endregion [import]                                        ┃
    #┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
#endregion [M] Meta-Logic                                  ┃
#┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
#┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
#region    [XPY_]                                          ┃
class XPY_:
    #┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    #region    [__init__()] 								   ┃
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
    #endregion [__init__()] 								   ┃
    #┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
    #┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    #region    [Say()] 		    							   ┃
    def Say(self, I):
        print(f"\033[96m[XPY]\033[0m {I}")
    #endregion [Say()] 		    							   ┃
    #┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
    #┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    #region    [X()] 										   ┃
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
    #endregion [X()] 										   ┃
    #┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
#endregion [XPY_]                                          ┃
#┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛