import unittest
from XYRobot import *


class TestXYRobot(unittest.TestCase):

    def test_position_x(self):
        test_bot = XYRobot("test_bot", 69)
        self.assertEqual(test_bot.x(), 69)

    def test_position_y(self):
        test_bot = XYRobot("test_bot", 0, 69)
        self.assertEqual(test_bot.y(), 69)

    def test_movement(self):
        test_bot = XYRobot("test_bot", 100, 100)
        test_bot.move_forward(69)
        test_bot.turn_left()
        test_bot.move_backward(69)
        self.assertEqual((test_bot.x(), test_bot.y()), (169, 169))

    def test_history(self):
        test_bot = XYRobot("test_bot", 100, 100)
        test_bot.move_forward(69)
        test_bot.turn_left()
        test_bot.move_backward(69)
        self.assertEqual(test_bot.history(), [('forward', 69), ('left', 90), ('backward', 69)])

    def test_undo(self):
        test_bot = XYRobot("test_bot", 100, 100)
        test_bot.move_forward(69)
        test_bot.turn_left()
        test_bot.move_backward(69)       
        test_bot.unplay()
        self.assertEqual((test_bot.x(), test_bot.y(), test_bot.angle(), test_bot.history()),(100, 100, 0, []))

unittest.main(verbosity=3)
