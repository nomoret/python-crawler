import re
import requests
from bs4 import BeautifulSoup
import time
import random



URL = "https://gall.dcinside.com/board/lists/"


def request(url):
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9',
        'Accept-Encoding': 'gzip,deflate',
        'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Host': 'gall.dcinside.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;Win64;x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    try:
        url_get = requests.get(url, headers=header)
    except:
        url_get = requests.get(url, headers=header)
    return url_get


def extract_last_page(name):
    result = request(f"{URL}?id={name}")
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find('div', {'class': 'bottom_paging_box'}).find_all('a')
    last_page = re.search(r"[0-9]+", pagination[-1]['href']).group()
    print(last_page)
    return last_page


def extract_post_number(html):
    return html.text


def extract_post_title(html):
    return html.findChildren("a", recursive=False)[0].text


def extract_post(name, last_page):
    post = []
    for page in range(1, last_page + 1):
        print(f"Scrapping Page {page}")
        result = request(f"{URL}?id={name}&page={page}")

        soup = BeautifulSoup(result.text, "html.parser")

        post_number_list = soup.find('table', {'class': 'gall_list'}).find_all('td', {'class': 'gall_num'})
        post_subject_list = soup.find('table', {'class': 'gall_list'}).find_all('td', {'class': 'gall_tit'})

        for index in range(len(post_subject_list)):
            subject_id = extract_post_number(post_number_list[index])
            if subject_id == '공지':
                continue

            subject = {
                'id': subject_id,
                'subject': extract_post_title(post_subject_list[index])
            }
            post.append(subject)

        random_number = random.randrange(1, 5)
        print(f'{page} page subject crawling complete. {random_number} sec sleep...')
        time.sleep(random_number)

    return post