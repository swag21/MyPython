# ========================== SWAG 21 ============================================================================
# Peanut Butter Jelly Time!

# First Goal: Create a program that can tell you whether or not you can make a peanut butter and jelly sandwich

# Second Goal: Modify that program to tell you: if you can make a sandwich, how many you can make

# Third Goal: Modify that program to allow you to make open-face sandwiches if you have an odd number of slices of bread ( )

# Fourth Goal: Modify that program to tell you: if you're missing ingredients, which ones you need to be able to make your sandwiches

# Fifth Goal: Modify that program to tell you: if you have enough bread and peanut butter but no jelly, that you can make a peanut butter sandwich but you should take a hard, honest look at your life.  Wow, your program is kinda judgy.


# What are the step-by-steps to recreate this?
# First, you need variables to store your information.  Remember, variables are just containers for your information that you give a name.

# You need three ingredients to make a PB&J, so you'll want three different variables:
# 		How much bread do you have? (make this a number that reflects how many slices of bread you have)
#		How much peanut butter do you have? (make this a number that reflects how many sandwiches-worth of peanut butter you have)
#		How much jelly do you have? (make this a number that reflects how many sandwiches-worth of jelly you have)




# For this exercise, we'll assume you have the requisite tools (plate, knife, etc)
# Once you've defined your variables that tell you how much of each ingredient you have, use conditionals to test whether you have the right amount of ingredients


# Based on the results of that conditional, display a message.

# To satisfy the first goal:
#		If you have enough bread (2 slices), peanut butter (1), and jelly (1), print a message like "I can make a peanut butter and jelly sandwich"; 
#		If you don't; print a message like "Looks like I don't have a lunch today"

# To satisfy the second goal:
#		Continue from the first goal, and add:
#		If you have enough bread (at least 2 slices), peanut butter (at least 1), and jelly (at least 1), print a message like "I can make this many sandwiches: " and then calculate the result.
#		If you don't; you can print the same message as before

# To satisfy the third goal:
#		Continue from the second goal, and add:
#		If you have an odd number of slices of bread* and odd amount of peanut butter and jelly, print a message like before, but mention that you can make an open-face sandwich, too.
#		If you don't have enough ingredients; still print the same message as before
#		* To calculate whether you have an odd number, see https://github.com/shannonturner/python-lessons/blob/master/section_01%20%28basics%29/simple_math.py

# To satisfy the fourth goal:
#		Continue from the third goal, but this time if you don't have enough ingredients, print a message that tells you which ones you're missing.

# To satisfy the fifth goal:
#		Continue from the fourth goal, but this time if you have enough bread and peanut butter but no jelly, print a message that tells you that you can make a peanut butter sandwich
#		Or if you have more peanut butter and bread than jelly, that you can make a certain number of peanut butter & jelly sandwiches and a certain number of peanut butter sandwiches

# --------------------------------------------------------------------------------

#define variables
bread_count = raw_input("What is the bread count:");
peanutButterSpead_count = raw_input("What is the peanut butter:");
jelly_count = raw_input("What is the jelly count:");


#convert string to int
try:
    bread_count = int(bread_count)
except ValueError:
    bread_count = 0


try:
    peanutButterSpead_count = int(peanutButterSpead_count)
except ValueError:
    peanutButterSpead_count = 0

try:
    jelly_count = int(jelly_count)
except ValueError:
    jelly_count = 0

print"\n -----------RESULT PB&J sandwiches ----------------";

if (bread_count > 0 and (bread_count % 2)  == 0):
     print "Have even amount of bread";
else :
     print "Have odd amount of bread";

message = "Looks like I don't have a lunch today";


not_enough_jelly = ((bread_count % 2)  == 1 and (peanutButterSpead_count % 2)  == 1 and (jelly_count % 2))  == 0 ;

if (bread_count >= 2 and (peanutButterSpead_count > 0)  and (jelly_count > 0)) :
    message = "I can make many sandwiches: {0}".format(bread_count / 2);
    if (bread_count == 2 and (peanutButterSpead_count == 1)  and (jelly_count == 1)):
       message  = "I can make a peanut butter and jelly sandwich";
    
    if((bread_count % 2)  == 1 and (peanutButterSpead_count % 2)  == 1 and (jelly_count % 2)  == 1 ):
      message = message + "\n I can also make open faced sandwich!";
    if(bread_count >= 2 and peanutButterSpead_count > 0 and (not_enough_jelly or (jelly_count < 0))) :
       message = message + "\n Can make {0} Peanut Butter Sandwich only.".format((bread_count / 2));

if(bread_count < 2) :
    message = message + "\n Not enough Bread";
if(peanutButterSpead_count < 1) :
  message = message + "\n Not enough Peanut Butter";
if(jelly_count < 1) :
  message = message + "\n Not enough Jelly";

print message;
