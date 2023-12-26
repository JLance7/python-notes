import unittest, pytest

# unittest (run with python -m unittest)
class TestCase(unittest.TestCase):
  def test_this(self):
    try:
      pass
    except Exception:
      self.fail('test failed')


# pytest (run with pytest)
def test():
  answer = 1 + 1
  assert(answer == 2)