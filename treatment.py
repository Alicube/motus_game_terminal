from colors import *
from display import *
from variables import *

class Game:

    def __init__(self,w_attempted,w_target,w_to_print,w_in_file,attempt):

        self.word_attempted =w_attempted
        self.word_target = w_target
        self.words_to_print = w_to_print
        self.words_allowed = w_in_file
        self.nb_of_attempts = attempt
    
    def play(self):

        # Si le mot n'existe pas dans la liste porposee, qu'on considere comme etant le dictionnaire français, alors le joueur a perdu
        if self.word_attempted not in self.words_allowed:
            print(inexistant_word_message)
            return False

        # surligner les lettres du mot tenté jaune,rouge ou rien
        word_attempted_to_color = Color_Word(self.word_attempted,self.word_target)
        word_attempted_colored = word_attempted_to_color.highlight_the_word()
        
        
        # enregistrer les mots tentés dans la liste words_to_print
        self.words_to_print.append(word_attempted_colored)


        # afficher les mots tentés
        words_to_print = Display(self.words_to_print,sleep_time)
        words_to_print.printf()

        
        # si le mot tenté est celui qu'il fallait trouver, le jeu est fini, et le joueur a gagne
        if self.word_attempted == self.word_target:
            print(bravo_message)
            return False
        
        # si le mot n'est pas trouve et qu'on a le nombre de tentatives égale au nombre de tentatives max autorisees, alors le joeur a perdu
        if  self.nb_of_attempts == attempts_max:
            print(no_more_attempts_message)
            return False
        
        return True