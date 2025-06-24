# -*- coding: utf-8 -*-

# ======================================================
#  1. CLASSE MADRE (O CLASSE BASE)
# ======================================================
class Modello:
    """
    Questa è la "docstring" della classe.
    Descrive lo scopo della classe Modello.
    È una buona pratica includerla sempre.
    """

    # --- METODO COSTRUTTORE ---
    def __init__(self, parametro1: str, parametro2: int):
        """
        Il costruttore, chiamato quando si crea un nuovo oggetto.
        Inizializza gli attributi dell'oggetto.

        Args:
            parametro1 (str): Descrizione del primo parametro.
            parametro2 (int): Descrizione del secondo parametro.
        """
        # Attributi dell'istanza: ogni oggetto avrà i propri valori
        self.attributo_testo = parametro1
        self.attributo_numero = parametro2
        print(f"-> Oggetto 'Modello' creato con testo='{self.attributo_testo}'")

    # --- METODI SPECIALI PER LA RAPPRESENTAZIONE ---
    def __repr__(self) -> str:
        """
        Rappresentazione ufficiale dell'oggetto (per sviluppatori).
        Dovrebbe essere non ambigua e, se possibile, codice valido.
        """
        return f"Modello(parametro1='{self.attributo_testo}', parametro2={self.attributo_numero})"

    def __str__(self) -> str:
        """
        Rappresentazione leggibile dell'oggetto (per gli utenti).
        Usata da print() e str().
        """
        return f"Un oggetto Modello con testo '{self.attributo_testo}' e numero {self.attributo_numero}."

    # --- METODI D'ISTANZA ---
    def metodo_di_esempio(self):
        """
        Un'azione che l'oggetto può compiere.
        Può accedere e modificare gli attributi dell'oggetto usando 'self'.
        """
        print(f"Ciao dal metodo di esempio! Il mio numero è {self.attributo_numero}.")
        self.attributo_numero += 1
        print(f"Ho appena incrementato il mio numero a {self.attributo_numero}.")


# ======================================================
#  2. CLASSE FIGLIA (EREDITARIETÀ)
# ======================================================
class ModelloAvanzato(Modello):
    """
    Questa classe eredita da 'Modello'.
    Ottiene tutti i suoi attributi e metodi e ne aggiunge di nuovi.
    """

    # --- COSTRUTTORE DELLA CLASSE FIGLIA ---
    def __init__(self, parametro1: str, parametro2: int, parametro3: bool):
        """
        Costruttore per il ModelloAvanzato.

        Args:
            parametro1 (str): Parametro da passare alla classe madre.
            parametro2 (int): Parametro da passare alla classe madre.
            parametro3 (bool): Nuovo parametro specifico di questa classe.
        """
        # 1. Chiama il costruttore della classe madre per inizializzare gli attributi ereditati
        super().__init__(parametro1, parametro2)

        # 2. Inizializza i nuovi attributi specifici della classe figlia
        self.attributo_booleano = parametro3
        print(f"--> Oggetto 'ModelloAvanzato' creato con booleano={self.attributo_booleano}")

    # --- SOVRASCRITTURA DI UN METODO (OVERRIDING) ---
    def metodo_di_esempio(self):
        """
        Questa classe fornisce la sua versione del metodo ereditato.
        Questo si chiama "override".
        """
        print(f"Ciao dal metodo avanzato! Il mio testo è '{self.attributo_testo}'.")
        # Possiamo ancora chiamare la versione del metodo della classe madre, se vogliamo
        # super().metodo_di_esempio()

    # --- RAPPRESENTAZIONE PERSONALIZZATA ---
    def __repr__(self) -> str:
        """
        È buona pratica aggiornare anche __repr__ per includere i nuovi attributi.
        """
        return (f"ModelloAvanzato(parametro1='{self.attributo_testo}', "
                f"parametro2={self.attributo_numero}, "
                f"parametro3={self.attributo_booleano})")


# ======================================================
#  3. SEZIONE DI ESEMPIO
# ======================================================
if __name__ == "__main__":
    print("--- Creazione di un oggetto della classe madre ---")
    obj1 = Modello("prova", 100)

    print("\n--- Uso dei metodi speciali ---")
    print(f"Uso di print() (chiama __str__): {obj1}")
    print(f"Rappresentazione per debug (da __repr__): {repr(obj1)}")

    print("\n--- Uso di un metodo d'istanza ---")
    obj1.metodo_di_esempio()
    print(f"Stato dopo la chiamata al metodo: {repr(obj1)}")

    print("\n" + "=" * 40 + "\n")

    print("--- Creazione di un oggetto della classe figlia ---")
    obj2 = ModelloAvanzato("avanzato", 200, True)

    print("\n--- Uso di metodi e attributi ereditati e non ---")
    print(f"Attributo ereditato: {obj2.attributo_testo}")
    print(f"Attributo specifico: {obj2.attributo_booleano}")

    print("\n--- Uso del metodo sovrascritto ---")
    obj2.metodo_di_esempio()
    print(f"Stato dopo la chiamata al metodo: {repr(obj2)}")