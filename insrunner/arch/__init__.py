#!/usr/bin/env python


class Architecture():

    @property
    def name(self):
        return self.arch_name

    def get_pc(self):
        return self.pc_reg
