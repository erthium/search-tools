import requests
from bs4 import BeautifulSoup


security_news_template = 'https://www.wired.com/category/security/?page={}'
website_url_template = 'https://www.wired.com{}'
link_class = 'SummaryItemHedLink-civMjp ejgyuy summary-item-tracking__hed-link summary-item__hed-link'


with open('security_news.csv', 'w', encoding='utf-8') as file:
    file.write('Title;;Link\n')
    for i in range(1, 100):
        print(f'Scrapping page: {i}')
        url = security_news_template.format(i)
        response = requests.get(url)
        page_soup = BeautifulSoup(response.text, 'html.parser')
        all_sections = page_soup.find_all('section', {'data-testid': 'SummaryRiverSection'})
        for section in all_sections:
            links = section.find_all('a', {'class': link_class})
            for link in links:
                title = link.find('h3').text
                href = link['href']
                news_response = requests.get(website_url_template.format(href))
                news_soup = BeautifulSoup(news_response.text, 'html.parser')
                time = news_soup.find('time').text
                file.write(f'{title};;{href};;{time}\n')
