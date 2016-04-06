import unittest
from node import Node

class TestNodeClass(unittest.TestCase):
  def setUp(self): 
    self.node1 = Node(1)

  def test_init(self):
    self.assertEqual(self.node1.data, 1)

if __name__ == '__main__':
    unittest.main()