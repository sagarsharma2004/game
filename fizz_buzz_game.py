a =(int)(input("Enter number:- "))
for i in range(1,a):
    if(i%3==0 and i%5==0):
        print(str(i)+" FizzBuzz")
    else:
        if(i%3==0):
            print(str(i)+" Fizz")
        elif(i%5==0):
            print(str(i)+" Buzz")
        else:
            print(str(i))