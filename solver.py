import os

folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'wordlists')
self_provided = os.path.join(folder, 'dictionary.txt')
enable_path = os.path.join(folder, 'enable1.txt')

if os.path.exists(self_provided):
    word_list_path = self_provided
else:
    word_list_path = enable_path

print(f'Using word list: {os.path.basename(word_list_path)}')

with open(word_list_path, 'r') as f:
    dictionary = f.read().split()

dictionary = [x.lower() for x in dictionary if len(x) >2 and len(x) < 17]

trie = {}

board = []
rows = []

for row_number in range(1, 5):
    row = input(f'Row {row_number}: ').lower()

    while not (row.isalpha() and len(row) == 4):
        row = input('Try again: ').lower()

    rows.append(row)
    board += row

print('\nYour Board:')
for row in rows:
    print(' '.join(row))
print()

for word in dictionary:
    current = trie
    for char in word:
        if char not in current:
            current[char] = {}
        current = current[char]
    current['*'] = True


def create_board(board):
    x = 1
    y = 1
    lits = []
    for letter in board:
        if x > 4:
            x = 1
            y += 1
        lits = lits + [Letters(letter, x, y)]
        x +=1

    for i in range(len(lits)):
        for j in range(len(lits)):
            if abs(lits[i].x - lits[j].x) <= 1 and abs(lits[i].y - lits[j].y) <= 1:
                if lits[j] not in lits[i].neighbors and not lits[j] is lits[i]:
                    lits[i].neighbors += [lits[j]]
    return lits


class Letters:

    def __init__ (self, char, x, y):
        self.char = char
        self.x = x
        self.y = y
        self.neighbors = []

def solver(board):
    words_list = set()
    x = create_board(board)
    def helper(letter, current_trie, cul_letters, used):
        if letter.char not in current_trie:
            return
        
        current_trie = current_trie[letter.char]
        cul_letters = cul_letters + [letter.char]
        used = used + [letter]

        if '*' in current_trie:
            words_list.add(''.join(cul_letters))

        for neighbor in letter.neighbors:
            if neighbor not in used:
                helper(neighbor, current_trie, cul_letters, used)
        
    for letters in x:
        helper(letters, trie, [], [])
    return words_list


solved_list = list(solver(board))
solved_list = sorted(solved_list, key=lambda x: (-len(x), x))
solved_list_scores = {}

for words in solved_list:
    if len(words) not in solved_list_scores:
        solved_list_scores[len(words)] = [words]
    else:
        solved_list_scores[len(words)] += [words]

scores_for_length = {
    3: 100,
    4: 400,
    5: 800,
    6: 1400,
    7: 1800,
    8: 2200,
    9: 2600,
    10: 3000,
    11: 3400,
    12: 3800,
    13: 4200,
    14: 4600,
    15: 5000,
    16: 5400,

}
total_score = 0

for length in solved_list_scores:
    total_score += scores_for_length[length] * len(solved_list_scores[length])

print(f'\ntotal possible score: {total_score}\n')


for length in solved_list_scores:
    print(f'\nlength: {length} \ntotal: {len(solved_list_scores[length])} \nworth: {scores_for_length[length]} \ntotal worth: {scores_for_length[length] * len(solved_list_scores[length])}\n')
    for words in solved_list_scores[length]:
        print(words)
