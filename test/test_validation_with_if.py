import unittest
import unittest.mock as mock
from input_validation import validation_with_if as validation_with_if


class MyTestCase(unittest.TestCase):
  
  
  def test_average(self):
    with mock.patch('builtins.input', side_effect=[85, 90, 95]):
      assert validation_with_if.average() == 90