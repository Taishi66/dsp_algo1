[Marc LY]-->	Proposition de travail avec ce document :
	[1]	Vous pouvez tenter de deviner ce que va être le résultat de l'exécution de chaque programme.
	[2] Vous pouvez copiez (et peut-être corriger au besoin) les programmes dans un interpréteur python, puis exécutez le code.
--
	Pour information, en général, entre chaque "----", vous avez du code qui fonctionne ^_^
	Pensez donc à bien effacé tout code residuel avant de tester quelque chose pour éviter d'avoir des "effets de bords" venant d'un programme précédent ou d'une ligne qui traînait par là :o)
--
	Je vous rappelle quelqu'un lien pour vous informez un peu plus sur python notamment (mais pas que) :
	[ ] https://www.w3schools.com
	[ ] le tuto python du W3C -->	https://www.w3schools.com/python/default.asp
	[ ] la partie "références" -->	https://www.w3schools.com/python/python_reference.asp
	[ ] les tables ou les listes -->	https://www.w3schools.com/python/python_arrays.asp
	[ ] la boucle for (pour) -->	https://www.w3schools.com/python/python_for_loops.asp
	[ ] la boucle while (tant que) -->	https://www.w3schools.com/python/python_while_loops.asp
--
	Et pensez à ouvrir ce fichier avec un éditeur de texte, pas un traitement de texte :o>
	... surtout si vous voulez faire des copiés/collés ^_^~
.

#######################################################################################################################

print("Bonjour tout le monde ^_^")


----

if 5 > 2:
	print("Five is greater than two!")

----

if not 5 > 2:
	print("5 est supérieur à 2")
else:
		print("Five is greater than two!")


----

messageEnCasDeOui = "5 est supérieur à 2"
 
if not 5 > 2:
	print(messageEnCasDeOui)
	print(messageEnCasDeOui)
	print(messageEnCasDeOui)
	print(messageEnCasDeOui)
	print(messageEnCasDeOui)
else:
		print("Five is greater than two!")
		print("Five is greater than two!")
		print("Five is greater than two!")
		print("Five is greater than two!")
		print("Five is greater than two!")
		print("Five is greater than two!")
 
 
----

messageEnCasDeOui = "5 est supérieur à 2 - nouveau message"
 
if 5 > 2:
 print(messageEnCasDeOui)
else:
       print("Five is greater than two!")
 
 
----

x = 3.14  # j'affecte la valeur de pi à x
y = "c'est la valeur de pi"
 
print(x, y)
 
 
----

x = 3.14
y = "John... n'est pas français"
print(x)
print(y)
 
 
----

x = 5
y = "John... n'est pas français 1345435345 9 3 49 "
print(x)
print(y)
 
print(type(x))
print(type(y))  # y est une string -- une chaîne de
 
 
----

 
a12 = 0
leNomDeMaMere = "Nathalie"
le_nom_de_m28349a_m82394ere = "Nathalie"
 
#NON, la variable "1a" ne peut pas être définie -->		1a = 7

_leNomDeMonPere = "quelconque"
 
 
----

x = "Python est "
y = "génial"
print(x, y)
 
 
print("-----")
z =  x + y
print(z)
 
 
----


x = "Salut"   # variable globale --> elle n'est pas dans un bloc
 
def maFonction():	# définition de la fonction maFonction()
	x = 5   # variable locale à la fonction (maFonction())
	print("Bonjour")
	print("Bonjour")
	print("Bonjour")
	print(x)
 
 
maFonction()	# utilisation de la fonction
 
print(x)
 
 
----


cars = ["Ford", "Volvo", "BMW"]
print(cars)
 
print(cars[0])
print(cars[1])
 
cars[0] = "Toyota"
print(cars)
 
print(len(cars))
 
print("------")
 
nbElement = 0
for x in cars:
	print(x)
	#nbElement = nbElement + 1
print("Le nombre d'élément est", nbElement)
 
print("------")
 
cars = ["Ford", "Volvo", "BMW"]
for x in cars:
	print(x)
 
print(type(cars))
# print(dir(cars))
 
cars.sort()
print(cars)
 
cars.remove("Volvo")
print(cars)
 
cars.remove(cars[1])
print(cars)
 
 
-----

def listerNombre(max):
	i = 1

	while i < max:
		print(i)
		i += 1

listerNombre(10)
 
 
-----

cars = ["toyota", "volvo", "truc", "t1", "t1", 133]

# parcours de tous les éléments de cars avec la boucle générique "for" 
for y in cars:
  print(y)
 
print("----")

# "l'équivalent" de la boucle MAIS pour 3 éléments seulement !
print(cars[0])
print(cars[1])
print(cars[2])
 
print("----")

# la même boucle mais "écrite à la main"
y = 0	# initialisation de la variable de boucle
while y < len(cars):	# boucle "tant que" avec la condition sur le nombre d'éléments de la table cars
	print(cars[y])	# instruction du bloc
	y = y + 1	# incrément de la variable de boucle -> doit être une instruction du bloc ! sinon elle ne serait pas exécuté par la boucle qui tournerait alors à l'infini

 
-----


a = 3 < 4
a = True

estFemme = False ou True

a = c < d

---------------------------------------

if 3 < 4 :
	print("ok")
else:
	print("faux")
	
---------------------------------------

if False :
  if True :
    print("ok")
  else:
    print("KO")
  print("Enchantée")
else:
  print("Enchanté")

---------------------------------------

if estUneFemme(p1) :
  print("Enchantée")
else:
  print("Enchanté")

---------------------------------------

if p1.estUneFemme() :
  print("Enchantée")
else:
  print("Enchanté")

---------------------------------------

estFemme = False
if estFemme :
  print("Enchantée")
else:
  print("Enchanté")


---------------------------------------

#Spécification : avec la définition des variables ci-dessous
p1 = ...
p2 = ..
...
pn = ...

#Si je vous donne une valeur entière i (par exemple 7)
#--> afficher à l'écran pi donc p7

if i == 1 :
  print(p1)
else if i == 2 :
  print(p2)
else if i == 3 :
  print(p3)
etc. jusqu'à
else if i == n :
  print(pn)

--------
#exemple complet avec n = 3 et i quelconque
p1 = 2
p2 = -7
p3 = 8
n = 3

i = 1
if i == 1 :
  print(p1)
else if i == 2 :
  print(p2)
else if i == 3 :
  print(p3)

---------------------------------------

# les trois types de valeurs que nous avons vu
valeur_numerique = 7	# nombre
valeur_booleenne = False	# valeur booléenne, la deuxième étant True
chaine_de_caractères = "blabla"	# une chaîne de caractères

---------------------------------------

t = [1, 2, 4, 6, 7]
# t est une table de 5 élément dont les éléments sont 1, 2, 4, 6 et 7

---------------------------------------

# spécification : vous disposez d'un tableau nom en entrée et d'une variable numérique i
nom = ["Marc", "Karwan", "Inrig", "Djafar"]
i = 3

# afficher à l'écran la valeur de la ième valeur du tableau nom
print(nom[i])

# afficher tous les éléments de nom
for e in nom :
  print(e)

# afficher p telle qu'elle est --> en python, on y voit sa structure syntaxique
print(nom)

# afficher tous les éléments de nom mais en accédant aux valeurs grâce à un index
i = 0
while i < 4 :
  print(nom[i])

# la boucle while ci-dessus est équivalente aux 4 lignes ci-dessous :
print(nom[0])
print(nom[1])
print(nom[2])
print(nom[3])

# afficher les éléments à l'envers
i = 3
while 0 <= i :
  print(nom[i])
  i = i + 1

---------------------------------------

v = "N'importe quoi"	# v <--- c'est une variable
# c'est aussi un objet

print(type(v))
print(dir(v))

# v est un objet donc je peux utiliser une fonction de "var" --> de la classe de var
r = v.swapcase()
print(r)

---------------------------------------

# calcul du pgcd selon l'algorithme d'Euclide proposé par Karwan
# https://en.wikipedia.org/wiki/Algorithm
# retranscription de l'organigramme en code python
a = A = int(input("Entrez un nombre> "))
b = B = int(input("Entrez un nombre> "))
while b != 0 :
  if a > b :
    a = a - b
  else:
    b = b - a
print("Le pgcd de ", A, "et", B, "est", a)

---------------------------------------

pour chaque u de usagerQuiDoitEnvoyerUnMessage faire
	pour chaque d de usagers faire
		envoyerMessage(u, d)


usagers = ["Sadia", "Martin",...]
usagerQuiDoitEnvoyerUnMessage = [...]

for u in usagerQuiDoitEnvoyerUnMessage:
  for d in usagers:
    if u != d:
      envoyerMessage(u, d)


pour toutes les personnes u qui veulent envoyer un message faire
  envoyer un message à tout le monde

fonction "envoyer un message à tout le monde"
  envoyer un message à tout le monde sauf moi

fonction ... sauf moi
  Si le destinataire n'est pas moi alors
    envoyer un message de u à d

	
-----------
