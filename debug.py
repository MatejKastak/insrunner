debug_enabled = True

from colors import Color

def debug_print(s):
    if debug_enabled:
        Color.print(Color.GREEN, s)
        
    
