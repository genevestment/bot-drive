import unittest

from drive.remote_control import ChannelInput, ChannelInputPosition


class RemoteControlTest(unittest.TestCase):

    def setUp(self):
        self.channel_input = ChannelInput()

    def test_read_channel_input_ok(self):
        input_line = bytes('100 200 300 400 500', encoding='utf-8')
        self.channel_input.read_channel_input(input_line=input_line)
        want = ChannelInput()
        want.channels = [0, 100, 200, 300, 400, 500]
        want.channels_position = [
            None,
            ChannelInputPosition(100, 1550),
            ChannelInputPosition(200, 1550),
            ChannelInputPosition(300, 2100),
            ChannelInputPosition(400, 1550),
            ChannelInputPosition(500, 1000),
        ]
        self.assertEqual(self.channel_input, want, 'Channel input has incorrect values')
