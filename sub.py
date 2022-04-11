
class Input():
    def __init__(self, first, sec): 
        self.first = first
        self.sec = sec
    @classmethod
    def from_input(cls):
        return cls(
            int(input("Enter first Number:")),
            int(input("Enter second Number:"))
        )
 
class Operation():
    def __init__(self,first,sec):           # on Number(start)
        self.first = first
        self.sec = sec
    @classmethod
    def sub(self,first,sec):                # on instance - other
        
        result = first - sec
        if (result>0):
            output = "POSITIVE"
        elif (result<0):
            output = "NEGATIVE"
        else :
            output = "ZERO"
            
        return(output) 
    
def main():
    inp = Input.from_input() 
    first_num = inp.first
    sec_num = inp.sec

    result = Operation.sub(first_num,sec_num) 
    print("Result is " + result)
    
main()
