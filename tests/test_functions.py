# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2015 Yann Lanthony
# Copyright (c) 2017-2018 Spyder Project Contributors
#
# Licensed under the terms of the MIT License
# (See LICENSE.txt for details)
# -----------------------------------------------------------------------------
"""Test qtsass conformers."""

from __future__ import absolute_import

# Standard library imports
from textwrap import dedent
import unittest

# Third party imports
import sass

# Local imports
from qtsass.api import compile


class BaseCompileTest(unittest.TestCase):
    def compile_scss(self, str):
        # NOTE: revise for better future compatibility
        wstr = '*{{t: {0};}}'.format(str)
        res = compile(wstr)
        return res.replace('* {\n  t: ', '').replace('; }\n', '')

class TestRgbaFunc(BaseCompileTest):
    def test_rgba(self):
        self.assertEqual(
            self.compile_scss('rgba(0, 1, 2, 0.3)'),
            'rgba(0, 1, 2, 30%)'
        )

class TestQLinearGradientFunc(BaseCompileTest):
    def test_color(self):
        self.assertEqual(
            self.compile_scss('qlineargradient(1, 2, 3, 4, (0 red, 1 blue))'),
            'qlineargradient(x1: 1.0, y1: 2.0, x2: 3.0, y2: 4.0, '
            'stop: 0.0 rgba(255, 0, 0, 100%), stop: 1.0 rgba(0, 0, 255, 100%))'
        )

    def test_rgba(self):
        self.assertEqual(
            self.compile_scss('qlineargradient(1, 2, 3, 4, (0 red, 0.2 rgba(5, 6, 7, 0.8)))'),
            'qlineargradient(x1: 1.0, y1: 2.0, x2: 3.0, y2: 4.0, '
            'stop: 0.0 rgba(255, 0, 0, 100%), stop: 0.2 rgba(5, 6, 7, 80%))'
        )
