import unittest
from node import Node
from linked_list import LinkedList

class TestNodeClass(unittest.TestCase):
  def setUp(self):
    self.myLL = LinkedList()
    
    self.myLL1 = LinkedList()
    self.myLL1.insert(1)
    self.myLL1.insert(2)
    self.myLL1.insert(3)
    self.myLL1.insert(4)
    self.myLL1.insert(5)
    self.myLL1.insert(6)

    self.myLL_one_dup = LinkedList()
    self.myLL_one_dup.insert(1)
    self.myLL_one_dup.insert(2)
    self.myLL_one_dup.insert(3)
    self.myLL_one_dup.insert(4)
    self.myLL_one_dup.insert(2)
    self.myLL_one_dup.insert(5)

    self.myLL_one_dup_multiple_times = LinkedList()
    self.myLL_one_dup_multiple_times.insert(1)
    self.myLL_one_dup_multiple_times.insert(2)
    self.myLL_one_dup_multiple_times.insert(2)
    self.myLL_one_dup_multiple_times.insert(3)
    self.myLL_one_dup_multiple_times.insert(4)
    self.myLL_one_dup_multiple_times.insert(2)
    self.myLL_one_dup_multiple_times.insert(2)
    self.myLL_one_dup_multiple_times.insert(5)
    self.myLL_one_dup_multiple_times.insert(2)

    self.myLL_multiple_dup_nodes = LinkedList()
    self.myLL_multiple_dup_nodes.insert(1)
    self.myLL_multiple_dup_nodes.insert(2)
    self.myLL_multiple_dup_nodes.insert(2)
    self.myLL_multiple_dup_nodes.insert(3)
    self.myLL_multiple_dup_nodes.insert(1)
    self.myLL_multiple_dup_nodes.insert(4)
    self.myLL_multiple_dup_nodes.insert(2)
    self.myLL_multiple_dup_nodes.insert(2)
    self.myLL_multiple_dup_nodes.insert(5)
    self.myLL_multiple_dup_nodes.insert(1)
    self.myLL_multiple_dup_nodes.insert(2)
    self.myLL_multiple_dup_nodes.insert(3)

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
    self.assertEqual(self.myLL1.count, 6)
    self.myLL1.remove(0)
    self.assertEqual(self.myLL1.count, 5)
    self.assertEqual(self.myLL1.head.data, 2)
    self.assertEqual(self.myLL1.tail.data, 6)

    self.myLL1.remove(3)
    self.assertEqual(self.myLL1.count, 4)

    self.myLL1.remove(3)
    self.assertEqual(self.myLL1.count, 3)
    self.assertEqual(self.myLL1.head.data, 2)
    self.assertEqual(self.myLL1.tail.data, 4)

    self.myLL1.remove(0)
    self.myLL1.remove(0)
    self.myLL1.remove(0)
    self.assertEqual(self.myLL1.count, 0)
    self.assertEqual(self.myLL1.head, None)
    self.assertEqual(self.myLL1.tail, None)

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

  def test_remove_dup_from_empty_LL(self):
    with self.assertRaises(Exception):
      self.myLL.remove_dup()

  def test_remove_dup_with_one_dup_node(self):
    self.myLL_one_dup.remove_dup()
    self.assertEqual(self.myLL_one_dup.count, 5)
    self.assertEqual(self.myLL_one_dup.tail.data, 5)

  def test_remove_dup_with_one_dup_node_at_tail(self):
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
    self.myLL_one_dup_multiple_times.remove_dup()
    self.assertEqual(self.myLL_one_dup_multiple_times.count, 5)
    self.assertEqual(self.myLL_one_dup_multiple_times.tail.data, 5)

  def test_remove_dup_with_multiple_dup_nodes(self):
    self.myLL_multiple_dup_nodes.remove_dup()  
    self.assertEqual(self.myLL_multiple_dup_nodes.count, 5)
    self.assertEqual(self.myLL_multiple_dup_nodes.tail.data, 5)
  
  def test_remove_dup_from_LL_with_no_dups(self):
    self.myLL1.remove_dup()
    self.assertEqual(self.myLL1.count, 6)

  def test_remove_dup_no_buffer_from_empty_LL(self):
    with self.assertRaises(Exception):
      self.myLL.remove_dup_no_buffer()

  def test_remove_dup_no_buffer_with_one_dup_node(self):
    self.myLL_one_dup.remove_dup_no_buffer()
    self.assertEqual(self.myLL_one_dup.count, 5)
    self.assertEqual(self.myLL_one_dup.tail.data, 5)

  def test_remove_dup_no_buffer_with_one_dup_node_at_tail(self):
    self.myLL.insert(1)
    self.myLL.insert(2)
    self.myLL.insert(3)
    self.myLL.insert(4)
    self.myLL.insert(5)
    self.myLL.insert(2)

    self.myLL.remove_dup_no_buffer()
    self.assertEqual(self.myLL.count, 5)
    self.assertEqual(self.myLL.tail.data, 5)

  def test_remove_dup_no_buffer_with_one_dup_node_multiple_times(self):
    self.myLL_one_dup_multiple_times.remove_dup_no_buffer()
    self.assertEqual(self.myLL_one_dup_multiple_times.count, 5)
    self.assertEqual(self.myLL_one_dup_multiple_times.tail.data, 5)

  def test_remove_dup_no_buffer_with_multiple_dup_nodes(self):
    self.myLL_multiple_dup_nodes.remove_dup_no_buffer()  
    self.assertEqual(self.myLL_multiple_dup_nodes.count, 5)
    self.assertEqual(self.myLL_multiple_dup_nodes.tail.data, 5)

  def test_remove_dup_no_buffer_from_LL_with_no_dups(self):
    self.myLL1.remove_dup_no_buffer()
    self.assertEqual(self.myLL1.count, 6)

  def test_get_count(self):
    self.assertEqual(self.myLL.get_count(), 0)

    self.myLL.insert(1)
    self.myLL.insert(2)

    self.assertEqual(self.myLL.get_count(), 2)

  def test_is_empty_returns_true_for_empty_LL(self):
    self.assertEqual(self.myLL.is_empty(), True)

  def test_is_empty_returns_false_for_nonempty_LL(self):
    self.myLL.insert(1)
    self.assertEqual(self.myLL.is_empty(), False)

  def test_get_kth_to_last_elem_in_LL(self):
    val = self.myLL1.get_from_end(3)
    self.assertEqual(val, 4)

  def test_get_kth_to_last_elem_in_empty_LL(self):
    with self.assertRaises(Exception):
      self.myLL.get_from_end(3)

  def test_get_kth_to_last_elem_in_empty_LL_out_of_bounds(self):
    with self.assertRaises(TypeError):
      self.myLL1.get_from_end(8)
    with self.assertRaises(TypeError):
      self.myLL1.get_from_end(-1) 

  def test_get_kth_to_last_elem_in_LL_at_tail(self):
    val = self.myLL1.get_from_end(1)
    self.assertEqual(val, 6)

  def test_get_kth_to_last_elem_in_LL_at_head(self):
    val = self.myLL1.get_from_end(6)
    self.assertEqual(val, 1)

if __name__ == '__main__':
    unittest.main()