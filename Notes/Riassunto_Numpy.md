# **Riepilogo Funzioni Fondamentali di NumPy**

Questa scheda riassume le funzioni, gli attributi e le tecniche più comuni e importanti della libreria NumPy, raggruppate per categoria.

### **1. Creazione di Array**

| Funzione | Spiegazione Breve |
| :---- | :---- |
| np.array(lista) | Crea un array NumPy partendo da una lista o una sequenza Python. |
| np.zeros((righe, col)) | Crea un array di dimensioni date, riempito di zeri (0.). |
| np.ones((righe, col)) | Crea un array di dimensioni date, riempito di uni (1.). |
| np.full((righe, col), val) | Crea un array di dimensioni date, riempito con il valore specifico val. |
| np.arange(start, stop, step) | Crea un array con una sequenza di numeri (simile a range di Python). |
| np.linspace(start, stop, num) | Crea un array con num punti equidistanti tra start e stop. |
| np.random.randint(min, max, size) | Crea un array di dimensioni size con interi casuali tra min (incluso) e max (escluso). |
| np.eye(N) | Crea una matrice identità N x N (1 sulla diagonale principale, 0 altrove). |

### **2. Attributi degli Array (per ispezionare)**

| Attributo | Spiegazione Breve |
| :---- | :---- |
| array.shape | Restituisce una tupla con le dimensioni dell'array (es. (3, 4)). |
| array.ndim | Restituisce il numero di dimensioni dell'array (es. 2 per una matrice). |
| array.size | Restituisce il numero totale di elementi nell'array. |
| array.dtype | Restituisce il tipo di dato degli elementi (es. int64, float64). |
| array.T | (Attributo) Traspone l'array (inverte righe e colonne). |

### **3. Indicizzazione e Slicing (per accedere ai dati)**

| Sintassi | Spiegazione Breve |
| :---- | :---- |
| array[i, j] | Accede al singolo elemento alla riga i, colonna j. |
| array[r_start:r_stop, c_start:c_stop] | **Slicing**: Estrae un blocco rettangolare. |
| array[:, j] | Estrae un'intera colonna (con indice j). |
| array[i, :] o array[i] | Estrae un'intera riga (con indice i). |
| array[[i, j], [k, l]] | **Fancy Indexing**: Seleziona elementi specifici, accoppiando coordinate. |
| array[maschera_booleana] | **Maschera Booleana**: Seleziona o modifica elementi basati su una condizione True/False. |

### **4. Calcoli (Ufuncs e Aggregazioni)**

| Funzione/Metodo | Spiegazione Breve |
| :---- | :---- |
| +, -, *, /, ** | **Ufuncs**: Operatori aritmetici che funzionano elemento per elemento. |
| np.sin(), np.cos(), np.log() | **Ufuncs**: Funzioni matematiche che si applicano a ogni elemento. |
| array.sum(), array.mean() | **Aggregazione**: Calcola la somma o la media di tutti gli elementi. |
| array.min(), array.max() | **Aggregazione**: Trova il valore minimo o massimo di tutti gli elementi. |
| array.sum(axis=0) | Esegue l'aggregazione lungo le **colonne** (verticalmente). |
| array.sum(axis=1) | Esegue l'aggregazione lungo le **righe** (orizzontalmente). |
| np.argmin(), np.argmax() | Restituisce l'**indice** (la posizione) del valore minimo o massimo. |

### **5. Manipolazione della Forma e Combinazione**

| Funzione/Metodo | Spiegazione Breve |
| :---- | :---- |
| array.reshape((r, c)) | Cambia la forma di un array senza cambiarne i dati (spesso crea una vista). |
| array.flatten() | Converte un array multidimensionale in un array 1D (crea sempre una **copia**). |
| array.ravel() | Converte un array multidimensionale in un array 1D (crea una **vista**, se possibile). |
| array[:, np.newaxis] | Aggiunge una nuova dimensione, trasformando un vettore riga in colonna e viceversa. Utile per il broadcasting. |
| np.vstack((a1, a2)) | Impila array verticalmente (uno sopra l'altro). |
| np.hstack((a1, a2)) | Impila array orizzontalmente (uno a fianco all'altro). |
| np.split(array, N_o_indici) | Divide un array in più sotto-array. |
| array.copy() | Crea una **copia** indipendente dell'array, non una *vista*. |

### **6. Algebra Lineare**

| Funzione | Spiegazione Breve |
| :---- | :---- |
| np.dot(a, b) | Prodotto matriciale tra due array (o prodotto scalare per vettori). |
| np.matmul(a, b) o a @ b | Prodotto matriciale (più moderno e chiaro di np.dot per matrici). |
| np.linalg.inv(matrix) | Calcola l'inversa di una matrice quadrata. |
| np.linalg.det(matrix) | Calcola il determinante di una matrice quadrata. |
| np.linalg.eig(matrix) | Calcola autovalori e autovettori di una matrice. |
| np.linalg.norm(array) | Calcola la norma (lunghezza) di un vettore o matrice. |
| np.transpose(array) | Traspone un array (alternativa a array.T). |

### **7. Confronti e Operazioni Logiche**

| Funzione/Operatore | Spiegazione Breve |
| :---- | :---- |
| ==, !=, <, >, <=, >= | Operatori di confronto elemento per elemento, restituiscono array booleani. |
| np.where(condizione, val_vero, val_falso) | Condizionale elemento per elemento: restituisce val_vero dove la condizione è True, val_falso altrove. |
| np.all(array) | Restituisce True se **tutti** gli elementi sono True (non zero). |
| np.any(array) | Restituisce True se **almeno un** elemento è True (non zero). |
| np.logical_and(a, b) | AND logico elemento per elemento tra due array booleani. |
| np.logical_or(a, b) | OR logico elemento per elemento tra due array booleani. |
| np.logical_not(array) | NOT logico elemento per elemento. |

### **8. Ordinamento e Ricerca**

| Funzione | Spiegazione Breve |
| :---- | :---- |
| np.sort(array) | Restituisce una **copia** ordinata dell'array. |
| array.sort() | Ordina l'array **in-place** (modifica l'originale). |
| np.argsort(array) | Restituisce gli **indici** che ordinerebbero l'array. |
| np.unique(array) | Restituisce i valori unici dell'array, ordinati. |
| np.searchsorted(array, valore) | Trova la posizione dove inserire 'valore' per mantenere l'ordinamento. |
| np.in1d(array1, array2) | Restituisce un array booleano che indica quali elementi di array1 sono presenti in array2. |

### **9. Tipi di Dato e Conversioni**

| Funzione/Metodo | Spiegazione Breve |
| :---- | :---- |
| array.astype(nuovo_tipo) | Converte l'array a un nuovo tipo di dato (es. float64, int32). |
| np.int32, np.int64 | Tipi di dato interi a 32 e 64 bit. |
| np.float32, np.float64 | Tipi di dato float a 32 e 64 bit (float64 è il default). |
| np.bool_ | Tipo di dato booleano NumPy. |
| np.isnan(array) | Restituisce un array booleano che indica dove ci sono valori NaN (Not a Number). |
| np.isinf(array) | Restituisce un array booleano che indica dove ci sono valori infiniti. |

### **10. Broadcasting**

Il **broadcasting** è una delle caratteristiche più potenti di NumPy: permette di eseguire operazioni tra array di forme diverse senza dover esplicitamente ridimensionarli.

| Concetto | Spiegazione |
| :---- | :---- |
| **Regola Broadcasting** | NumPy confronta le dimensioni partendo dalla fine: se sono uguali o una è 1, l'operazione è possibile. |
| **Esempio Pratico** | `array_2d + array_1d` funziona se l'array 1D ha la stessa lunghezza dell'ultima dimensione del 2D. |
| **Vantaggi** | Più efficiente e leggibile rispetto a loop espliciti per operazioni elemento per elemento. |

**Esempi di Broadcasting:**
```python
# Matrice 3x3 + vettore di lunghezza 3
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
vector = np.array([10, 20, 30])
result = matrix + vector  # Aggiunge il vettore a ogni riga della matrice

# Scalare + array (il caso più semplice)
array + 5  # Aggiunge 5 a ogni elemento
```