import re
''''def both_ends(s):
    if(len(s)<2):
        print("")
    else:

        print(s[:2]+s[-2:])



both_ends("string")

both_ends('spring') # 'spng')
both_ends('Hello')# 'Helo')
both_ends('a')# '')
both_ends('xyz')# 'xyyz')
'''

''''def fix_start(s):

    if len(s)>1:
        start = s[0]
        back = s[1:]
        #s.replace()
        x = back.replace(start, "*" )
        print(start + x)
    else:
        return


fix_start("babble")
fix_start('babble') # 'ba**le')
fix_start('aardvark')# 'a*rdv*rk')
fix_start('google')# 'goo*le')
fix_start('donut')# 'donut')
'''''

''''def mix_up(a, b):
    if len(a)>2 and  len(b)>2:
        print(a.replace(a[:2],b[:2]),b.replace(b[:2],a[:2]))

        #y = b.replace(b[:2],a[:2]))


#mix_up("mix","pod")
mix_up('mix', 'pod')
mix_up('dog', 'dinner')
mix_up('gnash', 'sport')
mix_up('pezzy', 'firm')
'''''

'''def verbing(s):
    if len(s)>=3:
        if s[-3:] == "ing":
            print(s[:-3] + "ly")
        else:
            print(s + "ing")

    else:
        print(s)

verbing("hail")
verbing("Swiming")
verbing("do")
'''

'''

def not_bad(s):
    if(s.find("not")) < (s.find("bad")):

        #print(s.replace("not ", "good"))
        n = s.find('not')
        b = s.find('bad')
        print(n)
        print(b)
        print(s[:n] + 'good' + s[b+3:])
   # x = re.search(r"(not+?) +", s)
    #print(x)


not_bad("this is not that bad!")


'''''

''''
def front_back(a, b):

        x = len(a)
        y = len(b)
        print(x, y)

        if x%2 == 0 :

            if y%2 == 0:

                print(a[:x//2] + b[:y//2])

            else :

                print(a[:x//2] + b[:y//2+1])
        else:

            if y%2 == 0:

                    print(a[:x//2+1] + b[:y//2])

            else :

                    print(a[:x//2+1] + b[:y//2+1])
            #  to split  the string in odd even fashion  if the string is odd take the

front_back('abc','xy')
front_back('abcd','xyz')
front_back('kitten','donut')
'''
a = 'apple'

b = 2.5

#print(a[:b])

x = len(a)/2

if len(a)%2==1:
    x = x+1
    print(x)