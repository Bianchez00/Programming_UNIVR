#  Guida a Pandas

*Un riepilogo di Pandas visto a lezione*

## 1. Oggetti Fondamentali: `Series` e `DataFrame`

Tutto in Pandas ruota attorno a due oggetti principali.

- **`pd.Series(data)`**: Pensa a una `Series` come a una singola colonna di una tabella o a un array con etichette (l'indice).
  ```python
  voti = pd.Series({'Matematica': 7, 'Italiano': 8})
  ```

- **`pd.DataFrame(data)`**: È una tabella completa, con righe e colonne etichettate. Puoi vederla come un insieme di `Series` che condividono lo stesso indice.
  ```python
  tabella = pd.DataFrame({'Voti': voti_series, 'Ore': ore_series})
  ```

## 2. Caricare e Ispezionare i Dati

Queste sono le prime operazioni che si fanno sempre su un nuovo dataset.

- **`pd.read_csv('file.csv')`**: Carica dati da un file CSV in un DataFrame.
- **`df.head(n)`**: Mostra le prime `n` righe del DataFrame (di default 5).
- **`df.info()`**: Fornisce un riepilogo tecnico: numero di righe, colonne, tipi di dati e memoria usata.
- **`df.describe()`**: Calcola le statistiche descrittive (media, deviazione standard, min, max, etc.) per le colonne numeriche.
- **`df.dtypes`**: Mostra il tipo di dato di ogni colonna.
- **`df.columns`**: Mostra i nomi delle colonne.
- **`df['colonna'].value_counts()`**: Conta le occorrenze di ogni valore unico in una colonna (una `Series`).

## 3. Pulire e Preparare i Dati

Questa è spesso la fase più importante, dove si "mettono in ordine" i dati.

### Gestire Colonne e Indici

- **`df.rename(columns={'vecchio_nome': 'nuovo_nome'})`**: Rinomina una o più colonne. È il metodo più sicuro.
- **`pd.to_datetime(df['colonna_data'])`**: Converte una colonna di testo in un formato data/ora. Fondamentale per le serie storiche.
- **`df.set_index('colonna_data')`**: Imposta una colonna come indice del DataFrame.

### Gestire i Dati Mancanti (`NaN`)

> **Ricorda:** Il confronto diretto `df['col'] == np.nan` non funziona! `NaN` non è uguale a se stesso.

- **`df['colonna'].isnull()`**: Restituisce una maschera booleana (`True` dove i valori sono `NaN`).
- **`df['colonna'].isnull().sum()`**: Il modo corretto per **contare** i valori mancanti in una colonna.
- **`df.dropna()`**: Restituisce un DataFrame senza le righe che contengono valori `NaN`.
- **`df.fillna(valore)`**: Restituisce un DataFrame dove i `NaN` sono stati sostituiti con `valore`.

### Gestire i Duplicati

- **`df.duplicated(subset=['colonna'])`**: Restituisce una maschera booleana per identificare le righe duplicate basandosi su una o più colonne.
- **`df.drop_duplicates(subset=['colonna'])`**: Rimuove le righe duplicate.

## 4. Selezionare e Filtrare i Dati (Indexing)

Questo è il cuore della manipolazione dei dati.

- **`df['colonna']`**: Seleziona una singola colonna (restituisce una `Series`).
- **`df.loc['etichetta']`**: Seleziona una o più righe in base alla loro **etichetta dell'indice**.
  > **Ricorda:** Nello slicing, `df.loc['A':'C']` **include** anche l'etichetta 'C'.
- **`df.iloc[posizione]`**: Seleziona una o più righe in base alla loro **posizione numerica** (partendo da 0).
- **`df.loc[righe, colonne]`**: La sintassi più potente per selezionare un sottoinsieme preciso specificando sia le righe che le colonne.
- **Maschere Booleane**: Il modo più potente per filtrare i dati in base a una o più condizioni.
  ```python
  # Esempio con condizione singola
  df[df['Prezzo'] > 100]

  # Esempio con condizioni multiple
  df[(df['Prezzo'] > 100) & (df['Categoria'] == 'Elettronica')]
  ```
  > **Ricorda:** Usa `&` per AND, `|` per OR, `~` per NOT e metti sempre le condizioni tra parentesi `()`.

## 5. Combinare più `DataFrame`

Per unire dati provenienti da tabelle diverse.

- **`pd.concat([df1, df2])`**: "Incolla" i DataFrame uno sotto l'altro (verticalmente).
  - `ignore_index=True`: Crea un nuovo indice pulito per il risultato.
  - `axis=1`: Incolla i DataFrame fianco a fianco (orizzontalmente).

- **`pd.merge(df_sx, df_dx, on='colonna_chiave', how='tipo_join')`**: Esegue un'unione in stile database.
  - `on='...'`: Specifica la colonna in comune da usare come chiave.
  - `how='...'`: Specifica il tipo di unione:
    - **`'inner'`** (default): Tiene solo le righe con chiavi presenti in **entrambi**.
    - **`'outer'`**: Tiene **tutte** le righe da entrambi, riempiendo i buchi con `NaN`.
    - **`'left'`**: Tiene **tutte** le righe del DataFrame di sinistra.
    - **`'right'`**: Tiene **tutte** le righe del DataFrame di destra.

## 6. Raggruppare e Aggregare i Dati

Per calcolare statistiche su sottoinsiemi dei tuoi dati.

- **`df.groupby('colonna')`**: Crea un oggetto `GroupBy`, dividendo i dati in gruppi basati sui valori unici della colonna.
  > **Ricorda:** Da solo non fa nulla. È un'operazione "pigra" che attende un'aggregazione.

- **`.sum()`, `.mean()`, `.count()`, `.max()`, etc.**: Le funzioni di aggregazione da applicare dopo un `groupby`.
  ```python
  # Calcola il prezzo medio per ogni categoria
  df.groupby('Categoria')['Prezzo'].mean()
  ```

- **`df.resample('M')`**: Un `groupby` specializzato per le serie storiche. Raggruppa i dati per periodi di tempo ('M' per mese, 'D' per giorno, etc.).

- **`.idxmax()`, `.idxmin()`**: Metodi utilissimi per trovare l'**indice** della riga che contiene il valore massimo o minimo di una colonna.

## 7. Ordinare e Trasformare i Dati

Operazioni essenziali per organizzare e modificare i tuoi dati.

### Ordinamento

- **`df.sort_values('colonna')`**: Ordina il DataFrame in base ai valori di una colonna.
  ```python
  # Ordine crescente (default)
  df.sort_values('Prezzo')
  
  # Ordine decrescente
  df.sort_values('Prezzo', ascending=False)
  ```
- **`df.sort_values(['col1', 'col2'])`**: Ordina per più colonne (prima per col1, poi per col2).
- **`df.sort_index()`**: Ordina in base all'indice delle righe.

### Applicare Funzioni Personalizzate

- **`df.apply(funzione)`**: Applica una funzione a ogni colonna del DataFrame.
- **`df['colonna'].apply(funzione)`**: Applica una funzione a ogni elemento di una colonna.
  ```python
  # Esempio: calcolare la radice quadrata
  df['Prezzo'].apply(lambda x: x ** 0.5)
  
  # Esempio con funzione personalizzata
  def categorizza_prezzo(prezzo):
      return 'Alto' if prezzo > 100 else 'Basso'
  
  df['Categoria_Prezzo'] = df['Prezzo'].apply(categorizza_prezzo)
  ```
- **`df['colonna'].map(dizionario)`**: Sostituisce i valori usando un dizionario di mappatura.
  ```python
  # Esempio: convertire codici in nomi
  mapping = {1: 'Piccolo', 2: 'Medio', 3: 'Grande'}
  df['Taglia_Nome'] = df['Taglia_Codice'].map(mapping)
  ```

### Operazioni sulle Stringhe

- **`df['col'].str.contains('pattern')`**: Trova le righe che contengono un pattern di testo.
- **`df['col'].str.replace('vecchio', 'nuovo')`**: Sostituisce del testo in una colonna.
- **`df['col'].str.upper()`, `.str.lower()`**: Converte in maiuscolo/minuscolo.
- **`df['col'].str.strip()`**: Rimuove spazi all'inizio e alla fine.

## 8. Salvare i Risultati

Dopo aver manipolato i dati, è importante sapere come salvarli.

- **`df.to_csv('file_output.csv')`**: Salva il DataFrame in formato CSV.
  - `index=False`: Non salva l'indice come colonna separata.
  - `sep=';'`: Cambia il separatore (utile per Excel italiano).
- **`df.to_excel('file_output.xlsx')`**: Salva in formato Excel.
- **`df.to_json('file_output.json')`**: Salva in formato JSON.