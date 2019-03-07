#!/usr/bin/env python3
import argparse

from shell import Shell
from debug import debug_enabled
import debugger
import elf

def parseArguments():
    parser = argparse.ArgumentParser(description='Interactive instruction runner')
    args = parser.parse_args()

def main():
    parseArguments()
    f = elf.create_elf()
    dbg = debugger.Debugger(f)
    s = Shell(dbg)
    s.start()

if __name__ == '__main__':
    main()
