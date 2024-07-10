class ChannelInputPosition:

    def __init__(self, low, high, rc_min, rc_max):
        self.neutral_low = low
        self.neutral_high = high
        # Offset by 1 to avoid divide by 0 problem.
        self.lowest = low - 1
        # Offset by 1 to avoid divide by 0 problem.
        self.highest = high + 1
        # rc_min is the lowest possible min value defined for the input.
        self.min = rc_min
        # rc_max is the highest possible max value defined for the input.
        self.max = rc_max

    def __repr__(self):
        return f'Channel neutral position low: {self.neutral_low}, lowest: {self.lowest}, high: {self.neutral_high}, highest: {self.highest}'


class ChannelInput:

    def __init__(self):
        # Index 0 is unused, so that we can have a 1:1 mapping of channel number.
        # Currently tracking channel 1 to 5 only.
        self.channels = [0, 0, 0, 0, 0, 0]
        self.channels_position = [
            None,
            ChannelInputPosition(low=1350, max=1550, rc_min=1200, rc_max=1750),
            ChannelInputPosition(low=1350, max=1550, rc_min=1200, rc_max=1750),
            ChannelInputPosition(low=1900, max=2100, rc_min=1750, rc_max=2250),
            ChannelInputPosition(low=1350, max=1550, rc_min=1200, rc_max=1750),
            ChannelInputPosition(low=800, max=1000, rc_min=800, rc_max=1600),
        ]

    def set_rc_position_boundary(self, channel_input: int,
                                 channel_input_position: ChannelInputPosition):
        if channel_input > channel_input_position.highest:
            channel_input_position.highest = channel_input
            if channel_input_position.highest > channel_input_position.max:
                channel_input_position.highest = channel_input_position.max
        elif channel_input < channel_input_position.lowest:
            channel_input_position.lowest = channel_input
            if channel_input_position.lowest < channel_input_position.min:
                channel_input_position.lowest = channel_input_position.min

    def read_channel_input(self, input_line: bytes):
        line = input_line.decode('utf-8').rstrip()
        # print(line)
        ch_inputs = line.split()
        if len(ch_inputs) >= 5:
            for i, c in enumerate(ch_inputs):
                self.channels[i + 1] = int(c)
                self.set_rc_position_boundary(int(c), self.channels_position[i + 1])

    def __eq__(self, other):
        return self.channels == other.channels

    def __repr__(self):
        return f'ch1: {self.channels[1]}, ch2: {self.channels[2]}, ch3: {self.channels[3]}, ch4: {self.channels[4]}, ch5: {self.channels[5]}'
