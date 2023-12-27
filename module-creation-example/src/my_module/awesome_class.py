class AwesomeClass:
  def __init__(self, awesome=True):
    self.awesome = awesome
  
  @staticmethod
  def print_cool():
    print('cool')
  
  def get_awesomeness(self):
    return self.awesome
  
  def set_awesome(self, awesome: bool):
    self.awesome = awesome