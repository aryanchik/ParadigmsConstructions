
def field(items, *args):
    assert len(args) > 0
    for i in range(len(items)):
        for j in range(len(args)):
            if items[i].get(args[j]) != None:
                print(items[i][args[j]])



goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'color': 'black'}
]

field(goods, 'title')
field(goods, 'title', 'price')




'''
def main():





if __name__ == "__main__":
    main()
'''
