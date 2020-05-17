import math

tinggi = int(input("Parameter : "))

def bolaPantul(tinggi):
    minimumpantulan = 1
    tinggipantulan = 0.75
    hasil1 = minimumpantulan/tinggi
    lnhasil1 = math.log(hasil1)
    lntinggipantulan = math.log(tinggipantulan)
    totalpantulandibawah1m = (lnhasil1/lntinggipantulan) + 1



    print('Return : ',totalpantulandibawah1m)

bolaPantul(tinggi)