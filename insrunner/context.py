# Current application context
# Author: Matej Kastak

from arch.arm import ArchitectureArm64
from arch.arm import ArchitectureArm32
from arch.x86 import ArchitectureX86_64
from arch.x86 import ArchitectureX86


class Singleton(type):
    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class Context(metaclass=Singleton):
    def __init__(self):
        self.debug_enabled = False
        self.clear_before_command = False
        self.generate_retdec_tests = False

    def create_arch(self, arch_str):
        archs = {
            'arm64': ArchitectureArm64(),
            'arm32': ArchitectureArm32(),
            'x86_64': ArchitectureX86_64(),
            'x86': ArchitectureX86(),
            None: ArchitectureX86_64(),
        }

        self.arch = archs[arch_str]

    def is_arm(self):
        return self.is_arm32() or self.is_arm64()

    def is_arm64(self):
        return self.arch.name == 'arm64'

    def is_arm32(self):
        return self.arch.name == 'arm32'

    def is_x86(self):
        return self.arch.name == 'x86'

    def is_x86_64(self):
        return self.arch.name == 'x86_64'
