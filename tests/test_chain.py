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

import unittest
from unittest.mock import MagicMock

from visualizer.classes.signalchain import ChainElement
from visualizer.classes.signalchain import ChainContainer

class TestChain(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_element(self):
        element1 = ChainElement()
        element2 = ChainElement()

        def function1(input_):
            return (input_[0] + 500, input_[1] + 500)

        def function2(input_):
            return (input_[0] + 600, input_[1] + 600)

        element1.function = function1
        element2.function = function2
        element1.update()
        element2.update()
        ret1 = element1.output
        ret2 = element2.output
        self.assertEqual(ret1, (500, 500))
        self.assertEqual(ret2, (600, 600))

    def test_chain(self):
        container = ChainContainer()
        element1, element2, element3 = (ChainElement(), ChainElement(),
            ChainElement())

        def function1(input_):
            return (100, 100)
        def function2(input_):
            return (input_[0] * 2, input_[1] * 2)
        def function3(input_):
            return (input_[0] - 5, input_[1] - 5)

        element1.function, element2.function, element3.function = (function1,
            function2, function3)
        container.add(element1)
        container.add(element2)
        container.add(element3)

        self.assertEqual(element3.output, (195, 195))
        container.remove(1)
        self.assertEqual(element3.output, (95, 95))


if __name__ == '__main__':
    unittest.main()
