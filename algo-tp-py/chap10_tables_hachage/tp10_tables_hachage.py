"""TP 10 — Tables de Hachage"""


class PhoneBook:
    """Annuaire téléphonique basé sur une table de hachage avec chaînage."""
    M = 10007

    def __init__(self):
        self._table = [[] for _ in range(self.M)]
        self._size  = 0

    def _hash(self, name: str) -> int:
        """Hash polynomiale (base 31) — O(|name|). TODO"""
        raise NotImplementedError

    def add_contact(self, name: str, phone: str) -> None:
        """Insère ou met à jour le contact — O(1) amorti. TODO"""
        raise NotImplementedError

    def get_phone(self, name: str) -> str:
        """Retourne le numéro ou lève KeyError — O(1) moyen. TODO"""
        raise NotImplementedError

    def delete_contact(self, name: str) -> bool:
        """Supprime le contact. Retourne True si trouvé. TODO"""
        raise NotImplementedError

    def print_stats(self) -> None:
        """Affiche taille, facteur de charge, longueur max de chaîne."""
        max_chain = max(len(bucket) for bucket in self._table)
        collisions = sum(1 for b in self._table if len(b) > 1)
        print(f"size={self._size} load={self._size/self.M:.3f} "
              f"max_chain={max_chain} collisions={collisions}")

    def __len__(self): return self._size


class OpenHashMap:
    """Table de hachage à adressage ouvert (sondage linéaire)."""
    M = 1009
    _DELETED = object()   # marqueur tombstone

    def __init__(self):
        self._keys   = [None] * self.M
        self._values = [None] * self.M

    def _hash(self, key: str) -> int:
        """Hash polynomiale base 31. TODO"""
        raise NotImplementedError

    def insert(self, key: str, value) -> None:
        """Sondage linéaire — O(1) amorti. TODO"""
        raise NotImplementedError

    def search(self, key: str):
        """Retourne la valeur ou None si absente. TODO"""
        raise NotImplementedError

    def remove(self, key: str) -> bool:
        """Marque la case comme DELETED. Retourne True si trouvée. TODO"""
        raise NotImplementedError
