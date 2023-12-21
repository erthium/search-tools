#include <string>
#include <algorithm>
#include <iostream>
#include <codecvt>
#include <locale>

using namespace std;

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

string simplyfy(const string& word){
    string reencoded;
    wstring_convert<codecvt_utf8<wchar_t>> converter;
    wstring normalized = converter.from_bytes(word);
    for (wchar_t c : normalized){
        if (c < 128) reencoded += tolower(c);
    }
    return reencoded;
}

double similarity_percentage(const string& a, const string& b){
    if (a.length() == 0 || b.length() == 0) return 0;
    int lev_dist = iterative_lev(a, b);
    double max_len = max(a.length(), b.length());
    return 1 - lev_dist / max_len;
}

bool word_in_word(const string& a, const string& b){
    if (a.length() == 0 || b.length() == 0) return false;
    if (a.length() > b.length()) return false;
    for (int i = 0; i < b.length() - a.length() + 1; i++){
        if (b.substr(i, a.length()) == a) return true;
    }
    return false;
}
// format is -> title;;link;;date
const string news_path = "../../local_data/security_news.csv";
void check_word_news(const string& word, double limit = 0.72){

}


int main(){
    cout << "Ertuğrul Şentürk" << endl;
    cout << simplyfy("Ertuğrul Şentürk") << endl;
    return 0;
}
