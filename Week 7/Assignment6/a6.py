#!/usr/bin/env python
# coding: utf-8


a = []
#Hello, please change the following code to f = open("home/$USER/Assignment6/agesex.csv, "r")
#if you will open it in tux. 
f = open("agesex.csv", "r")
for x in f:
    y = x.rstrip()
    z = list(y.split(","))
    a.append(z)
    #print(y)
print("\n\n")


def percentChange(a, b):
    if (a<b):
        diff = b-a
        change = (diff/a) * 100
        return round(change, 2)
    else:
        diff = a-b
        change = (diff/a) * 100
        return round(change, 2)
def proportion(t, a):
    percentA = (a/t)*100
    return round(percentA, 2)
print("SEX\t AGE\t    2010\t    2017\t  CHANGE\tPERCENT_CHANGE")
for i in range((len(a))):
    for j in range((len(a[0]))):
        if (a[i][j] == "999"):
               print(a[i][0],"\t", a[i][1],"\t", a[i][4],"\t", a[i][11],"\t", int(a[i][11]) - int(a[i][4]),"\t", percentChange(int(a[i][4]), int(a[i][11])))
print("\n\nThe male population changed more.\n\n")
print("---" * 25)
print("\n\n")



print("SEX\t AGE\t    2017\tProportion")
for i in range((len(a))):
    for j in range((len(a[0]))):
        if (a[i][j] == "0" and a[i][j+1] == "999"):
            total = int(a[i][11])
            print(a[i][0],"\t", a[i][1],"\t", total,"\t", "100%")
        if (a[i][j] == "1" and a[i][j+1] == "999"):
            b = int(a[i][11])
            print(a[i][0],"\t", a[i][1],"\t", b,"\t", proportion(total, b))
        if (a[i][j] == "2" and a[i][j+1] == "999"):
            b = int(a[i][11])
            print(a[i][0],"\t", a[i][1],"\t", b,"\t", proportion(total, b))
print("\n\nThe female population has the biggest proportion.\n\n")





