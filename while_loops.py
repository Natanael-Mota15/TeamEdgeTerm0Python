#********************************************************************
 #                                                                  
 #  Team Edge Mini-project: WHILE LOOP CHALLENGES
 # 
 #   Complete the following loop challenges below. Follow the ToDos
 #   1. IN YOUR PRIME: Declare a while loop that prints all the prime 
 #      numbers between 0 and 100 (use the helper function provided)
 #   2. FOUND: use a while loop to search the contents of a list for
 #     the key!
 #   3. BUGGIN: Find out why these while loops don't do what they say 
 #     they do.
 #   4. MATH QUIZ: Prompt a user to solve a random math problem, if 
 #      they get it right, say congrats, if not, keep prompting.
 #   5. WHAT AM I: Write a game loop that prompts that never stops
 #      asking, "Iknow you are a _____, but what am I?"
 # 
 # ***************************************************************/
import random
print("------------------- CHALLENGE 1 : IN YOUR PRIME -------------------")

#Here is a humble while loop in action. We need a variable to hold the counter value.
num = 0
while num <= 10:
    print("example counter--> " + str(num))
    num += 1


#------------ Helper function, do not mess with this part below ---------------??

def test_prime(n):
  if n==1:
    return False

  elif n == 2:
    return True

  else:
    for x in range(2, n-1):
      if n % x == 0:
        return False
    return True

#-->TODO: Declare a while loop that prints all the prime numbers between 0 and 100, use test_prime() helper function
num_1 = 0
while num_1 <= 100:
  if test_prime(num_1):
    print(num_1)
  num_1 += 1




print("------------------- CHALLENGE 2 : FOUND   -------------------")

#here is a list full of items
items = ["pencil" , "eraser" , "mirror" , "comb" , "spoon" , "key" , "earrings" ,"cat food" , "magazine"]

#-->TODO: Use a while loop to search the contents of a list for the key! If it exists, print "found the key!"
y = -1
while items[y] != "key":
  if y < len(items):
    y += 1
if items[y] == "key":
  print("Key here")


print("------------------- CHALLENGE 3 : BUGGIN   -------------------")

#Oh no! these functions have loops that don't do what they say they should do. Can you fix that?
#One more thing...to stop an infite loop you hit Control + C in the terminal  

#-->TODO: Make me count  2, 4, 6,..., 50

def even_numbers_to_fifty():
    num = 0
    while num < 50:
      num += 2
      print("number: " + str(num))

even_numbers_to_fifty()

#-->TODO: Make this design  below
#
#          [ 0 ]
#          [ 0, 1 ]
#          [ 0, 1, 2 ]
#          [ 0, 1, 2, 3 ]
#          [ 0, 1, 2, 3, 4 ]
#          [ 0, 1, 2, 3, 4, 5 ]
#          [ 0, 1, 2, 3, 4 ]
#          [ 0, 1, 2, 3 ]
#          [ 0, 1, 2 ]
#          [ 0, 1 ]
#          [ 0 ]



def pattern():

  index = 0 
  my_list =[]
  pl = 5  
  while index <= 5:
    my_list.append(index)
    print(my_list)
    index += 1

  while pl >= 1:
    my_list.pop(pl)
    print(my_list)
    pl -= 1

 

    

pattern()


print("------------------- CHALLENGE 4 : MATH QUIZ   -------------------")



#-->TODO: Make a Math Quiz that asks two random numbers (between 0 and 100 to make it easy).
#         The user enters the answer. If wrong, keep prompting. If correct, say congrats!!
#         Use this handy boolean to get you started! You will need input()!

is_correct = False

#num1 = random.randrange(1, 100)
#num2 = random.randrange(1, 100)
#sum1 = num1 + num2

#ans = input(f" what is the sum of {num1} and {num2}")
#if int(ans) == sum1:
 # print("Correct")
 # ansc = True
#elif int(ans) != sum1:
#  ansc = False
#while ansc == False:
 # print("No, try again")
  #ans = input(f" what is the sum of {num1} and {num2}")





print("------------------- CHALLENGE 5 : WHAT AM I?   -------------------")

#-->TODO: Write a game loop that prompts that never stops asking, "I know you are a _____, but what am I?"
#         You are given two starter functions and a loop to get started! 
#         Notice how one function calls the other and uses the returned value as the input. This is called Recursion! 

keep_asking = True
active = True
def prompt_user():
  global ans
  ans = input ("I know you are a person, but what am I?")
  response()
  pass

def response(ans):
  if ans == "something":
    print ("correct")
  elif ans == "stop":
    print("ok")
    active = False
  elif (ans != "stop") and (ans  != "something"):
    print("sorry")
    pass

#-->TODO: Challenge! write a secret word to break out of the loop!
while active:
  prompt_user(response(ans))