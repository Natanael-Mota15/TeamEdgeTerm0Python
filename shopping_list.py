#********************************************************************
 #                                                                 
 #  Team Edge List Mini-project: THE SHOPPING LIST HELPER
 # 
 #  This project prompts users using input() to prompt users
 #  to add (or remove) items from a shopping list. It starts empty
 #  and each time the program is run it asks you to either add or 
 #  remove an item from the list. It also updates the user of its
 #  contents. The shopping list also checks to see if an item 
 #  is already present in the list and prevents you from adding it
 #  again, giving feedback along the way. 
 # 
 # ***************************************************************/
import random

active = True

print("Welcome to Shopping List!")
wallet = input("how much is in your wallet?")
welcome_message = ("Hi! I'm your shopping assistant. Let me take your order. \n You can type 'add milk' to add milk to your shopping list. \n or you can type 'remove milk' to remove it. \n")





#-->Todo: declare a shopping_list list
list = []




def prompt_user():
    print(f"You have this amount to spend:{wallet}")
    reply = input("What do you want to add, remove, replace or checkout?  >>  ")
    rs = reply.split()
    if reply == "add":
        add_item()
    elif rs[0] == ("add") and rs[1] == str(rs[1]):
        y = rs[1]
        if y in list:
            print("You already have that")
            prompt_user()
        else:
            list.append(y)
            print (list)
            print (f"Amount of items:{len(list)}")
            prompt_user()

    elif reply == "remove":
        remove_item()
        rs = reply.split()
    elif reply == "replace":
        replace()
    elif rs[0] == ("remove") and rs[1] == str(rs[1]):
        rsx = rs[1]
        list.remove(rsx)
        print (list)
        print (f"Amount of items:{len(list)}")
        prompt_user()
    elif reply == "checkout":
        print (f"Amount of items:{len(list)}")
        price()
        print ("Items:\n" + str(list)  + "\nthanks  for shopping, have a nice day!")
    else:
        print("not an option, be more clear")
        prompt_user()
    return reply


def check_answer():
    num = random.randrange(1,3) 
    if num == 1:
        print(welcome_message)
    elif num == 2:
        print("Hi! I'm your shopping assistant. Let me take your order. \n Just choose between add or remove and order")
    pass
check_answer()

def add_item():
#this function can take in a string and store it in an array
    y = input("What do you want to add?")
    if (y == "") or (y == " ") or (y == "  ") or (y == "   "):
        print ("error")
        add_item()
    if y in list:
        print("You already have that")
        prompt_user()
    else:
        list.append(y)
        print (list)
        print (f"Amount of items:{len(list)}")
        prompt_user()
    pass


def remove_item():
    x = input("What do you want to remove?")
    if (x == " ") or (x == "  ") or (x == "   "):
        print ("error")
        remove_item()
    else:
        list.remove(x)
        print (list)
        print (f"Amount of items:{len(list)}")
        prompt_user()
    pass

def replace():
    rp = input("What do you want to replace?")
    rpp = input("With what?")
    if rp in list: 
        num = list.index(rp)
        list[num] = rpp
        print(list)
        print (f"Amount of items:{len(list)}")
        prompt_user()
    if rp not in list:
        print("error, try again later")
        prompt_user()

def price():
    if len(list) == 0:
        pricet = 0
    elif len(list) == 1:
        pricet = random.randrange(5, 10)
    elif len(list) == 2:
        pricet = random.randrange(10, 15)
    elif len(list) == 3:
        pricet = random.randrange(15, 20)
    elif len(list) == 4:
        pricet = random.randrange(20, 25)
    elif len(list) == 5:
        pricet = random.randrange(25, 30)
    elif len(list) == 6:
        pricet = random.randrange(30, 35)
    elif len(list) == 7:
        pricet = random.randrange(35, 40)
    total = int(wallet) - pricet
    print ("total:" + str(pricet))
    if int(pricet) > int(wallet):
        print ("you to poor")
    else:
        print ("money remaining:" +  str(total))





prompt_user()
while active:
    list.sort()
   # check_answer(prompt_user()) 
    #this makes the program continously prompt and check response while the boolean 'active' returns True