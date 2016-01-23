number = 23
running = True

while running:

    guess = int(raw_input('enter number'))

    if guess==number:
            print 'correct'

            running= False
            print 'done'

    elif guess<number:

        print'less'

    else:
        print 'too high'







