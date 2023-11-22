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

Comment vous semble évoluer la courbe ? Observez bien les différentes courbes du graphique ci-dessous. Quelle est la plus ressemblante à notre situation ? *Écrivez votre réponse ici*

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
Selon moi le tri par selection va regarder toute la liste,
il va selectionner l'element le plus petit et le placer au début de la liste.
Ensuite, il recommence avec le reste de la liste tant qu'elle n'est pas vide.

Puis implémentez l'algorithme en python dans la fonction `sort` du fichier `sort/selection.py`. Vérifiez son bon fonctionnement en éxécutant le fichier `python3 -m unittest`. Le test correspondant au tri par sélection doit passer.

Mesurez le temps d'éxécution pour un tableau de :

- 1000 entrées
- 2000 entrées
- ...
- 10000 entrées

Tracez le graphique correspondant.

Quelle semble être la complexité de notre fonction de tri ? Cela est-il logique par rapport au code que vous avez implémenté ?
Le tri par selection est de complexité O(N**2)
Car entre la première et la dernière valeur les entrées sont multiplé par 10
alors que les temps sont multipliés par 100.
De plus on a directement une double boucle dans le programme
qui regarde tout les éléments, ce qui fait N*N donc N**2

### 2. Tri par insertion

Observez attentivement l'animation de tri par insertion ci-dessous pour en comprendre le fonctionnement.

<img src="img/insertion.gif">

Écrivez en français classique ce que vous voyez. Quel est le fonctionnement ? Comment l'expliqueriez-vous à quelqu'un ? 
Selon moi, Le tri par insertion va regarder le deuxieme element de la liste
et le placer avant ou après le premier si il est plus petit ou non. Puis faire
pareil avec les autres éléments en les comparant avec tous ceux avant

Puis implémentez l'algorithme en python dans la fonction `sort` du fichier `sort/insertion.py`. Utilisez les tests automatiques pour vérifier votre implémentation.

Mesurez le temps d'éxécution pour un tableau de :

- 1000 entrées
- 2000 entrées
- ...
- 10000 entrées

Tracez le graphique correspondant.

Quelle semble être la complexité de notre fonction de tri ? Cela est-il logique par rapport au code que vous avez implémenté ?
Le tri par insertion est de complexité O(N**2)
Car entre la première et la dernière valeur les entrées sont multiplé par 10
alors que les temps sont multipliés par 100.
De plus on a directement une double boucle dans le programme
qui regarde tout les éléments, ce qui fait N*N donc N**2

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
Le tri fusion prend un tableau.
Si le tableau n'est pas vide ou n'est pas composé d'un seul élément,
Python vas le divisé en deux en rappelant la meme fonction puis le merger.
A chaque fois avant de merger les différents tableaux vont se réduire,
jusqu'à ce que chaque tableau n'ait qu'un élément.
Ensuite les tableaux vont se merger petit à petit en restant croissant et
en formant au final un seul tableau

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

Quelle semble être la complexité de notre fonction de tri ? Cela est-il logique par rapport au code que vous avez implémenté ? 
Le tri fusion a l'air d'etre de complexité N*log(N)
car on subdivise le tri en plusieurs tri de 1 élément.
Puis on les recombine ensemble en les lisant.
Le nombre d'étape ou on lit chaque valeur est 
a chaque fois que l'on merge des élements (2**(k))>=n>(2**(k-1))+1.
Il a donc k étapes ou on lit tout n. k est plus petit que N
car on prend le k supérieur ou égal à N

Question bonus : Y a-t-il des tailles de tableaux pour lesquelles le tri par fusion n'est pas aussi rapide que les précédents tris abordés ? 
Si on considère que le tri par fusion a une complexité inférieur aux autres tri
alors plus le nombre de valeur va augmenté
plus l'écart entre les différentes complexités va augmenté également.
Le tri sera toujours plus rapide qu'un tri avec une complexité supérieur

### 4. sort()

Bien que tout cela soit fascinant, Python possède sa propre méthode de tri : `sort()`.

Une dernière fois, analysez le temps d'exécution et découvrez si python fait mieux que nos implémentations rudimentaires ;)

## Pour rendre ce TP

Merci de faire une Pull Request vers ce repository.

Le nom de la PR doit contenir votre nom.

Vérifiez que votre code est conforme aux normes pep8 et aux autres critères de qualité dont nous avons parlé.

La PR doit également contenir un ou plusieurs graphiques présentant vos résultats sur la complexité des fonctions de tri.
