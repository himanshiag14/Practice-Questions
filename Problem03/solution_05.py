#WAF that greets a user if no name is provided it should greet with a defualt name

def greet(name ="Tisha"):
    return "Hello, "+ name+" !"

# name = greet("Himanshi")
print(greet("Himanshi"))