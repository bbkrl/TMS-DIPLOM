import json

import requests

from bs4 import BeautifulSoup

ITEMS_ON_PAGE = 100
HH_HEADERS = {
    'Host': "hh.ru",
    'User-Agent': "Safari",
    'Accept': '*/*',
    'Accept-Encoding': "gzip, deflate, br",
    'Connection': "keep-alive"
}


def extract_hh_max_page(url) -> int:
    """функция возвращает максимальное кол-во страниц"""

    pages = []

    hh_request = requests.get(url, headers=HH_HEADERS)

    hh_soup = BeautifulSoup(hh_request.text, 'html.parser')

    paginator = hh_soup.find_all('span', {'class': "pager-item-not-in-short-range"})

    for page in paginator:
        pages.append(int(page.find('a').text))

    return pages[-1]


def extract_job(html, keyword) -> dict:
    """ищет название вакансии и название компании и возвращает словарь"""
    title = html.find('a').text

    vacancy_link = html.find('a')['href']

    company = html.find('div', {'class': 'vacancy-serp-item__meta-info-company'}).text
    company = company.strip()

    location = html.find("div", {"data-qa": "vacancy-serp__vacancy-address"}).text
    location = location.partition(',')[0]

    return {'title': title, 'company': company, 'location': location, 'vacancy_link': vacancy_link, 'category': keyword}


def extract_hh_jobs(last_page: int, url, keyword) -> list:
    jobs = []

    for page in range(last_page):
        result = requests.get(f'{url}&page={page}', headers=HH_HEADERS)
        print(f'Парсинг страницы {page}:{result}')
        soup = BeautifulSoup(result.text, 'html.parser')
        results = soup.find_all('div', {'class': 'vacancy-serp-item-body__main-info'})
        for result in results:
            job = extract_job(result, keyword)
            jobs.append(job)
    return jobs


def get_jobs(keyword):
    url = f"https://hh.ru/search/vacancy?text={keyword}&per_page={ITEMS_ON_PAGE}"

    hh_max_pages = extract_hh_max_page(url)
    hh_jobs = extract_hh_jobs(hh_max_pages, url, keyword)
    return hh_jobs
