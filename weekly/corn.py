import datetime
import requests

from django.contrib.auth.models import User
from django.utils import timezone

from bs4 import BeautifulSoup as bs4

from weekly.models import Weekly


def weekly_create_job():
    url = "https://maria.catholic.or.kr/mobile/bondang/bondang_jubo.asp?orgnum=851"
    html = requests.get(url, verify=False).text
    soup = bs4(html, 'html.parser')
    ul = soup.find_all('ul', class_='jubo_list')[0]
    li = ul.find_all('li')[0]
    title = li.find('a').text.strip()
    date = title[:10]

    today = datetime.date.today()
    user_id = User.objects.first()
    content = f'''
        <p>
            <a href="https://maria.catholic.or.kr/root_file/church/{date}/%EB%8C%80%EC%B9%984%EB%8F%99.pdf" target="_blank">
                https://maria.catholic.or.kr/root_file/church/{date}/%EB%8C%80%EC%B9%984%EB%8F%99.pdf
            </a>
            <br>
        </p>'''

    if str(date) == str(today):
        Weekly.objects.create(
            user=user_id,
            title=title,
            content=content,
            created_at=timezone.now(),
            updated_at=timezone.now()
        )