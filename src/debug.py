from colors import Color
from context import Context


def debug_print(s):
    if Context().debug_enabled:
        Color.print(Color.GREEN, str(s))


def debug_enabled():
    return Context().debug_enabled
