# terminal_controlled_bot_wireless_encrypted.py

from cyberbot import *
import radio

def ascii_shift(key, text):
    result = ""
    for letter in text:
        ascii = ( ord(letter) + key - 32 ) % 94 + 32
        result = result + chr(ascii)
    return result
    
key = 5

radio.on()
radio.config(channel=7,length=64)

sleep(1000)

print("Ready...\n")

while True:
    packet = radio.receive()
    if packet is not None:
        print("Receive encrypted: ", packet)
        
        packet = ascii_shift(key, packet)
        
        print("packet: ", packet)

        dictionary = eval(packet)

        vL = dictionary['vL']
        vR = dictionary['vR']
        ms = dictionary['ms']
        
        bot(18).servo_speed(vL)
        bot(19).servo_speed(-vR)
        sleep(ms)
        bot(18).servo_speed(None)
        bot(19).servo_speed(None)