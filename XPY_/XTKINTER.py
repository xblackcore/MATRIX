#┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
#region    [import]                                        ┃
#	┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
#	region    [from Python import *]                          ┃
import tkinter as tk
from tkinter import filedialog, simpledialog
#	endregion [from Python import *]                          ┃
#	┣━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━┫
#	region    [from MATRIX import *]                          ┃

#	endregion [from MATRIX import *]                          ┃
#	┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
#endregion [import]                                        ┃
#┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
#┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
#region    [AskDirectory()] 							   ┃
def FileDialogAskDirectory():
    """
        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        # [FileDialogAskDirectory()]
        ## Opens a dialog box for the user to select a directory
        \n┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
        ## [O]
         - Open a dialog box
        ## [->]
         - If X = FileDialogAskDirectory(), X == '*Absolute Path'|
        \n┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
        ## [+]
         - tkinter
        \n┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
        ## [!]
         - |
        \n┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
        ## [?]
         - |
        \n┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
        ## [>]
            ```python
                Tk = tk.Tk()
                Tk.withdraw()
                Directory = filedialog.askdirectory()
                return(Directory)
            ```
        \n┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
    """
    Tk = tk.Tk()
    Tk.withdraw()
    Directory = filedialog.askdirectory()
    return(Directory)
#endregion [AskDirectory()] 							   ┃
#┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
#┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
#region    [AskOpenFile()] 								   ┃
def AskOpenFile():
    filedialog.askopenfile()
#endregion [AskOpenFile()] 								   ┃
#┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛