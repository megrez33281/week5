class Myclass (object):
    x = 0
    y = 0

    def my_print(self):
        self.x += 1
        Myclass .y += 1     #使用Myclass呼叫object時，會影響到class本身，用self呼叫只會影響到呼叫class之object
        print('(x, y) =  ({}, {})'.format(self.x,self.y))



class AClass:
    def __init__(self,x,y):#此處要求的參數為初始呼叫class會要求的
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y


a = AClass(7,8)
print(a.add())

f = Myclass
a = Myclass()
b = f()

b.my_print()            #(x, y) =  (1, 1)
b.my_print()            #(x, y) =  (2, 2)
a.my_print()            #(x, y) =  (1, 3)

