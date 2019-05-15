# Assembling based on r2 assembler
# Author: Matej Kastak

import r2pipe

from debug import debug_print, debug_enabled
from context import Context


class Debugger:

    def __init__(self, file_name):
        if debug_enabled():
            self.r2 = r2pipe.open(file_name)
        else:
            # Close the stderr, so we don't see any warninigs
            self.r2 = r2pipe.open(file_name, ['-2'])
        self.command_wrapper('e asm.assembler=arm.ks')
        self.command_wrapper('aa')
        self.command_wrapper('ood')
        self.seek_to_main()

    def command_wrapper(self, cmd):
        debug_print(cmd)
        return self.r2.cmd(cmd)

    def get_fp(self):
        return Context().arch.get_fp()

    def get_sp(self):
        return Context().arch.get_sp()

    def get_pc(self):
        return Context().arch.get_pc()

    def get_control_registers(self):
        return [self.get_pc(), self.get_sp(), self.get_fp()]

    def seek_to_main(self):
        self.command_wrapper('s main')

    def jump_to_main(self):
        self.command_wrapper('dr ' + self.get_pc() + ' = main')

    def seek_to_pc(self):
        # TODO: Seek to instruction pointer
        pass

    def emulate_instruction(self, i):
        # TODO: Maybe don't jump to main just keep counter of instructions and
        # after some reasonable ammount jump to main
        self.jump_to_main()
        self.write_instruction(i)
        self.exec_instruction()

    def write_instruction(self, i):
        r2_cmd = 'wa {}'.format(i)
        # TODO: Find a way to check if the instruction is valid
        # right now we just try to write whatever is not a command
        # and since we close stderr for radare2
        self.command_wrapper(r2_cmd)

    def zero_registers(self):
        for reg in self.get_registers().keys():
            if reg in self.get_control_registers():
                continue
            self.command_wrapper('dr {} = 0'.format(reg))

    def exec_instruction(self, count=1):
        for _ in range(count):
            self.command_wrapper('ds')

    def get_registers(self):
        return self.r2.cmdj('drj')

    def get_memory(self):
        return self.r2.cmdj('drj')
