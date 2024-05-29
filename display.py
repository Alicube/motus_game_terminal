import time

class Display():

    def __init__(self,w_to_print,sleep):
        self.words_to_print = w_to_print
        self.sleep_time = sleep

    def print_time(self,word):        
        for letter in word:
            print(letter, end='',flush=True)
            time.sleep(self.sleep_time)

    def printf(self):
        print(*self.words_to_print[:-1],sep="\n")
        self.print_time(self.words_to_print[-1])
