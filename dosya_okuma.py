f=open('Arabalar.txt')
aboneListesi=[]
for l in f:
    ls=l.strip()
    ll=ls.split(':')
    aboneListesi.append(ll[0])