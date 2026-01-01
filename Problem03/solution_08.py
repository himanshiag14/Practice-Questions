#create a funtion that acepts any number of keyword arguement and prints them in the format key:value

#**kwargs

def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

print_kwargs(name="shaktiman",power="lazer")
print_kwargs(name="shaktiman")
print_kwargs(name="shaktiman",power="lazer",enemy="Dr jackel")