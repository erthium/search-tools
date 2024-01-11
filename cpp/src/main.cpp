#include <string>
#include <algorithm>
#include <iostream>
#include "utf8proc.h"

using namespace std;

size_t min(size_t a, size_t b){
    if (a < b) return a;
    return b;
}


int recursive_lev(const string& a, const string& b){
    if (a.length() == 0) return b.length();
    if (b.length() == 0) return a.length();
    if (a[0] == b[0]) return recursive_lev(a.substr(1), b.substr(1));
    return 1 + min(recursive_lev(a.substr(1), b),
                    min(recursive_lev(a, b.substr(1)),
                    recursive_lev(a.substr(1), b.substr(1))));
}


int iterative_lev(const string& a, const string& b, bool print_matrix = false){
    int a_len = a.length();
    int b_len = b.length();

    if (a_len == 0) return b.length();
    if (b_len == 0) return a.length();

    int d[a_len + 1][b_len + 1];
    for (int i = 0; i < a_len + 1; i++){
        for (int j = 0; j < b_len + 1; j++){
            d[i][j] = 0;
        }
    }

    for (int i = 1; i < a_len + 1;  i++){
        d[i][0] = i;
    }
    for (int j = 1; j < b_len + 1; j++){
        d[0][j] = j;
    }

    for (int i = 1; i < a_len + 1; i++)
    {
        for (int j = 1; j < b_len + 1; j++)
        {
            int sub_cost = 1;
            if (a[i - 1] == b[j - 1]) sub_cost = 0;
            d[i][j] = min(d[i - 1][j] + 1,
                          min(d[i][j - 1] + 1,
                          d[i - 1][j - 1] + sub_cost));
        }
    }
    if (print_matrix){
        for (int i = 0; i < a_len + 1; i++){
            for (int j = 0; j < b_len + 1; j++){
                cout << d[i][j] << " ";
            }
            cout << endl;
        }
        cout << "Distance: " << d[a_len][b_len] << endl;
    }
    return d[a_len][b_len];
}


string simplify(const string& word){
    utf8proc_uint8_t *normalized = utf8proc_NFKD((utf8proc_uint8_t*)word.c_str());
    string word_normalized = "";
    size_t i = 0;
    while (normalized[i] != 0){
        // if current char is ASCII, add it to the string
        if (normalized[i] < 128) word_normalized += (char)normalized[i];
        i++;
    }
    return word_normalized;
}


double similarity_percentage(const string& a, const string& b){
    if (a.length() == 0 || b.length() == 0) return 0;
    int lev_dist = iterative_lev(a, b);
    double max_len = max(a.length(), b.length());
    return 1 - lev_dist / max_len;
}


bool word_in_word(const string& word, const string& to_check_in){
    if (word.length() == 0 || to_check_in.length() == 0) return false;
    if (word.length() > to_check_in.length()) return false;
    int iter_count = to_check_in.length() - word.length() + 1;
    for (int i = 0; i < iter_count; i++){
        if (to_check_in.substr(i, word.length()) == word) return true;
    }
    return false;
}


// format is -> title;;link;;date
const string news_path = "../../local_data/security_news.csv";
void check_word_news(const string& word, double limit = 0.72){

}


int main(){
    cout << simplify("Ertuğrul Şentürk") << endl;
    return 0;
}
