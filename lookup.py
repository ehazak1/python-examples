'''lookup.py

Cascading dictionary lookups are everywhere
    Python variables: locals() --> globals() --> __builtins__.__dict__
    Python attributes: instance.__dict__ --> Class.__dict --> ParentClass.__dict__
    Python import: sys.path (current working dir --> $PYTHON_PATH --> site_packages -->

    terminal executable: $PATH
    memory access: L1 --> L2 --> L3 --> main memory --> virtual memory

'''

defaults = {'bg': 'black', 'fg': 'green', 'h': 24, 'w': 80}
settings = {'fg': 'cyan', 'h': 40, 'w': 80}
user = {'fg': 'magenta'}


def lookup(key):
    # LYBL: Look before you leap
    if key in settings:
        return settings[key]
    return defaults[key]


def lookup(key, *dictionaries):
    # EAFP: Easier to Ask Forgivness than Permission
    # The Pythonic Way!
    for d in dictionaries:
        try:
            return d[key]
        except KeyError:
            continue
    raise KeyError(key)

import os
import time

def safe_remove(filename):
    # LYBL: always creats a race condition!
    # :-( race condition
    if os.path.exists(filename):
        sleep(10)
        os.remove(filename)

def safe_remove(filename):
    # EAFP
    try:
        os.remove(filename)
    except OSError:
        pass # ignore/supress
            
