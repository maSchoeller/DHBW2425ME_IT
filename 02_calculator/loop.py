loopSize = int(input("Bitte geben Sie die Anzahl der Wiederholungen ein: "))
liste = range(loopSize)
print(liste)
# for i in liste:
#     print("Hallo Welt!" + str(i))

while loopSize >= 0:
    print("Hallo Welt!" + str(loopSize))
    loopSize -= 1
