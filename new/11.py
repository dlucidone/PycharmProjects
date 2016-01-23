w='week'
m='month'
input_str = str(input())

a, b, c = input_str.split(" ")

a1=int(a)
c1=str(c)
#type(c1)
if c1 == w:
    if 1<=a1<=7:
        print(52)
elif c1 == m:

             if a1>=29:
                print(11)

             elif a1<=28:
                    print(12)
