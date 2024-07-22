import pigpio
import serial
# import RPi.GPIO as GPIO
import time

from drive.motor import Motors
from drive.remote_control import ChannelInput

controller_pins = {
    'left_front': 26,  # GPIO 26, physical pin 37, left front motor controller
    'right_front': 19,  # GPIO 19, physical pin 35, right front motor controller
    'left_back': 6,  # GPIO 13, physical pin 31, left back motor controller
    'right_back': 13,  # GPIO 6, physical pin 33, right back motor controller
}


def init_hardware():
    ser = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=1)
    ser.flush()
    ser.reset_input_buffer()
    pi = pigpio.pi()
    for _, pin in controller_pins.items():
        pi.set_mode(pin, pigpio.OUTPUT)
        pi.set_PWM_frequency(pin, 500)
        pi.set_PWM_range(pin, 255)

    return ser, pi


def read_rc_input(ser, channel_input: ChannelInput):
    if ser.in_waiting > 0:
        channel_input.read_channel_input(ser.readline())
    return channel_input


def main():
    ser, pi = init_hardware()
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
            motors.manual_drive(pi=pi, channel_input=channel_input, controller_pins=controller_pins)
            print(f'Motors status: {motors}')
        else:
            print('auto drive')

        # Necessary buffer delay to allow time for the RC input to read new data.
        time.sleep(0.02)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Stopped by user')
