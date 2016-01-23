stock = {'Google': 28.93,
            'Facebook': 76.19,
            'Yahoo': 102.56,
            'Amazon': 48.23
         }

print(min(zip(stock.keys(), stock.values())))
print(max(zip(stock.keys(), stock.values())))
print(sorted(zip(stock.keys(), stock.values())))
