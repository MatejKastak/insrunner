#!/usr/bin/env python3
import argparse

from shell import Shell
import debugger
import elf
from context import Context


def parseArguments():
    parser = argparse.ArgumentParser(
        description='Interactive instruction runner')
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('-c', '--clear', action='store_true')
    parser.add_argument('-t', '--retdec', action='store_true')
    args = parser.parse_args()

    Context().debug_enabled = args.verbose
    Context().clear_before_command = args.clear
    Context().generate_retdec_tests = args.retdec


def main():
    parseArguments()
    f = elf.create_elf()
    dbg = debugger.Debugger(f)
    s = Shell(dbg)
    s.start()


if __name__ == '__main__':
    main()
