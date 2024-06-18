import unittest

from drive.motor import Motors


class MotorsTest(unittest.TestCase):

    def setUp(self):
        self.motors = Motors()

    def test_default_motor_is_stopped(self):
        self.assertEqual(self.motors.left_front, 0, 'Left front motor is running')
        self.assertEqual(self.motors.right_front, 0, 'Right front motor is running')
        self.assertEqual(self.motors.left_back, 0, 'Left back motor is running')
        self.assertEqual(self.motors.right_back, 0, 'Right back motor is running')

    def test_stop_has_motor_stopped(self):
        new_motors = Motors()
        new_motors.left_front = 100
        new_motors.stop()
        self.assertEqual(self.motors.left_front, 0, 'Left front motor is running')
        self.assertEqual(self.motors.right_front, 0, 'Right front motor is running')
        self.assertEqual(self.motors.left_back, 0, 'Left back motor is running')
        self.assertEqual(self.motors.right_back, 0, 'Right back motor is running')
