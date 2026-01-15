menu  = {
    'pizza':100,
    'pasta':120,
    'noodles':80,
    'cold coffee':100,
    'burger':120,
    'maggie':70
}

print('welcome to Home pour cafe')
print('pizza:100\npasta:120\nnoodles:80\ncold coffee:100\nburger:120\nmaggie:70')

order_total = 0

item_1 = input("enter the name of item you want to order:")
if item_1 in menu:
    order_total += menu[item_1]
    print("your item {item_1} has been added to your order..")

else:
    print(f'ordered item{item} is not available')

another_order = input("do you want another item? (yes/no)")
if another_order == "yes":
    item_2 = input("enter the name of your second item: ")
    if item_2 in menu:
        order_total += menu[item_2]
        print("your item {item_2}has been added to your order..")

print(f'The total amount to be paid is {order_total}')