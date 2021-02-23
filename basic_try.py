import sys
colors=["red","blue",
        "green"]
try:
    print(colors[5])
except:
    print("you are out of your league")
    print(sys.exc_info()[1])
print("play ball")

