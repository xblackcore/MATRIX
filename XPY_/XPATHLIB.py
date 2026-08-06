#┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
#region    [import]                                        ┃
#	┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
#	region    [from Python import *]                          ┃
from pathlib import Path
#	endregion [from Python import *]                          ┃
#	┣━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━┫
#	region    [from MATRIX import *]                          ┃
from XPRINT import Ok
#	endregion [from MATRIX import *]                          ┃
#	┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
#endregion [import]                                        ┃
#┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
#┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
#region    [PathCWD()] 									   ┃
def PathCWD():
    return Path.cwd()
#endregion [PathCWD()] 									   ┃
#┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
#┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
#region    [MakeFolder()] 	    						   ┃
def MakeFolder(
    I,
    Parents = True,
    ExistOk = True
):
    """
        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        # [MakeFolder()]
        ## Create a new directory at this given path
        \n┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
        ## [I]
         - I: Str | Directory path
        ## [X]
         - Parents = True | Create missing parent directories
         - ExistOK = True | Do not raise an exception if the directory already exists
        \n┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
        ## [->]
         - Str | The input path
        \n┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
        ## [+]
         - pathlib.Path.mkdir()
        \n┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
        ## [!]
         - Raises 'FileExistsError' if 'ExistOk' is 'False' and the directory already exists
         - Raises OSError if the directory cannot be created
        \n┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
        ## [?]
         - Automatically creates parent directories when Parents=True|
        \n┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
        ## [>]
         - |
        ```python
            MakeFolder("/")

            Path(I).mkdir(
                parents = Parents,
                exist_ok = ExistOk
            )
            return I
        ```
        \n┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
    """
    Ok("MakeFolder(")
    Ok(f"\tI       = '{I}'")
    Ok(f"\tParents = '{Parents}'")
    Ok(f"\tExistOk = '{ExistOk}'")
    Ok(")")
    Ok("try: Path(I).mkdir()")
    try:

        Path(I).mkdir(
            parents = Parents,
            exist_ok = ExistOk
        )
        Ok(f"\tOk, return I:'{I}'")
        return I
    except:
        Ok("except: return None")
        return None
#endregion [MakeFolder()] 	    						   ┃
#┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
#┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
#region    [PathExists(I: str)] 						   ┃
def PathExists(I: str) -> bool:
    return Path(I).exists()
#endregion [PathExists(Path: str)] 						   ┃
#┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
#┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
#region    [] 											   ┃
if __name__ == "__main__":
    MakeFolder("Test/Test")
#endregion [] 											   ┃
#┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛