# collects input-output mapping from an IME

from pynput.keyboard import Key, Controller
import time
import itertools
from pathlib import Path
import os
from datetime import datetime
import string
from threading import Lock, Thread


my_dir = Path(os.path.dirname(__file__))

now_time = datetime.now()
output_filename = my_dir/now_time.strftime('record_%m_%d__%H_%M')
output_file = open(output_filename, 'w')

key_candidates = string.ascii_lowercase[:-1] # no z
#code_lengths = [1,2,3,4]
code_lengths = [4]
start_pos = 'yuba' # start code pos
selection_attempt = 5
flush_count = 1000


line_count = 0
sync_lock = Lock()
current_phrase = ''
receiving = True
finished = False
skip_keys = False


def key_sender():
    global current_phrase, receiving, finished, start_pos, skip_keys
    keyboard = Controller()

    time.sleep(2.0)
    
    for code_length in code_lengths:
        for keys in itertools.product(key_candidates, repeat=code_length):

            if start_pos is not None:
                if ''.join(keys) != start_pos:
                    continue
                else:
                    start_pos = None

            for num in range(1, 1 + selection_attempt):

                
                while not receiving:
                    time.sleep(0.000001)

                if skip_keys:
                    skip_keys = False
                    break
                
                current_phrase = '{} {}'.format(''.join(keys), num)

                for key in keys:
                    keyboard.press(key)
                    keyboard.release(key)
                keyboard.press(str(num))
                keyboard.release(str(num))
                keyboard.press(Key.space)
                keyboard.release(Key.space)
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)

                receiving = False


    finished = True

t = Thread(target=key_sender)
t.start()

while True:
    receiving = True
    inp = input()
    inp = inp.strip()
    
    if inp[-1] in string.digits:
        skip_keys = True
    
    output_file.write(current_phrase + f' {inp.strip()}\n')

    line_count += 1
    if line_count % flush_count == 0:
        output_file.flush()


    if finished:
        break
    

output_file.close()