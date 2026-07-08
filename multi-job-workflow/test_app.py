from app import greet

def test_greet():
    assert greet() == "Hello from EyesOnCloud App!"

test_greet()
print("All tests passed!")
