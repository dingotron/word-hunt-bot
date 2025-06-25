"""
creates the dictionary trie
"""

import pickle
import pygtrie

def create_dict_trie():
    """
    Creates a dictionary trie from the words in the file 'dict.txt'.
    The trie is saved to 'dict_trie.pkl'.
    """
    with open('CSW22.txt', 'r') as f:
        words = [line.strip() for line in f if line.strip()]

    trie = pygtrie.CharTrie()
    for word in words:
        trie[word] = True

    with open('dict_trie.pkl', 'wb') as f:
        pickle.dump(trie, f)

if __name__ == '__main__':
    create_dict_trie()
    print("Dictionary trie created and saved to 'dict_trie.pkl'.")
