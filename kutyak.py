
#id; kutyanév

# 0      1
with open("KutyaNevek.csv","r",encoding="utf-8-sig") as f:
    fejlec1 = f.readline()
    kutya_nevek = [sor.strip().split(";") for sor in f]
    
    
#id;  név;  eredeti név
    
# 0     1         2

with open("KutyaFajtak.csv","r",encoding="utf-8-sig") as f2:
    fejlec2 = f2.readline()
    kutya_fajtak = [sor.strip().split(";") for sor in f2]


# id;   fajta_id;   név_id;   életkor;   utolsó orvosi ellenőrzés

# 0          1        2           3               4

with open("Kutyak.csv","r",encoding="utf-8-sig") as f3:
    fejlec3 = f3.readline()
    kutyak = [sor.strip().split(";") for sor in f3]
    

print(f"3.feladat: Kutyanevek száma: {len(kutya_nevek)}")

korok = [int(sor[3]) for sor in kutyak]

atlag = f"{sum(korok) / len(korok):.2f}"

atlag = str(atlag).replace('.',',')

print(f"6.feladat: Kutyák átlag életkora: {atlag}")


    
# id;   fajta_id;   név_id;   életkor;   utolsó orvosi ellenőrzés

# 0          1        2           3               4

nagy = max(korok)

nev_id = [sor[2] for sor in kutyak if nagy == int(sor[3])][0]

nev_id_vizsgalo = [sor[1] for sor in kutya_nevek if nev_id == sor[0]][0]

fajta_id = [sor[1] for sor in kutyak if nagy == int(sor[3])][0]

fajta_id_vizsgalo = [sor[1] for sor in kutya_fajtak if fajta_id == sor[0]][0]

print(f"7.feladat: Legidősebb kutya neve és fajtája: {nev_id_vizsgalo}, {fajta_id_vizsgalo}")


allatorvos = [sor[1] for sor in kutyak if sor[4] == "2018.01.10"]


#id;  név;  eredeti név
    
# 0     1         2

nevek = []
for sor in kutya_fajtak:
  for v in allatorvos:
    if v == sor[0]:
      nevek.append(sor[1])
      
print("8.feladat: Január 10.-én vizsgált kutya fajták: ")
[print(f"       {sor}: {sor.count(sor)} kutya") for sor in nevek]

stat = dict()
for sor in kutyak:
    stat[sor[4]] = stat.get(sor[4],0) + 1
    
legtobb_terheles_hany_kutya = max([db for orvosi, db in stat.items()])

legtobb_terheles_datum = [orvosi for orvosi, db in stat.items() if legtobb_terheles_hany_kutya == db][0]

print(f"9.feladat: Legjobban leterhelt nap: {legtobb_terheles_datum}: {legtobb_terheles_hany_kutya} kutya")
print("10.feladat: névstatisztika.txt")

kutya_idek = [sor[2] for sor in kutyak]
nevek_listaja = []
nevek = []
for elem in kutya_idek:
  for nev in kutya_nevek:
    if elem == nev[0]:
      nevek.append(nev[1])
      
stat_nevek = dict()
for nev in nevek:
    stat_nevek[nev] = stat_nevek.get(nev,0) + 1
    
for nev,db in stat_nevek.items():
    nevek_listaja.append(f"{nev};{db}")


class Nevek:
    def __init__(self,sor):
        nev,szam = sor.strip().split(";")
        self.nev = nev
        self.szam = int(szam)
        
        
with open("Névstatisztika.txt","w",encoding="UTF-8") as f2:
    for sor in nevek_listaja:
        f2.write(sor+"\n")
    

with open("Névstatisztika.txt","r",encoding="UTF-8") as f3:
    lista = [Nevek(sor) for sor in f3]
    
with open("Névstatisztika.txt","w",encoding="utf-8") as f4:
  lista.sort(key=lambda x:x.szam, reverse=True) 
  for sor in lista:
    f4.write(f"{sor.nev};{sor.szam}\n")