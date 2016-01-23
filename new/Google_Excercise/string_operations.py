s = "hi"

print(s[1])

print(len(s))

print(s +"there")

print(s, "there")  # Notice the diff between + and ,(comma)


pi = 3.14

text = "the value of pi is "+ str(pi)

print(text)

# no ++ operator in python

a=5
b=6

print(b/a)    # Notice the diff between / and //
print(b//a)     # the / perform division(float) and //perform int division

raw = r'this\t\n and that'
print(raw)

raw1 = u'this\t\n is unicode'
print(raw1)

multi = """three commas allow you to type multi line comment """
print(multi)


x = " Hello World 2016 "
y = 2016

print(x.lower()) # return lowercase

print(x.upper())  # return uppercase

print(x.strip(" "))  # return string  with whitespace removed from start and end

print(x.isalpha())

print(x.isdigit())

print(x.isspace())

print(x.find('e')) # searches for the given other string within x and return int value

print(x.replace('Hell', 'Hello'))

print(x.split(" "))

#print(x.join())

print(x[-1])
print(x[-5])
print(x[:-3])
print(x[-3:])
print(x[1:100])

text1 = ("%d little pigs come out or I'll %s and %s and %s" %(3, 'huff', 'puff', 'blow down'))
print(text1)

ustring = u'A unicode \u018e string \xf1'
print(ustring)

q = ustring.encode('utf-8')
print(q)

#t = Unicode(q, 'utf-8')




