from typing import List, NewType              

# def greeting(name: str) -> str:
#   return name

# name = greeting('josh')
# print(name)

# class Vector(list[float]):
#     pass

# def scale(scaler: float, vector: Vector) -> Vector:
#    return [scaler * num for num in vector]

# output = scale(2, Vector([1.2, 1.3, 1.4]))
# print(output)

# UserId = NewType('UserId', int)
# id = UserId(22)
# print(type(id))

# from collections.abc import Sequence, Mapping

# class Employee:
#    pass

# def my_func(employees: Sequence(Employee), age_name: Mapping[str, str]) -> None:
#    pass

# x: tuple[int, str] = (1, 'hi')
  
Vector = list[float]

my_list: Vector = [1.2, 1.3, 1.4]
print(type(Vector))

from collections.abc import Sequence
from typing import Optional, Any

ConnectionOptions = dict[str, str]
Address = tuple[str, int]
Server = tuple[Address, ConnectionOptions]


# The static type checker will treat the previous type signature as
# being exactly equivalent to this one.
def broadcast_message(
        message: str,
        servers: Sequence[tuple[tuple[str, int], dict[str, str]]]) -> None:
    pass

broadcast_message('hello', [(('123', 123), {'stuff': 'val'}), (('address', 1234), {'stuff': 'val2'})])

x: list[int | str] = [3, 5, "test", "fun"]  # Python 3.10+

# Use Optional[X] for a value that could be None
# Optional[X] is the same as X | None or Union[X, None]
y: Optional[str] = "something"


def test(x: Any) -> None: pass

class BankAccount:
    def __init__(self, name: str, balance: float = 0.0) -> None:
      self.name = name
      self.balance = balance
    
    def deposit(self, amount: float | int) -> None:
       self.balance += amount
    
    def withdraw(self, amount: float | int) -> None:
       self.balance -= amount

bank: BankAccount = BankAccount('Josh', 2)
bank.deposit(2)

class AuditBankAccount(BankAccount):
  def __init__(self, name: str, balance: float = 0.0) -> None:
    super().__init__(name, balance)
    self.audit_log: list[str] = []
  
  def deposit_log(self, amount: float | int) -> None:
     self.audit_log.append(f'Deposited {amount}')
     self.deposit(amount)
  
  def withdraw_log(self, amount: float | int) -> None:
     self.audit_log.append(f'Withdrew {amount}')
     self.withdraw(amount)

  def print_log(self) -> None:
     print(self.audit_log)
  

audit_bank: AuditBankAccount = AuditBankAccount('Josh', 2)
audit_bank.deposit_log(2)
audit_bank.deposit_log(4)
audit_bank.print_log()

  
  