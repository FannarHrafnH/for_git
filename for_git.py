#Fannar Hrafn Haraldsson
#24.1.17
#forritun gitverkefni
#1.spurning
#cd er hvernig við færum okkur um skelina
#cd ~ færir okkur á root
#ls segir okkar hvað er að gerast í kringum okkur
#pwd segir okkur hvar við erum og hvaða PATH það er
#mkdir býr til möppu
#2.spurning
#git clone leyfir manni að gera afrit af geymslu
#git log sýnir allar skráningar
#git status sýnir vegi sem hafa mun á milli index og HEAD skráningu
#git diff sýnir munin á milli greinar og einhvers annars
#git checkout sækir ákveðna grein
#3.spurning
#a)sýnir breytingar sem þú hefur gert en ert ennþá ekki búinn að commita
#b)munur mill index og síðasta commitinu þínu, það sem þú mundur commita ef þú notar git commit án -a
#c)sjá muninn milli tveggja commits
#4.spurning
#kerfi eins og git til að skrá útgáfur og vinna á sama kóða á sama tíma og aðrir
#5.spurning
#hafa skráningu af öllum breytingum og geta unnið á kóða hjá sjálfum sér án þess að það hafi áhrif á aðra sem eru líka að vinna með sama kóða
#6.spurning
#hvert sinn sem að þú hefur gert kóða sem virkar
#7.spurning
#Working directory er directory með öll files undir git stjórn
#staging area er file sem innheldur allt sem mun bætast við næst þegar þú commitar
#repository er þar sem þú geymir allar úgáfunar
#8.spurning
#eiginlega alltaf, engin ástæða til að vera að breyta master alltaf, betra að gera breytingar fyrst annar staðar og síðan commita
#9.spurning
#Linus Torvald
#10.spurning
#Allstaðar sem þarf að vinna við kóða eða rafræn skjöl

#Liður 1
#spyr notenda um tvær tölur
tala1=int(input("Sláðu inn tölu 1: "))
tala2=int(input("Sláðu inn tölu 2: "))
#reikna summu
tala3=tala1+tala2
#reikna margfeldi
tala4=tala1*tala2
#prenta niðurstöður
print("Summa talna er:",tala3,)
print("Margfeldi talna er:",tala4)
#Liður 2
#Spyr notanda um fornafn og eftirnafn
fornafn=input("Fornafn?: ")
eftirnafn=input("Eftirnafn: ")
#prenta halló
print("Halló",fornafn,eftirnafn)
#Liður 3
#spyr notanda um texta
strengur=input("Sláðu inn texta: ")
#geri teljara til hér fyrir for lykkju
lastafir=0
hastafir=0
#fer í gegnum streng og finn hástafi,lástafi og lástafi eftir hástöfum
for stak in strengur: