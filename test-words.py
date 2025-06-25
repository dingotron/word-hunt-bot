import pickle
import pygtrie

def main():
    # testing plural words in the dictionary
    # load the dictionary trie
    with open('dict_trie.pkl', 'rb') as f:
        dict_trie = pickle.load(f)
    
    # input word to test
    while True:
        word = input("Enter a word to test: ").upper().strip()

        if dict_trie.has_key(word):
            print(f"{word} : YES")
        else:
            print(f"{word} : NO")
        
        if word == "QUIT":
            break
if __name__ == "__main__":
    main()