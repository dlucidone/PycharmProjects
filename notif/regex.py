import re
def getDomain(url):

    pat = r'((https?):\/\/)?(\w+\.)*(?P<domain>\w+)\.(\w+)(\/.*)?'
    ext = r'(*(https?):\/\/)?(\w+\.)*(\w+)\.(?P<extension>\w+)(\/.*)?'
    m = re.match(pat, url)
    if m:
        domain = m.group('domain')
        return domain
    else:
        return False
    n = re.match(ext, url)
    if n:
        domain = m.group('extension')
        return ext
    else:
        return False

print(getDomain("http://www.google.com"))
print(getDomain("http://www.internet.org"))
print(getDomain("http://www.wikipedia.com"))
print(getDomain("this is ssomethoivdbvjdv  dscvbjsbcjdc http://www.Facebook.org"))