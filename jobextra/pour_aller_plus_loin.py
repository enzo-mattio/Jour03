def inverser_caractère(ma_chaine):
  # slicing pour inverser la chaîne
  chaine_inverse = ma_chaine[::-1]
  return chaine_inverse

ma_chaine_endroit = "nikana"
ma_chaine_inverse = inverser_caractère(ma_chaine_endroit)
print(ma_chaine_inverse)