## 2 ## 
class Car :
    color = ""
    speed = 0
    
    def upSpeed(self, value) :
        self.speed += value 

test = Car()
test.upSpeed(5)
print(test.speed)  

## 4 ##
class Horse :
    speed = 0
    
    def reset(self, speed):
        self.speed = speed
        
    def get(self):
        return self.speed

hor.reset(50)
print(hor.get())  

## 6 ##
class Car :
    def method(self):
        print("슈퍼 클래스")
    
class Sedan(Car):
    def method(self):
        print("서브 클래스")
        
myCar = Car()
mySedan = Sedan()
myCar.method()
mySedan.method()

# Answer: 슈퍼 클래스 서브 클래스

## 7 ##
class Car : 
    speed = 0
    
    def upSpeed(self, value) :
        self.speed = self.speed + value
    
class RVcar: 
    seatNum = 0
    
    def getSeatNum(self) :
        return self.seatNum
