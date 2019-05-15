#!/usr/bin/env python3
#
# Insrunner main file
# Parsing the command line and initialize shell
# Author: Matej Kastak

import argparse

from shell import Shell
import debugger_gas
import debugger_r2
import elf
from context import Context


def parseArguments():
    parser = argparse.ArgumentParser(
        description='Interactive instruction runner')
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('-a', '--arch', type=str, choices=['arm64', 'x86_64'])
    parser.add_argument('-b', '--backend', type=str, choices=['r2', 'gas'])
    parser.add_argument('-c', '--clear', action='store_true')
    parser.add_argument('-r', '--retdec', action='store_true')
    args = parser.parse_args()

    Context().debug_enabled = not args.verbose
    Context().clear_before_command = args.clear
    Context().generate_retdec_tests = args.retdec
    Context().create_arch(args.arch)
    Context().backend = args.backend


def main():
    parseArguments()

    f = elf.create_elf()
    if Context().backend == 'gas':
        dbg = debugger_gas.Debugger(f)
    else:
        # Gas should work everywhere
        dbg = debugger_r2.Debugger(f)

    s = Shell(dbg)
    s.start()


if __name__ == '__main__':
    main()
