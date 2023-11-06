"""
Aprēķināt noteiktas skaitļu summu no 1 līdz n, kur n ir lietotāja ievadīts skaitlis.
"""

n=int(input("Ievadi skaitli: "))
summa=0
# 1----5---1+2+3+4

for skaitlis in range (1,n+1):
    summa+=skaitlis

print(f"Skaitļu no 1 līdz {n} summa ir {summa}.")
