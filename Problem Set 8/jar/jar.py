class Jar:
    def __init__(self, capacity=12):
        if int(capacity) >= 0:
            self._capacity = capacity
            self.size = 0
        else:
            raise ValueError

    def __str__(self):
        if self._size:
            return "🍪" * self._size
        else:
            return ""

    def deposit(self, n):
        if self._size + n <= self._capacity:
            self._size += n
        else:
            raise ValueError("Capacity has been exceeded")

    def withdraw(self, n):
        if self._size - n >= 0:
            self._size -= n
        else:
            raise ValueError("Not enough cookies")

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @size.setter
    def size(self, size):
        self._size = size

#def main():
#   jar = Jar()
#   prompt = input("Deposit or Withdraw?: ").lower().strip()
#   try:
#      if prompt == "deposit":
#        jar.deposit(n)
#       print (f"Number of cookies is {jar.size}")
#   elif prompt == "withdraw":
#            n = int(input("How many cookies?: "))
#           jar.withdraw(n)
#            print (f"Number of cookies is {jar.size}")
#
#    except ValueError as e:
#        print(e)
#
#if __name__ == "__main__":
#    main()
