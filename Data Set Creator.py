import random

open("dataset.ds", "w").write("")

with open("dataset.ds", "a") as file:
    for i in range(10000):
        rd = random.randint(0, 99999999)
        file.write(str(rd) + ":" + str(rd*2) + "\n")

