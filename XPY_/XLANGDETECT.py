#┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
#region    [import]                                        ┃
#	┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
#	region    [from Python import *]                          ┃
from langdetect import detect
#	endregion [from Python import *]                          ┃
#	┣━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━┫
#	region    [from MATRIX import *]                          ┃

#	endregion [from MATRIX import *]                          ┃
#	┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
#endregion [import]                                        ┃
#┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
#┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
#region    [LanguageDetect()] 							   ┃
def LanguageDetect(Text: str,) -> str:
    """
        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        # [LanguageDetect(Text: str) -> str]
        ## Detect language of input text
        \n┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
        ## [I]
         - Text: str -> str | Text to detect
        ## [->]
         - Str | Language of text
            - Spanish = es
            - English = en
        \n┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
        ## [+]
         - from langdetect import detect
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
        return detect(Text)
    except:
        return "Fail"
#endregion [LanguageDetect()] 							   ┃
#┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛