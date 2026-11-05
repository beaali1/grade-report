nomre = {"ali": 18, "sara": 15, "reza": 20, "mina": 11}
bala = 0
boland = ""
print(nomre)
for i in nomre:
    if nomre[i] > bala:
        bala = nomre[i]
        boland = i
print(nomre[i])
print(boland)