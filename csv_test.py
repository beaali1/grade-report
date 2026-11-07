with open("nomre.csv") as f:
    matn = f.read()
    jam = 0
    for khat in matn.split()[1:]:
        i = khat.split(",")
        jam = jam + int(i[1])
        
miangin = jam / len(matn.split()[1:])
print(miangin)