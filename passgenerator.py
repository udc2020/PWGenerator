import random
import string

def final_pass():
   characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")


   ## shuffling the characters
   random.shuffle(characters)

   ## picking random characters from the list
   password = []
   for i in range(10):
      password.append(random.choice(characters))

   ## shuffling the resultant password
   random.shuffle(password)

   ## converting the list to string
   ## printing the list
   
   return "".join(password)

