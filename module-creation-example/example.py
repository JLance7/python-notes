from my_module import math
from my_module.another_dir import more_math
from my_module.awesome_class import AwesomeClass

print(math.add_one(1))
print(more_math.sub_one(1))

ac = AwesomeClass(True)
print(ac.get_awesomeness())