
fruits=["Apple","Mango","Banana"]
def make_pie(index):
    try:
        fruit=fruits[index]
    except IndexError:
        print(" fruit pie")
    else:
        print(fruit +"pie")

make_pie(2)