import unittest
from linked_list import LinkedList

class TestLinkedListClass(unittest.TestCase):
  def setUp(self):
    self.LL = LinkedList()

  def test_init(self):
    self.assertEqual(self.LL.head, None)
    self.assertEqual(self.LL.tail, None)
    self.assertEqual(self.LL.count, 0)

  def test_get_count(self):
    self.assertEqual(self.LL.get_count(), 0)

    self.LL.insert(1)
    self.LL.insert(2)

    self.assertEqual(self.LL.get_count(), 2)

  def test_is_empty(self):
    self.assertTrue(self.LL.is_empty())

    self.LL.insert(1)
    self.assertFalse(self.LL.is_empty())    

  def test_insert(self):
    self.LL.insert(1)
    self.LL.insert(2)
    self.LL.insert(3)

    self.assertEqual(self.LL.count, 3)
    self.assertEqual(self.LL.head.data, 1)
    self.assertEqual(self.LL.tail.data, 3)

  def test_remove(self):
    self.LL.insert(1)
    self.LL.insert(2)
    self.LL.insert(3)
    self.LL.insert(4)

    self.assertEqual(self.LL.count, 4)
    self.LL.remove(2)
    self.assertEqual(self.LL.count, 3)
    self.assertEqual(self.LL.head.data, 1)
    self.assertEqual(self.LL.tail.data, 4)

  def test_remove_from_empty_LL_raises_exception(self):
    with self.assertRaises(Exception):
      self.LL.remove(3)
  
  def test_remove_out_of_bounds_index_raises_typeError(self):
    self.LL.insert(1)
    self.LL.insert(2)
    self.LL.insert(3)

    with self.assertRaises(TypeError):
      self.LL.remove(-1)
    with self.assertRaises(TypeError):
      self.LL.remove(3)

  def test_remove_from_head(self):
    self.LL.insert(1)
    self.LL.insert(2)
    self.LL.insert(3)

    self.LL.remove(0)
    self.assertEqual(self.LL.count, 2)
    self.assertEqual(self.LL.head.data, 2)
    self.assertEqual(self.LL.tail.data, 3)

  def test_remove_from_tail(self):
    self.LL.insert(1)
    self.LL.insert(2)
    self.LL.insert(3)

    self.LL.remove(2)
    self.assertEqual(self.LL.count, 2)
    self.assertEqual(self.LL.head.data, 1)
    self.assertEqual(self.LL.tail.data, 2)

  def test_remove_last_node(self):
    self.LL.insert(1)

    self.LL.remove(0)
    self.assertTrue(self.LL.is_empty())
    
  def test_remove_dup_when_no_dupes_returns_None(self):
    self.LL.insert(1)
    var = self.LL.remove_dup()

    self.assertIsNone(var)

  def test_remove_dup_only_one_pair(self):
    self.LL.insert(1)
    self.LL.insert(2)
    self.LL.insert(3)
    self.LL.insert(2)
    self.LL.insert(4)

    self.assertEqual(self.LL.count, 5)
    self.LL.remove_dup()
    self.assertEqual(self.LL.count, 4)

  def test_remove_dup_multiple_of_one(self):
    self.LL.insert(1)
    self.LL.insert(2)
    self.LL.insert(3)
    self.LL.insert(2)
    self.LL.insert(2)
    self.LL.insert(2)
    self.LL.insert(4)

    self.assertEqual(self.LL.count, 7)
    self.LL.remove_dup()
    self.assertEqual(self.LL.count, 4)

  def test_remove_dup_multiple_of_multiple(self):
    self.LL.insert(1)
    self.LL.insert(2)
    self.LL.insert(3)
    self.LL.insert(3)
    self.LL.insert(3)
    self.LL.insert(2)
    self.LL.insert(4)

    self.assertEqual(self.LL.count, 7)
    self.LL.remove_dup()
    self.assertEqual(self.LL.count, 4)

  def test_remove_dup_from_tail(self):
    self.LL.insert(1)
    self.LL.insert(2)
    self.LL.insert(3)
    self.LL.insert(3)
    self.LL.insert(2)


    self.assertEqual(self.LL.count, 5)
    self.LL.remove_dup()
    self.assertEqual(self.LL.count, 3)
    self.assertEqual(self.LL.tail.data, 3)

  def test_remove_dup_no_buffer_when_no_dupes_returns_None(self):
    self.LL.insert(1)
    var = self.LL.remove_dup_no_buffer()

    self.assertIsNone(var)

  def test_remove_dup_no_buffer_only_one_pair(self):
    self.LL.insert(1)
    self.LL.insert(2)
    self.LL.insert(3)
    self.LL.insert(2)
    self.LL.insert(4)

    self.assertEqual(self.LL.count, 5)
    self.LL.remove_dup_no_buffer()
    self.assertEqual(self.LL.count, 4)

  def test_remove_dup_no_buffer_multiple_of_one(self):
    self.LL.insert(1)
    self.LL.insert(2)
    self.LL.insert(3)
    self.LL.insert(2)
    self.LL.insert(2)
    self.LL.insert(2)
    self.LL.insert(4)

    self.assertEqual(self.LL.count, 7)
    self.LL.remove_dup_no_buffer()
    self.assertEqual(self.LL.count, 4)

  def test_remove_dup_no_buffer_multiple_of_multiple(self):
    self.LL.insert(1)
    self.LL.insert(2)
    self.LL.insert(3)
    self.LL.insert(3)
    self.LL.insert(3)
    self.LL.insert(2)
    self.LL.insert(4)

    self.assertEqual(self.LL.count, 7)
    self.LL.remove_dup_no_buffer()
    self.assertEqual(self.LL.count, 4)

  def test_remove_dup_no_buffer_from_tail(self):
    self.LL.insert(1)
    self.LL.insert(2)
    self.LL.insert(3)
    self.LL.insert(3)
    self.LL.insert(2)


    self.assertEqual(self.LL.count, 5)
    self.LL.remove_dup_no_buffer()
    self.assertEqual(self.LL.count, 3)
    self.assertEqual(self.LL.tail.data, 3)

  def test_kth_to_last_from_empty_LL(self):
    with self.assertRaises(Exception):
      self.LL.kth_to_last(3)

  def test_kth_to_last_out_of_bounds(self):
    self.LL.insert(1)
    self.LL.insert(2)
    self.LL.insert(3)

    with self.assertRaises(TypeError):
      self.LL.kth_to_last(4)

    with self.assertRaises(TypeError):
      self.LL.kth_to_last(-1)

  def test_kth_to_last(self):
    self.LL.insert(1)
    self.LL.insert(2)
    self.LL.insert(3)

    val = self.LL.kth_to_last(2)
    self.assertEqual(val, 2)

  def test_kth_to_last_at_head(self):
    self.LL.insert(1)
    self.LL.insert(2)
    self.LL.insert(3)

    val = self.LL.kth_to_last(3)
    self.assertEqual(val, 1)

  def test_kth_to_last_at_tail(self):
    self.LL.insert(1)
    self.LL.insert(2)
    self.LL.insert(3)

    val = self.LL.kth_to_last(1)
    self.assertEqual(val, 3)

  def test_delete_middle_node(self):
    self.LL.insert(1)
    self.LL.insert(2)
    self.LL.insert(8)
    self.LL.insert(3)
    self.LL.insert(4)

    ptr = self.LL.head
    for x in range(0, 2):
      ptr = ptr.next

    self.LL = self.LL.delete_middle_node(ptr)
    self.assertEqual(self.LL.count, 4)

  def test_delete_middle_node_with_None_ptr(self):
    ptr = self.LL.head

    with self.assertRaises(TypeError):
      self.LL.delete_middle_node(ptr)

  def test_partition_from_empty_LL(self):
    with self.assertRaises(Exception):
      self.LL.partition(3)

  def test_partition_with_nonexistant_x(self):
    self.LL.insert(1)
    self.LL.insert(2)
    self.LL.insert(3)
    self.LL.insert(4)
    self.LL.insert(5)
    self.LL.insert(6)

    partitioned_LL = self.LL.partition(0)
    current = self.LL.head
    current1 = partitioned_LL.head
    while (current is not None and current1 is not None):
      self.assertEqual(current.data, current1.data)
      current = current.next
      current1 = current1.next

    partitioned_LL1 = self.LL.partition(7)
    current = self.LL.head
    current1 = partitioned_LL.head
    while (current is not None and current1 is not None):
      self.assertEqual(current.data, current1.data)
      current = current.next
      current1 = current1.next

  def test_partition(self):
    self.LL.insert(4)
    self.LL.insert(2)
    self.LL.insert(1)
    self.LL.insert(3)
    self.LL.insert(-1)
    self.LL.insert(8)
    self.LL.insert(4)

    partioned_LL = self.LL.partition(4)
    current = partioned_LL.head
    while (current.data is not 4 and current is not None):
      current = current.next

    while current is not None:
      self.assertGreaterEqual(current.data, 4)
      current = current.next

if __name__ == '__main__':
    unittest.main()