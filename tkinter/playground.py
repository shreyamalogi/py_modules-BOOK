def add(*args):              #  *args (arguments)
    print(args[1])
    
    sum =0
    for n in args:
        sum += n
    return sum

#print(add(3,5,6,2,1,7,4,3))

def calculate (**kwargs):           #   **kwargs (unlimited keyword arguments)
    print(kwargs)
          
calculate(add = 3, multiply = 5) 
calculate()                            
# output
# {'add': 3, 'multiply': 5}