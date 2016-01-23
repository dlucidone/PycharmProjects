while True:
    try:
        number=int(input("enter your fav num: \n"))
        print(18/number)
        break

    except ZeroDivisionError:
        print("Zero is not your Fav No.")

    except:
        break

    finally:
        print('Done')