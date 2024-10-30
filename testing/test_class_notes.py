from class_notes10_21_24 import Animal
def test_get_name():
    testanimal= Animal("bob", "bobcat", 27, "M", "Epic")
    name = testanimal.get_name()
    assert name == "bob"
