import functionhelper


def easyFoodOnline():
    food_price_dict = {'biryani': 120, 'veg-pizza': 90, "non-veg-pizza": 120, 'meals': 100}

    food_list = []
    quantity_list = []

    invalid = False
    while not invalid:
        username = input("Enter the username:")
        invalid = functionhelper.one.check_username(username)
    print(food_price_dict)
    extra_order = 'y'
    while extra_order.lower() == 'y':
        food_dish = input("Enter the food of your choice: ")
        food_quantity = functionhelper.one.order_quantity(food_dish, food_price_dict)

        if food_quantity != 0:
            food_list.append(food_dish)
            quantity_list.append(food_quantity)

        extra_order = input("Would you like to order something else y/n:")
    print("New order generated sucessfully")
    if len(food_list) == 0:
        print("no bill to print")
    else:
        bill = functionhelper.one.calculate_bill(food_price_dict, food_list, quantity_list)

    file_read = open('Order_Details.txt', 'r')
    lines = file_read.readlines()
    for line in lines:
        last_line_list = line.removesuffix('/n').split(':')
    result = functionhelper.one.generate_orderid(last_line_list) + ':' + username + ':'
    for i in range(0, len(food_list)):
        if i == len(food_list) - 1:
            result += food_list[i] + '#' + str(quantity_list[i]) + ':'
        else:
            result += food_list[i] + '#' + str(quantity_list[i]) + ','
    result += str(int(bill))

    file_append = open('Order_Details.txt', 'a')
    file_append.write('\n' + result)

    file_append.close()
    file_read.close()


easyFoodOnline()
