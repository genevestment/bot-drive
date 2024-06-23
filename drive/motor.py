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

    def left_front_motor(self, channel_input):
        ch1_left_front = 0.0
        ch2_left_front = 0.0
        if channel_input.channels[1] > channel_input.channels_position[1].neutral_high:
            ch1_left_front = self.bounded_motor_speed(
                (channel_input.channels[1] - channel_input.channels_position[1].neutral_high) /
                (channel_input.channels_position[1].highest -
                 channel_input.channels_position[1].neutral_high))
        elif channel_input.channels[1] < channel_input.channels_position[1].neutral_low:
            ch1_left_front = self.bounded_motor_speed(
                (channel_input.channels[1] - channel_input.channels_position[1].neutral_low) /
                (channel_input.channels_position[1].neutral_low -
                 channel_input.channels_position[1].lowest))

        if channel_input.channels[2] > channel_input.channels_position[2].neutral_high:
            ch2_left_front = self.bounded_motor_speed(
                (channel_input.channels[2] - channel_input.channels_position[2].neutral_high) /
                (channel_input.channels_position[2].highest -
                 channel_input.channels_position[2].neutral_high))
        elif channel_input.channels[2] < channel_input.channels_position[2].neutral_low:
            ch2_left_front = self.bounded_motor_speed(
                (channel_input.channels[2] - channel_input.channels_position[2].neutral_low) /
                (channel_input.channels_position[2].neutral_low -
                 channel_input.channels_position[2].lowest))

        if ch1_left_front <= 0 and ch2_left_front <= 0:
            self.left_front = min(ch1_left_front, ch2_left_front)
        elif ch1_left_front >= 0 and ch2_left_front >= 0:
            self.left_front = max(ch1_left_front, ch2_left_front)
        elif (ch1_left_front <= 0 and ch2_left_front >= 0) or (ch1_left_front >= 0 and
                                                               ch2_left_front <= 0):
            self.left_front = ch2_left_front + ch1_left_front

    def right_front_motor(self, channel_input):
        ch1_right_front = 0.0
        ch2_right_front = 0.0
        print(f'channels = {channel_input.channels}')
        print(f'channel positions = {channel_input.channels_position}')
        if channel_input.channels[1] > channel_input.channels_position[1].neutral_high:
            ch1_right_front = self.bounded_motor_speed(
                (channel_input.channels_position[1].neutral_high - channel_input.channels[1]) /
                (channel_input.channels_position[1].highest -
                 channel_input.channels_position[1].neutral_high))
        elif channel_input.channels[1] < channel_input.channels_position[1].neutral_low:
            ch1_right_front = self.bounded_motor_speed(
                (channel_input.channels_position[1].neutral_low - channel_input.channels[1]) /
                (channel_input.channels_position[1].neutral_low -
                 channel_input.channels_position[1].lowest))

        if channel_input.channels[2] > channel_input.channels_position[2].neutral_high:
            ch2_right_front = self.bounded_motor_speed(
                (channel_input.channels[2] - channel_input.channels_position[2].neutral_high) /
                (channel_input.channels_position[2].highest -
                 channel_input.channels_position[2].neutral_high))
        elif channel_input.channels[2] < channel_input.channels_position[2].neutral_low:
            ch2_right_front = self.bounded_motor_speed(
                (channel_input.channels[2] - channel_input.channels_position[2].neutral_low) /
                (channel_input.channels_position[2].neutral_low -
                 channel_input.channels_position[2].lowest))

        print(f'ch1 right front = {ch1_right_front}, ch2 right front = {ch2_right_front}')
        if ch1_right_front <= 0 and ch2_right_front <= 0:
            self.right_front = min(ch1_right_front, ch2_right_front)
        elif ch1_right_front >= 0 and ch2_right_front >= 0:
            self.right_front = max(ch1_right_front, ch2_right_front)
        elif (ch1_right_front <= 0 and ch2_right_front >= 0) or (ch1_right_front >= 0 and
                                                                 ch2_right_front <= 0):
            self.right_front = ch2_right_front + ch1_right_front

    def left_back_motor(self, channel_input):
        ch1_left_back = 0.0
        ch2_left_back = 0.0

        if channel_input.channels[1] > channel_input.channels_position[1].neutral_high:
            ch1_left_back = self.bounded_motor_speed(
                (channel_input.channels_position[1].neutral_high - channel_input.channels[1]) /
                (channel_input.channels_position[1].highest -
                 channel_input.channels_position[1].neutral_high))
        elif channel_input.channels[1] < channel_input.channels_position[1].neutral_low:
            ch1_left_back = self.bounded_motor_speed(
                (channel_input.channels_position[1].neutral_low - channel_input.channels[1]) /
                (channel_input.channels_position[1].neutral_low -
                 channel_input.channels_position[1].lowest))

        if channel_input.channels[2] > channel_input.channels_position[2].neutral_high:
            ch2_left_back = self.bounded_motor_speed(
                (channel_input.channels[2] - channel_input.channels_position[2].neutral_high) /
                (channel_input.channels_position[2].highest -
                 channel_input.channels_position[2].neutral_high))
        elif channel_input.channels[2] < channel_input.channels_position[2].neutral_low:
            ch2_left_back = self.bounded_motor_speed(
                (channel_input.channels[2] - channel_input.channels_position[2].neutral_low) /
                (channel_input.channels_position[2].neutral_low -
                 channel_input.channels_position[2].lowest))

        self.left_back = max(ch1_left_back, ch2_left_back)

    def right_back_motor(self, channel_input):
        ch1_right_back = 0.0
        ch2_right_back = 0.0

        if channel_input.channels[1] > channel_input.channels_position[1].neutral_high:
            ch1_right_back = self.bounded_motor_speed(
                (channel_input.channels[1] - channel_input.channels_position[1].neutral_high) /
                (channel_input.channels_position[1].highest -
                 channel_input.channels_position[1].neutral_high))
        elif channel_input.channels[1] < channel_input.channels_position[1].neutral_low:
            ch1_right_back = self.bounded_motor_speed(
                (channel_input.channels[1] - channel_input.channels_position[1].neutral_low) /
                (channel_input.channels_position[1].neutral_low -
                 channel_input.channels_position[1].lowest))

        if channel_input.channels[2] > channel_input.channels_position[2].neutral_high:
            ch2_right_back = self.bounded_motor_speed(
                (channel_input.channels[2] - channel_input.channels_position[2].neutral_high) /
                (channel_input.channels_position[2].highest -
                 channel_input.channels_position[2].neutral_high))
        elif channel_input.channels[2] < channel_input.channels_position[2].neutral_low:
            ch2_right_back = self.bounded_motor_speed(
                (channel_input.channels[2] - channel_input.channels_position[2].neutral_low) /
                (channel_input.channels_position[2].neutral_low -
                 channel_input.channels_position[2].lowest))

        self.left_front = max(ch1_right_back, ch2_right_back)

    def manual_drive(self, channel_input):
        print(f'Manual drive with input: {channel_input}')
        self.left_front_motor(channel_input)
        self.right_front_motor(channel_input)
        self.left_back_motor(channel_input)
        self.right_back_motor(channel_input)

    def stop(self):
        self.left_front = 0
        self.left_back = 0
        self.right_front = 0
        self.right_back = 0
