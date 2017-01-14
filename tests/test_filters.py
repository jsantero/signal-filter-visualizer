"""Copyright (C) 2016  Juha-Matti Santero

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""

from math import pi
import unittest
from unittest.mock import MagicMock

import numpy as np
from PyQt5.QtWidgets import QApplication

from visualizer.dialogs.filter_variants import Bessel
from visualizer.dialogs.filter_variants import Butter
from visualizer.dialogs.filter_variants import Cheby1
from visualizer.dialogs.filter_variants import Cheby2
from visualizer.dialogs.filter_variants import Elliptic
from visualizer.dialogs.filter_variants import Rolling

class TestFilters(unittest.TestCase):

    x = np.linspace(0, 10, num=1001, endpoint=True)
    y = 5 * np.sin(2 * pi * 8 * x)  # Ampl. 5 at 8 Hz
    y += 6 * np.sin(2 * pi * 12 * x)  # + 6 at 12 Hz
    y += 10 * np.sin(2 * pi * 25 * x)  # + 10 at 25 Hz
    y += 15 * np.sin(2 * pi * 40 * x)  # + 15 at 40 Hz

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_bessel(self):
        filt = Bessel()
        for i in range(4, 10):
            filt.order = i
            for freq in (8, 12, 25, 40):
                filt.lowCutoff = freq
                filt._type = 'lowpass'
                output = filt.filter((self.x, self.y))
                self.assertIsNotNone(output)
                self.assertNotEqual(
                    (output[0].tolist(), output[1].tolist()), (0,0))
                self.assertNotEqual(output[1].tolist(), self.y.tolist())

                filt.highCutoff = freq
                filt._type = 'highpass'
                output = filt.filter((self.x, self.y))
                self.assertIsNotNone(output)
                self.assertNotEqual(
                    (output[0].tolist(), output[1].tolist()), (0,0))
                self.assertNotEqual(output[1].tolist(), self.y.tolist())

                filt.lowCutoff -= 2
                filt.highCutoff += 2
                filt._type = 'bandstop'
                output = filt.filter((self.x, self.y))
                self.assertIsNotNone(output)
                self.assertNotEqual(
                    (output[0].tolist(), output[1].tolist()), (0,0))
                self.assertNotEqual(output[1].tolist(), self.y.tolist())

                filt._type = 'bandpass'
                output = filt.filter((self.x, self.y))
                self.assertIsNotNone(output)
                self.assertNotEqual(
                    (output[0].tolist(), output[1].tolist()), (0,0))
                self.assertNotEqual(output[1].tolist(), self.y.tolist())

    def test_butter(self):
        filt = Butter()
        for i in range(4, 10):
            filt.order = i
            for freq in (8, 12, 25, 40):
                filt.lowCutoff = freq
                filt._type = 'lowpass'
                output = filt.filter((self.x, self.y))
                self.assertIsNotNone(output)
                self.assertNotEqual(
                    (output[0].tolist(), output[1].tolist()), (0,0))
                self.assertNotEqual(output[1].tolist(), self.y.tolist())

                filt.highCutoff = freq
                filt._type = 'highpass'
                output = filt.filter((self.x, self.y))
                self.assertIsNotNone(output)
                self.assertNotEqual(
                    (output[0].tolist(), output[1].tolist()), (0,0))
                self.assertNotEqual(output[1].tolist(), self.y.tolist())

                filt.lowCutoff -= 2
                filt.highCutoff += 2
                filt._type = 'bandstop'
                output = filt.filter((self.x, self.y))
                self.assertIsNotNone(output)
                self.assertNotEqual(
                    (output[0].tolist(), output[1].tolist()), (0,0))
                self.assertNotEqual(output[1].tolist(), self.y.tolist())

                filt._type = 'bandpass'
                output = filt.filter((self.x, self.y))
                self.assertIsNotNone(output)
                self.assertNotEqual(
                    (output[0].tolist(), output[1].tolist()), (0,0))
                self.assertNotEqual(output[1].tolist(), self.y.tolist())

    def test_cheby1(self):
        filt = Cheby1()

        for i in range(4, 10):
            filt.order = i

            for ripple in (1.0, 2.0, 3.0):
                filt.maxRipple = ripple

                for freq in (8, 12, 25, 40):
                    filt.lowCutoff = freq
                    filt._type = 'lowpass'
                    output = filt.filter((self.x, self.y))
                    self.assertIsNotNone(output)
                    self.assertNotEqual(
                        (output[0].tolist(), output[1].tolist()), (0,0))
                    self.assertNotEqual(output[1].tolist(), self.y.tolist())

                    filt.highCutoff = freq
                    filt._type = 'highpass'
                    output = filt.filter((self.x, self.y))
                    self.assertIsNotNone(output)
                    self.assertNotEqual(
                        (output[0].tolist(), output[1].tolist()), (0,0))
                    self.assertNotEqual(output[1].tolist(), self.y.tolist())

                    filt.lowCutoff -= 2
                    filt.highCutoff += 2
                    filt._type = 'bandstop'
                    output = filt.filter((self.x, self.y))
                    self.assertIsNotNone(output)
                    self.assertNotEqual(
                        (output[0].tolist(), output[1].tolist()), (0,0))
                    self.assertNotEqual(output[1].tolist(), self.y.tolist())

                    filt._type = 'bandpass'
                    output = filt.filter((self.x, self.y))
                    self.assertIsNotNone(output)
                    self.assertNotEqual(
                        (output[0].tolist(), output[1].tolist()), (0,0))
                    self.assertNotEqual(output[1].tolist(), self.y.tolist())

    def test_cheby2(self):
        filt = Cheby2()

        for i in range(4, 10):
            filt.order = i

            for attenuation in (10.0, 12.0, 15.0):
                filt.minAttenuation = attenuation

                for freq in (8, 12, 25, 40):
                    filt.lowCutoff = freq
                    filt._type = 'lowpass'
                    output = filt.filter((self.x, self.y))
                    self.assertIsNotNone(output)
                    self.assertNotEqual(
                        (output[0].tolist(), output[1].tolist()), (0,0))
                    self.assertNotEqual(output[1].tolist(), self.y.tolist())

                    filt.highCutoff = freq
                    filt._type = 'highpass'
                    output = filt.filter((self.x, self.y))
                    self.assertIsNotNone(output)
                    self.assertNotEqual(
                        (output[0].tolist(), output[1].tolist()), (0,0))
                    self.assertNotEqual(output[1].tolist(), self.y.tolist())

                    filt.lowCutoff -= 2
                    filt.highCutoff += 2
                    filt._type = 'bandstop'
                    output = filt.filter((self.x, self.y))
                    self.assertIsNotNone(output)
                    self.assertNotEqual(
                        (output[0].tolist(), output[1].tolist()), (0,0))
                    self.assertNotEqual(output[1].tolist(), self.y.tolist())

                    filt._type = 'bandpass'
                    output = filt.filter((self.x, self.y))
                    self.assertIsNotNone(output)
                    self.assertNotEqual(
                        (output[0].tolist(), output[1].tolist()), (0,0))
                    self.assertNotEqual(output[1].tolist(), self.y.tolist())

    def test_elliptic(self):
        filt = Elliptic()

        for i in range(4, 10):
            filt.order = i

            for ripple in (1.0, 2.0, 3.0):
                filt.maxRipple = ripple

                for attenuation in (10.0, 12.0, 15.0):
                    filt.minAttenuation = attenuation

                    for freq in (8, 12, 25, 40):
                        filt.lowCutoff = freq
                        filt._type = 'lowpass'
                        output = filt.filter((self.x, self.y))
                        self.assertIsNotNone(output)
                        self.assertNotEqual(
                            (output[0].tolist(), output[1].tolist()), (0,0))
                        self.assertNotEqual(output[1].tolist(), self.y.tolist())

                        filt.highCutoff = freq
                        filt._type = 'highpass'
                        output = filt.filter((self.x, self.y))
                        self.assertIsNotNone(output)
                        self.assertNotEqual(
                            (output[0].tolist(), output[1].tolist()), (0,0))
                        self.assertNotEqual(output[1].tolist(), self.y.tolist())

                        filt.lowCutoff -= 2
                        filt.highCutoff += 2
                        filt._type = 'bandstop'
                        output = filt.filter((self.x, self.y))
                        self.assertIsNotNone(output)
                        self.assertNotEqual(
                            (output[0].tolist(), output[1].tolist()), (0,0))
                        self.assertNotEqual(output[1].tolist(), self.y.tolist())

                        filt._type = 'bandpass'
                        output = filt.filter((self.x, self.y))
                        self.assertIsNotNone(output)
                        self.assertNotEqual(
                            (output[0].tolist(), output[1].tolist()), (0,0))
                        self.assertNotEqual(output[1].tolist(), self.y.tolist())

    def test_rolling(self):
        filt = Rolling()

        for _type in ['mean', 'rms', 'median', 'max']:
            filt._type = _type
            filt.samplingRate = 0
            for length in (5, 9, 13):
                filt.windowLength = length
                output = filt.filter((self.x, self.y))
                self.assertIsNotNone(output)
                self.assertNotEqual(
                    (output[0].tolist(), output[1]), (0,0))
                self.assertNotEqual(output[1], self.y.tolist())

            filt.samplingRate = 100
            for length in (0.1, 0.2, 0.3):
                filt.windowLength = length
                output = filt.filter((self.x, self.y))
                self.assertIsNotNone(output)
                self.assertNotEqual(
                    (output[0].tolist(), output[1]), (0,0))
                self.assertNotEqual(output[1], self.y.tolist())


if __name__ == '__main__':
    app = QApplication([])
    unittest.main()
