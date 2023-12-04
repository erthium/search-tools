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
"""
double similarity_percentage(const string& a, const string& b){
    if (a.length() == 0 || b.length() == 0) return 0;
    int lev_dist = iterative_lev(a, b);
    double max_len = max(a.length(), b.length());
    return 1 - lev_dist / max_len;
}
"""


from unicodedata import normalize
def simplyfy_string(s_input:str) -> str:
    normalized = normalize('NFKD', s_input)
    reencoded = normalized.encode('ascii', 'ignore').decode('utf-8')
    return reencoded.lower()

def similarity_percentage(a:str, b:str) -> float:
    if len(a) == 0 or len(b) == 0: return 0
    a = simplyfy_string(a)
    b = simplyfy_string(b)
    return 1 - iterative_lev(a, b) / max(len(a), len(b))


def check_word(word:str):
    with open('../local_data/en_dict.csv', 'r') as file:
        for line in file:
            line = line.split(',')
            similarity = similarity_percentage(word, line[0])
            if similarity > 0.7:
                print(f'Word: {line[0]} - Similarity: %{similarity * 100} - Meaning: {line[2]}')


def main():
    """
    iterative_lev("1234", "4321", True)
    iterative_lev("a", "1234", True)
    iterative_lev("asd", "asdd", True)
    iterative_lev("asd", "asd", True)

    print(recursive_lev("1234", "4321"))
    print(recursive_lev("a", "1234"))
    print(recursive_lev("asd", "asdd"))
    print(iterative_lev("asd", "asd"))

    print(similarity_percentage("asd", "asd"))
    print(similarity_percentage("asd", "asdd"))
    print(similarity_percentage("asd", "asddd"))
    print(similarity_percentage("asd", "asdddd"))
    
    print(simplyfy_string("Staré Město"))
    """
    check_word("Shape1")




if __name__ == '__main__':
    main()

