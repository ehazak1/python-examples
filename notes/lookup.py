''' lookup.py

Cascading dictionary lookups are everywhere.

    Python variables: locals() --> globals --> __builtins__.__dict__
    Python attributes: instance.__dict__ --> Class.__dict__ --> ParentClass.__dict__
    Python import: sys.path (current working dir --> $PYTHON_PATH --> site_packages --> 

    terminal executable: $PATH
    memory access: L1 --> L2 --> L3 --> main memory --> virtual memory
    
'''

defaults = {'bg': 'black', 'fg': 'green', 'h': 24, 'w': 40}
settings = {'fg': 'cyan', 'h': 40, 'w': 80}
user = {'fg': 'magenta'}

def lookup(key, *dictionaries):
    # EAFP: Easier to Ask Forgiveness than Permission
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
    # LBYL: always creates a race condition!
    if os.path.exists(filename):
        time.sleep(10)
        os.remove(filename)

def safe_remove(filename):
    # EAFP: The Pythonic Way!
    try:
        os.remove(filename)
    except OSError:
        pass # suppress

# safe_remove('tmp.txt')
