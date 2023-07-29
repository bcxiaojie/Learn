class Animal:
    
    def __init__(self,name,legs,age):
        self.name = name
        self.legs = legs
        self.__age = age # 私有实例，无法在子类中被访问
        
    def info(self):
        print(f"{self.name} has {self.legs} legs")
        
    def __private_info(self): # 私有方法无法在子类中被调用
        print(f"{self.name} has {self.__age} years old")
        
        
class Dog(Animal):
    
    # 会将父类中的方法覆盖
    def info(self):
        print(f"{self.name} has {self.legs} legs")

class Cat(Animal):
    def walk(self):
        print(f"{self.name} is walking by {self.legs}'s legs" )
    
if __name__ == "__main__":
    d1 = Dog("旺财",4)
    d1.info()
    
    c1 = Cat("猫猫",4)
    c1.walk()
