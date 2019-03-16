import signal
import sys

from context import Context
from debug import debug_print
from colors import Color


class Shell():

    def __init__(self, dbg):
        self.ins_history = []
        # TODO: Keep history of registers? Can get memory intensive?
        self.dbg = dbg
        self.commands_dict = {
            'exit': self.stop,
            'quit': self.stop,
            'registers': self.print_diff,
            'memory': self.print_memory,
            'clear': self.clear_screen,
            'history': self.print_history,
            'zero': self.dbg.zero_registers
            # Add command to pass a string to radare?
        }

        self.before_regs = dbg.get_registers()
        self.after_regs = self.before_regs

        if Context().debug_enabled:
            self.commands_dict.update({
                'debug': self.debug,
            })
        self.running = True
        signal.signal(signal.SIGINT, self.int_handler)
        Color.print(Color.RED, 'Initialized shell')

    def debug(self):
        import ipdb
        ipdb.set_trace()

    def print_prompt(self):
        # TODO: Ability to change prompt
        # TODO: Ability to always clear before command, this should be nice
        # to keep screen clean and look like UI
        print('> ', end='')

    def print_history(self):
        for i, ins in enumerate(self.ins_history):
            print(str(i) + ' -> ' + ins)

    def clear_screen(self):
        for _ in range(200):
            print('')

    def process_input(self, i):
        commands = i.split(';')

        for c in commands:
            self.execute_command(c.strip())

    def execute_command(self, command):
        if Context().clear_before_command:
            self.clear_screen()
            self.print_prompt()
            print(command)

        debug_print(command)
        if command in self.commands_dict:
            self.commands_dict[command]()
        else:
            self.run_instruction(command)

    def run_instruction(self, command):

        # Save the instruction
        self.ins_history.append(command)

        self.before_regs = self.dbg.get_registers()
        self.dbg.emulate_instruction(command)
        self.after_regs = self.dbg.get_registers()

        self.print_register_diff(self.before_regs, self.after_regs)

    def print_diff(self):
        self.print_register_diff(self.before_regs, self.after_regs)

    def print_register_diff(self, a, b):
        for k, v in b.items():
            if a[k] != v:
                print(k + ': ', end='')
                Color.print(Color.BLUE, str(v))
            else:
                print(k + ': ' + str(v))

    def print_memory(self):
        # TODO: We prob dont need json format
        # Just get the hexdump already formatted and color differences?? :D
        pass

    def print_registers(self):
        pass

    def start(self):
        while(self.running):
            self.print_prompt()
            self.process_input(input())

    def stop(self):
        self.running = False

    def int_handler(self, signum, frame):
        print('\nCaught SIGINT signal... exiting')
        sys.exit(0)
