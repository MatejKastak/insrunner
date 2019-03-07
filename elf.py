import os

from debug import debug_enabled, debug_print

def r(cmd):
    if debug_enabled:
        debug_print(cmd)
        os.system(cmd)
    else:
        os.system(cmd + ' > /dev/null 2>&1')
    

def create_elf(file_name='source'):
    template = """ .global main
.global _start
.global __start

.text
_start:
__start:
main:
	.skip 0x200, 0
"""
    assembly_file = file_name + '.as'
    object_file = file_name + '.o'
    binary_file = file_name

    assembler = 'as'
    linker = 'ld'

    with open(assembly_file, 'w') as source_file:
        source_file.write(template)

    r("{} {} -o {}".format(assembler, assembly_file, object_file))
    r("{} {} -o {}".format(linker, object_file, binary_file))

    return file_name
