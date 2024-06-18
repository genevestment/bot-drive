from drive.remote_control import ChannelInput


class Motors:

    def __init__(self):
        self.left_front = 0
        self.left_back = 0
        self.right_front = 0
        self.right_back = 0

    def __repr__(self):
        return f'Left front: {self.left_front}, right front: {self.right_front}, left back: {self.left_back}, right back: {self.right_back}'

    def left_front_motor(self, ch1, ch2, ch3, ch4):
        pass

    def right_front_motor(self, ch1, ch2, ch3, ch4):
        pass

    def left_back_motor(self, ch1, ch2, ch3, ch4):
        pass

    def right_back_motor(self, ch1, ch2, ch3, ch4):
        pass

    def manual_drive(self, channel_input: ChannelInput):
        print(f'Manual drive with input: {channel_input}')

    def stop(self):
        self.left_front = 0
        self.left_back = 0
        self.right_front = 0
        self.right_back = 0
