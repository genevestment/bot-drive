import unittest

from drive.remote_control import ChannelInput, ChannelInputPosition


class RemoteControlTest(unittest.TestCase):

    def setUp(self):
        self.channel_input = ChannelInput()

    def test_read_channel_input_ok(self):
        input_line = bytes('1400 1400 1900 1500 900', encoding='utf-8')
        self.channel_input.read_channel_input(input_line=input_line)
        want = ChannelInput()
        want.channels = [0, 1400, 1400, 1900, 1500, 900]
        want.channels_position = [
            None,
            ChannelInputPosition(low=1350, high=1550, rc_min=1200, rc_max=1750),
            ChannelInputPosition(low=1350, high=1550, rc_min=1200, rc_max=1750),
            ChannelInputPosition(low=1900, high=2100, rc_min=1750, rc_max=2250),
            ChannelInputPosition(low=1350, high=1550, rc_min=1200, rc_max=1750),
            ChannelInputPosition(low=800, high=1000, rc_min=800, rc_max=1600),
        ]
        self.assertEqual(self.channel_input, want, 'Channel input has incorrect values')

    def test_read_channel_input_below_min(self):
        input_line = bytes('1000 1400 1500 1300 900', encoding='utf-8')
        self.channel_input.read_channel_input(input_line=input_line)
        want = ChannelInput()
        want.channels = [0, 1000, 1400, 1500, 1300, 900]
        want.channels_position = [
            None,
            ChannelInputPosition(low=1350, high=1550, rc_min=1200, rc_max=1750),
            ChannelInputPosition(low=1350, high=1550, rc_min=1200, rc_max=1750),
            ChannelInputPosition(low=1900, high=2100, rc_min=1750, rc_max=2250),
            ChannelInputPosition(low=1350, high=1550, rc_min=1200, rc_max=1750),
            ChannelInputPosition(low=800, high=1000, rc_min=800, rc_max=1600),
        ]
        want.channels_position[1].lowest = 1200
        want.channels_position[2].lowest = 1349
        want.channels_position[3].lowest = 1750
        want.channels_position[4].lowest = 1300
        want.channels_position[5].lowest = 799
        want.channels_position[1].highest = 1551
        want.channels_position[2].highest = 1551
        want.channels_position[3].highest = 2101
        want.channels_position[4].highest = 1551
        want.channels_position[5].highest = 1001
        self.assertEqual(self.channel_input, want,
                         'Channel input with lower than min has incorrect values')

    def test_read_channel_input_above_max(self):
        input_line = bytes('1900 1400 2200 1300 900', encoding='utf-8')
        self.channel_input.read_channel_input(input_line=input_line)
        want = ChannelInput()
        want.channels = [0, 1900, 1400, 2200, 1300, 900]
        want.channels_position = [
            None,
            ChannelInputPosition(low=1350, high=1550, rc_min=1200, rc_max=1750),
            ChannelInputPosition(low=1350, high=1550, rc_min=1200, rc_max=1750),
            ChannelInputPosition(low=1900, high=2100, rc_min=1750, rc_max=2250),
            ChannelInputPosition(low=1350, high=1550, rc_min=1200, rc_max=1750),
            ChannelInputPosition(low=800, high=1000, rc_min=800, rc_max=1600),
        ]
        want.channels_position[1].lowest = 1349
        want.channels_position[2].lowest = 1349
        want.channels_position[3].lowest = 1899
        want.channels_position[4].lowest = 1300
        want.channels_position[5].lowest = 799
        want.channels_position[1].highest = 1750
        want.channels_position[2].highest = 1551
        want.channels_position[3].highest = 2200
        want.channels_position[4].highest = 1551
        want.channels_position[5].highest = 1001
        self.assertEqual(self.channel_input, want,
                         'Channel input with lower than min has incorrect values')
