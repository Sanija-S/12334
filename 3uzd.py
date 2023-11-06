"""
Izvadīt visus pirmsskaitļus no 1 līdz 100, izmantojot for un if.

1) kas ir pirmskaitlis- skaitlis lielaks par 1 kas dalas ar 2 skaitliem
20 apgabals....1 lidz 100
3.0 priekšraksti for un if

# nosaku gala punktu, **- kvadrat sakne 
"""

def ir_pirmskaitlis(skaitlis):
    if skaitlis<2:
        return False
    for dalītajs in range(2, int(skaitlis**0.5)+1) 
     if skaitlis% dalītajs==0:
        return False
     return True
    for skaitlis in range(1,101):
       if ir_pirmskaitlis(skaitlis):
          print(skaitlis, end= " ")
