class Burger:
    def __init__(self, name, price, cnt):
        self.name = name
        self.price = price
        self.cnt = cnt

    def __lt__(self, other):
        return self.cnt < other.cnt

    def __le__(self, other):
        return self.cnt < other.cnt or (self.cnt == other.cnt and self.price > other.price)

    def __eq__(self, other):
        return self.price == other.price and self.cnt == other.cnt

    def __ne__(self, other):
        return self.price != other.price or self.cnt != other.cnt

    def __gt__(self, other):
        return self.cnt > other.cnt or (self.cnt == other.cnt and self.price < other.price)

    def __ge__(self, other):
        return self.cnt > other.cnt or (self.cnt == other.cnt and self.price < other.price)

    @staticmethod
    def get_sorted(burger_list):
        sorted_burger_list = sorted(
            burger_list,
            key=lambda burger: (-burger.cnt, -burger.price)
        )
        return sorted_burger_list

class Drink:
    def __init__(self, name, price, cnt):
        self.name = name
        self.price = price
        self.cnt = cnt

    def __lt__(self, other):
        return self.cnt < other.cnt

    def __le__(self, other):
        return self.cnt < other.cnt or (self.cnt == other.cnt and self.price > other.price)

    def __eq__(self, other):
        return self.price == other.price and self.cnt == other.cnt

    def __ne__(self, other):
        return self.price != other.price or self.cnt != other.cnt

    def __gt__(self, other):
        return self.cnt > other.cnt or (self.cnt == other.cnt and self.price < other.price)

    def __ge__(self, other):
        return self.cnt > other.cnt or (self.cnt == other.cnt and self.price < other.price)

    @staticmethod
    def get_sorted(drinks_list):
        sorted_drinks_list = sorted(
            drinks_list,
            key=lambda drink: (-drink.cnt, -drink.price)
        )
        return sorted_drinks_list

class Combo:
    def __init__(self, name, price, cnt):
        self.name = name
        self.price = price
        self.cnt = cnt

    def __lt__(self, other):
        return self.cnt < other.cnt

    def __le__(self, other):
        return self.cnt < other.cnt or (self.cnt == other.cnt and self.price > other.price)

    def __eq__(self, other):
        return self.price == other.price and self.cnt == other.cnt

    def __ne__(self, other):
        return self.price != other.price or self.cnt != other.cnt

    def __gt__(self, other):
        return self.cnt > other.cnt or (self.cnt == other.cnt and self.price < other.price)

    def __ge__(self, other):
        return self.cnt > other.cnt or (self.cnt == other.cnt and self.price < other.price)

    @staticmethod
    def get_sorted(combos_list):
        sorted_combos_list = sorted(
            combos_list,
            key=lambda combo: (-combo.cnt, -combo.price)
        )
        return sorted_combos_list

class Snack:
    def __init__(self, name, price, cnt):
        self.name = name
        self.price = price
        self.cnt = cnt

    def __lt__(self, other):
        return self.cnt < other.cnt

    def __le__(self, other):
        return self.cnt < other.cnt or (self.cnt == other.cnt and self.price > other.price)

    def __eq__(self, other):
        return self.price == other.price and self.cnt == other.cnt

    def __ne__(self, other):
        return self.price != other.price or self.cnt != other.cnt

    def __gt__(self, other):
        return self.cnt > other.cnt or (self.cnt == other.cnt and self.price < other.price)

    def __ge__(self, other):
        return self.cnt > other.cnt or (self.cnt == other.cnt and self.price < other.price)

    @staticmethod
    def get_sorted(snacks_list):
        sorted_snacks_list = sorted(
            snacks_list,
            key=lambda snack: (-snack.cnt, -snack.price)
        )
        return sorted_snacks_list

class User:
    def __init__(self):
        self.burgers_list = []
        self.drinks_list = []
        self.snacks_list = []
        self.burgers = {}
        self.snacks = {}
        self.drinks = {}
        self.burgers['Ангус Сибирский'] = 484.99
        self.burgers['Воппер Сибирский'] = 359.99
        self.burgers['Воппер'] = 289.99
        self.burgers['Ангус Пармеджано'] = 439.99
        self.burgers['Чикенбургер'] = 99.99
        self.burgers['Цезарь Кинг'] = 139.99
        self.burgers['Фиш Бургер'] = 184.99
        self.snacks['Кинг Фри'] = 99.99
        self.snacks['Наггетсы'] = 119.99
        self.snacks['Креветки'] = 239.99
        self.snacks['Крылышки'] = 209.99
        self.snacks['Сырные медальоны'] = 104.99
        self.snacks['Луковые Кольца'] = 94.99
        self.snacks['Стрипсы'] = 219.99
        self.drinks['Стакан 0.4'] = 129.99
        self.drinks['Стакан 0.5'] = 159.99
        self.drinks['Стакан 0.8'] = 199.99
        self.drinks['Сок'] = 79.99
        self.drinks['Шейк'] = 144.99
        self.drinks['Пиво'] = 199.99

    def try_add_burger(self, name_of_burger, cnt_of_burger):
        if name_of_burger in self.burgers:
            self.burgers_list.append(Burger(name_of_burger, self.burgers[name_of_burger], cnt_of_burger))
            return True
        return False

    def try_add_drink(self, name_of_drink, cnt_of_drink):
        if name_of_drink in self.drinks:
            self.drinks_list.append(Drink(name_of_drink, self.drinks[name_of_drink], cnt_of_drink))
            return True
        return False

    def try_add_snack(self, name_of_snack, cnt_of_snack):
        if name_of_snack in self.snacks:
            self.snacks_list.append(Snack(name_of_snack, self.snacks[name_of_snack], cnt_of_snack))
            return True
        return False


class BurgerKing:
    def __init__(self):
        self.users = {}

    def new_order_from_user(self, user, order):
        if user not in self.users:
            self.users[user] = User()
        cnt_burgers = 0
        cnt_drinks = 0
        cnt_snacks = 0
        for position in order:
            if self.users[user].try_add_burger(position[0], position[1]):
                cnt_burgers += 1
            elif self.users[user].try_add_drink(position[0], position[1]):
                cnt_drinks += 1
            elif self.users[user].try_add_snack(position[0], position[1]):
                cnt_snacks += 1

        for burger in self.users[user].burgers.keys():
            flag = True
            for already_in_order in self.users[user].burgers_list:
                if burger == already_in_order.name:
                    flag = False
                    break
            if flag:
                self.users[user].try_add_burger(burger, 0)

        for drink in self.users[user].drinks.keys():
            flag = True
            for already_in_order in self.users[user].drinks_list:
                if drink == already_in_order.name:
                    flag = False
                    break
            if flag:
                self.users[user].try_add_drink(drink, 0)

        for snack in self.users[user].snacks.keys():
            flag = True
            for already_in_order in self.users[user].snacks_list:
                if snack == already_in_order.name:
                    flag = False
                    break
            if flag:
                self.users[user].try_add_snack(snack, 0)

    def genereate_combos(self):
        burgers_sorted = Burger.get_sorted(self.users['user'].burgers_list)
        drinks_sorted = Drink.get_sorted(self.users['user'].drinks_list)
        snacks_sorted = Snack.get_sorted(self.users['user'].snacks_list)
        combos = []
        for i in range(min(min(len(burgers_sorted), min(len(drinks_sorted), len(snacks_sorted))), 3)):
            combo = f"{burgers_sorted[i].name}\n{drinks_sorted[i].name}\n{snacks_sorted[i].name}\n{burgers_sorted[i].price + drinks_sorted[i].price + snacks_sorted[i].price}₽"
            combos.append(combo)
        return combos
