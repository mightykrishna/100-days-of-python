scores=input("input a list of student");
for i in range(0,len(scores)):
    scores[i]=int (scores[i])
print(scores)
max=0
for i in scores:
    if i>max:
        max=i

print(f"The highest score in the class is :{max}")

    
