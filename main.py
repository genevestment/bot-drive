import serial
import time

from drive.motor import Motors
from drive.remote_control import ChannelInput


def init_hardware():
    ser = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=1)
    ser.flush()
    ser.reset_input_buffer()
    return ser


def read_rc_input(ser, channel_input: ChannelInput):
    if ser.in_waiting > 0:
        channel_input.read_channel_input(ser.readline())
    return channel_input


def main():
    ser = init_hardware()
    channel_input = ChannelInput()
    motors = Motors()
    while True:
        try:
            channel_input = read_rc_input(ser, channel_input)
            # Debounce unstable signal, use multiple channels to double check.
            if int(channel_input.channels[1]) == 0 or int(channel_input.channels[5]) == 0:
                continue
        except Exception as e:
            print(f'Error reading RC input: {e}')

        if channel_input and channel_input.channels[5] < 1100:
            motors.manual_drive(channel_input=channel_input)
            print(f'Motors status\n{motors}\n')
        else:
            print('auto drive')

        # Necessary buffer delay to allow time for the RC input to read new data.
        time.sleep(0.02)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Stopped by user')
