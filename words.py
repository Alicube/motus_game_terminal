import os

class Words:
    
    def __init__(self,f_path):
        self.file_path = f_path
    
    def get_words_list(self):
        if not os.path.isfile(self.file_path):
            return []
        words_list = [''.join(filter(str.isalpha, i)) for i in open(self.file_path,"r").readlines()]
        return words_list