#ractangle
class Com:
    def sun(self, rows, cols):
       for i in range(rows):
           print("*" * cols)
#triangle
    def moon(self, rows ):
        for i in range(1, rows+1):
           print("*" * i)

#pyramid

    def star(self, rows ):
        for i in range(1, rows+1):
            space=rows-i
            st=2*i-1
            print(" " * space +"*"*st)
               
