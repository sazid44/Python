'''
#Exercise 1
phone=input("phone: ")
dictionary={
    "1":"one",
    "2": "two",
    "3": "three",
    "4": "four",
}
output=''
for a in phone:
  output+=dictionary.get(a, "!")+" "
print(output)

# Exercise 2
message=input(">")
words=message.split(' ')
dict={
    "happy":"(❁´◡`❁)",
    "sad":"`(*>﹏<*)′"
}
out = ""
for word in words:
    out +=dict.get(word,word) +" "
print(out)
'''
#Exercise 3
q1='What is the color of grass?\n1.red\n2.blue\n3.green'
user=input(q1+"\nans: ")
if(user=='c'):
    print("You are correct")
else:
    print("You are wrong")