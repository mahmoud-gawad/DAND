from bs4 import BeautifulSoup
import requests
import time

def continue_crawl(search_history, target_url, limit):
    last_visited = search_history[-1]
    if last_visited == target_url:
        print('Eureka!')
        return False
    elif len(search_history) > limit:
        print('Too many pages visited, I am exhausted :(')
        return False
    elif search_history.count(last_visited) > 1:
        print('Uh-oh! Looks like we are running around in circles :S')
        return False
    return True

def find_first_link(url):
    last_article = requests.get(url)
    soup = BeautifulSoup(last_article.text, 'html.parser')
    all_paragraphs = soup.find(id='mw-content-text').find(class_='mw-parser-output').find_all('p')
    done = False
    first_link = None
    for p in all_paragraphs:
        if p.get('class') == ['mw-empty-elt']:
            continue
        else:
            all_links = p.find_all('a')
            for a in all_links:
                if a['href'][0] != '/' or a['title'][0:4] == 'Help' or a.parent.name == 'span' or a.parent.name == 'small':
                    continue
                else:
                    first_article_link = a['href']
                    first_link = requests.compat.urljoin('https://en.wikipedia.org/', first_article_link)
                    done = True
                    break
        if done:
            break
    return first_link

start_url = "https://en.wikipedia.org/wiki/Special:Random"
target_url = "https://en.wikipedia.org/wiki/Philosophy"
article_chain = [start_url]

while continue_crawl(article_chain, target_url, 25):
    print(article_chain[-1])
    first_link = find_first_link(article_chain[-1])
    if not first_link:
        print('We reached a page with no links, aborting mission!')
        break
    article_chain.append(first_link)
    time.sleep(2)
