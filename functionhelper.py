class one:
    def check_username(username: str):
        l_name = list(username)
        for i in l_name:
            if not (('A' <= i <= 'Z') or ('a' <= i <= 'z') or (i == ' ')):
                return False
        return True

    def order_quantity(food_dish: str, food_price_dict):
        if food_dish in food_price_dict.keys():
            food_quantity = int(input("Enter the number of items: "))
            return food_quantity
        else:
            return 'no food item is present'

    def generate_orderid(dataid):
        try:
            finalid = int(dataid[0].removeprefix('O'))
            if finalid != 0:
                return 'O' + str(finalid + 1)
        except (IndexError, ValueError):
            print("no order register so added first order")
            return 'O101'

    def calculate_bill(food_price_dict: dict, food_list, quantity_list):
        cal_bill = 0
        for i in range(0, len(food_list)):
            if food_list[i] in food_price_dict:
                cal_bill += food_price_dict[food_list[i]] * quantity_list[i]
        if cal_bill > 299:
            discount = 10
            cal_bill = cal_bill - ((cal_bill * discount) / 100)
            return cal_bill
        else:
            return cal_bill
