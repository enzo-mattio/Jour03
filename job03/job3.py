def afficher_chiffres():
    for i in range(101):
        if i == 26 or i == 37 or i == 88:
            continue
        print(i)

afficher_chiffres

def afficher_chiffres2():
  i = 0
  while i <= 100:
    if i == 26 or i == 37 or i == 88:
            i += 1
            continue
    print(i)
    i += 1

afficher_chiffres2()