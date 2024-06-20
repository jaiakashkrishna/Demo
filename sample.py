import unittest

def get_details():
    name = "John Doe"
    age = 30
    return f"My name is {name} and I am {age} years old."

class TestMain(unittest.TestCase):
    def test_get_details(self):
        self.assertEqual(get_details(), "My name is John Doe and I am 30 years old.")

if __name__ == "__main__":
    print(get_details())
    unittest.main()


