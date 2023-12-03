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



def main():
    iterative_lev("1234", "4321", True)
    iterative_lev("a", "1234", True)
    iterative_lev("asd", "asdd", True)

    print(recursive_lev("1234", "4321"))
    print(recursive_lev("a", "1234"))
    print(recursive_lev("asd", "asdd"))
    print(iterative_lev("asd", "asd"))



if __name__ == '__main__':
    main()

