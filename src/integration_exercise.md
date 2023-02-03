(temp file)

Voici pour votre bon plaisir un exercice concret où vous devrez mettre en application les connaissances que vous venez d'acquérir avec Python, Numpy et Matplotlib. Vous devez trouver la durée de chaque poussée lors de la propulsion d'un fauteuil roulant, dont nous avons enregistré le moment de propulsion à l'aide d'une roue instrumentée.

Concrètement, à l'aide de ce fichier CSV :

[data](https://felixchenier.uqam.ca/wp-content/uploads/2021/06/data.csv)[Download](https://felixchenier.uqam.ca/wp-content/uploads/2021/06/data.csv)

qui contient une colonne de temps (s) et une colonne de moments de propulsion (Nm), vous devez générer un code qui calcule deux valeurs : la moyenne et l'écart-type des durées de toutes les poussées.

Pour cet exercice, considérez que la durée d'une poussée est la durée pendant laquelle le moment de propulsion est supérieur à 5 Nm.

a) Pensez à une stratégie pour pouvoir y arriver (quelles étapes devez-vous faire). Ne lisez pas les prochaines lettres, ça vous donnera la réponse !

b) Ouvrez le fichier à l'aide de `np.loadtxt` et affichez-le sur une courbe à l'aide de `plt.plot`. Pour l'utilisation de `np.loadtxt`, ne pas oublier de sauter la première ligne et de spécifier la virgule comme délimiteur de données.

c) Générez la variable `is_pushing`, un numpy array de dimension N qui comporte `True` si on est en train de pousser, et `False` sinon.

d) Générez la variable `is_starting_push`, un numpy array de dimension N-1 qui comporte `True` si au temps donné, on passe d'un recouvrement à une poussée, et `False` sinon.

e) Générez la variable `is_starting_recovery`, un numpy array de dimension N-1 qui comporte `True` si on passe d'une poussée à un recouvrement, et `False` sinon.

f) Générez la variable `push_starts`, un numpy array qui comprend tous les temps de début de poussée.

g) Générez la variable `recovery_start`, un numpy array qui comprend tous les temps de fin de poussée.

h) Générez la variable `push_lengths`, un numpy array qui comprend toutes les durées de poussée.

i) Calculez la moyenne et l'écart-type des durées de poussée.