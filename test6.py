class Zain:
    def kit(self,a,b):
       try:
          result=a/b
          print(result)
       except ZeroDivisionError:
          print("Number is not devided by zero")

       finally:
          print("Regardless testcase pass or fail this code will be")   
       
config=Zain()
config.kit(5,0)


