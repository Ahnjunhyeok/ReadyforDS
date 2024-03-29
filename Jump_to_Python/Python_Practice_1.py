# 6-1. 파이썬 프로그래밍 시작하기
# 가장 중요한 점: 프로그램을 만들려면 가장 먼저 "입력"과 "출력"을 생각하라.

# 메모장에 적으면서 짜보자. 
# 함수 이름은? GuGu로 짓자
# 입력 받는 값은? 2
# 출력하는 값은 2단(2, 4, 6, 8, ... 18)
# 결과는 어떤 형태로 저장하기? 연속된 자료형이니까 리스트

# 이제 해보자
# 1. 먼저 에디터를 열고 다음과 같이 입력한다. 입력값을 어떻게 할지 결정한다. 
# result = GuGu(2)

# 2. 결괏값을 어떤 형태로 받을 것인지 고민해보자. 2단이니까 2, 4, 6, ... 18까지 갈 것이다. 
# 즉, 결괏값을 어떤 자료형으로 받을 것인지 고민하고 적절한 자료형을 선택하는 것이 매우 중요하다. 

# 3. 어떻게 만들지 생각을 마쳤으니 본격적인 프로그래밍을 시작한다. 
def GuGu(n):
  print(n)

# 위와 같은 함수를 만들고 GuGu(2) 처럼 실행하면 2를 출력하게 된다. 

# 4. 이제 결괏값을 담을 리스트를 하나 생성하자. 앞에서 작성한 print(n)은 입력이 잘 되는지를 확인하기 위한 것이었으므로 지워도 좋다. 
def GuGu(n):
  result = []

# 5. 다음으로 result에 2, 4, 6, 8... , 18을 어떻게 넣어야 할 지 생각해보자. 
# 리스트에 요소를 추가하는 append 내장 함수를 사용하기로 한다. 

def GuGu(n):
  result = []
  result.append(n*1)
  result.append(n*2)
  result.append(n*3)
  result.append(n*4)
  result.append(n*5)
  result.append(n*6)
  result.append(n*7)
  result.append(n*8)
  result.append(n*9)
  return result

print(GuGu(2))

# 무식한 방법이긴 하지만 입력값 2를 주었을때 원하는 결괏값을 얻을 수 있었다. 

# 6. 위 함수는 너무 반복이 많다. 가만히 보면 result.append(n*x)의 x 위치에 1부터 9까지 숫자만 다르게 들어가있다는 것을 알 수 있다. 
# 똑같은 일을 반복할 때는 '반복문'을 사용한다고 했다. 
i = 1
while i < 10: # i가 10보다 작은 동안
  print(i) # i 값 출력
  i = i + 1 # i 값 1 증가

# 7. 이상의 생각을 바탕으로 완성한 GuGu 함수는 다음과 같다. 
def GuGu(n):
  result = []
  i = 1
  while i < 10:
    result.append(n * i)
    i = i + 1
  return result 

print(GuGu(2))

# 프로그래밍을 할 땐 매우 구체적으로 접근해야 머리가 덜 아프다는 것을 기억하자. 

# 6-2. 3과 5의 배수 합하기
# 다음 문제를 풀어보자
# 10 미만의 자연수에서 3과 5의 배수를 구하면 3, 5, 6, 9이다. 이들의 총합은 23이다. 
# 1000 미만의 자연수에서 3의 배수와 5의 배수의 총합을 구하라. 

# 입력받는 값은? 1부터 999까지 
# 출력하는 값은? 3의 배수와 5의 배수의 총합
# 생각해 볼 것은?
# 1. 3의 배수와 5의 배수는 어떻게 찾을까?
# 2. 3의 배수와 5의 배수가 겹칠 때는 어떻게 하지?

# 중요 포인트 2가지
# 1. 1000미만의 자연수를 구하는 방법
# 2. 3의 배수와 5의 배수를 구하는 방법

# 진행 과정
# 1. 변수에 초깃값 1을 준 후 루프를 돌리며 1씩 증가시켜서 999까지 진행하는 방법이다. 
n = 1
while n < 1000:
  print(n)
  n += 1 
# 1-1. range 함수를 사용할 수도 있다. 
for n in range(1, 1000):
  print(n)
# 2. 3과 5의 배수를 구하는 방법
# 3으로 나누어 떨어지는 경우, 5로 나누어 떨어지는 경우를 구하면 된다. 
# % 연산자를 사용하면 쉽게 찾을 수 있다.

# 3의 배수
for n in range(1, 1000):
  if n % 3 == 0:
    print(n)
    
# 5의 배수는 3 대신 5를 넣으면 된다. 
# 이를 정리해서 만든 최종 풀이는 다음과 같다. 
result = 0
for n in range(1, 1000):
  if n % 3 or n % 5 == 0:
    result += n

print(result)

# 하지만 이 문제는 함정이 하나가 있다. 3과 5 모두로 나누어지는 즉, 15와 같은 수를 이중으로 더해서는 안 된다는 점이다. 따라서 or을 사용했다. 
