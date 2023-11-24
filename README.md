# TP : Faisons le tri

## Introduction

Le problème du tri est parmi les plus élémentaires en algorithmique, mais ses ramifications peuvent être poussées.

Le but de ce TP est d'implémenter différentes méthodes standard de tri et de comparer leur efficacité.

Nous aborderons par ce TP la notion de complexité algorithmique, c'est à dire l'évaluation de l'efficacité des algorithmes, indispensable pour les comparer entre eux.

### L'input

Nous travaillerons sur un tableau de nombres, par exemple :

```py
array: list[int] = [2, 34, -4, 2, 8, 1]
```

Notez que les entiers pourraient être remplacés par des nombres décimaux, des chaînes de caractère (à trier par ordre alphabétique) ou même des objets complexes (à trier selon une certaine clé de l'objet). Le fonctionnement est le même.

#### Comment générer un tableau de nombres aléatoires ?

Cela peut-être pratique pour générer de grands tableaux.

Voici comment générer un tableau de 10 nombres compris entre 0 et 100 :

```py
import random
array = [random.randint(0, 100) for i in range(10)]
```

#### Comment mesurer le temps écoulé ?

Cela sera indispensable pour évaluer nos algorithmes.

```py
import time
start: float = time.time()
# do something
end: float = time.time()
print("Temps écoulé :", end - start)
```

#### Exercice préliminaire : temps de génération d'un tableau

Complétez la fonction `generate_array_of_number` du fichier `sort/range.py` pour qu'elle génère un tableau de n nombres aléatoires entre 0 et 100.

Mesurez combien de temps prend python à générer un tableau composés de :

- 1 000 000 entrées
- 2 000 000 entrées
- 3 000 000 entrées
- ...
- 10 000 000 entrées

**Astuce** : vous pouvez écrire les nombres avec des underscores pour mieux les lire : `1_000_000`

Sur un tableur, générez un tableau permettant de visualiser le temps d'éxécution en fonction de la taille de l'entrée.

<img src="./img/array_exectime.png">

Comment vous semble évoluer la courbe ? Observez bien les différentes courbes du graphique ci-dessous. Quelle est la plus ressemblante à notre situation ?

<span style="color:lightblue">Après des tests en générant des tableaux de 1M à 10M d'éléments, la croissance du temps de calcul semble évoluer
de manière linéaire (O(n))</span>.

<img src="img/o.webp" width="400">

#### Quelques exemples de complexités courante :

- Un algorithme de complexité O(1) a un temps d'éxécution qui ne dépend pas de la taille de l'entrée. C'est très efficace.
- Un algorithme de complexité O(n) a un temps d'éxécution qui est proportionnel à la taille du problème à résoudre. Autrement dit, multiplier la taille de l'entrée par 10 multipliera le temps d'éxécution par 10. C'est une croissance linéaire. C'est plutôt efficace.
- Un algorithme de complexité O(n²) a un temps d'éxécution qui est proportionnel au carré de la taille du problème à résoudre. Autrement dit, multiplier la taille de l'entrée par 10 multipliera le temps d'éxécution par 100 ! Ce n'est pas terrible du tout...

## Les algorithmes

### 1. Tri par sélection

Observez attentivement l'animation de tri par sélection ci-dessous pour en comprendre le fonctionnement.

<img src="img/selection.gif">

Écrivez en français classique ce que vous voyez. Quel est le fonctionnement ? Comment l'expliqueriez-vous à quelqu'un ?
<br>
<span style="color:lightblue">
L'algorithme semble commencer au début du tableau. A chaque itération, l'algorithme va comparer le nombre actuel au plus petit
trouvé précédemment et ce jusqu'à atteindre la fin du tableau. Lorsque l'algorithme arrive à la fin du tableau, il échange le plus petit nombre trouvé
avec la position du premier nombre considéré comme "non trié". Il incrémente ensuite la position du début des nombres non triés et recommence à partir de la.</span>


Puis implémentez l'algorithme en python dans la fonction `sort` du fichier `sort/selection.py`. Vérifiez son bon fonctionnement en éxécutant le fichier `python3 -m unittest`. Le test correspondant au tri par sélection doit passer.

Mesurez le temps d'éxécution pour un tableau de :

- 1000 entrées
- 2000 entrées
- ...
- 10000 entrées

Tracez le graphique correspondant.

<img src="img/selection_exectime.png">

Quelle semble être la complexité de notre fonction de tri ? Cela est-il logique par rapport au code que vous avez implémenté ?
<br>
<span style="color:lightblue">
La complexité de l'algorithme par sélection semble être de O(N²), cela semble être logique car au mieux le tableau est déjà trié, au pire il faut accéder au tableau n + n-1 + n-2 + ... fois, ce qui est très long.
</span>

### 2. Tri par insertion

Observez attentivement l'animation de tri par insertion ci-dessous pour en comprendre le fonctionnement.

<img src="img/insertion.gif">

Écrivez en français classique ce que vous voyez. Quel est le fonctionnement ? Comment l'expliqueriez-vous à quelqu'un ?
<br>
<span style="color:lightblue">
L'algorithme commence au début du tableau. Pour chaque nombre, il regarde si le nombre derrière lui est supérieur. (Ou ne fait rien pour la première itération). Si le nombre derrière est plus grand, il continue avec le nombre encore derrière jusqu'à ce que le nombre soit inférieur, auquel cas il insère le nombre juste après lui. Il marque ce nombre comme "rangé" et passe au nombre non rangé suivant.
</span>

Puis implémentez l'algorithme en python dans la fonction `sort` du fichier `sort/insertion.py`. Utilisez les tests automatiques pour vérifier votre implémentation.

Mesurez le temps d'éxécution pour un tableau de :

- 1000 entrées
- 2000 entrées
- ...
- 10000 entrées

Tracez le graphique correspondant.

<img src="img/insertion_exectime.png">

Quelle semble être la complexité de notre fonction de tri ? Cela est-il logique par rapport au code que vous avez implémenté ?
<br>
<span style="color:lightblue">
La complexité de l'algorithme par sélection semble être de O(N²), cela semble être logique car au mieux chaque élément est trié et donc il n'y a aucun déplacement, au pire chaque élément inséré est inséré au tout début du tableau, ce qui peut être très long.
</span>

### 3. Tri par fusion

Le tri par fusion est plus complexe : il utilise en effet la récursion, c'est à dire une fonction qui s'appelle elle-même.

Exemple :

```py
def loop_forever():
    loop_forever()
```

L'appel de cette fonction va entraîner une boucle infinie, car il n'y a pas de condition qui stoppe la boucle.

Voici une fonction récursive avec une "condition" pour la récursion.

```py
def increment_until_10(i):
    if i < 10:
        return increment_until_10(i + 1)
    else:
        return i
```

Si on appelle `increment_until_10(1)`, la fonction sera appelée 9 fois supplémentaires pour "compter" jusqu'à 10.

#### Exercice préliminaire : récursion

Complétez la fonction `sort` du fichier `sort/recursion.py` en suivant les instructions suivantes.

Utilisez le concept de la récursion pour calculer la factorielle du nombre passé en paramètre.

Pour rappel, la factorielle de 5 est 5 x 4 x 3 x 2 x 1 = 120.

Utilisez les tests automatiques pour vérifier votre implémentation.

#### Implémentation du tri par fusion

Observez bien le schéma suivant : il représente le concept du tri par fusion.

<img src="img/fusion.png">

Cet algorithme est de type "diviser pour régner".

Écrivez en français classique ce que vous voyez. Quel est le fonctionnement ? Comment l'expliqueriez-vous à quelqu'un ?
<br>
<span style="color:lightblue">
L'algorithme utilise la méthode dite dichotomique (divier pour régner). Il commence par diviser le tableau en deux autant de fois que nécéssaire afin d'arriver à une seule valeur par tableau. L'algorithme fusionne ensuite les deux tableaux en comparant les deux et en insérant les valeurs des deux tableaux en ordre croissant.
</span>

Complétez la fonction `sort` du fichier `sort/fusion.py` en suivant les instructions suivantes.

Il vous faudra deux fonctions :

- `sort`, la fonction principale, qui sera chargée de diviser les tableaux ayant plus d'un élément, et de rappeler `sort` avec ces nouveaux tableaux
- `merge`, la fonction qui sera appelée pour fusionner deux tableaux

Utilisez les tests automatiques pour vérifier votre implémentation.

Mesurez le temps d'éxécution pour un tableau de :

- 1000 entrées
- 2000 entrées
- ...
- 10000 entrées

Tracez le graphique correspondant.

<img src="./img/fusion_exectime.png">

Quelle semble être la complexité de notre fonction de tri ? Cela est-il logique par rapport au code que vous avez implémenté ?
<br>
<span style="color:lightblue">
La complexité (malgré les apparences) est de O(n log n). Cela est logique car contrairement aux algorithmes précédents, il n'y a pas
d'imbrication de boucle.
</span>

Question bonus : Y a-t-il des tailles de tableaux pour lesquelles le tri par fusion n'est pas aussi rapide que les précédents tris abordés ?
<br>
<span style="color:lightblue">
Sachant que la complexité des algorithmes précédents est n² et que la complexité actuelle est de n\*log(n), le tri par fusion sera toujours plus rapide car pour n'importe quelle valeur de n supérieur à 0, n\*log(n) < n².
</span>

### 4. sort()

Bien que tout cela soit fascinant, Python possède sa propre méthode de tri : `sort()`.

Une dernière fois, analysez le temps d'exécution et découvrez si python fait mieux que nos implémentations rudimentaires ;)

<img src="./img/python_exectime.png"/>

<span style="color:lightblue">
Python semble faire mieux que nous, le temps d'exécution comparé au Fusion Sort est plus rapide d'un facteur 100 !
Pour une même taille de tableau, le sort natif de python met 100x moins de temps que notre fusion sort.
<br>
La complexité de l'algorithme implémenté par python semble être 0(n).
</span>

## Pour rendre ce TP

Merci de faire une Pull Request vers ce repository.

Le nom de la PR doit contenir votre nom.

Vérifiez que votre code est conforme aux normes pep8 et aux autres critères de qualité dont nous avons parlé.

La PR doit également contenir un ou plusieurs graphiques présentant vos résultats sur la complexité des fonctions de tri.
