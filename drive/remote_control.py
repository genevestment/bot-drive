class ChannelInput:

    def __init__(self):
        self.ch1 = 0
        self.ch2 = 0
        self.ch3 = 0
        self.ch4 = 0
        self.ch5 = 0

    def read_channel_input(self, input_line: bytes):
        line = input_line.decode('utf-8').rstrip()
        # print(line)
        ch_inputs = line.split()
        if len(ch_inputs) >= 5:
            self.ch1, self.ch2, self.ch3, self.ch4, self.ch5 = ch_inputs

    def __eq__(self, other):
        return self.ch1 == other.ch1 \
            and self.ch2 == other.ch2 \
            and self.ch3 == other.ch3 \
            and self.ch4 == other.ch4 \
            and self.ch5 == other.ch5

    def __repr__(self):
        return f'ch1: {self.ch1}, ch2: {self.ch2}, ch3: {self.ch3}, ch4: {self.ch4}, ch5: {self.ch5}'
