# 문제2.
# 다음과 같은 텍스트에서 모든 태그를 제외한 텍스트만 출력하세요.

#find 쓰고 slicing 써서 잘라내던가

# 웹문서 크롤링 할 때 태그는 필요없으니 전처리 작업 유형임

s = """
    <html>
        <body style='background-color:#ffff'>
            <h4>Click</h4>
            <a href='http://www.python.org'>Here</a>
            <p>
            	To connect to the most powerful tools in the world.
            </p>
        </body>
    </html>"""

indexbegin = 0
while True:
    indexbegin = s.find('<', indexbegin)
    if indexbegin == -1:
        break
    indexend = s.find('>')
    if indexend != -1:
        s = s[:indexbegin] + s[indexend+1:]
    else:
        indexend += 1

print(s)



#코드에서 else: indexend += 1 의 역할은 무엇입니까? 의미를 알 수 없어서 없애봤는데 일단 문제는 안생기는 것 같습니다.
#끝을 못찾으면 indexend 값은 -1 이고
#1증가하면 그냥 0이 됩니다.
