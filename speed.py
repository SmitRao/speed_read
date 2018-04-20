'''Speed Reading Program'''

__author__ = "Smit Rao <rao.smit.2@gmail.com>"
__version__ = "0.0.1"
__all__ = ['speed']


"""
This is a speed-reading program for those who are easily distracted and wish to
read at a faster pace.
"""

if __name__ != '__main__':
    raise ImportError('importing this file is prohibited.')

import epub
import time
import enchant
import pygame
import math

def set_word_speed() -> None:
    '''Set a word speed in Words Per Minute.'''
    
    speed = input("Enter your WPM speed:\n> ")
    while (not speed.isnumeric()) or (not 100 <= int(speed) <= 1000):
        speed = input("Please enter an integer between (100, 1000):\n> ")
    WPM = int(speed)
    return 60 / WPM

def opens_correctly(file: str) -> bool:
    '''Return whether file opens correctly; id est no error raised.'''
    
    try:
        test = open(file)
    except FileNotFoundError:
        return False
    else:
        return True        

def choose_file() -> None:
    '''Choose an EPUB-format e-book to read.'''
    
    file = input('Please choose a book to read:\n> ')
    while '.epub' not in file or not opens_correctly(file):
        file = input('Please choose a valid e-book (.epub):\n> ')
    return file
'''
pygame.display.init()

from pygame.locals import *
screen = pygame.display.\
    set_mode((pygame.display.Info().current_w, \
              pygame.display.Info().current_h), FULLSCREEN)
'''

##### CONSTANTS #####

TIME_INTERVAL = set_word_speed() # Converts WPM to decimal seconds.
FILE = choose_file() # Choose EPUB file.
CONTENTS = [] # Contents of e-book (raw). To process before displaying.
PUNCTUATION_END = '.,?!:;}])\'">~*+=-%'
PUNCTUATION_START = '([{\'"<~*=-$%#@'
ENGLISH_DICTIONARY = enchant.Dict("en_US")

##### Add raw data to CONTENTS #####

book = epub.open_epub(FILE)
for item in book.opf.manifest.values():
    CONTENTS.append(book.read_item(item))

######## Begin program #############

for sentence in CONTENTS:
    for candidate_word in sentence.split():
        try:
            word = candidate_word.decode("utf-8")
            if ENGLISH_DICTIONARY.check(word):
                time.sleep(TIME_INTERVAL)
                print(word)
            elif word[0] in PUNCTUATION_START and word[-1] not in PUNCTUATION_END \
            and ENGLISH_DICTIONARY.check(word[1:]):
                time.sleep(TIME_INTERVAL)
                print(word)
            elif word[0] not in PUNCTUATION_START and word[-1] in PUNCTUATION_END \
            and ENGLISH_DICTIONARY.check(word[:-1]):
                time.sleep(TIME_INTERVAL)
                print(word)
            elif word[0] in PUNCTUATION_START and word[-1] in PUNCTUATION_END \
            and ENGLISH_DICTIONARY.check(word[1:-1]):
                time.sleep(TIME_INTERVAL)
                print(word)
        except ValueError:
            pass
        except UnicodeDecodeError:
            pass
        except enchant.errors.Error:
            pass



