import os
import json
import time
import requests
from bs4 import BeautifulSoup


def get_realtime_keywords():
    '네이버 검색어 크롤링을 하고 ...'
    html = requests.get('https://www.naver.com/').text
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup.select('.PM_CL_realtimeKeyword_rolling_base .ah_k')
    keywords = [tag.text for tag in tags]

    return keywords


def insert(partition_key, row_key, **kwargs):
    '파이썬 기본문법만으로 Azure Table NoSQL에 INSERT를 합니다.'
    doc = dict(
        PartitionKey=partition_key,
        RowKey=row_key,
        **kwargs)

    tablePath = os.environ['tablePath']
    with open(tablePath, 'wt', encoding='utf8') as f:
        json.dump(doc, f)


if __name__ == '__main__':
    # 키워드를 긁어와서
    keywords = get_realtime_keywords()
    # Azure Table에 추가
    insert('naver_realtime_keywords', int(time.time()), keywords=keywords)