import unittest
import unittest.mock as mock
from input_validation import validation_with_if as validation_with_if


class MyTestCase(unittest.TestCase):
  
  
  # def test_average(self):
  #   with mock.patch('builtins.input', side_effect=[85, 90, 95]):
  #     assert validation_with_if.average() == 90
  

  def test_negative_entry_at_index_zero(self):
    with mock.patch('builtins.input', side_effect=[-1, 95, 95]):
      assert validation_with_if.average() == -1
  

  def test_negative_entry_at_index_one(self):
    with mock.patch('builtins.input', side_effect=[95, -1, 95]):
      assert validation_with_if.average() == -1
  

  def test_negative_entry_at_index_two(self):
    with mock.patch('builtins.input', side_effect=[95, 95, -1]):
      assert validation_with_if.average() == -1
