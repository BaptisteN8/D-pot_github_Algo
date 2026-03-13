"""Tests pytest — TP 10 : Tables de Hachage"""
import pytest, random, string
from tp10_tables_hachage import PhoneBook, OpenHashMap


class TestPhoneBook:
    def test_add_and_get(self):
        pb = PhoneBook()
        pb.add_contact("Alice", "0601020304")
        assert pb.get_phone("Alice") == "0601020304"

    def test_len(self):
        pb = PhoneBook()
        pb.add_contact("Alice","06"); pb.add_contact("Bob","07")
        assert len(pb) == 2

    def test_delete(self):
        pb = PhoneBook()
        pb.add_contact("Alice","06")
        assert pb.delete_contact("Alice") is True
        assert len(pb) == 0
        with pytest.raises(KeyError):
            pb.get_phone("Alice")

    def test_delete_nonexistent(self):
        pb = PhoneBook()
        assert pb.delete_contact("Unknown") is False

    def test_update(self):
        pb = PhoneBook()
        pb.add_contact("Alice","06"); pb.add_contact("Alice","07")
        assert pb.get_phone("Alice") == "07"
        assert len(pb) == 1

    def test_not_found_raises(self):
        with pytest.raises(KeyError):
            PhoneBook().get_phone("Ghost")

    @pytest.mark.timeout(2)
    def test_many_contacts(self):
        pb = PhoneBook()
        names = ["".join(random.choices(string.ascii_lowercase, k=8)) for _ in range(500)]
        for n in names:
            pb.add_contact(n, "0600000000")
        for n in names:
            assert pb.get_phone(n) == "0600000000"


class TestOpenHashMap:
    def test_insert_search(self):
        m = OpenHashMap()
        m.insert("x","hello"); m.insert("y","world")
        assert m.search("x") == "hello"
        assert m.search("y") == "world"

    def test_not_found(self):
        assert OpenHashMap().search("ghost") is None

    def test_remove(self):
        m = OpenHashMap()
        m.insert("key","val")
        assert m.remove("key") is True
        assert m.search("key") is None

    def test_remove_nonexistent(self):
        assert OpenHashMap().remove("ghost") is False

    def test_collision_resolution(self):
        """Plusieurs insertions — aucune ne doit se perdre."""
        m = OpenHashMap()
        pairs = [(f"k{i}", f"v{i}") for i in range(50)]
        for k, v in pairs:
            m.insert(k, v)
        for k, v in pairs:
            assert m.search(k) == v

    def test_insert_after_delete(self):
        """On peut réinsérer une clé après l'avoir supprimée."""
        m = OpenHashMap()
        m.insert("a","1"); m.remove("a"); m.insert("a","2")
        assert m.search("a") == "2"
