date, name, price = ['january 1,2016', 'Bread gloves', 8.61]

print(date)
print(name)
print(price)


def unpack_list(list_var):
    first, *middle, last = list_var

    avg = sum(middle)/len(middle)
    print(avg)

unpack_list([56, 64, 98, 76, 88])
