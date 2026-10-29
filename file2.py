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
    miangin = jam / len(matn.split())

with open("gozaresh.txt" , "w") as g:
    g.write("miangin:" + str(miangin) +"\n")
    g.write("behtarin:" + behtarin + "\n")
    g.write("balatarin:" + str(bala) + "\n")


    

    
        