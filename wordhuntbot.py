"""
word hunt bot
"""
import pickle
import pygtrie 

def main():
    board_string = input("Enter the board string: ").upper().strip()

    board = [board_string[i:i+4] for i in range(0, 16, 4)]
    print("Board:")
    for row in board:
        print(' '.join(row))

    with open('dict_trie.pkl', 'rb') as f:
        dict_trie = pickle.load(f)

    valid_words = set()
    for i in range(4):
        for j in range(4):
            dfs(board, [(i, j)], dict_trie, valid_words)
    
    print("Valid words found:")
    for word in sorted(valid_words, key=lambda x: (len(x), x)):
        print(word)


def dfs(board, path, dict_trie, valid_words):
    """ Depth-first search to find all dictionary valid words on the board
    starting from the given path """

    current_word = ''.join(board[i][j] for i, j in path)
    
    if dict_trie.has_key(current_word):
        valid_words.add(current_word)

    if not dict_trie.has_subtrie(current_word):
        return

    i, j = path[-1]
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if di == 0 and dj == 0:
                continue
            ni, nj = i + di, j + dj
            if 0 <= ni < 4 and 0 <= nj < 4 and (ni, nj) not in path:
                dfs(board, path + [(ni, nj)], dict_trie, valid_words)


if __name__ == "__main__":
    main()