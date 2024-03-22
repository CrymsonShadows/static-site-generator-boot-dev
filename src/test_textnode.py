import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node1 = TextNode("This is node 1", "bold" ,"https://google.com")
        node2 = TextNode("This is node 2", "bold", "https://google.com")
        self.assertNotEqual(node1, node2)
        node3 = TextNode("This is node 2", "bold")
        self.assertNotEqual(node2, node3)



if __name__ == "__main__":
    unittest.main()
