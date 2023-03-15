
def _init_(x,y):
    self.x = x
    self.y = y
    
def my_print():
        self.x += 1
        Myclass .y += 1     #使用Myclass呼叫object時，會影響到class本身，用self呼叫只會影響到呼叫class之object
        print('(x, y) =  ({}, {})'.format(self.x,self.y))

        return x
    
def add(a,b):
        
    return a+b

def main():
    f = Myclass     
    a = Myclass()
    b = f()
    
    b.my_print()            #(x, y) =  (1, 1)
    b.my_print()            #(x, y) =  (2, 2)
    a.my_print()            #(x, y) =  (1, 3)


        


if __name__ == "__main__":

    main()
