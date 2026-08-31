#!/usr/bin/env python
#┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
#region    [M]  										   ┃
# __doc__
"""
    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    # []
    ##
    \n┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
    ## [I]
    - |
    ## [X]
    - |
    \n┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
    ## [*]
    - |
    ## [**]
    - |
    \n┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
    ## [O]
    - |
    ## [->]
    - |
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
PROPIETY: str = "BlackCore"
# import
import sys, traceback, linecache, os
import inspect
from XSHUTIL import GetTerminalSizeColumns
import XOS as XOS
#endregion [M]  										   ┃
#┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
#┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
#┃ [DeleteBackLine()] 									   ┃

#┃ [DeleteBackLine()] 									   ┃
#┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
#┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
#┃ [Print(*X)] 											   ┃
def Print(*X):
    """
        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        # [ Print(*X) ] META of print()
        Receives ***X** as a binary set  **('Text to print', 'Style; if None = Default')**\n
        of the input to be processed and the process to be applied.
      \n┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
        ## [*]
         - *X = ("A", "B")
         - *X = ( A , "B")
         - *X = ( A , "B", C, "B"...)
             - A, C: Text or variable to print
             - B: Style or mod to apply for A, C
             - If (A), or (A, None),
      \n┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
        ## [->]
         > Print("A", "red")
         >> *Print red color 'A'
         > Print("A", "bold")
         >> *Print bold 'A'
      \n┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
        ## [!]
         -
         - No spaces were assumed between odd-numbered entries; if ("Text", None, "Text"), print TextText, a space must be inserted in one of the two odd-numbered entries.
      \n┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
        ## [?]
        Valid 2ºn inputs (XN2) = {
        \n
        - Text string
        - 'DeleteBackLine' for delete the backline
        ---
        Valid 2ºn inputs (XN2) =
        \n
        - White
            - WhiteBright
            - WhiteBackground
        - Black
            - BlackBackground
        - Gray
        - Grey
        - Red
            - RedBright
            - RedBackground
        - Green
            - GreenBright
            - GreenBackground
        - Yellow
            - YellowBright
            - YellowBackground
        - Blue
            - BlueBright
            - BlueBackground
        - Magenta
            - MagentaBright
            - MagentaBackground
        - Cyan
            - CyanBright
            - CyanBackground
        - Bold
        - Dim
        - Italic
        - Underline
        - Blink
        - Reverse
        - Hidden
        - Strike
      \n┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
        ## [>]
      \n\t┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        \t Print("Text")
        \t >> Text
        \n\t┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
        \t A = 1
        \t Print(A)
        \t >> 1
        \n\t┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
        \t Print("Normal", None, "Red", "red", "Normal", None)
        \t >> Normal A:Red Normal
        \n┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
    """
    if len(X) == 1:
        if X == "DelateBackLine":
            print("\033[1A\033[2K", end="")
        else:
            print(X[0])
            return
    else:
        CODES = {
            "Black": "\033[30m",
            "Red": "\033[31m",
            "Green": "\033[32m",
            "Yellow": "\033[33m",
            "Blue": "\033[34m",
            "Magenta": "\033[35m",
            "Cyan": "\033[36m",
            "White": "\033[37m",
            "Gray": "\033[90m",
            "Grey": "\033[90m",
            "RedBright": "\033[91m",
            "GreenBright": "\033[92m",
            "YellowBright": "\033[93m",
            "BlueBright": "\033[94m",
            "MagentaBright": "\033[95m",
            "CyanBright": "\033[96m",
            "WhiteBright": "\033[97m",
            "BlackBackground": "\033[40m",
            "RedBackground": "\033[41m",
            "GreenBackground": "\033[42m",
            "YellowBackground": "\033[43m",
            "BlueBackground": "\033[44m",
            "MagentaBackground": "\033[45m",
            "CyanBackground": "\033[46m",
            "WhiteBackground": "\033[47m",
            "Bold": "\033[1m",
            "Dim": "\033[2m",
            "Italic": "\033[3m",
            "Underline": "\033[4m",
            "Blink": "\033[5m",
            "Reverse": "\033[7m",
            "Hidden": "\033[8m",
            "Strike": "\033[9m",
        }
        RESET = "\033[0m"

        Dict  = []
        for N in range(0, len(X), 2):
            XN   = X[N]
            XN1  = X[N + 1] if N + 1 < len(X) else None
            Str  = str(XN)
            Code = CODES.get(XN1) if XN1 else None
            Dict.append(
                f"{Code}{Str}{RESET}" if Code else Str
            )
        print("".join(Dict))
#┃ [Print(*X)] 											   ┃
#┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
box




def DeleteBackLine(End = True):
    """
        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        # [DeleteBackLine(End = True)]
        ## Delete last line in terminal
        \n┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
        ## [X]
         - End = True | Add 'end=""' to command
        \n┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
        ## [O]
         - Delete last line in terminal
        \n┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
        ## [!]
         - Use default print becouse is incompatible with META-Print
        \n┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
        ## [?]
         - |
        \n┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
        ## [>]
        ```python
            if End:
                print("\033[1A\033[2K", end="")
            else:
                print("\033[1A\033[2K")
        ```
        \n┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
    """
    if End:
        print("\033[1A\033[2K", end="")
    else:
        print("\033[1A\033[2K")
def Ok(Text=None, Color="Gray", FBack=2):
    """
        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        # [Ok()]
        ## Print the caller location as:
         - [File/Function/Line] Text
        ---
        The location block can be colorized using the
        META-PRINT color system.
        \n┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
        ## [I]
         - Text   = None | Accompanying text of the []
         - Color  = "Gray" | Color of []. Anherited from the meta-print, execute Print() to see more.
         - FBack  = 2 |
        \n┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
        ## [O]
         -
        \n┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
        ## [+]
         - XPRINT.Print()
         - XINSPECT.Frame()
        \n┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
        ## [!]
         - |
        \n┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
        ## [?]
         - |
        \n┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
        ## [>]
         - |
        ```python
            Frame2 = Frame(2)
            while Frame2:
                File = os.path.basename(Frame2.f_code.co_filename)
                if File != "XINSPECT.py":
                    File      = File
                    Function  = Frame2.f_code.co_name
                    Line      = Frame2.f_lineno
                    break
                Frame2 = Frame2.f_back
            else:
                File = "?"
                Function = "?"
                Line = 0
            if Text and Color:
                Print(f"[{File}/{Function}/{Line}]", Color, f" {Text}")
            elif Text and not Color:
                Print(f"[{File}/{Function}/{Line}] {Text}")
            elif Color and not Text:
                Print(f"[{File}/{Function}/{Line}]", Color)
            else:
                Print(f"[{File}/{Function}/{Line}]")
        ```
        \n┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
    """

    from XINSPECT import Frame
    Frame2 = Frame(FBack)

    while Frame2:
        File = os.path.basename(Frame2.f_code.co_filename)
        if File != "XINSPECT.py":
            File      = File
            Function  = Frame2.f_code.co_name
            Line      = Frame2.f_lineno
            break
        Frame2 = Frame2.f_back

    else:
        File = "?"
        Function = "?"
        Line = 0

    if Text and Color:
        Print(f"[{File}/{Function}/{Line}]", Color, f" {Text}")
    elif Text and not Color:
        Print(f"[{File}/{Function}/{Line}] {Text}")
    elif Color and not Text:
        Print(f"[{File}/{Function}/{Line}]", Color)
    else:
        Print(f"[{File}/{Function}/{Line}]")
def Error(I = None):
    Print(I if I else "Error", "Red")
def Box(
    Section = 0,
    Type = "Heavy",
    Style = "White",
    Width = 60,
    Title = "",
    SubTitle = "",
    Ident = 0
):
    """
        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        # [Box()]
        ##
        \n┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
        ## [I]
         - |
        ## [X]
         - |
        \n┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
        ## [*]
         - |
        ## [**]
         - |
        \n┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
        ## [O]
         - |
        ## [->]
         - |
        \n┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
        ## [+]
         - |
        \n┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
        ## [!]
         - |
        \n┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
        ## [?]
         - Valid codes:

        \n┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
        ## [>]
         - |
        \n┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
    """
    #┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    #region    [Type == "heavy"] 							   ┃
    if Type.lower() == "heavy":
        #      0   1   2   3   4   5   6   7   8
        CH = ["┏","┓","━","┃","┗","┛","┣","┫"," "]

    LenTitle = len(Title) + 2
    LenSubTitle = len(SubTitle)
    #endregion [Type == "heavy"] 							   ┃
    #┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
    #┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    #region    [(LenTitle + LenSubTitle) > Width] 			   ┃
    if LenTitle + LenSubTitle > Width:
        Subtitle = ""
        LenSubTitle = 0
    #endregion [(LenTitle + LenSubTitle) > Width] 			   ┃
    #┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
    #┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    #region    [LN = X] 									   ┃
    Ident = Ident * 4
    # ┏━━━━━━━━━━━━━━━━━━┓
    L0 = CH[8] * Ident + CH[0] + CH[2] * (Width - 2) + CH[1]
    # ┃ [Title] Subtitle ┃
    L1 = CH[8] * Ident + CH[3] + f" [{Title}]" + f" {SubTitle}" + CH[8] * (Width-4-(LenTitle + LenSubTitle)) + CH[3]
    # ┃ [Title]     	 ┃
    L2 = CH[8] * Ident + CH[3] + f" [{Title}]" + CH[8] * (Width-3-LenTitle) + CH[3]
    # ┃ Subtitle         ┃
    L3 = CH[8] * Ident + CH[3] + f" {SubTitle}" + CH[8] * (Width-3-LenSubTitle) + CH[3]
    # ┃				     ┃
    L4 = CH[8] * Ident + CH[3] + CH[8] * (Width - 2) + CH[3]
    # ┣━━━━━━━━━━━━━━━━━━┫
    L5 = CH[8] * Ident + CH[6] + CH[2] * (Width - 2) + CH[7]
    # ┗━━━━━━━━━━━━━━━━━━┛
    L6 = CH[8] * Ident + CH[4] + CH[2] * (Width - 2) + CH[5]
    #endregion [LN = X] 									   ┃
    #┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
    #┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    #region    [if Title AND/OR SubTitle: LX = LN] 			   ┃
    if Title and SubTitle:
        LX = L1
    elif Title:
        LX = L2
    elif SubTitle:
        LX = L3
    else:
        LX = L4
    #endregion [if Title AND/OR SubTitle: LX = LN] 			   ┃
    #┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
    #┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    #region    [Section == N] 								   ┃
    if Section == 0:
        Print(L0, Style)
        Print(LX, Style)
    elif Section == 1:
        Print(L4, Style)
        Print(L5, Style)
        Print(LX, Style)
    elif Section == 2:
        Print(LX, Style)
        Print(L6, Style)
    #endregion [Section == N] 								   ┃
    #┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

#┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
#┃ [.U] 												   ┃
"""

"""
#┃ [.U] 												   ┃
#┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛