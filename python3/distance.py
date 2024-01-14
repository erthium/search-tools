"""

"""

def recursive_lev(a:str, b:str) -> int:
    if len(a) == 0: return len(b)
    if len(b) == 0: return len(a)
    if a[0] == b[0]: return recursive_lev(a[1:], b[1:])
    return 1 + min([
        recursive_lev(a[1:], b),
        recursive_lev(a, b[1:]),
        recursive_lev(a[1:], b[1:])
    ])


def iterative_lev(a:str, b:str, print_matrix:bool = False) -> int:
    a_len = len(a)
    b_len = len(b)

    if a_len == 0: return len(b)
    if b_len == 0: return len(a)

    d = [[0 for _ in range(b_len + 1)] for _ in range(a_len + 1)]

    for i in range(1, a_len + 1):
        d[i][0] = i

    for j in range(1, b_len + 1):
        d[0][j] = j
    
    for i in range(1, a_len + 1):
        for j in range(1, b_len + 1):
            sub_cost = 1
            if a[i - 1] == b[j - 1]: sub_cost = 0
            d[i][j] = min([
                d[i - 1][j] + 1,
                d[i][j - 1] + 1,
                d[i - 1][j - 1] + sub_cost
            ])
    
    if print_matrix:
        for i in range(a_len + 1):
            for j in range(b_len + 1):
                print(d[i][j], end=' ')
            print()
        print(f'Distance: {d[a_len][b_len]}')
    return d[a_len][b_len]


def simplyfy(s_input:str) -> str:
    from unicodedata import normalize
    normalized = normalize('NFKD', s_input)
    reencoded = normalized.encode('ascii', 'ignore').decode('utf-8')
    return reencoded.lower()


def similarity_percentage(a:str, b:str) -> float:
    if len(a) == 0 or len(b) == 0: return 0
    a = simplyfy(a)
    b = simplyfy(b)
    return 1 - iterative_lev(a, b) / max(len(a), len(b))


def word_in_word(word:str, word_in:str) -> bool:
    if len(word) == 0 or len(word_in) == 0: return False
    word = simplyfy(word)
    word_in = simplyfy(word_in)
    return word in word_in
