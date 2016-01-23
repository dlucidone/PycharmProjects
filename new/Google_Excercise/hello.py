import sys

def hello(name):
        if name == 'Alice' or name == 'Nick':
                name = name + '???'
        else:
                print('Else')
                #DoesNotExist(name)  # checksOnlywhenrunline
        name = name + '!!!!'
        print('Hello', name)


# Define  a main() function that prints a little greeting.

def main():
        #print "hello"
        #print sys.argv

        hello(sys.argv[0])


# this is the standard boilerplate that calls the main()
 #function

if __name__ == '__main__':
        main()

