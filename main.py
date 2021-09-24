import random

class FileReader:
    def __init__(self) -> None:
        pass
    
    def read_file(self, file_path: str) -> list:
        
        word_list = []
        
        with open(file_path, 'r') as f:
            for line in f:
                word_list.append(line.strip())
        
        return word_list
    

class WordFactory:
    def __init__(self, word_list: list, user_input: list) -> None:
        
        self.user_input = user_input
        self.word_list = word_list
        
    def organize_words(self) -> dict:
        
        word_index = {}
        
        for word in self.word_list:
            
            word_length = len(word)
            
            if word_length in word_index:
                word_index[word_length].append(word)
            
            else:
                word_index[word_length] = [word]
        
                
        return word_index
    
    
    
    def phrase_builder(self) -> list:
        
        matches = self.organize_words()
        new_sentence = list()
        
        for word in self.user_input:
            
            possible_matches = list()
            
            if len(word) in matches:
                
                for words in matches[len(word)]:
                    
                    if words.startswith(word[0]) and len(words) == len(word):
                        possible_matches.append(words)
            else:
                
                print(f'No possible substitute found for "{word}"')
                possible_matches.append(word)
            
            if len(possible_matches) > 1:
                random_word = random.randint(0, len(possible_matches) - 1)
                
            else:
                random_word = 0
            
            new_word_choice = possible_matches[random_word]
            
            new_sentence.append(new_word_choice)
            
        return new_sentence
            

        
    
    
                
class InputFactory:
    def __init__(self) -> None:
        
        self.user_input = str(input("Please enter your phrase: "))
        
    def input_collection(self) -> list:
        return self.user_input.split()
        
    

class SentenceOutput:
    def __init__(self) -> None: 
        pass

    def phase_builder(self, new_sentence: list) -> str:
        
        output = ' '.join(new_sentence)
            
        print('\nresult:', output)
        
    
if __name__ == '__main__':
    
    print("#############################################################")
    print("There is no need to capitalize the beginning of your sentence")
    print("#############################################################\n")
    Game = True
    while Game:
        
        r = FileReader()
        word_list = r.read_file("./word_list.txt")
        
        i = InputFactory()
        user_input = i.input_collection()
        
        w = WordFactory(word_list, user_input)
        new_sentence = w.phrase_builder()
        
        output = SentenceOutput()
        output.phase_builder(new_sentence)
    
        game = input("\nWould you like to continue? Y/N ")
        
        if game.lower() == ('y' or 'yes'):
            continue
        else:
            Game = False
    
