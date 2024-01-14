from distance import similarity_percentage, word_in_word, simplyfy
import os

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
NEWS_PATH = os.path.join(SCRIPT_DIR, '../local_data/security_news.csv')


def check_word_eng_dict(word:str):
    with open('../local_data/en_dict.csv', 'r') as file:
        for line in file:
            line = line.split(',')
            similarity = similarity_percentage(word, line[0])
            if similarity > 0.7:
                print(f'Word: {line[0]} - Similarity: %{similarity * 100} - Meaning: {line[2]}')


def check_word_news(word:str, limit:int = 0.72) -> None:
    with open(NEWS_PATH, 'r') as file:
        for line in file:
            line = line.split(';;')
            title_pieces = line[0].split()
            for piece in title_pieces:
                similarity = similarity_percentage(word, piece)
                if similarity > limit or word_in_word(word, piece):
                    print(f'Title: {line[0]}')
                    print(f'Matched Word: {piece}')
                    print(f'Similarity: %{(similarity*100):.2f}')
                    print(f'Link: {line[1]}')


def main():
    # General test for functions above
    """  
    iterative_lev("1234", "4321", True)
    iterative_lev("a", "1234", True)
    iterative_lev("asd", "asdd", True)
    iterative_lev("asd", "asd", True)

    print(recursive_lev("1234", "4321"))
    print(recursive_lev("a", "1234"))
    print(recursive_lev("asd", "asdd"))
    print(iterative_lev("asd", "asd"))

    # To show the inefficiency of the recursive algorithm
    # in an imperative language
    print(recursive_lev("123456789123456789", "912345678912345678"))

    
    print(similarity_percentage("asd", "asd"))
    print(similarity_percentage("asd", "asdd"))
    print(similarity_percentage("asd", "asddd"))
    print(similarity_percentage("asd", "asdddd"))
    
    print(simplyfy("Staré Město"))
    """
    check_word_news("gpt")
    #print(simplyfy('Ertuğrul Şentürk'))


if __name__ == '__main__':
    main()
