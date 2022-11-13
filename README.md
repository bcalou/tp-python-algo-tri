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

Sur un tableur, générez un tableau permettant de visualiser le temps d'exécution en fonction de la taille de l'entrée.

Comment vous semble évoluer la courbe ? Observez bien les différentes courbes du graphique ci-dessous. Quelle est la plus ressemblante à notre situation ? 

_Le tableau semble évoluer avec une complexité O(n) soit linéairement._

<img title="" src="img/o.webp" alt="" width="" data-align="center">

#### Quelques exemples de complexités courante :

- Un algorithme de complexité O(1) a un temps d'éxécution qui ne dépend pas de la taille de l'entrée. C'est très efficace.
- Un algorithme de complexité O(n) a un temps d'éxécution qui est proportionnel à la taille du problème à résoudre. Autrement dit, multiplier la taille de l'entrée par 10 multipliera le temps d'éxécution par 10. C'est une croissance linéaire. C'est plutôt efficace.
- Un algorithme de complexité O(n²) a un temps d'éxécution qui est proportionnel au carré de la taille du problème à résoudre. Autrement dit, multiplier la taille de l'entrée par 10 multipliera le temps d'éxécution par 100 ! Ce n'est pas terrible du tout...

## Les algorithmes

### 1. Tri par sélection

Observez attentivement l'animation de tri par sélection ci-dessous pour en comprendre le fonctionnement.

<img title="" src="img/selection.gif" alt="" data-align="center">

Écrivez en français classique ce que vous voyez. Quel est le fonctionnement ? Comment l'expliqueriez-vous à quelqu'un ?

_On parcours le tableau en gardant le plus petit élément puis on le déplace au début du tableau, puis on recommence en partant du second élément et on répète l'opération en déplacent le plus petit élément à la cas dont on est parti, on recommence jusqu'à avoir trié tout le tableau_

_On parcours la liste un a un en partant de la première position en notant le nombre le plus petit puis on échange sa position avec l'indexe 0. On répète l'opération en partant de la seconde position en échangeant sa position avec l'indexe 1. On répète l'opération jusqu'à ce que l'on ai trié tout le tableau._

Puis implémentez l'algorithme en python dans la fonction `sort` du fichier `sort/selection.py`. Vérifiez son bon fonctionnement en éxécutant le fichier `test.py`.

Mesurez le temps d'éxécution pour un tableau de :

- 1000 entrées
- 2000 entrées
- ...
- 10000 entrées

Tracez le graphique correspondant.

*J'ai tracé tout les graphiques dans un seul graphique (j'ai doublé le nombre d'entrées pour avoir des résultats plus significatifs)*

Quelle semble être la complexité de notre fonction de tri ? Cela est-il logique par rapport au code que vous avez implémenté ? _La complexité semble être O(n²), cela semble logique car le tableau est reparcouru en partie à chaque fois que l'on déplace l'élément le plus petit au début du tableau_

### 2. Tri par insertion

Observez attentivement l'animation de tri par insertion ci-dessous pour en comprendre le fonctionnement.

<img title="" src="img/insertion.gif" alt="" data-align="center">

Écrivez en français classique ce que vous voyez. Quel est le fonctionnement ? Comment l'expliqueriez-vous à quelqu'un ?

_Pour chaque éléments du tableau on vérifie si l'élément précédent est plus petit et si c'est le cas on l'échange et on revérifie jusqu'à ce que son élément précédent ne soit pas plus petit, puis on passe à l'élément suivant en répétant l'opération jusqu'à ce que tout le tableau soit trié_

_Pour chaque cases du tableau on recherche les nombres plus élevé dans les cases précédentes puis on insert la case actuelle devant les dernière case ayant ce nombre_

Puis implémentez l'algorithme en python dans la fonction `sort` du fichier `sort/insertion.py`. Vérifiez son bon fonctionnement en exécutant le fichier `test.py`.

Mesurez le temps d'exécution pour un tableau de :

- 1000 entrées
- 2000 entrées
- ...
- 10000 entrées

Tracez le graphique correspondant.

_J'ai tracé tout les graphiques dans un seul graphique (j'ai doublé le nombre d'entrées pour avoir des résultats plus significatifs)_

Quelle semble être la complexité de notre fonction de tri ? Cela est-il logique par rapport au code que vous avez implémenté ? 

*La complexité de cet algorithme semble être de O(n²) car pour chaque élément on reparcourt le tableau*

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

Vérifiez son bon fonctionnement en exécutant le fichier `test.py`.

#### Implémentation du tri par fusion

Observez bien le schéma suivant : il représente le concept du tri par fusion.

<img title="" src="img/fusion.png" alt="" width="348" data-align="center">

Cet algorithme est de type "diviser pour régner".

Écrivez en français classique ce que vous voyez. Quel est le fonctionnement ? Comment l'expliqueriez-vous à quelqu'un ? 

_L'algorithme a un fonctionnement  en deux parties distinctes : la séparation en deux et le tri, pour la séparation on prend une liste de nombre puis on la sépare en deux, ces deux nouvelles listes subissent la même opération de séparation jusqu'à ce qu'elle ne soient plus divisible, dans ce cas là on les revoie simplement et on les tris en une nouvelle liste qu'on renvoie Ce tris s'effectue de en recherchant le plus petit nombre dans le premier élément de chaque liste et on le "déplace" dans une nouvelle liste triée qu'on renvoie. Petit à petit on trie chaque liste triés de la manière décrie si dessus jusqu'à avoir une seule liste triée_

Complétez la fonction `sort` du fichier `sort/fusion.py` en suivant les instructions suivantes.

Il vous faudra deux fonctions :

- `sort`, la fonction principale, qui sera chargée de diviser les tableaux ayant plus d'un élément, et de rappeler `sort` avec ces nouveaux tableaux
- `merge`, la fonction qui sera appelée pour fusionner deux tableaux

Vérifiez son bon fonctionnement en exécutant le fichier `test.py`.

Mesurez le temps d'exécution pour un tableau de :

- 1000 entrées
- 2000 entrées
- ...
- 10000 entrées

Tracez le graphique correspondant.

*J'ai tracé tout les graphiques dans un seul graphique (j'ai doublé le nombre d'entrées pour avoir des résultats plus significatifs)*

Quelle semble être la complexité de notre fonction de tri ? Cela est-il logique par rapport au code que vous avez implémenté ?

*La complexité de l'algorithme semble être O(log n). Cela semble cohérant avec le fait de séparer le tableau en deux de manière récursive*

Question bonus : Y a-t-il des tailles de tableaux pour lesquelles le tri par fusion n'est pas aussi rapide que les précédents tris abordés ? 

*D'après mes observations les très petit tableau (particulièrement si ils sont multiples de 3) on tendance à être trié plus rapidement par les algorithmes plus simplistes, étant donné la vitesse d'exécution la marge d'erreur des mesure est très élevée donc il s'agit plus d'une intuitions basées sur des données pas forcément fiables.*

### 4. sort()

Bien que tout cela soit fascinant, Python possède sa propre méthode de tri : `sort()`.

Une dernière fois, analysez le temps d'exécution et découvrez si python fait mieux que nos implémentations rudimentaires ;)

# Pour rendre ce TP

Merci de faire une `Pull Request` vers ce repository.

Le nom de la PR doit contenir votre nom et celui de votre collègue si vous êtes en binôme.

Vérifiez que votre code est conforme aux normes pep8 (commande `pycodestyle .` à la racine)et aux autres critères de qualité dont nous avons parlé.

La PR doit également contenir un ou plusieurs graphiques présentant vos résultats sur la complexité des fonctions de tri.

*Les tableaux sont si dessous*

<img src="./Graph comparatif des algorithmes.jpg" title="" alt="" data-align="center">

<img src="./Graph du temps de création d'un tableau aléatoire.jpg" title="" alt="" data-align="center">
