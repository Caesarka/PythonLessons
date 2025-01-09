Hello = 'Hello'
hello = 'hello'
HelloWorld = "Hello, world"
Bye = 'Bye'
Aye = 'Aye'

def compare(first, second):
    if first > second:
        print(f"{first} is more than {second}")
    elif first == second:
        print(f"{first} is equal to {second}")
    else:
        print(f"{first} is less than {second}")

compare(Hello, hello)
compare(Hello, HelloWorld)
compare(Hello, Bye)
compare(Hello, Aye)

compare(hello, HelloWorld)
compare(hello, Bye)
compare(hello, Aye)

compare(HelloWorld, Bye)
compare(HelloWorld, Aye)

compare(Bye, Aye)
