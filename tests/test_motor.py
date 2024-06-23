import unittest

from drive.motor import Motors
from drive.remote_control import ChannelInput


class MotorsTest(unittest.TestCase):

    def setUp(self):
        self.motors = Motors()

    def test_default_motor_is_stopped(self):
        self.assertEqual(self.motors.left_front, 0, msg='Left front motor is running')
        self.assertEqual(self.motors.right_front, 0, msg='Right front motor is running')
        self.assertEqual(self.motors.left_back, 0, msg='Left back motor is running')
        self.assertEqual(self.motors.right_back, 0, msg='Right back motor is running')

    def test_stop_has_motor_stopped(self):
        new_motors = Motors()
        new_motors.left_front = 100
        new_motors.stop()
        self.assertEqual(self.motors.left_front, 0, msg='Left front motor is running')
        self.assertEqual(self.motors.right_front, 0, msg='Right front motor is running')
        self.assertEqual(self.motors.left_back, 0, msg='Left back motor is running')
        self.assertEqual(self.motors.right_back, 0, msg='Right back motor is running')

    def test_bounded_motor_speed_positive(self):
        got = self.motors.bounded_motor_speed(0.8)
        want = 0.8
        self.assertEqual(got, want, msg='Incorrect positive below boundary motor speed')

    def test_bounded_motor_speed_negative(self):
        got = self.motors.bounded_motor_speed(-0.8)
        want = -0.8
        self.assertEqual(got, want, msg='Incorrect negative below boundary motor speed')

    def test_bounded_motor_speed_positive_above_boundary(self):
        got = self.motors.bounded_motor_speed(1.8)
        want = 1.0
        self.assertEqual(got, want, msg='Incorrect positive above boundary motor speed')

    def test_bounded_motor_speed_negative_above_boundary(self):
        got = self.motors.bounded_motor_speed(-1.8)
        want = -1.0
        self.assertEqual(got, want, msg='Incorrect negative above boundary motor speed')

    def test_left_front_motor_forward(self):
        ch1 = 1450
        ch2 = 1600
        input_line = bytes(f'{ch1} {ch2} 0 0 0', encoding='utf-8')
        channel_input = ChannelInput()
        channel_input.read_channel_input(input_line=input_line)
        self.motors.left_front_motor(channel_input=channel_input)
        self.assertAlmostEqual(self.motors.left_front,
                               1.0,
                               msg='Left motor forward wrong speed multiple')

    def test_left_front_motor_forward_half_speed(self):
        ch1 = 1450
        # Initial full speed sets the highest speed
        ch2 = 1750
        input_line = bytes(f'{ch1} {ch2} 0 0 0', encoding='utf-8')
        channel_input = ChannelInput()
        channel_input.read_channel_input(input_line=input_line)

        ch2 = 1650
        input_line = bytes(f'{ch1} {ch2} 0 0 0', encoding='utf-8')
        channel_input.read_channel_input(input_line=input_line)
        self.motors.left_front_motor(channel_input=channel_input)
        self.assertAlmostEqual(self.motors.left_front,
                               0.5,
                               msg='Left motor forward wrong half speed multiple')

    def test_left_front_motor_backward(self):
        ch1 = 1450
        ch2 = 1300
        input_line = bytes(f'{ch1} {ch2} 0 0 0', encoding='utf-8')
        channel_input = ChannelInput()
        channel_input.read_channel_input(input_line=input_line)
        self.motors.left_front_motor(channel_input=channel_input)
        self.assertAlmostEqual(self.motors.left_front,
                               -1.0,
                               msg='Left motor backward wrong speed multiple')

    def test_left_front_motor_backward_half_speed(self):
        ch1 = 1450
        # Initial full speed sets the highest speed
        ch2 = 1150
        input_line = bytes(f'{ch1} {ch2} 0 0 0', encoding='utf-8')
        channel_input = ChannelInput()
        channel_input.read_channel_input(input_line=input_line)

        ch2 = 1250
        input_line = bytes(f'{ch1} {ch2} 0 0 0', encoding='utf-8')
        channel_input.read_channel_input(input_line=input_line)
        self.motors.left_front_motor(channel_input=channel_input)
        self.assertAlmostEqual(self.motors.left_front,
                               -0.5,
                               msg='Left motor backward wrong half speed multiple')

    def test_left_front_motor_right(self):
        ch1 = 1600
        ch2 = 1450
        input_line = bytes(f'{ch1} {ch2} 0 0 0', encoding='utf-8')
        channel_input = ChannelInput()
        channel_input.read_channel_input(input_line=input_line)
        self.motors.left_front_motor(channel_input=channel_input)
        self.assertAlmostEqual(self.motors.left_front,
                               1.0,
                               msg='Left motor right wrong speed multiple')

    def test_left_front_motor_left(self):
        ch1 = 1300
        ch2 = 1450
        input_line = bytes(f'{ch1} {ch2} 0 0 0', encoding='utf-8')
        channel_input = ChannelInput()
        channel_input.read_channel_input(input_line=input_line)
        self.motors.left_front_motor(channel_input=channel_input)
        self.assertAlmostEqual(self.motors.left_front,
                               -1.0,
                               msg='Left motor left wrong speed multiple')

    def test_left_front_motor_right_diagonal_forward(self):
        ch1 = 1600
        ch2 = 1600
        input_line = bytes(f'{ch1} {ch2} 0 0 0', encoding='utf-8')
        channel_input = ChannelInput()
        channel_input.read_channel_input(input_line=input_line)
        self.motors.left_front_motor(channel_input=channel_input)
        self.assertAlmostEqual(self.motors.left_front,
                               1.0,
                               msg='Left motor right diagonal forward wrong speed multiple')

    def test_left_front_motor_left_diagonal_forward(self):
        ch1 = 1300
        ch2 = 1600
        input_line = bytes(f'{ch1} {ch2} 0 0 0', encoding='utf-8')
        channel_input = ChannelInput()
        channel_input.read_channel_input(input_line=input_line)
        self.motors.left_front_motor(channel_input=channel_input)
        self.assertAlmostEqual(self.motors.left_front,
                               0.0,
                               msg='Left motor left diagonal forward wrong speed multiple')

    def test_left_front_motor_right_diagonal_backward(self):
        ch1 = 1600
        ch2 = 1300
        input_line = bytes(f'{ch1} {ch2} 0 0 0', encoding='utf-8')
        channel_input = ChannelInput()
        channel_input.read_channel_input(input_line=input_line)
        self.motors.left_front_motor(channel_input=channel_input)
        self.assertAlmostEqual(self.motors.left_front,
                               0.0,
                               msg='Left motor right diagonal forward wrong speed multiple')

    def test_left_front_motor_left_diagonal_backward(self):
        ch1 = 1300
        ch2 = 1300
        input_line = bytes(f'{ch1} {ch2} 0 0 0', encoding='utf-8')
        channel_input = ChannelInput()
        channel_input.read_channel_input(input_line=input_line)
        self.motors.left_front_motor(channel_input=channel_input)
        self.assertAlmostEqual(self.motors.left_front,
                               -1.0,
                               msg='Left motor left diagonal forward wrong speed multiple')

    def test_left_front_motor_right_diagonal_forward_different_speed(self):
        ch1 = 1750
        # Initial full speed sets the highest speed
        ch2 = 1750
        input_line = bytes(f'{ch1} {ch2} 0 0 0', encoding='utf-8')
        channel_input = ChannelInput()
        channel_input.read_channel_input(input_line=input_line)

        ch1 = 1670
        ch2 = 1600
        input_line = bytes(f'{ch1} {ch2} 0 0 0', encoding='utf-8')
        channel_input.read_channel_input(input_line=input_line)
        self.motors.left_front_motor(channel_input=channel_input)
        self.assertAlmostEqual(
            self.motors.left_front,
            0.6,
            msg='Left motor right diagonal forward different speed has wrong speed multiple')

    def test_left_front_motor_left_diagonal_backward_different_speed(self):
        ch1 = 1150
        # Initial full speed sets the highest speed
        ch2 = 1150
        input_line = bytes(f'{ch1} {ch2} 0 0 0', encoding='utf-8')
        channel_input = ChannelInput()
        channel_input.read_channel_input(input_line=input_line)

        ch1 = 1300
        ch2 = 1230
        input_line = bytes(f'{ch1} {ch2} 0 0 0', encoding='utf-8')
        channel_input.read_channel_input(input_line=input_line)
        self.motors.left_front_motor(channel_input=channel_input)
        self.assertAlmostEqual(
            self.motors.left_front,
            -0.6,
            msg='Left motor left diagonal backward different speed has wrong speed multiple')

    def test_right_front_motor_forward(self):
        ch1 = 1450
        ch2 = 1600
        input_line = bytes(f'{ch1} {ch2} 0 0 0', encoding='utf-8')
        channel_input = ChannelInput()
        channel_input.read_channel_input(input_line=input_line)
        self.motors.right_front_motor(channel_input=channel_input)
        self.assertAlmostEqual(self.motors.right_front,
                               1.0,
                               msg='Right front motor forward wrong speed multiple')

    def test_right_front_motor_forward_half_speed(self):
        ch1 = 1450
        # Initial full speed sets the highest speed
        ch2 = 1750
        input_line = bytes(f'{ch1} {ch2} 0 0 0', encoding='utf-8')
        channel_input = ChannelInput()
        channel_input.read_channel_input(input_line=input_line)

        ch2 = 1650
        input_line = bytes(f'{ch1} {ch2} 0 0 0', encoding='utf-8')
        channel_input.read_channel_input(input_line=input_line)
        self.motors.right_front_motor(channel_input=channel_input)
        self.assertAlmostEqual(self.motors.right_front,
                               0.5,
                               msg='Right front motor forward wrong half speed multiple')

    def test_right_front_motor_backward(self):
        ch1 = 1450
        ch2 = 1300
        input_line = bytes(f'{ch1} {ch2} 0 0 0', encoding='utf-8')
        channel_input = ChannelInput()
        channel_input.read_channel_input(input_line=input_line)
        self.motors.right_front_motor(channel_input=channel_input)
        self.assertAlmostEqual(self.motors.right_front,
                               -1.0,
                               msg='Right front motor backward wrong speed multiple')

    def test_right_front_motor_backward_half_speed(self):
        ch1 = 1450
        # Initial full speed sets the highest speed
        ch2 = 1150
        input_line = bytes(f'{ch1} {ch2} 0 0 0', encoding='utf-8')
        channel_input = ChannelInput()
        channel_input.read_channel_input(input_line=input_line)

        ch2 = 1250
        input_line = bytes(f'{ch1} {ch2} 0 0 0', encoding='utf-8')
        channel_input.read_channel_input(input_line=input_line)
        self.motors.right_front_motor(channel_input=channel_input)
        self.assertAlmostEqual(self.motors.right_front,
                               -0.5,
                               msg='Right front motor backward wrong half speed multiple')

    def test_right_front_motor_right(self):
        ch1 = 1600
        ch2 = 1450
        input_line = bytes(f'{ch1} {ch2} 0 0 0', encoding='utf-8')
        channel_input = ChannelInput()
        channel_input.read_channel_input(input_line=input_line)
        self.motors.right_front_motor(channel_input=channel_input)
        self.assertAlmostEqual(self.motors.right_front,
                               -1.0,
                               msg='Right front motor right wrong speed multiple')

    def test_right_front_motor_left(self):
        ch1 = 1300
        ch2 = 1450
        input_line = bytes(f'{ch1} {ch2} 0 0 0', encoding='utf-8')
        channel_input = ChannelInput()
        channel_input.read_channel_input(input_line=input_line)
        self.motors.right_front_motor(channel_input=channel_input)
        self.assertAlmostEqual(self.motors.right_front,
                               1.0,
                               msg='Right front motor left wrong speed multiple')

    def test_right_front_motor_right_diagonal_forward(self):
        ch1 = 1600
        ch2 = 1600
        input_line = bytes(f'{ch1} {ch2} 0 0 0', encoding='utf-8')
        channel_input = ChannelInput()
        channel_input.read_channel_input(input_line=input_line)
        self.motors.right_front_motor(channel_input=channel_input)
        self.assertAlmostEqual(self.motors.right_front,
                               0.0,
                               msg='Right front motor right diagonal forward wrong speed multiple')

    def test_right_front_motor_left_diagonal_forward(self):
        ch1 = 1300
        ch2 = 1600
        input_line = bytes(f'{ch1} {ch2} 0 0 0', encoding='utf-8')
        channel_input = ChannelInput()
        channel_input.read_channel_input(input_line=input_line)
        self.motors.right_front_motor(channel_input=channel_input)
        self.assertAlmostEqual(self.motors.right_front,
                               1.0,
                               msg='Right front motor left diagonal forward wrong speed multiple')

    def test_right_front_motor_right_diagonal_backward(self):
        ch1 = 1600
        ch2 = 1300
        input_line = bytes(f'{ch1} {ch2} 0 0 0', encoding='utf-8')
        channel_input = ChannelInput()
        channel_input.read_channel_input(input_line=input_line)
        self.motors.right_front_motor(channel_input=channel_input)
        self.assertAlmostEqual(self.motors.right_front,
                               -1.0,
                               msg='Right front motor right diagonal forward wrong speed multiple')

    def test_right_front_motor_left_diagonal_backward(self):
        ch1 = 1300
        ch2 = 1300
        input_line = bytes(f'{ch1} {ch2} 0 0 0', encoding='utf-8')
        channel_input = ChannelInput()
        channel_input.read_channel_input(input_line=input_line)
        self.motors.right_front_motor(channel_input=channel_input)
        self.assertAlmostEqual(self.motors.right_front,
                               0.0,
                               msg='Right front motor left diagonal forward wrong speed multiple')

    def test_right_front_motor_right_diagonal_forward_different_speed(self):
        ch1 = 1750
        # Initial full speed sets the highest speed
        ch2 = 1750
        input_line = bytes(f'{ch1} {ch2} 0 0 0', encoding='utf-8')
        channel_input = ChannelInput()
        channel_input.read_channel_input(input_line=input_line)

        ch1 = 1670
        ch2 = 1600
        input_line = bytes(f'{ch1} {ch2} 0 0 0', encoding='utf-8')
        channel_input.read_channel_input(input_line=input_line)
        self.motors.right_front_motor(channel_input=channel_input)
        self.assertAlmostEqual(
            self.motors.right_front,
            -0.35,
            msg='Right front motor right diagonal forward different speed has wrong speed multiple')

    def test_right_front_motor_left_diagonal_backward_different_speed(self):
        ch1 = 1150
        # Initial full speed sets the highest speed
        ch2 = 1150
        input_line = bytes(f'{ch1} {ch2} 0 0 0', encoding='utf-8')
        channel_input = ChannelInput()
        channel_input.read_channel_input(input_line=input_line)

        ch1 = 1300
        ch2 = 1230
        input_line = bytes(f'{ch1} {ch2} 0 0 0', encoding='utf-8')
        channel_input.read_channel_input(input_line=input_line)
        self.motors.right_front_motor(channel_input=channel_input)
        self.assertAlmostEqual(
            self.motors.right_front,
            -0.35,
            msg='Right front motor left diagonal backward different speed has wrong speed multiple')
