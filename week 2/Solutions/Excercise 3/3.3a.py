# Exercise 3.3
s=input("Enter a string: ")
total=0
for i in range(1,len(s),2):
    print(s[i])
    if s[i] in "aeiou":
        total+=1
print(total)