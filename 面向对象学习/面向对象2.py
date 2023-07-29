class Person:
    # 使用构造器
    def __init__(self,name):
        self.name = name # 实例变量，和类变量不太一样
        self.email = f"{name}@qq.com"
        
    
    
    # 类方法
    def say_hello(self):
        print(f"hello,{self.name},email:{self.email}")
        
        
if __name__ == "__main__":
    example1 = Person("zhang_san")
    example1.say_hello()
    
    example2 = Person("li_si")
    example2.say_hello()
        
        
    