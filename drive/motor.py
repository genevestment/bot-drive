import pigpio

_MOTOR_NEUTRAL = 192


class Motors:

    def __init__(self):
        self.left_front = 0
        self.left_back = 0
        self.right_front = 0
        self.right_back = 0

    def __repr__(self):
        return f'Left front: {self.left_front}, right front: {self.right_front}, left back: {self.left_back}, right back: {self.right_back}'

    def bounded_motor_speed(self, x: float) -> float:
        if x > 1.0:
            return 1.0
        elif x < -1.0:
            return -1.0
        return x

    # up right wheel orientation defines the mecanum wheel who's rolling direction is towards
    # the up and right direction. This applies to the left front wheel and right back wheel.
    # They have the same orientation and rotation.
    def _up_right_wheel_orientation_drive(self, channel_input) -> float:
        ch1_speed_multiplier = 0.0
        ch2_speed_multiplier = 0.0
        speed_multiplier = 0.0
        if channel_input.channels[1] > channel_input.channels_position[1].neutral_high:
            ch1_speed_multiplier = self.bounded_motor_speed(
                (channel_input.channels[1] - channel_input.channels_position[1].neutral_high) /
                (channel_input.channels_position[1].highest -
                 channel_input.channels_position[1].neutral_high))
        elif channel_input.channels[1] < channel_input.channels_position[1].neutral_low:
            ch1_speed_multiplier = self.bounded_motor_speed(
                (channel_input.channels[1] - channel_input.channels_position[1].neutral_low) /
                (channel_input.channels_position[1].neutral_low -
                 channel_input.channels_position[1].lowest))

        if channel_input.channels[2] > channel_input.channels_position[2].neutral_high:
            ch2_speed_multiplier = self.bounded_motor_speed(
                (channel_input.channels[2] - channel_input.channels_position[2].neutral_high) /
                (channel_input.channels_position[2].highest -
                 channel_input.channels_position[2].neutral_high))
        elif channel_input.channels[2] < channel_input.channels_position[2].neutral_low:
            ch2_speed_multiplier = self.bounded_motor_speed(
                (channel_input.channels[2] - channel_input.channels_position[2].neutral_low) /
                (channel_input.channels_position[2].neutral_low -
                 channel_input.channels_position[2].lowest))

        if ch1_speed_multiplier <= 0 and ch2_speed_multiplier <= 0:
            speed_multiplier = min(ch1_speed_multiplier, ch2_speed_multiplier)
        elif ch1_speed_multiplier >= 0 and ch2_speed_multiplier >= 0:
            speed_multiplier = max(ch1_speed_multiplier, ch2_speed_multiplier)
        elif (ch1_speed_multiplier <= 0 and
              ch2_speed_multiplier >= 0) or (ch1_speed_multiplier >= 0 and
                                             ch2_speed_multiplier <= 0):
            speed_multiplier = ch1_speed_multiplier + ch2_speed_multiplier
        return speed_multiplier

    # up left wheel orientation defines the mecanum wheel who's rolling direction is towards
    # the up and left direction. This applies to the right front wheel and left back wheel.
    # They have the same orientation and rotation.
    def _up_left_wheel_orientation_drive(self, channel_input) -> float:
        ch1_speed_multiplier = 0.0
        ch2_speed_multiplier = 0.0
        speed_multiplier = 0.0
        if channel_input.channels[1] > channel_input.channels_position[1].neutral_high:
            ch1_speed_multiplier = self.bounded_motor_speed(
                (channel_input.channels_position[1].neutral_high - channel_input.channels[1]) /
                (channel_input.channels_position[1].highest -
                 channel_input.channels_position[1].neutral_high))
        elif channel_input.channels[1] < channel_input.channels_position[1].neutral_low:
            ch1_speed_multiplier = self.bounded_motor_speed(
                (channel_input.channels_position[1].neutral_low - channel_input.channels[1]) /
                (channel_input.channels_position[1].neutral_low -
                 channel_input.channels_position[1].lowest))

        if channel_input.channels[2] > channel_input.channels_position[2].neutral_high:
            ch2_speed_multiplier = self.bounded_motor_speed(
                (channel_input.channels[2] - channel_input.channels_position[2].neutral_high) /
                (channel_input.channels_position[2].highest -
                 channel_input.channels_position[2].neutral_high))
        elif channel_input.channels[2] < channel_input.channels_position[2].neutral_low:
            ch2_speed_multiplier = self.bounded_motor_speed(
                (channel_input.channels[2] - channel_input.channels_position[2].neutral_low) /
                (channel_input.channels_position[2].neutral_low -
                 channel_input.channels_position[2].lowest))

        if ch1_speed_multiplier <= 0 and ch2_speed_multiplier <= 0:
            speed_multiplier = min(ch1_speed_multiplier, ch2_speed_multiplier)
        elif ch1_speed_multiplier >= 0 and ch2_speed_multiplier >= 0:
            speed_multiplier = max(ch1_speed_multiplier, ch2_speed_multiplier)
        elif (ch1_speed_multiplier <= 0 and
              ch2_speed_multiplier >= 0) or (ch1_speed_multiplier >= 0 and
                                             ch2_speed_multiplier <= 0):
            speed_multiplier = ch1_speed_multiplier + ch2_speed_multiplier
        return speed_multiplier

    def _up_left_wheel_speed(self, pi, pin, speed_multiplier):
        speed = _MOTOR_NEUTRAL + (speed_multiplier * 60)
        print(f'{pin} speed: {speed}')
        if speed <= 0:
            speed = 1
        elif speed >= 255:
            speed = 254
        pi.set_PWM_dutycycle(pin, int(speed))

    def _up_right_wheel_speed(self, pi, pin, speed_multiplier):
        speed = _MOTOR_NEUTRAL - (speed_multiplier * 60)
        print(f'{pin} speed: {speed}')
        if speed <= 0:
            speed = 1
        elif speed >= 255:
            speed = 254
        pi.set_PWM_dutycycle(pin, int(speed))

    def left_front_motor(self, pi, channel_input, controller_pin):
        self.left_front = round(self._up_right_wheel_orientation_drive(channel_input=channel_input),
                                2)
        print(f'left front = {self.left_front}')
        self._up_left_wheel_speed(pi=pi, pin=controller_pin, speed_multiplier=self.left_front)

    def right_front_motor(self, pi, channel_input, controller_pin):
        self.right_front = round(self._up_left_wheel_orientation_drive(channel_input=channel_input),
                                 2)
        print(f'right front = {self.right_front}')
        self._up_right_wheel_speed(pi=pi, pin=controller_pin, speed_multiplier=self.right_front)

    def left_back_motor(self, pi, channel_input, controller_pin):
        self.left_back = round(self._up_left_wheel_orientation_drive(channel_input=channel_input),
                               2)
        print(f'left back = {self.left_back}')
        self._up_right_wheel_speed(pi=pi, pin=controller_pin, speed_multiplier=self.left_back)

    def right_back_motor(self, pi, channel_input, controller_pin):
        self.right_back = round(self._up_right_wheel_orientation_drive(channel_input=channel_input),
                                2)
        print(f'right back = {self.right_back}')
        self._up_left_wheel_speed(pi=pi, pin=controller_pin, speed_multiplier=self.right_back)

    def manual_drive(self, pi, channel_input, controller_pins):
        # print(f'Manual drive with input: {channel_input}')
        # Group left front and right back in a pair.
        self.left_front_motor(pi=pi,
                              channel_input=channel_input,
                              controller_pin=controller_pins['left_front'])
        self.right_back_motor(pi=pi,
                              channel_input=channel_input,
                              controller_pin=controller_pins['right_back'])
        # Group right front and left back in a pair.
        self.right_front_motor(pi=pi,
                               channel_input=channel_input,
                               controller_pin=controller_pins['right_front'])
        self.left_back_motor(pi=pi,
                             channel_input=channel_input,
                             controller_pin=controller_pins['left_back'])

    def stop(self):
        self.left_front = 0
        self.left_back = 0
        self.right_front = 0
        self.right_back = 0
