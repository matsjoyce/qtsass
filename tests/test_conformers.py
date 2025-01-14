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

# Local imports
from qtsass.conformers import NotConformer, QLinearGradientConformer


class TestNotConformer(unittest.TestCase):

    qss_str = 'QAbstractItemView::item:!active'
    css_str = 'QAbstractItemView::item:_qnot_active'

    def test_conform_to_scss(self):
        """NotConformer qss to scss."""

        c = NotConformer()
        self.assertEqual(c.to_scss(self.qss_str), self.css_str)

    def test_conform_to_qss(self):
        """NotConformer css to qss."""

        c = NotConformer()
        self.assertEqual(c.to_qss(self.css_str), self.qss_str)

    def test_round_trip(self):
        """NotConformer roundtrip."""

        c = NotConformer()
        conformed_css = c.to_scss(self.qss_str)
        self.assertEqual(c.to_qss(conformed_css), self.qss_str)


class TestQLinearGradientConformer(unittest.TestCase):

    css_vars_str = 'qlineargradient($x1, $x2, $y1, $y2, (0 $red, 1 $blue))'
    qss_vars_str = (
        'qlineargradient(x1:$x1, x2:$x2, y1:$y1, y2:$y2'
        'stop: 0 $red, stop: 1 $blue)'
    )

    css_nostops_str = 'qlineargradient(0, 0, 0, 0)'
    qss_nostops_str = 'qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0)'

    css_str = 'qlineargradient(0, 0, 0, 0, (0 red, 1 blue))'
    qss_singleline_str = (
        'qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0, '
        'stop: 0 red, stop: 1 blue)'
    )
    qss_multiline_str = dedent("""
    qlineargradient(
        x1: 0,
        y1: 0,
        x2: 0,
        y2: 0,
        stop: 0 red,
        stop: 1 blue
    )
    """).strip()
    qss_weird_whitespace_str = (
        'qlineargradient( x1: 0, y1:0, x2: 0, y2:0, '
        '   stop:0 red, stop: 1 blue )'
    )

    css_rgba_str = (
        'qlineargradient(0, 0, 0, 0,'
        '   (0 rgba(0, 1, 2, 0.3), 0.99 rgba(7, 8, 9, 1)))'
    )
    qss_rgba_str = (
        'qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0, '
        'stop: 0 rgba(0, 1, 2, 30%), stop: 0.99 rgba(7, 8, 9, 100%))'
    )

    def test_does_not_affect_css_form(self):
        """QLinearGradientConformer no affect on css qlineargradient func."""

        c = QLinearGradientConformer()
        self.assertEqual(c.to_scss(self.css_str), self.css_str)
        self.assertEqual(c.to_qss(self.css_str), self.css_str)

    def test_conform_singleline_str(self):
        """QLinearGradientConformer singleline qss to scss."""

        c = QLinearGradientConformer()
        self.assertEqual(c.to_scss(self.qss_singleline_str), self.css_str)

    def test_conform_multiline_str(self):
        """QLinearGradientConformer multiline qss to scss."""

        c = QLinearGradientConformer()
        self.assertEqual(c.to_scss(self.qss_multiline_str), self.css_str)

    def test_conform_weird_whitespace_str(self):
        """QLinearGradientConformer weird whitespace qss to scss."""

        c = QLinearGradientConformer()
        self.assertEqual(c.to_scss(self.qss_weird_whitespace_str), self.css_str)

    def test_conform_nostops_str(self):
        """QLinearGradientConformer qss with no stops to scss."""

        c = QLinearGradientConformer()
        self.assertEqual(c.to_scss(self.qss_nostops_str), self.css_nostops_str)

    def test_conform_vars_str(self):
        """QLinearGradientConformer qss with vars to scss."""

        c = QLinearGradientConformer()
        self.assertEqual(c.to_scss(self.qss_vars_str), self.css_vars_str)

    def test_conform_rgba_str(self):
        """QLinearGradientConformer qss with vars to scss."""

        c = QLinearGradientConformer()
        #self.assertEqual(c.to_scss(self.qss_rgba_str), self.css_rgba_str)
        print('TODO: QSS to SCSS with nested qlineargradient(rgba())')
