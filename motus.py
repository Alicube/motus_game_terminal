import random
from colors import *
from variables import *
from words import Words
from treatment import *


#importation des mots de la liste proposee
word = Words(words_file)
words_allowed = word.get_words_list()

words_to_print=[]

word_target = random.choice(words_allowed)

nb_of_attempts = 1
play = True


while play:

    word_attempted = input(Input_word).upper() 

    game = Game(w_attempted = word_attempted,
                w_target=word_target,
                w_to_print=words_to_print,
                w_in_file=words_allowed,
                attempt=nb_of_attempts)
                
                

    play = game.play()

    nb_of_attempts+=1