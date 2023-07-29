class Person:
    name = "xiao_ming" # 类变量
    
    
    # 类方法
    def say_hello(self):
        print(f"hello,{Person.name}")
        
        
if __name__ == "__main__":
    # 访问类中变量
    print(Person.name)
    
    # 访问类中方法
    # 1.实例化变量
    example = Person()
    example.say_hello()
    print(example.name)
    # 类中的变量可修改
    example2 = Person()
    example2.name = "zhang_san"
    print(example2.name)
        
        
        
    