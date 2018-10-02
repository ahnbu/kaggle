
# coding: utf-8

# # 사전테스트

# In[1]:


print ("테스트")


# # 그로쓰해킹 가격체크

# In[61]:


import requests

html = requests.get("https://dsschool.co.kr/marketing/suggestions").text

# print(html)

from bs4 import BeautifulSoup

soup = BeautifulSoup(html,'lxml')

# print(soup.prettify())

#soup.find_all('div') # suop.find('div')라고 하면 첫 div 태그 부분만 불러옴

#soup.select('h3.class_course-price')

soup.select('div#id_course-beginner') # 이렇게하면 빈괄호가 나옴
soup.select('p.class_course-target') # 이렇게하면 빈괄호가 나옴

soup.find_all('div', {"id":"course-beginner"})
price = soup.find_all('h3', {"class":"course-price"}) # h3가 들어간 여러 개의 코드를 리스트로 받음

# print(price)

price_discount = price[1].get_text() # h3가 포함된 코드 리스트 중에서 첫번째 것을 받음
discount_rate = int(price_discount[10:-6]) # 정수화

# print(discount_rate)


# # 이메일 보내기

# In[62]:


import smtplib
from email.mime.text import MIMEText

google_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
google_server.ehlo()
google_server.login('byungwook.an@gmail.com', 'Ahnbu7891')

# 정확하게 했는데, 안되는 경우는 gmail의 보안 수준이 높기 때문임
# https://myaccount.google.com/security에서 보안 수준이 낮은 앱의 액세스 를 '사용'으로 하면 발송이 잘 될 것

me = 'byungwook.an@gmail.com'
you = 'byungwook.an@gmail.com'
contents = '이메일 내용'

# 오늘 날짜
from datetime import date, timedelta
today = date.today()
today1 = today.strftime('%m/%d')

subject = "[참고] 오늘(" + today1 + ") 그로쓰해킹 할인율이 " + str(discount_rate) + "%입니다."
subject2 = "[중요] 오늘(" + today1 + ") 그로쓰해킹 할인율이 " + str(discount_rate) + "%입니다."

# print(subject + subject2)

msg = MIMEText(contents, _charset = 'euc-kr')
msg['Subject'] = subject
msg['From'] = me
msg['To'] = you

msg1 = MIMEText(contents, _charset = 'euc-kr')
msg1['Subject'] = subject2
msg1['From'] = me
msg1['To'] = you

if discount_rate > 40 :
    #print("와우!! 드디어 할인율이 " + str(discount_rate) + "% 되었네요." + "\n" + "얼른 신청하세요!")
    google_server.sendmail('byungwook.an@gmail.com','byungwook.an@gmail.com',msg1.as_string())
    # str만 들어가야 한다고 하니, 정수를 str으로 변환시켜서 넣었음
else:
    #print("아직 할인율이 " + str(discount_rate) + "% 밖에 안되요." + "\n" + "조금 더 기다려주세요.")
    google_server.sendmail('byungwook.an@gmail.com','byungwook.an@gmail.com',msg.as_string())

google_server.quit()    


# In[3]:


'''
<div id="course-beginner" class="course course-column active" data-default-pricing="890000" data-pricing="667500" data-discount="25" data-current-course="marketing_beginner_15">
        <h3 class="course-name">입문 과정</h3>
        <h3 class="course-summary">4주 과정, 매주 5시간</h3>
        <h3 class="course-price"><s>1,050,000 원</s></h3>
        <h3 class="course-price">735,000원 (30% 할인가)</h3>
        <p style="font-size: 12px; margin: 0;">* 기자재 비용 포함 (유료 광고 툴, 실습 광고 비용 등)</p>

        <hr />

        <p class="course-target">데이터 마케팅 경험이 전혀 없어도 가능</p>
        <p class="course-description">최신 디지털 마케팅 툴을 활용하는 실용적인 스킬들을 갖게 되시고, 워크샵 기간동안 실제 예산을 태워 디지털 광고를 집행/분석/후속 운영을 해보는 과정입니다.</p>

        <p class="course-discount">
            <span class="remain-seat">현재 잔여 좌석 6개</span>
        </p>

        <a href="#" id="btn-purchase-marketing-beginner" class="btn-course btn-purchase">30% 할인 결제하기</a>
      </div>
'''


# # 스케줄러
