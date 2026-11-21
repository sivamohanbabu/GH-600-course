import unittest

from main import hello_world


class HelloWorldTests(unittest.TestCase):
    def test_hello_world(self) -> None:
        self.assertEqual(hello_world(), "Hello, World!")


if __name__ == "__main__":
    unittest.main()
