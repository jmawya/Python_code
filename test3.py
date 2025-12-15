def fun(n):
    print(n, 'x 2 =', n * 2)
    print(n, 'x 3 =', n * 3)
    print(n, 'x 4 =', n * 4)
    print(n, 'x 5 =', n * 5)
    print(n, 'x 6 =', n * 6)
    print(n, 'x 7 =', n * 7)
    print(n, 'x 8 =', n * 8)
    print(n, 'x 9 =', n * 9)
    print(n, 'x 10 =', n * 10)

# Take input OUTSIDE the function
n = input("enter:")
n=int(n)

# Call the function
fun(n)
for i in range(1,101):
    print(i)
fruits=["Banana", "DKD" , "tree" ]
for f in fruits:
    print(f)
for i in range(4):
    print(i);    

def day(x, y):
    print(f"Happy birthday {x}")
    print(f"YOU Are {y} years")
    print("so happy for you")

day("Joe", 20 )
day("jerry", 25)
day("jeny", 25)

class Com:
    def config(self):
        print("12d,4s5,d85")


computer = Com()
computer.config()    