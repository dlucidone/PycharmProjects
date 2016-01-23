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




'''inp = str(input())

a, b = inp.rsplit(" ")
a1=int(a)
b1=int(b)
for n in range[a1:b1]:
    p=bin(n)
    fw= open('abc.txt', w)
    fw.write(p[2:])
    '''