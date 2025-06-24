# Riepilogo di Sintassi Matplotlib (Cheat Sheet)

Questa è una guida di riferimento rapido per creare i tipi di grafici più comuni con Matplotlib, usando l'interfaccia a oggetti (`ax`).

---

### Personalizzazioni Comuni (per quasi tutti i grafici)

Queste funzioni si usano sull'oggetto `ax` per personalizzare l'aspetto generale del grafico, indipendentemente dal tipo.

- `ax.set_title('Mio Titolo')`: Imposta il titolo del grafico.
- `ax.set_xlabel('Etichetta X')`: Imposta l'etichetta per l'asse orizzontale.
- `ax.set_ylabel('Etichetta Y')`: Imposta l'etichetta per l'asse verticale.
- `ax.set_xlim(min, max)`: Imposta i limiti (l'intervallo visibile) dell'asse X.
- `ax.set_ylim(min, max)`: Imposta i limiti dell'asse Y.
- `ax.legend()`: Mostra la legenda (funziona se hai specificato l'argomento `label` nel tuo comando di plotting).
- `ax.grid(True)`: Mostra una griglia di sfondo.

---

### 1. Grafico a Linee (`ax.plot`)

Usato per visualizzare l'andamento di una o più variabili nel tempo o rispetto a un'altra variabile continua.

**Sintassi di Base:**
`ax.plot(x, y)`

| Parametro | Spiegazione |
| :--- | :--- |
| **`x`, `y`** | Liste o array NumPy con le coordinate dei punti da disegnare. |
| **`color`** | Stringa che definisce il colore della linea (es. `'blue'`, `'#FF5733'`, `'g'`). |
| **`linestyle`** | Stringa che definisce lo stile della linea (es. `'-'` per solida, `'--'` per tratteggiata, `':'` per puntinata). |
| **`linewidth`** | Numero che definisce lo spessore della linea. |
| **`marker`** | Stringa che definisce il simbolo da usare per ogni punto (es. `'o'` per cerchi, `'s'` per quadrati, `'x'`). |
| **`label`** | Stringa usata come nome della linea nella legenda. |

**Template di Codice:**
```python
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
x_dati = np.linspace(0, 10, 50)
y_dati = np.sin(x_dati)
ax.plot(x_dati, y_dati, color='red', linestyle='--', marker='o', label='Seno')
ax.set_title('Grafico a Linee Esempio')
ax.set_xlabel('Asse X')
ax.set_ylabel('Asse Y')
ax.legend()
plt.show()
```

### 2. Grafico a Dispersione (`ax.scatter`)

Usato per mostrare la relazione tra due variabili numeriche. Ogni punto è rappresentato individualmente.

**Sintassi di Base:**
`ax.scatter(x, y)`

| Parametro    | Spiegazione                                                                                                                        |
|:-------------|:-----------------------------------------------------------------------------------------------------------------------------------|
| **`x`, `y`** | Liste o array NumPy con le coordinate dei punti da disegnare.                                                                      |
| **`s`**      | Dimensione dei punti. Può essere un singolo numero (tutti i punti uguali) o un array per dare a ogni punto una dimensione diversa. |
| **`c`**      | Colore dei punti. Può essere un singolo colore o un array di valori numerici che verranno mappati su una scala di colori.          |
| **`cmap`**   | Stringa che definisce la mappa di colori da usare quando c è un array di numeri (es. 'viridis', 'coolwarm')                        |
| **`alpha`**  | Numero tra 0 e 1 che definisce la trasparenza dei punti. Utile per vedere le sovrapposizioni.                                      |
| **`marker`** | Stringa che definisce il simbolo da usare per ogni punto (es. `'o'` per cerchi, `'s'` per quadrati, `'x'`).                        |
| **`label`**  | Stringa usata come nome della linea nella legenda.                                                                                 |

**Template di Codice:**
```python
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
x_dati = np.random.rand(50)
y_dati = np.random.rand(50)
dimensioni = 1000 * np.random.rand(50)
colori = np.random.rand(50)

scatter_plot = ax.scatter(x_dati, y_dati, s=dimensioni, c=colori, cmap='viridis', alpha=0.7)

ax.set_title('Scatter Plot Esempio')
ax.set_xlabel('Variabile 1')
ax.set_ylabel('Variabile 2')

fig.colorbar(scatter_plot, label='Valore Colore') # Aggiunge la barra dei colori
plt.show()
```
### 3. Grafico a Barre (`ax.bar` e `ax.barh`)

Usato per confrontare valori numerici tra diverse categorie.

**Sintassi di Base:**
`ax.bar(x, height) (Verticale)`
`ax.barh(y, width) (Orizzontale)`

| Parametro              | Spiegazione                                                                                                                    |
|:-----------------------|:-------------------------------------------------------------------------------------------------------------------------------|
| **`x`/ `y`**           | Lista di stringhe o numeri per le etichette delle categorie.                                                                   |
| **`height / width`**   | Lista di valori numerici che definisce l'altezza/lunghezza di ogni barra.                                                      |
| **`color`**            | Colore delle barre.                                                                                                            |
| **`edgecolor`**        | Colore del bordo delle barre.                                                                                                  |
| **`width / height`**   | Numero che definisce lo spessore/altezza di ogni barra (default 0.8).                                                          |
| **`label`**            | Etichetta per la legenda.                                                                                                      |

**Template di Codice:**
```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
categorie = ['Gruppo A', 'Gruppo B', 'Gruppo C']
valori = [10, 25, 18]

ax.bar(categorie, valori, color='coral', edgecolor='black', label='Dati Esempio')

ax.set_title('Grafico a Barre Esempio')
ax.set_ylabel('Valori')
ax.legend()
plt.show()
```
### 4. Istogramma(`ax.hist`)

Usato per visualizzare la distribuzione di una singola variabile numerica.

**Sintassi di Base:**
`ax.hist(data)`

| Parametro      | Spiegazione                                                                                                |
|:---------------|:-----------------------------------------------------------------------------------------------------------|
| **`Data`**     | Lista o array NumPy di numeri da analizzare.                                                               |
| **`bins`**     | Numero intero di "contenitori" in cui dividere i dati.                                  |
| **`density`**  | Booleano. Se True, normalizza l'istogramma per rappresentare una densità di probabilità (area totale = 1). |                                                    |
| **`color`**    | Colore delle barre.                                                                                        |
| **`alpha`**    | Trasparenza, utile per sovrapporre più istogrammi.                                                         |
| **`histtype`** | Stile dell'istogramma (es. 'bar', 'step', 'stepfilled').                                                   |
| **`label`**    | Etichetta per la legenda.                                                                                  |
**Template di Codice:**
```python
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
dati = np.random.randn(1000)

ax.hist(dati, bins=30, density=True, color='skyblue', alpha=0.8, label='Distribuzione Dati')

ax.set_title('Istogramma Esempio')
ax.legend()
plt.show()
```
### 5. Box Plot(`ax.boxplot`)

Usato per mostrare la distribuzione di una o più variabili attraverso i loro quartili.

**Sintassi di Base:**
`ax.boxplot(data)`

| Parametro          | Spiegazione                                                                              |
|:-------------------|:-----------------------------------------------------------------------------------------|
| **`Data`**         | Un array per un singolo box plot, o una lista di array per confrontare più gruppi.       |
| **`labels`**       | Lista di stringhe da usare come etichette per ogni box plot sull'asse X.                 |
| **`vert`**         | Booleano. Se False, crea box plot orizzontali                                            |                                                    |
| **`patch_artist`** | Booleano. Se True, riempie la "scatola" con un colore, permettendoti di personalizzarla. |

**Template di Codice:**
```python
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
dati_A = np.random.normal(0, 1, 100)
dati_B = np.random.normal(1, 2, 100)

ax.boxplot([dati_A, dati_B], labels=['Gruppo A', 'Gruppo B'], patch_artist=True)

ax.set_title('Box Plot Esempio')
plt.show()
```
### 6. Grafico a Contorni (`ax.contourf`)

Usato per mostrare la distribuzione di una o più variabili attraverso i loro quartili.

**Sintassi di Base:**
`ax.contourf(X, Y, Z)`

| Parametro    | Spiegazione                                                         |
|:-------------|:--------------------------------------------------------------------|
| **`X,Y`**    | Griglie di coordinate 2D, create tipicamente con np.meshgrid.       |
| **`Z`**      | Griglia 2D con i valori ("altezza") per ogni punto (X, Y).          |
| **`levels`** | Numero intero che definisce quanti livelli di colore disegnare.     |                                                    |
| **`cmap`**   | Stringa che definisce la mappa di colori da usare (es. 'viridis').  |

**Template di Codice:**
```python
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)
Z = np.sin(X) ** 2 + np.cos(Y) ** 2

mappa_colori = ax.contourf(X, Y, Z, levels=15, cmap='viridis')

ax.set_title('Grafico a Contorni Esempio')
fig.colorbar(mappa_colori, label='Valore Z')
plt.show()
```

### 7. Heatmap(`sns.heatmap(data)`)

Ideale per visualizzare una matrice di dati, come una matrice di correlazione, usando il colore.

**Sintassi di Base:**
`sns.heatmap(data)`

| Parametro    | Spiegazione                                                         |
|:-------------|:--------------------------------------------------------------------|
| **`data`**    | Un array 2D o un DataFrame di Pandas da visualizzare.       |
| **`annot`**      | Booleano. Se True, scrive il valore numerico in ogni cella.         |
| **`fmt`** | Stringa di formattazione per i numeri quando annot=True (es. '.2f' per due decimali).     |                                                    |
| **`cmap`**   | SMappa di colori. Per le correlazioni, 'coolwarm' o 'RdBu_r' sono ottime scelte.  |
| **`ax`**   | L'asse Matplotlib su cui disegnare il grafico.  |
**Template di Codice:**
```python
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

# Dati di esempio
dati_matrice = pd.DataFrame(np.random.rand(5, 5), columns=['A', 'B', 'C', 'D', 'E'])
matrice_corr = dati_matrice.corr()

fig, ax = plt.subplots()
sns.heatmap(matrice_corr, annot=True, cmap='coolwarm', fmt='.2f', ax=ax)
ax.set_title('Heatmap Esempio')
plt.show()
```
### 8. Grafico con Barre di Errore (`ax.errorbar`)

Fondamentale in ambito scientifico per visualizzare un valore e la sua incertezza o errore di misura.

**Sintassi di Base:**
`ax.errorbar(x, y, yerr=errore_y)`

| Parametro | Spiegazione |
| :--- | :--- |
| **`x`, `y`** | Liste o array NumPy con le coordinate dei punti dati. |
| **`yerr`** | L'errore/incertezza per l'asse Y. Può essere un singolo valore (uguale per tutti i punti) o un array con un errore specifico per ogni punto. |
| **`xerr`** | Simile a `yerr`, ma per le barre di errore orizzontali. |
| **`fmt`** | Una stringa di formattazione che controlla l'aspetto dei punti e delle linee. Ad esempio, `'o'` disegna solo i punti, `'-'` solo la linea, `'o-'` entrambi. |
| **`ecolor`** | Imposta il colore delle linee della barra di errore. È buona pratica renderle di un colore più tenue. |
| **`elinewidth`** | Numero che definisce lo spessore delle linee della barra di errore. |
| **`capsize`** | Numero che definisce la lunghezza dei "tappi" alle estremità delle barre di errore, per una migliore leggibilità. |
| **`label`** | Stringa usata nella legenda. |

**Template di Codice:**
```python
import matplotlib.pyplot as plt
import numpy as np

# Dati di esempio con rumore
rng = np.random.RandomState(42)
x = np.linspace(0, 10, 30)
y = np.sin(x) + rng.randn(30) * 0.5
errore_y = 0.5  # Incertezza costante per tutti i punti

fig, ax = plt.subplots(figsize=(10, 6))

ax.errorbar(
    x, y, 
    yerr=errore_y, 
    fmt='o',  # 'o' per scatter plot
    color='black',
    ecolor='lightgray',
    elinewidth=3,
    capsize=5,
    label='Dati Sperimentali'
)

ax.set_title('Grafico con Barre di Errore', fontsize=16)
ax.set_xlabel('Misura', fontsize=12)
ax.set_ylabel('Valore ± Incertezza', fontsize=12)
ax.legend()
plt.show()
```
### 9. Istogramma 2D (`ax.hist2d`)

Un istogramma a due dimensioni è usato per visualizzare la densità congiunta di due variabili numeriche. [cite_start]Il grafico viene diviso in una griglia di rettangoli, e il colore di ogni rettangolo indica quanti punti dati cadono al suo interno. 

**Sintassi di Base:**
`ax.hist2d(x, y)`

| Parametro | Spiegazione |
| :--- | :--- |
| **`x`, `y`** | Liste o array NumPy 1D con le coordinate dei punti da analizzare. Devono avere la stessa lunghezza. |
| **`bins`** | Numero di "contenitori" (rettangoli) da usare lungo ogni asse. [cite_start]Può essere un singolo numero (es. `30`) per avere lo stesso numero di bins su entrambi gli assi, o una lista `[bins_x, bins_y]` per specificarli separatamente.  |
| **`cmap`** | [cite_start]Stringa che definisce la mappa di colori da usare per rappresentare la densità (es. `'viridis'`, `'Blues'`, `'Reds'`).  |
| **`cmin`** | Numero. I rettangoli con un conteggio di punti inferiore a questo valore non verranno colorati. È utile per nascondere il rumore di fondo e concentrarsi sulle aree a maggiore densità. |
| **`cmax`** | Numero. Imposta il valore massimo per la scala di colori. |

**Template di Codice:**
```python
import matplotlib.pyplot as plt
import numpy as np

# 1. Genera dati di esempio con una certa correlazione
rng = np.random.RandomState(0)
mean = [0, 0]
cov = [[1, 1], [1, 2]]
x, y = rng.multivariate_normal(mean, cov, 10000).T

# 2. Crea la figura e gli assi
fig, ax = plt.subplots(figsize=(8, 6))

# 3. Disegna l'istogramma 2D
#    hist2d restituisce una tupla; il quarto elemento è l'immagine mappabile per la colorbar
mappa_colori = ax.hist2d(x, y, bins=30, cmap='viridis', cmin=1)

# 4. Aggiungi una colorbar per interpretare i colori
fig.colorbar(mappa_colori[3], ax=ax, label='Conteggio Punti nel Bin')

# 5. Aggiungi titoli e etichette
ax.set_title('Istogramma 2D della Densità dei Dati', fontsize=16)
ax.set_xlabel('Variabile X', fontsize=12)
ax.set_ylabel('Variabile Y', fontsize=12)

plt.show()
```
### 10. Binning Esagonale (`ax.hexbin`)

Simile a `hist2d`, il binning esagonale è un'alternativa per visualizzare la densità congiunta di due variabili numeriche. [cite_start]Invece di usare una griglia di quadrati, divide il piano in una griglia di **esagoni regolari**.  Spesso il risultato è esteticamente più gradevole perché la forma dell'esagono approssima meglio un cerchio rispetto a un quadrato.

**Sintassi di Base:**
`ax.hexbin(x, y)`

| Parametro | Spiegazione |
| :--- | :--- |
| **`x`, `y`** | Liste o array NumPy 1D con le coordinate dei punti da analizzare. Devono avere la stessa lunghezza. |
| **`gridsize`** | [cite_start]Numero che definisce quanti esagoni creare lungo la direzione orizzontale.  È l'analogo di `bins` in `hist2d`. Può essere un singolo numero (es. `30`) o una tupla `(nx, ny)`. |
| **`cmap`** | [cite_start]Stringa che definisce la mappa di colori da usare per rappresentare la densità (es. `'viridis'`, `'inferno'`).  |
| **`C`** | Un array 1D opzionale di valori. Se fornito, il colore di ogni esagono non rappresenterà più il conteggio dei punti, ma il risultato di una funzione di aggregazione applicata a questi valori. |
| **`reduce_C_function`** | La funzione da applicare ai valori `C` che cadono in ogni esagono. [cite_start]Le opzioni più comuni sono `np.mean` (default), `np.sum`, `np.max`.  |

**Template di Codice:**
```python
import matplotlib.pyplot as plt
import numpy as np

# 1. Genera dati di esempio con una certa correlazione
rng = np.random.RandomState(0)
mean = [0, 0]
cov = [[1, 1], [1, 2]]
x, y = rng.multivariate_normal(mean, cov, 10000).T

# 2. Crea la figura e gli assi
fig, ax = plt.subplots(figsize=(8, 6))

# 3. Disegna il grafico a binning esagonale
mappa_colori = ax.hexbin(x, y, gridsize=30, cmap='inferno')

# 4. Aggiungi una colorbar per interpretare i colori
fig.colorbar(mappa_colori, ax=ax, label='Conteggio Punti nel Bin')

# 5. Aggiungi titoli e etichette
ax.set_title('Binning Esagonale della Densità dei Dati', fontsize=16)
ax.set_xlabel('Variabile X', fontsize=12)
ax.set_ylabel('Variabile Y', fontsize=12)

plt.show()
```