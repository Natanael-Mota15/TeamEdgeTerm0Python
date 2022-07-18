#********************************************************************
                                                                  
 #  Team Edge list Challenges!                                     
  
 #  Use this program to learn about Python lists:
    
 #  1. Declare and store data in lists
 #  2. Access list data by index
 #  3. Modify list data by index
 #  4. Multi-dimensional lists (lists inside lists!)
 #  5. List methods: append() and pop()
 #  6. The length of the list - introduce conditionals
 #  7. Strings as sequences - join() split() 
 #  
 #  Follow the -->To Dos ! run the program to test often and debug
 # ***************************************************************





print("------------------- CHALLENGE 1 -------------------")
#This is an empty Python list:
empty_list = []

#this list has 5 Strings. We can print it:
names = ["Julian", "Wolf", "Alex", "Steph", "Alessandro"]
print("names: " + str(names))  

#-->TODO: Declare another list called friends with at least 5 strings inside (if you don't have 5 friends make them up!)
people = ["Austen", "jack", "Joni", "Benny", "Eli"]
print("my name" + str(people))

#this list holds numbers
numbers = [12.9, 23.4 , 100, 3.1415 , 500, 1.20]
print("numbers: " + str(numbers)) 

#-->TODO: Declare another list and add in at least 5 numbers. Why five? I don't know. It just feels right.
num = [1, 2, 3, 4, 5]
print("my numbers" + str(num))

#this list has mixed data types. It's allowed in Python!
random_stuff = ["Aardvark", True, False, 1.23, "Grandpa"]
print("random: " + str(random_stuff))

#-->TODO: Declare and log a list filled with the first 5 things that come into your head, booleans, Strings, numbers are all cool,
bla = ["p", 345, "blablabla", "-_-", "wow", 3939393]
print("random things" + str(bla))

#-->TODO: Declare and log two more lists with whatever you want. 
best_things = ["good soda", 15, "games", "life", " in some cases money"]
bad_thing = ["fees", "depts", "bad grades", 0, "grounds"]
print ("best things:" + str(best_things))
print ("bad things" + str(bad_thing))

print("------------------- CHALLENGE 2 -------------------")
 
#This code logs the first element of the names list:
print("The first name is " + names[0])

#-->TODO: Print the name of your best friend from your friends list
print("Best freind:" + people[0])

#-->TODO: Print the first AND last elements of any list you made, or make a brand new one.
print("things:" + best_things[0] + best_things[4])

print("------------------- CHALLENGE 3 -------------------")
#this code changes the value of the second element of the names list, then we print the list:
names[1] = "Alyssa"
print(names)

#-->TODO: Replace your friends! Modify the list to replace any or all of your friends with new ones.
people[0] = "Gaby"
people[1] = "Gio"
people[2] = "Daniel"
people[3] = "Amy"
people[4] = "Andrea"
print(people)

#The code below uses the times_ten() function to multiply the first element in our list by 10:
def times_ten(number):
    number = number * 10
    return number

numbers[0] = times_ten(numbers[0])
print(numbers)

#-->TODO: Write another function that multiplies a number by 1000 and print the list, as above 

def time(num):
    num = num * 1000
    return num

num[0] = time(num[0])
print(num)

#-->TODO: Replace your random list elements with anything you want, using the index. 
best_things[0] = "howl"
best_things[1] = "charzard"
best_things[2] = "pokeball"
best_things[3] = "masterball"
best_things[4] = "boom"

print (str(best_things))

print("------------------- CHALLENGE 4 -------------------")

#As it turns out, you can also store lists within lists! Declare them and store them as variables.
child_list_1 = ["This", "is" , "a", "meaningless", "list"]
child_list_2 = ["This" ,"list" , "is", "also" , "meaningless"]
parent_list = [child_list_1, child_list_2]
print("This list has babies: " + str(parent_list))

#-->TODO: Store and print all the lists we have worked on thus far in a new parent list
lists = [best_things, bad_thing, num, people]
print (str(lists))

print("------------------- CHALLENGE 5 -------------------")

#We can add elements into a list wihtout replacing anything. Using append() adds an element to the END of the list:
movies = ["Toy Story 4", "The Dark Knight", "Parasite"]
print("Movies: " + str(movies))
movies.append("Joker")
movies.append("Black Panther")
print("Movies now has: " + str(movies))
lists.append("awesome")
print(lists)

#-->TODO: Declare a list with 5 favorite songs
fav_songs = ["7 years", "cold as ice", "believer", "something just like this", "sky full of stars"]
#-->TODO: Add 2-3 more songs using .append() and print both before and after.
fav_songs.append("falling")
fav_songs.append("just so you know")
#We can also remove elements using .pop(), which removes the last element or the element at the given index. You can store it after it comes out:
cities = ["New York", "Oakland", "Las Vegas", "Topeka"]
print("cities: " + str(cities))
unwanted_city = cities.pop()
print("unwanted city: " + str(unwanted_city))

#-->TODO: remove your last song using .pop() and print the removed element as above
print("fav_songs: " + str(fav_songs))
unwanted_song = fav_songs.pop()
print("unwanted song: " + str(unwanted_song))
#Note: there are more methods to remove and modify list elements. We will cover those later

print("------------------- CHALLENGE 6 -------------------")

#Lists have properties. one of the most important is the size, or length. Here are two examples:
print(f"I have {len(names)} friends")

how_many_cities = len(cities)
print(f"There are {how_many_cities} ciites in my list")

#-->TODO: Print out the number of friends, or other items from other lists using string literals as above
print("i have " + str(len(people))  + " friends")

#The len() function is key, especially in conditionals or to simply count how many times to do something.

if len(numbers) > 3:
    print("There are more than 3 numbers in my list")
else:
    print("I need more numbers in my list!!!")

#-->TODO: Write another if/else statement to check the size of your songs list. If you have 5 of less, add two more songs!
if len(fav_songs) < 5:
    fav_songs.append("Stiches")
    fav_songs.append("Enemies")
else:
    print("Good Job")


print("------------------- CHALLENGE 6 -------------------")

#Strings can also be thought of lists:
sentence = "I am a boring sentence."
boring_list = sentence.split(" ") #split the sentence by each space to get a list of words
print("boring sentence as a list: " + str(boring_list))

word = "Abracadabra"
word_split_list = word.split() #split by nothing, and you get each character in the string as its own element.
print("letter by letter: " + str(word_split_list))

#using this you can split strings up by any character!
bleb = "bla ble blu"
bleb_split = bleb.split()
print (bleb_split)

#-->TODO: Change the name of the person who is late in this sentence and print it.
split_me = "I heard Alex was late to class today."
splitted_me = split_me.split()
splitted_me[2] = "Bob"
print (str(splitted_me))

#-->TODO: Add an exclamation mark to this sentence using split() and append(), then print. (yes, there are other ways, but...)
make_me_exciting = "What a wonderful day"
use_these_kinds_variables = make_me_exciting.split()
use_these_kinds_variables.append("!")
print(use_these_kinds_variables)
#We can also join our list elements into a string using.....join()!
rejoined = " ".join(boring_list)  #joins it using spaces
print('back in one piece: ' + rejoined)

#-->TODO:  Finally, put the split_me sentence today and the make_me_exciting strings back together and print. You should see a string
xy = " ".join(splitted_me)  
xt = " ".join(use_these_kinds_variables) 
print('back in one piece: ' + xy + xt)