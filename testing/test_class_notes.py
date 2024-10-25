from class_notes import Animal
def test_get_name():
    testanimal= Animal("bob", "bobcat", 27, "M", "Epic")
    name = testanimal.get_name()
    assert name == "bob"
