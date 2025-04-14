# we  ahve to give 2 args then
# we  can add only 1 argument


def make_pizza(*toppings,base):
    print(toppings,base)

vrush = make_pizza("tomato","paneer",base ="thin crust") # so here its notaking so we need to pass base
print(vrush)