# built_in_function.py

# 프로그래밍을 할때 중요한 부분 중 하나이다. 이미 만들어진 프로그램이 있는지를 확인하고, 있다면 그걸 사용하는 방향으로 가야한다. 
# 대표적으로 파이썬 배포본에 함께 들어 있는 파이썬 라이브러리를 살펴보는 것이 매우 중요하다. 
# 지금 살펴볼 것들은 내장 함수이다. 이미 몇 가지 내장 함수를 배웠다. 파이썬 내장 함수는 외부 모듈과 달리 import가 필요하지 않기 때문에 아무런 설정 없이 바로 사용할 수 있다. 

# abs
# abs(x)는 어떤 숫자를 압력받았을 때, 그 숫자의 절댓값을 돌려주는 함수이다. 
print(abs(3))
print(abs(-3))
print(abs(-1.2))

# all
# all(x)는 반복 가능한(iterable) 자료형 x를 입력 인수로 받으며 이 x가 모두 참이면 True, 거짓이 하나라도 있으면 False를 돌려준다. 
# 여기서 반복 가능한 자료형이란 for문으로 그 값을 출력할 수 있는 것을 의미한다. 
# 리스트, 튜플, 문자열, 딕셔너리, 집합 등이 있다. 
print(all([1, 2, 3]))
# 리스트 자료형 [1, 2, 3]은 모든 요소가 참이므로 True를 돌려준다. 

print(all([1, 2, 3, 0]))
# 리스트 자료형 [1, 2, 3, 0] 중에서 요소 0은 거짓이므로 False를 돌려준다. 

# any
# any(x)는 all(x)의 반대이다. x 중 하나라도 참이 있으면 True를 돌려주고, x가 모두 거짓일 때만 False를 돌려준다. 
print(any([1, 2, 3, 0]))
# 리스트 자료형 [1, 2, 3, 0] 중에서 1, 2, 3이 참이므로 True를 돌려준다. 

print(any([0, ""]))
# 0, "" 모두 거짓이므로 False를 돌려준다. 

# chr 
# chr(i)는 아스키(ASKII) 코드 값을 입력받아 그 코드에 해당하는 문자를 출력하는 함수이다. 
# 아스키 코드란 0에서 127 사이의 숫자를 각각 하나의 문자 또는 기호에 대응시켜 놓은 것이다. 
print(chr(97)) # 아스키 코드 97은 소문자 a
print(chr(48)) # 아스키 코드 48은 숫자 0

# dir 
# dir은 객체가 자체적으로 가지고 있는 변수나 함수를 보여준다. 
print(dir([1, 2, 3]))
print(dir({"1":"a"}))

# divmod
# divmod(a, b)는 2개의 숫자를 입력으로 받는다. 그리고 a를 b로 나눈 몫과 나머지를 튜플 형태로 돌려주는 함수이다. 
print(divmod(7, 3))

# 몫을 구하는 연산자 //와 나머지를 구하는 연산자 %를 각가가 사용한 결과와 비교해본다. 
print(7 // 3)
print(7 % 3)

# enumerate
# enumerate는 "열거하다" 라는 뜻이다. 이 함수는 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 돌려준다. 
for i, name in enumerate(["body", "foo", "bar"]):
  print(i, name)

# 순서 값과 함께 body, foo, bar가 순서대로 출력되었다. 즉 위 예제와 같이 enumerate를 for문과 함께 사용하면 자료형의 현재 순서(index)와 그 값을 쉽게 알 수 있다. 
# for문처럼 반복되는 구간에서 객체가 현재 어느 위치에 있는지 알려 주는 인덱스 값이 필요할 때 enumerate 함수를 사용하면 매우 유용하다. 

# eval
# eval은 실행 가능한 문자열(1+2, "hi" + "a"와 같은 것)을 입력으로 받아 문자열을 실행한 결괏값을 돌려주는 함수이다. 
print(eval("1+2"))
print(eval('"hi" + "a"'))
print(eval("divmod(4, 3)"))

# 보통 eval은 입력받은 문자열로 파이썬 함수나 클래스를 동적으로 실행하고 싶을 때 사용한다. 
# filter
# filter 함수는 첫 번째 인수로 함수 이름을, 두 번째 인수로 그 함수에 차례로 들어갈 반복가능한 자료형을 받는다.
def positive(l):
  result = [] # 반환 값이 참인 것만 걸러내서 저장할 변수
  for i in l:
    if i > 0: # i가 0보다 클때 
      result.append(i) # 리스트에 i 추가
    return result 

print(positive([1, -3, 2, 0, -5, 6]))

# 즉 위에서 만든 positive 함수는 리스트를 입력값으로 받아 각각의 요소를 판별해서 양수 값만 돌려주는 함수이다. 

# filter 함수를 사용하면 위 내용을 다음과 같이 간단하게 작성할 수 있다. 
def positive(x):
  return x > 0

print(list(filter(positive, [1, -3, 2, 0, -5, 6])))

# 여기에서는 두 번째 인수인 리스트의 요소들이 첫 번째 인수인 positive 함수에 입력되었을 때 반환 값이 참이 된 것만 묶어서 돌려준다.
# 앞의 예시에서는 1, 2, 6만 양수여서 x > 0 문장이 참이 되므로 [1, 2, 6] 이라는 결괏값을 돌려주게 된 것이다. 

# 앞의 함수는 lambda를 사용하면 더욱 간편하게 코드를 작성할 수 있다. 
print(list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6])))
