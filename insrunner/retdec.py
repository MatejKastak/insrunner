
from debug import debug_print
from context import Context


class Retdec():

    def __init__(self, out_file='retdec_tests.cpp', header_comm=False):
        self.ignored_regs = Context().arch.ignored_regs
        self.out_file = out_file

    def append_test(self, str):
        debug_print('Appending test case to file: {}'.format(self.out_file))

    def generate_test(self, after_regs, before_regs, instruction):
        test_case = ''
        test_case += self.generate_header(instruction)
        test_case += self.generate_registers_set(before_regs)
        test_case += self.generate_emulate(instruction)
        test_case += self.generate_registers_loaded()
        test_case += self.generate_registers_stored(before_regs, after_regs)
        # TODO: Merge memory loads and stores to one function
        test_case += self.generate_memory_loaded()
        test_case += self.generate_memory_stored()
        test_case += self.generate_value_called()
        test_case += self.generate_footer()
        debug_print(test_case)

        self.append_test(test_case)

    def generate_header(self, instruction):
        # TODO: try to get the operands from the opcode
        return 'TEST_P({}, ARM64_INS_{}_r_r)\n{{\n'.format(
            Context().arch.retdec_translator, instruction.split(' ')[0].upper())

    def generate_registers_set(self, before):
        set_regs = []  #['{ARM64_REG_X0, 0xffffffff},', '{ARM64_REG_X0, 0xffffffff},']

        for reg, val in before.items():
            if reg not in self.ignored_regs and val != 0:
                set_regs.append('{{ARM64_REG_{0}, {1:#016x}}},'.format(reg.upper(), val))

        if len(set_regs) != 0:
            return "\tsetRegisters({{\n\t\t{}\n\t}});\n".format(
                '\n\t\t'.join(set_regs)
            )
        else:
            return ''

    def generate_emulate(self, instruction):
        return '\temulate("{}");\n'.format(instruction)

    def generate_registers_loaded(self):
        # TODO: Generate register loads
        loaded_regs = ['ARM64_REG_X0', 'ARM64_REG_S0']
        if len(loaded_regs) == 0:
            return '\tEXPECT_NO_REGISTERS_LOADED();\n'
        else:
            return '\tEXPECT_JUST_REGISTERS_LOADED({{\n\t\t{}\n\t}});\n'.format(
                ', '.join(loaded_regs))

    def generate_registers_stored(self, before, after):
        stored_regs = []
        for reg, val in after.items():
            if reg not in self.ignored_regs and val != before[reg]:
                stored_regs.append('{{ARM64_REG_{0}, {1:#016x}}},'.format(reg.upper(), val))

        if len(stored_regs) == 0:
            return '\tEXPECT_NO_REGISTERS_STORED();\n'
        else:
            return '\tEXPECT_JUST_REGISTERS_STORED({{\n\t\t{}\n\t}});\n'.format(
                '\n\t\t'.join(stored_regs))

    def generate_memory_loaded(self):
        loaded_mem = []
        if len(loaded_mem) == 0:
            return '\tEXPECT_NO_MEMORY_LOADED();\n'
        else:
            return '\tEXPECT_JUST_MEMORY_LOADED({{\n\t\t{}\n\t}});'.format(
                '\n\t\t'.join(loaded_mem))

    def generate_memory_stored(self):
        stored_mem = []
        if len(stored_mem) == 0:
            return '\tEXPECT_NO_MEMORY_STORED();\n'
        else:
            return '\tEXPECT_JUST_MEMORY_STORED({{\n\t\t{}\n\t}});'.format(
                '\n\t\t'.join(stored_mem))

    def generate_value_called(self):
        value_called = []
        if len(value_called) == 0:
            return '\tEXPECT_NO_VALUE_CALLED();\n'
        else:
            return '\tEXPECT_JUST_VALUE_CALLED({{\n\t\t{}\n\t}});'.format(
                '\n\t\t'.join(value_called))

    def generate_footer(self):
        return '}\n\n'


"""
//
// ARM64_INS_MOV
//

TEST_P(Capstone2LlvmIrTranslatorArm64Tests, ARM64_INS_MOV_r_r)
{
        setRegisters({
                {ARM64_REG_X1, 0xcafebabecafebabe},
        });

        emulate("mov x0, x1");

        EXPECT_JUST_REGISTERS_LOADED({ARM64_REG_X1});
        EXPECT_JUST_REGISTERS_STORED({
                {ARM64_REG_X0, 0xcafebabecafebabe},
        });
        EXPECT_NO_MEMORY_LOADED_STORED();
        EXPECT_NO_VALUE_CALLED();
}
"""
