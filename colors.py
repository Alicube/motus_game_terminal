from colorama import Back, deinit, init

class Colors:

    def __init__(self,letter):
        self.letter_to_color = letter

    
    def red_back(self):
        init()
        red_letter=Back.RED + self.letter_to_color + Back.RESET
        deinit()
        return(red_letter)


    def yellow_back(self):
        init()
        yellow_letter=Back.YELLOW + self.letter_to_color + Back.RESET
        deinit()
        return(yellow_letter)

class DictonnaryTreatement():

    def __init__(self,word_attempted="",w_target=""):
        self.word_to_color = word_attempted
        self.word_target = w_target
    
    def red_letters(self):
        dict_red_letters_count = {}
        for letter_idx in range(len(self.word_to_color)):
            
            letter = self.word_to_color[letter_idx]
            letter_target = self.word_target[letter_idx]
            if letter not in dict_red_letters_count.keys():
                    dict_red_letters_count[letter] = 0
            if letter == letter_target:
                dict_red_letters_count[letter]+=1
        
        return dict_red_letters_count

    def function_dict_word(self):
        dict_word={}
        for i in self.word_target:
            dict_word[i]=self.word_target.count(i)
        return dict_word

class Color_Word(DictonnaryTreatement):

        
    def highlight_the_word(self):
        # creer des dictionnaires qui nous permettront de ne pas surligner des lettres en jaune alors qu'elles sont deja rouge
        dict_red_letters_count=self.red_letters()
        dict_word_target  = self.function_dict_word()
        colored_word = ''
        
        for letter_idx in range(len(self.word_to_color)):
        
            letter = self.word_to_color[letter_idx]
            letter_target = self.word_target[letter_idx]

            letter_to_color = Colors(letter)
            
            if letter in self.word_target:

                # lettre au bon index a surligner en rouge
                if letter == letter_target:
                    colored_word+=letter_to_color.red_back()
                    dict_red_letters_count[letter]-=1 if dict_red_letters_count[letter] else 0
                    dict_word_target[letter]-=1 if dict_word_target[letter] else 0
                    
                else:

                    if  dict_word_target[letter]:
                        if dict_word_target[letter]-dict_red_letters_count[letter] > 0:
                            # lettre pas au bon index a surligner en jaune
                            dict_word_target[letter]-=1  
                            colored_word+=letter_to_color.yellow_back()
                        else:
                            colored_word+=letter
                    else:
                        colored_word+=letter
            
            # lettre pas presente dans le motus_target (le mot recherche)
            else:
                colored_word+=letter
        return(colored_word)