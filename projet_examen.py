

N_délégué = 0
Liste0 = []
Liste1 = []
while N_délégué > 0:
    N = int(input("Entrez le nome de délégués à élir : "))
print("Donnez le nom des  délégués :")
numro_1 = input(" candidat N°1 ->")
numro_2 = input(" candidat N°2 ->")
for K in range(10):
    print(f"Vous êtes le {K + 1} votant !!!! ")
    user = int(input("entre un numero entre 1 et 2 : "))
    Liste1.append(user)
cpt1 = Liste1.count(1)
cpt2 = Liste1.count(2)
print(cpt1, cpt2)
if cpt1 > cpt2:
    print(f"Le gagnant est {numro_1} avec {cpt1} votants sur {cpt2} pour {numro_2}")
elif cpt1 < cpt2:
    print(f"Le gagnant est {numro_2} avec {cpt2} votants sur {cpt1} pour {numro_1}")
elif cpt1 == cpt2:
    print(f"{numro_1} et {numro_2} sont à égalité avec chacun {cpt1} votants.")
else:
    print("FIN DES VOTES")
