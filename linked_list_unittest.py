import unittest
from node import Node
from linked_list import LinkedList

class TestNodeClass(unittest.TestCase):
  def setUp(self):
    self.myLL = LinkedList()

  def test_init(self):
    self.assertEqual(self.myLL.head, None)
    self.assertEqual(self.myLL.tail, None)
    self.assertEqual(self.myLL.count, 0)

  def test_insert(self):
    self.myLL.insert(1)
    self.myLL.insert(2)
    self.myLL.insert(3)

    self.assertEqual(self.myLL.head.data, 1)
    self.assertEqual(self.myLL.tail.data, 3)
    self.assertEqual(self.myLL.count, 3)

  def test_remove(self):
    self.myLL.insert(1)
    self.myLL.insert(2)
    self.myLL.insert(3)
    self.myLL.insert(4)
    self.myLL.insert(5)
    self.myLL.insert(6)

    self.assertEqual(self.myLL.count, 6)
    self.myLL.remove(0)
    self.assertEqual(self.myLL.count, 5)
    self.assertEqual(self.myLL.head.data, 2)
    self.assertEqual(self.myLL.tail.data, 6)

    self.myLL.remove(3)
    self.assertEqual(self.myLL.count, 4)

    self.myLL.remove(3)
    self.assertEqual(self.myLL.count, 3)
    self.assertEqual(self.myLL.head.data, 2)
    self.assertEqual(self.myLL.tail.data, 4)

    self.myLL.remove(0)
    self.myLL.remove(0)
    self.myLL.remove(0)
    self.assertEqual(self.myLL.count, 0)
    self.assertEqual(self.myLL.head, None)
    self.assertEqual(self.myLL.tail, None)

  def test_remove_from_empty_LL(self):
    with self.assertRaises(Exception):
      self.myLL.remove(3)

  def test_remove_out_of_bounds_index_raises_exception(self):
    self.myLL.insert(1)
    self.myLL.insert(2)
    self.myLL.insert(3)

    with self.assertRaises(TypeError):
      self.myLL.remove(-1)

    with self.assertRaises(TypeError):
      self.myLL.remove(3)

  def test_is_empty_returns_true_for_empty_LL(self):
    self.assertEqual(self.myLL.is_empty(), True)

  def test_is_empty_returns_false_for_nonempty_LL(self):
    self.myLL.insert(1)
    self.assertEqual(self.myLL.is_empty(), False)

  def test_remove_dup_from_empty_LL(self):
    with self.assertRaises(Exception):
      self.myLL.remove_dup()

  def test_remove_dup_with_one_dup_node(self):
    self.myLL.insert(1)
    self.myLL.insert(2)
    self.myLL.insert(3)
    self.myLL.insert(4)
    self.myLL.insert(2)
    self.myLL.insert(5)

    self.myLL.remove_dup()    
    self.assertEqual(self.myLL.count, 5)
    self.assertEqual(self.myLL.tail.data, 5)

  def test_remove_dup_with_one_dup_node_at_end(self):
    self.myLL.insert(1)
    self.myLL.insert(2)
    self.myLL.insert(3)
    self.myLL.insert(4)
    self.myLL.insert(5)
    self.myLL.insert(2)

    self.myLL.remove_dup()    
    self.assertEqual(self.myLL.count, 5)
    self.assertEqual(self.myLL.tail.data, 5)
    
  def test_remove_dup_with_one_dup_node_multiple_times(self):
    self.myLL.insert(1)
    self.myLL.insert(2)
    self.myLL.insert(2)
    self.myLL.insert(3)
    self.myLL.insert(4)
    self.myLL.insert(2)
    self.myLL.insert(2)
    self.myLL.insert(5)
    self.myLL.insert(2)

    self.myLL.remove_dup()    
    self.assertEqual(self.myLL.count, 5)
    self.assertEqual(self.myLL.tail.data, 5)

  def test_remove_dup_with_multiple_dup_nodes(self):
    self.myLL.insert(1)
    self.myLL.insert(2)
    self.myLL.insert(2)
    self.myLL.insert(3)
    self.myLL.insert(1)
    self.myLL.insert(4)
    self.myLL.insert(2)
    self.myLL.insert(2)
    self.myLL.insert(5)
    self.myLL.insert(1)
    self.myLL.insert(2)
    self.myLL.insert(3)

    self.myLL.remove_dup()    
    self.assertEqual(self.myLL.count, 5)
    self.assertEqual(self.myLL.tail.data, 5)

  
  def test_remove_dup_from_LL_with_no_dups(self):
    self.myLL.insert(1)
    self.myLL.insert(2)
    self.myLL.insert(3)
    self.myLL.insert(4)
    self.myLL.insert(5)
    self.myLL.insert(6)

    before = self.myLL.count
    self.myLL.remove_dup()

    self.assertEqual(before, self.myLL.count)



if __name__ == '__main__':
    unittest.main()