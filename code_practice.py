## 4 ##

score = int(input("점수를 입력하세요 : "))

if score >= 90 : 
    print("장학생", end='')
elif score >= 60 :
        print("합격", end='')
else:
        print("불합격", end='')
        
print("입니다. ^^")

## 5 ##

num = 5
res = '짝수' if num % 2 == 0  else '홀수'

### print(res) = '홀수"

## 6 ##

nn = [100, 200, 300, 400, 500]
nn[1] = 777
print(nn) 
#1) [100, 777, 300, 400, 500]

nn = [100, 200, 300, 400, 500]
nn[1] = [444, 555]
print(nn) 
#2) [100, [444, 555], 300, 400, 500]

nn = [100, 200, 300, 400, 500]
nn[1:4] = [444, 555]
print(nn) 
#3) [100, 444, 555, 500]

nn = [100, 200, 300, 400, 500]
nn[2:] = []
print(nn)
#4) [100, 200]

## 8 ##

num = 0

for n in range(3333,9999) :
    if n%1234 == 0 :
        continue
        num += n
    if num > 100000 : 
        break
            
print(num)

## 9 ##

hap = 0

n = 1234

while n in range(1234, 4568) : 
    if n%444 == 0 :
        hap += n
    n += 1

print(hap)


## 심화문제 14 ##
myData = [[n*m for n in range(1,3)] for m in range(2,4)]
# Answer : [[2, 4], [3, 6]]


## 5 ##

nn = [100, 200, 300, 400, 500]
print(nn[4])
print(nn[-1])
print([nn[-2]])
print(nn[1:4])
print(nn[0:1])
print(nn[2:-1])
print(nn[0::2])
print(nn[::-1])
print(nn[::-2])

#1) 500
#2) 500
#3) [400]
#4) [200, 300, 400]
#5) [100]
#6) [300, 400]
#7) [100, 300, 500]
#8) [500, 400, 300, 200, 100]
#9) [500, 300, 100]



