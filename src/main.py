"""
int recursive_lev(const string& a, const string& b){
    if (a.length() == 0) return b.length();
    if (b.length() == 0) return a.length();
    if (a[0] == b[0]) return recursive_lev(a.substr(1), b.substr(1));
    return 1 + min(recursive_lev(a.substr(1), b),
                    min(recursive_lev(a, b.substr(1)),
                    recursive_lev(a.substr(1), b.substr(1))));
}
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


"""
int iterative_lev(const string& a, const string& b){
    int a_len = a.length();
    int b_len = b.length();

    int d[a_len + 1][b_len + 1] = {0};
    for (int i = 1; i < a_len; i++){
        d[i][0] = i;
    }
    for (int j = 1; j < b_len; j++){
        d[0][j] = j;
    }

    for (int i = 1; i < a_len; i++)
    {
        for (int j = 1; j < b_len; j++)
        {
            int sub_cost = 1;
            if (a[i - 1] == b[j - 1]) sub_cost = 0;
            d[i][j] = min(d[i - 1][j] + 1,
                          min(d[i][j - 1] + 1,
                          d[i - 1][j - 1] + sub_cost));
        }
    }
    return d[a_len - 1][b_len - 1];
}
"""

def iterative_lev(a:str, b:str) -> int:
    pass    

def main():
    pass

if __name__ == '__main__':
    main()

