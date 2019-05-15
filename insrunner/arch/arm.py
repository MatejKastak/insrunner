#!/usr/bin/env python
# Arm architectures
# Author: Matej Kastak

from . import Architecture


class ArchitectureArm64(Architecture):

    def __init__(self):
        self.pc_reg = 'pc'
        self.ignored_regs = {'pc', 'pstate'}  # TODO: check implementation
        self.retdec_translator = 'Capstone2LlvmIrTranslatorArm64Tests'


class ArchitectureArm32(Architecture):

    def __init__(self):
        self.pc_reg = 'pc'
        self.ignored_regs = {'pc', 'pstate'}  # TODO: check implementation
        self.retdec_translator = 'Capstone2LlvmIrTranslatorArmTests'
