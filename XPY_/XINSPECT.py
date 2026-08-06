#┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
#region    [import]                                        ┃
#	┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
#	region    [from Python import *]                          ┃
import inspect, os
#	endregion [from Python import *]                          ┃
#	┣━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━┫
#	region    [from MATRIX import *]                          ┃

#	endregion [from MATRIX import *]                          ┃
#	┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
#endregion [import]                                        ┃
#┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
#┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
#region    [Frame()] 	        						   ┃
def Frame(
    FBack = 0,
    IfFrameIsNoneReturn = None
):
    """
        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        # [Frame()]
            > FBack = 0,
            > IfFrameIsNoneReturn = None
        ## Returns the caller's frame, or the value of 'IfFrameIsNoneReturn' (default: None) if no frame is available.
        \n┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
        ## [X]
         - FBack = 0 | Number of stack frames to go back
            - 0 = A, caller of CurrentFrame()
            - 1 = B, caller of A
            - 2 = C, caller of B
            - ...
         - IfFrameIsNoneReturn = None | Whats return if Frame is None
        \n┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
        ## [->]
         - Frame: <frame at 0x0000000000000000, file 'A:\\X\\Y.*', line *Z*, code CurrentFrame>
        \n┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
        ## [+]
         - import inspect
        \n┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
        ## [>]
        ```python
            Frame = inspect.currentframe()
            for _ in range(FBack):
                if Frame is None:
                    return IfFrameIsNoneReturn
                Frame = Frame.f_back
            return Frame
        ```
        \n┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
    """
    Frame = inspect.currentframe()
    for _ in range(FBack):
        if Frame is None:
            return IfFrameIsNoneReturn
        Frame = Frame.f_back
    return Frame
#endregion [Frame()] 							           ┃
#┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
#┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
#region    [GetSource()] 								   ┃
def GetSource(I):
    """
        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        # [GetSource()]
        ## Return the text of the source code for an object.
        ---
        The argument may be a module, class, method, function, traceback, frame,
        or code object. The source code is returned as a single string.
        - If the source code cannot be retrieved, returns 'None'
        \n┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
        ## [I]
         - I | Function, class, module, method, traceback, frame or code object
        \n┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
        ## [->]
         - str | Source code of object
         - except: None | If fail
        \n┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
        ## [+]
         - import inspect
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
    try:
        return inspect.getsource(I)
    except:
        return None
#endregion [GetSource()] 								   ┃
#┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
#┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
#region    [FrameInfo()] 								   ┃
def FrameInfo(
    FBack = 0,
):
    """
        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        # [FrameInfo(FBack = 0)]
        ## Return about 'Frame(FBack = N)': 'Filename', 'CodeName' and 'LineNumber'
        \n┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
        ## [X]
         - FBack = int | Levels to improve
        \n┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
        ## [->]
         - for _ in range()
            - FrameCodeFileName: File name of frame
            - FrameCodeName: Function of frame
            - FrameLineNumber: Code line (number) of frame
         - |
        \n┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
        ## [+]
         - import inspect
        \n┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
        ## [!]
         - |
        \n┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
        ## [?]
         - 'inspect' use 'f_back' like 'Frame.f_back' to improve the caller target
        \n┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
        ## [>]
         - |
        \n┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
    """

    CurrentFrame = Frame()

    for _ in range(FBack):
        CurrentFrame = CurrentFrame.f_back

    FrameCodeFileName = os.path.basename(CurrentFrame.f_code.co_filename)
    FrameCodeName = CurrentFrame.f_code.co_name
    FrameLineNumber = CurrentFrame.f_lineno

    return FrameCodeFileName, FrameCodeName, FrameLineNumber
#endregion [FrameInfo()] 								   ┃
#┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
#┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
#region    [LineNumber(FBack)] 							   ┃
def LineNumber(
    FBack = 0
):
    CurrentFrame = Frame()
    for _ in range(FBack):
        CurrentFrame = CurrentFrame.f_back
    FrameLineNumber = CurrentFrame.f_lineno
    return FrameLineNumber
#endregion [LineNumber(FBack)] 							   ┃
#┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
#┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
#region    [""" """] 									   ┃
"""
def CurrentFile(Level=1):
    return CallerFrame(Level + 1).f_code.co_filename
def CurrentFileName(Level=1):
    return os.path.basename(CurrentFile(Level + 1))
def CurrentFunction(level: int = 0):
    frame = CallerFrame(level + 1)
    return frame.f_code.co_name if frame else "<unknown>"
def CurrentLine(Level=1):
    return CallerFrame(Level + 1).f_lineno
def CurrentClass(Level=1):

    frame = CallerFrame(Level + 1)

    if "self" in frame.f_locals:
        return frame.f_locals["self"].__class__.__name__

    if "cls" in frame.f_locals:
        return frame.f_locals["cls"].__name__

    return None




#endregion
#region Debug
def CurrentLocation(Level=1):

    file = CurrentFileName(Level + 1)
    func = CurrentFunction(Level + 1)
    cls = CurrentClass(Level + 1)
    line = CurrentLine(Level + 1)

    if cls:
        return f"{file}/{cls}.{func}:{line}"

    return f"{file}/{func}:{line}"
def PrintLocation(*Text):
    print(f"[{CurrentLocation(2)}]", *Text)
#endregion
#region Source

#endregion
#region Stack
def CurrentStack():
    return inspect.stack()
def StackNames():
    return [frame.function for frame in inspect.stack()]
#endregion
"""
#endregion [""" """] 									   ┃
#┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛