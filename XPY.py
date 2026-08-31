#!/usr/bin/env python
#┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
#region    [M]  										   ┃
# __doc__
"""---
    # [XPY] Meta Python
    Wrapper of XPY_/XPY.py

    ---
    ## [def]
    ```python
        def X(X):
            
    ```
"""
# __author__
__author__ = "Sir. Doyle; S.Class Astartes at BlackCoreΔ"
# __version__
__version__ = "1.0"
# __annotations__
DEBUG: bool = False
#endregion [M]  										   ┃
#┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
#┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
#region    [X] 											   ┃
def X(X):
    try:
        from XPY_ import XPY
        XPY.XPY_(*X)
    except Exception as E:
        print(f"\033[91m[{__file__[0].upper() + __file__[1:]}] def X():\033[0m")
        print(f"\033[91m > {E}\033[0m")

if __name__ == "__main__":
    try:
        X(None)
    except Exception as E:
        print(f"\033[91m┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\033[0m")
        print(f"\033[91m[{__file__[0].upper() + __file__[1:]}] if __name__ == \"__main__\":\033[0m")
        print(f"\033[91m > {E}\033[0m")
        print(f"\033[91m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\033[0m")
        raise SystemExit(1)

#endregion [X] 											   ┃
#┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛