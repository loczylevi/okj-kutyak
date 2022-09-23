class Kutya_nevek:
    def __init__(self,sor):
        id_n,kutyanev = sor.strip().split(";")
        self.id_n = id_n
        self.kutyanev = kutyanev
    
class Kutya_fajtak:
    def __init__(self,sor):
        id_fajta,nev_f,eredeti_nev = sor.strip().split(";")
        self.id_fajta = id_fajta
        self.nev_f = nev_f
        self.eredeti_nev = eredeti_nev


class Kutyak:
    def __init__(self,sor):
        id_kutyak,fajta_id,nev_id,eletkor,orvosi = sor.strip().split(";")
        self.id_kutyak = id_kutyak
        self.fajta_id = fajta_id
        self.nev_id = nev_id
        self.eletkor = int(eletkor)
        self.orvosi = orvosi
#id; kutyanév
with open("KutyaNevek.csv","r",encoding="utf-8-sig") as f:
    fejlec1 = f.readline()
    kutya_nevek = [Kutya_nevek(sor) for sor in f]
    
    
#id;  név;  eredeti név
with open("KutyaFajtak.csv","r",encoding="utf-8-sig") as f2:
    fejlec2 = f2.readline()
    kutya_fajtak = [Kutya_fajtak(sor) for sor in f2]


# id;   fajta_id;   név_id;   életkor;   utolsó orvosi ellenőrzés
with open("Kutyak.csv","r",encoding="utf-8-sig") as f3:
    fejlec3 = f3.readline()
    kutyak = [Kutyak(sor) for sor in f3]
    

print(f"3.feladat: Kutyanevek száma: {len(kutya_nevek)}")

korok = [sor.eletkor for sor in kutyak]

atlag = f"{sum(korok) / len(korok):.2f}"

atlag = str(atlag).replace('.',',')

print(f"6.feladat: Kutyák átlag életkora: {atlag}")



nagy = max(korok)

nev_id = [sor.nev_id for sor in kutyak if nagy == sor.eletkor][0]

nev_id_vizsgalo = [sor.kutyanev for sor in kutya_nevek if nev_id == sor.id_n][0]

fajta_id = [sor.fajta_id for sor in kutyak if nagy == sor.eletkor][0]

fajta_id_vizsgalo = [sor.nev_f for sor in kutya_fajtak if fajta_id == sor.id_fajta][0]

print(f"7.feladat: Legidősebb kutya neve és fajtája: {nev_id_vizsgalo}, {fajta_id_vizsgalo}")


allatorvos = [sor.fajta_id for sor in kutyak if sor.orvosi == "2018.01.10"]

nevek = []
for sor in kutya_fajtak:
  for v in allatorvos:
    if v == sor.id_fajta:
      nevek.append(sor.nev_f)
      
print("8.feladat: Január 10.-én vizsgált kutya fajták: ")
[print(f"       {sor}: {sor.count(sor)} kutya") for sor in nevek]

stat = dict()
for sor in kutyak:
    stat[sor.orvosi] = stat.get(sor.orvosi,0) + 1
    
legtobb_terheles_hany_kutya = max([db for orvosi, db in stat.items()])

legtobb_terheles_datum = [orvosi for orvosi, db in stat.items() if legtobb_terheles_hany_kutya == db][0]

print(f"9.feladat: Legjobban leterhelt nap: {legtobb_terheles_datum}: {legtobb_terheles_hany_kutya} kutya")


kutya_idek = [sor.nev_id for sor in kutyak]
nevek_listaja = []
nevek = []
for elem in kutya_idek:
  for nev in kutya_nevek:
    if elem == nev.id_n:
      nevek.append(nev.kutyanev)
      
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