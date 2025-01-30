score = 0
question = "answer the questions or die?"
print (question)
user_answer = input ("your answer:")
if user_answer.lower() == "yes":
    print ("exactly!")
    score += 1
else:
    print ("oops! the correct answer is YES.")
 

question = "yazzi ate too much bread, true or false?"
print (question)
user_answer = input ("your answer:")
if user_answer.lower() == "true":
    print ("VERY TRUE!!")
    score += 1
else:
    print ("oops! the correct answer is TRUE.")
  

question = "is mia britsh, true or false?"
print (question)
user_answer = input ("your answer:")
if user_answer.lower() == "false":
    print ("mia is in fact NOT british")
    score += 1
else:
    print ("oops! the correct answer is FALSE.")
    

question = "does nati need to go outside and blow her nose there, true or false?"
print (question)
user_answer = input ("your answer:")
if user_answer.lower() == "true":
    print ("YESSSS")
    score += 1
else:
    print ("oops! the correct answer is TRUE.")

question = "cats or dogs?"
print (question)
user_answer = input ("your answer:")
if user_answer.lower() == "cats":
    print ("yes of course")
    score += 1
else:
    print ("oops! the correct answer is CATS!!.")


question = "where is astrid from??"
print (question)
user_answer = input ("your answer:")
if user_answer.lower() == "sweden":
    print ("YES IKEA LAND")
    score += 1
else:
    print ("oops! the correct answer is SWEDEN.")
print (f"your score is {score}")