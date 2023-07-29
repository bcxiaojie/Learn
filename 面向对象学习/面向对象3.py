class Person:
    up = 0.1
    
    def __init__(self,name,xin_zi):
        self.name = name 
        self.email = f"{name}@qq.com"
        self.xin_zi = xin_zi
        
    def zhang_xin(self):
        self.xin_zi *= 1+self.up
        self.xin_zi = int(self.xin_zi)
        
    
    
    def say_hello(self):
        print(f"hello,{self.name},email:{self.email}")


if __name__ == "__main__":
    Person.up = 0.2 # 修改类变量
    p1 = Person("张三",100)
    p1.zhang_xin()
    print(p1.xin_zi)
    
    p2 = Person("李四",8000)
    p2.zhang_xin()
    p2.zhang_xin()
    print(p2.xin_zi)

        
    