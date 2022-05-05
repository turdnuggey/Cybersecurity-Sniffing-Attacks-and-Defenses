# terminal_bot_controller_wireless_encrypted.py

from microbit import *
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

print("\nSpeeds are -100 to 100\n")

while True:
    vL = int(input("Enter left speed: "))
    vR = int(input("Enter right speed: "))
    ms = int(input("Enter ms to run: "))
    
    dictionary = {  }
    dictionary['vL'] = vL
    dictionary['vR'] = vR
    dictionary['ms'] = ms

    packet = str(dictionary)
    
    print("packet: ", packet)
    
    packet = ascii_shift(key, packet)
    
    print("packet: ", packet)
    radio.send(packet)
    
    print()