#!/usr/bin/env python
# X86 architectures
# Author: Matej Kastak

from . import Architecture


class ArchitectureX86(Architecture):

    def __init__(self):
        self.arch_name = 'x86'
        self.pc_reg = 'eip'
        self.ignored_regs = {'eip'}  # TODO: check implementation
        self.retdec_translator = 'Capstone2LlvmIrTranslatorX86Tests'


class ArchitectureX86_64(Architecture):

    def __init__(self):
        self.arch_name = 'x86_64'
        self.pc_reg = 'rip'
        # TODO: check implementation
        self.ignored_regs = {'rip', 'orax', 'rflags'}
        self.retdec_translator = 'Capstone2LlvmIrTranslatorX86Tests'
