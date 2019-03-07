import signal
import sys
import debugger

from debug import debug_print
from colors import Color

class Shell():

    def __init__(self, dbg):
        # Keep list of instructions for history
        # Keep history of registers? Can get memory intensive?
        self.dbg = dbg
        self.commands_dict = {
            'exit': self.stop,
            'quit': self.stop,
            'registers': self.print_registers,
            'memory': self.print_memory,
            'clear': self.clear_screen,
            # Add command to pass a string to radare?
        }
        self.running = True
        signal.signal(signal.SIGINT, self.int_handler)
        Color.print(Color.RED, 'Initialized shell')

    def print_prompt(self):
        # TODO: Ability to change prompt
        # TODO: Ability to always clear before command, this should be nice
        # to keep screen clean and look like UI
        print('> ', end='')

    def clear_screen(self):
        for _ in range(200):
            print('')

    def process_input(self, i):
        commands = i.split(';')

        for c in commands:
            self.execute_command(c.strip())
        new_reg_state = self.dbg.get_registers()

    def execute_command(self, command):
        debug_print(command)
        if command in self.commands_dict:
            self.commands_dict[command]()
        else:
            self.run_instruction(command)

    def run_instruction(self, command):
        self.before_regs = self.dbg.get_registers()
        self.dbg.emulate_instruction(command)
        self.after_regs = self.dbg.get_registers()

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
