#!/usr/bin/env python3
import argparse

from shell import Shell
from debug import debug_print
import debugger
import elf
from context import Context


def parseArguments():
    parser = argparse.ArgumentParser(
        description='Interactive instruction runner')
    parser.add_argument('-v', '--verbose', action='store_true')
    args = parser.parse_args()

    Context().debug_enabled = args.verbose
    debug_print(args.verbose)


def main():
    parseArguments()
    f = elf.create_elf()
    dbg = debugger.Debugger(f)
    s = Shell(dbg)
    s.start()


if __name__ == '__main__':
    main()
