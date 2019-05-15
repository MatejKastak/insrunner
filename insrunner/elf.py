# Elf helper functions
# Author: Matej Kastak

import os

from debug import debug_enabled, debug_print
from context import Context
from subprocess import check_call, CalledProcessError


def rr(cmd):
    return check_call(cmd, shell=True)


def r(cmd):
    if debug_enabled:
        debug_print(cmd)
        os.system(cmd)
    else:
        os.system(cmd + ' > /dev/null 2>&1')


def remove_elf(file_name='source'):

    assembly_file = file_name + '.as'
    object_file = file_name + '.o'
    binary_file = file_name

    r("rm {} {} {}".format(assembly_file, object_file, binary_file))


def create_elf(file_name='source', ins=None):
    template = ''
    if not Context().is_arm():
        template += '.intel_syntax noprefix\n'
    template += """.global main
.global _start
.global __start

.text
_start:
__start:
main:
"""

    if ins is not None:
        template += '\t' + ins + '\n'
    else:
        template += '\t.skip 0x200, 0\n'

    assembly_file = file_name + '.as'
    object_file = file_name + '.o'
    binary_file = file_name

    assembler = 'as'
    linker = 'ld'

    with open(assembly_file, 'w') as source_file:
        source_file.write(template)

    try:
        rr("{} {} -o {}".format(assembler, assembly_file, object_file))
        rr("{} {} -o {}".format(linker, object_file, binary_file))
    except CalledProcessError as e:
        debug_print('Command failed with err: {}'.format(e))
        return None

    return file_name
