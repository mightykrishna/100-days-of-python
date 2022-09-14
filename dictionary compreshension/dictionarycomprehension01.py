sentence="What is the Airspeed Velocity of an Unladen Swallow?"
#for word in sentence.split():
#    print(word)
result ={word: len(word) for word in sentence.split()}
print(result)