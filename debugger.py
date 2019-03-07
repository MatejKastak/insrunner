import r2pipe

from debug import debug_print, debug_enabled

class Debugger:

    def __init__(self, file_name):
        if debug_enabled:
            # Close the stderr, so we don't see any warninigs
            self.r2 = r2pipe.open(file_name, ['-2'])
        else:
            self.r2 = r2pipe.open(file_name)
        self.command_wrapper('aa')
        self.command_wrapper('ood')
        self.seek_to_main()

    def command_wrapper(self, cmd):
        debug_print(cmd)
        self.r2.cmd(cmd)

    def get_ip(self):
        # Todo: Determine the right register based on the architecture
        return 'rip'

    def seek_to_main(self):
        self.command_wrapper('s main')

    def jump_to_main(self):
        self.command_wrapper('dr ' + self.get_ip() + ' = main')

    def emulate_instruction(self, i):
        self.jump_to_main()
        self.write_instruction(i)
        self.exec_instruction()

    def write_instruction(self, i):
        r2_cmd = 'wa {}'.format(i)
        self.command_wrapper(r2_cmd)

    def exec_instruction(self, count=1):
        # for _ in range(count):
        self.command_wrapper('ds')

    def get_registers(self):
        return self.r2.cmdj('drj')

    def get_memory(self):
        return self.r2.cmdj('drj')
        