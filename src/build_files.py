#!/usr/bin/env python3.10

import argparse 
import os 
import shutil 
from dotenv import load_dotenv

try:
    NUMBER_ROOMS = int(os.environ['NUMBER_ROOMS'])
except:
    NUMBER_ROOMS = 15 

ROOM_TEXT = '''
# @ Uncomment this line to use this text as 'room' text. Leave the leading '@' character.
Text will be saved until the end of the file.
'''


class Writer:



    def __init__(self):
        
        self.verbose = True
        self.phrases = []
        
        parser = argparse.ArgumentParser(description="Bert Chat File Maker", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        parser.add_argument('--name', default='./../data/phrases.txt.orig', help='name for "phrases" input file.')
        parser.add_argument('--list', action='store_true', help='list all possible phrases.')
        parser.add_argument('--verbose', action="store_true", help="print verbose output.")
        parser.add_argument('--write', action="store_true", help="change file contents")
        self.args = parser.parse_args()
        
        self.verbose = self.args.verbose 
        self.list = self.args.list 
        self.write = self.args.write 

    def read_input_file(self):
        with open(self.args.name, "r") as phrases:
            phrase = phrases.readlines()
            for i in phrase:
                p = i.split(";")
                p = [ x.strip() for x in p ]
                self.phrases.append(p)

            pass 
        print(self.phrases)

    def write_output_files(self):
        try: 
            s = os.stat(self.args.name)
        except:
            exit()
        if self.write: 
            shutil.copy(self.args.name, "./../data/phrases.txt")
        for i in range(len(self.phrases) ):
            line_ending = "_" + ("000" + str(i + 1))[-3:] + ".txt"
            if self.verbose: 
                print(line_ending)
            if self.write: 
                with open("./../data/responses" + line_ending, "w") as responses:
                    responses.write("1\n" + self.phrases[i][1] + "\n")
            
        for i in range(NUMBER_ROOMS):
            line_ending = "_" + ("000" + str(i + 1))[-3:] + ".txt"

            if self.write: 
                with open("./../data/room" + line_ending, "w") as rooms:
                    for ii in range(len(self.phrases) ):
                        rooms.write(str(i+ 1) + ";1.0" + "\n")
                    rooms.write(ROOM_TEXT + "\n")


if __name__ == '__main__':
    w = Writer()
    w.read_input_file()
    w.write_output_files()

