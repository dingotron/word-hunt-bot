"""
word hunt bot
"""
import pickle
import pygtrie 

def main():
    b_size = int(input("Enter the board size (4 for 4x4): "))
    board_string = input("Enter the board string: ").upper().strip()

    board = [board_string[i * b_size:(i + 1) * b_size] for i in range(b_size)]
    print("Board:")
    for row in board:
        print(' '.join(row))

    with open('dict_trie.pkl', 'rb') as f:
        dict_trie = pickle.load(f)

    valid_words = set()
    for i in range(b_size):
        for j in range(b_size):
            dfs(board, [(i, j)], dict_trie, valid_words, b_size)
    
    print("Valid words found:")
    for word in sorted(valid_words, key=lambda x: (len(x), x)):
        print(word)
    print(f"Total valid words: {len(valid_words)}")


def dfs(board, path, dict_trie, valid_words, b_size):
    """ Depth-first search to find all dictionary valid words on the board
    starting from the given path """

    current_word = ''.join(board[i][j] for i, j in path)
    
    if len(current_word) > 2 and dict_trie.has_key(current_word):
        valid_words.add(current_word)

    if not dict_trie.has_subtrie(current_word):
        return

    i, j = path[-1]
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if di == 0 and dj == 0:
                continue
            ni, nj = i + di, j + dj
            if 0 <= ni < b_size and 0 <= nj < b_size and (ni, nj) not in path:
                dfs(board, path + [(ni, nj)], dict_trie, valid_words, b_size)


if __name__ == "__main__":
    main()