print("Az alabbi típusok vannak: nev, magassag, varos, szem, kg")
tipus=input("Mi alapjan szurunk?")
feltetel=input("add meg a feltetelt:")

gege={"nev":"gege","magassag":188,"varos":"budapest","szem":"zold","suly":90}
gergo={"nev":"gergo","magassag":188,"varos":"budapest","szem":"zold","suly":9}

for i in (gege,gergo):
    if str(i[tipus]) == feltetel:
        print ("Neve: ",i["nev"], "Magassaga: ", i["magassag"])