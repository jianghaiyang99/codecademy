items_for_brunch = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}

items_for_ealry_bird ={
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}

items_for_dinner ={
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}

items_for_kids ={
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}


#先创建了一个巨大的class
class Menu:
    def __init__(self,name,items,start_time,end_time):
        self.name = name
        self.items = items #在这里居然接受的是一个字典
        self.start_time = start_time
        self.end_time = end_time
    #也不命个名啥的，或许是想等一下再来？
    def __repr__(self):
        result = "the name of the Menu is {}, it starts available from {} to {} ".format(self.name,self.start_time,self.end_time)
        return result

    def calculate_bill(self,purchased_items):
        #purchased_items是一个list, 就是你买的东西，都会记录到这个了列表里。
        total_price = 0
        for i in purchased_items:
            singeleprice = self.items[i]
            total_price += singeleprice
        return total_price


#通过这个class，创建了四个菜单。

brunch = Menu("brunch",items_for_brunch,11,16)
early_bird = Menu("early_bird",items_for_ealry_bird,15,18)
dinner = Menu("dinner",items_for_dinner,17,23)
kids = Menu("kids",items_for_kids,11,20)

print(brunch.calculate_bill(["pancakes","home fries","coffee"]))



#
class Franchise:
    def __init__(self,address,menus): #这个menus要存入四个 object，那它只能是list了
        self.address = address
        self.menus = menus

    def __repr__(self):
        result = "the address of the store is at: {}".format(self.address)
        return result

    # 16,early bird,kids17,earlybirds,dinner,kins18,dinner,kids20,dinner23
    def available_menus(self,time):
        result = []
        if time >= 11 and time <15:
            result.append(all_menus[0])
            result.append(all_menus[3])
            return result
        if time>= 15 and time < 16:
            result.append(all_menus[0])
            result.append(all_menus[1])
            result.append(all_menus[3])
        if time>=16 and time < 17:
            result.append(all_menus[1])
            result.append((all_menus[3]))
        if time>=




all_menus = [items_for_brunch,items_for_ealry_bird,items_for_dinner,items_for_kids,items_for_arepas_men]
flagship_store = Franchise("1232 West End Road",all_menus)
new_installment = Franchise("12 East Mulberry Street",all_menus)

out =flagship_store.available_menus(12)
print(out)


class Business:
    def __init__(self,name,fra):
        self.name = name
        self.fra = fra


first_b = Business("Basta Fazoolin' with my Heart",[flagship_store,new_installment])
