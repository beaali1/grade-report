with open("nomre.txt") as f:
    matn = f.read()
    bala = 0
    jam = 0 
    behtarin = ""
    for nomre in matn.split():
        i = nomre.split(",")
        jam = int(i[1]) + jam
        if int(i[1]) > bala:
            bala = int(i[1])
            behtarin = i[0]
    print("behtarin:",behtarin,":",bala,"\n")
    print(jam/len(matn.split()))

    

    
        