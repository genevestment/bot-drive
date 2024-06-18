import unittest

from drive.remote_control import ChannelInput


class RemoteControlTest(unittest.TestCase):

    def setUp(self):
        self.channel_input = ChannelInput()

    def test_read_channel_input_ok(self):
        input_line = bytes('100 200 300 400 500', encoding='utf-8')
        self.channel_input.read_channel_input(input_line=input_line)
        want = ChannelInput()
        want.ch1, want.ch2, want.ch3, want.ch4, want.ch5 = ('100', '200', '300', '400', '500')
        self.assertEqual(self.channel_input, want, 'Channel input has incorrect values')
