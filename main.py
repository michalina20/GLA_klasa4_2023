input = open("ekodom.txt","r")


data_zakonczenia = 0
data_rozpoczecia = 0
dr = None
max_okres = None
ilosc = 0
for i in input:
   i= i.split()
   if int(i[1])==0:
       if ilosc == 0:
           dr = i[0]
       ilosc= ilosc + 1
       print(ilosc)
   else:
       ilosc = 0
   if max_okres == None or max_okres <ilosc:
       max_okres = ilosc
       data_zakonczenia = i[0]
       data_rozpoczecia = dr
print("najdluzszy okres:", max_okres)
print("data rozpoczecia:", data_rozpoczecia)
print("data zakonczenia:", data_zakonczenia)


