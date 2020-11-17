# 웹에서는 문자열을 많이 다룬다
# 딥러닝은 숫자를 많이 쓰나 문자열은 많이 안씀

# 한줄 문자열 literal
s1 = 'Hello World'
s2 = "Hello World"
print(s1, type(s1), type(s2))
#s2 = 'Hello\nworld'
# \n 줄바꿈 개행문자?
# literal로 바로 문자열 입력하고자 할때
print('==============Multi-Line String literal ==============')
s3 = """Hello  
World"""
# \n 없이 줄바꿈
print(s3)

# 여러줄 주석을 대신하여 사용할 수 있다
# 다른 언어에서는 /* abcde.. */ 로 하면 되는데 파이썬은 미지원
"""
주석1
주석2
주석3
"""

# escape 문자열 (\붙어있는 문자)
print('===================== escape =====================')
print('hello\nWorld')
print('I say \'hello world\'')
print(" I say \"hello world\"")
print("둘리\t010-0000-0000")


print('================= 문자열 연산: 길이 =================')
print(len(s1))


print('================= 문자열 연산: 반복 =================')
str1 = 'First String'
str2 = 'Second String'

str3 = str1*3
print(str3)

print('================= 문자열 연산: 인덱싱 =================')
print(str1[0], str1[2], str1[3], str1[11])
# IndexError : string index out of range
# print(strl[12])

print('================== 문자열 연산: 연결 ==================')
str4 = str1 + ' ' + str2
print(str4)

# literal들을 연결할 때에는 + 생략 가능
str5 = 'hello'  ' ' 'world'
print(str5)

# 문자열과 정수 객체는 + 연산을 할 수 없다
name = '둘리'
age = 10
# print(name + age)
print(name + str(age))

print('============== 문자열 연산: in, not in ==============')
print("S" in str1)
print("S" not in str2)

print('=========== 문자열 객체는 변경할 수 없다.(immutable) ===========')
#str1[0] = 'f'
#print(str1)


print('================ 문자열 연산: 슬라이싱 ================') # 11/11 강의
str6 = str2[2:5]
print(str6)

str7 = str2[2:]    # 끝자리를 지정하지 않으면 슬라이싱될 게 없어서 다 표시됨.
print(str7)

str8 = str2[:]     # 생략할 수 있고 0으로 표시됨
print(str8)



print('================ 문자열 연산: 객체 함수 ================')
# 대소문자 관련 함수
s = 'i Like Python'
print(s.upper())        # 대문자로 다 바꿈
print(s.lower())        # 소문자로 다 바꿈
print(s.swapcase())     # 대소문자를 서로 바꿈
print(s.capitalize())   # 다 소문자로 바꾸되 맨앞에만 대문자로
print(s.title())

# 검색 관련 함수
s = 'I Like Python, I Like Deep Learning Also'
print(s.count("Like"))
print(s.find("Like"))
print(s.find("Like", 5))   # ,뒤에 공란이면 0이고 5라 입력하면 5번째부터 찾으라는 명령
print(s.find("AI"))
print(s.rfind("Like"))     # 오른쪽에서부터 찾으라는 명령어 (검색 개체가 있는 이동수만큼 값이 출력됨)

# 해당 오류 발생 시 나타내는 문자열
#try:
# print(s.index("AI"))
#except ValueError as e:
#    print('죄송합니다. 예기치 않은 상황으로 프로그램을 종료합니다.')
#    print(e)

try:
    print(s.index("AI"))
except ValueError as e:
    print('index() 함수는 발견하지 못하면 예외가 발생한다.')

print(s.rindex("Like"))
print(s.startswith("i Like"))
print(s.endswith("Also"))
print(s.endswith("Also", 0, 13))

# 편집자 및 치환
s = '     spam and ham     '
print('----' +  s.strip()  + '----')
print('----' +  s.rstrip()  + '----')
print('----' +  s.lstrip()  + '----')

s = '<><><abc><defg><><>'
print('----' +  s.strip('<>')  + '----')

s = 'Hello Java Java Java'
print(s.replace('Java', 'python'))   # 지정문자를 바꾸는 방법

# 분리
# 수집 -> 적재(분산저장) -> 전처리 -> 분석 -> 결과(insight) 작업도 해야됨 (앞으로 해야될 일? 그리고 중요)
s = 'one:two:three:four'
r= s.split(':')
print(r, type(r))

r = s.split(':', 2)    # 두번째까지만 분리하고 나머진 분리하지 않음
print(r)

r = s.rsplit(':', 2)
print(r)

# 라인 분리
lines = """1st line
2nd line
3rd line
4th line
"""
r = lines.split('\n')
print(r)

r = lines.splitlines()
print(r)


"1line\n2line\n3line\4line" # 이런 형태

# 결합 (list에 있는 문자열을 결합하는 것)
s = ' & '.join(r)
print(s)

# 판별
print('1234'.isdigit())
print('abcd'.isalpha())
print('1234'.isalpha())
print('abcdefg'.islower())
print('ABCDEFG'.isupper())

# 타언어는 2차원 데이터를 지원함
# int[3][2] arr:
# arr[0][0] = 0;                 0   1
# arr[0][1] = 1;                10  15
# arr[1][0] = 10;               20  21
# arr[1][1] = 15;
# arr[2][0] = 20;
# arr[2][1] = 21;

# arr = [0, 1, 2] 파이썬은 2차원을 지원하지 않지만, 다른언어는 배열을 지원(2차원 행렬이 만들어짐)

print('================ 문자열 연산: 포맷팅 ================')
#epoch = 1000
#init = (0, 0)
#diff = 10

#"epoch =" str(100) + "회 초기값" + str(init)
#f'epoch ={epoch} 회, 초기값:{init}'

#name = '둘리', age = 10

f1 = "name: " + name + ", age: " + str(10)  # 정수 안되기 때문에 str
print(f1)

f2 = "name: " + format(name, 's') + ", age: " + format(age, 'd')
print(f2)

f3 = "name: {}, age: {}"
print(f3.format(name, age))   #객체가 많아지면 실수할 위험이 있으니 유의

f4 = "name: {1}, age: {0}"
print(f4.format(age, name))

f5 = f'name: {name}, age: {age}'    # 최근에 생긴 방법, 이 방법 사용 추천
print(f5)