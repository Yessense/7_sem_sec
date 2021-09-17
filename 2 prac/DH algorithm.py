import erathosphene

n = 1000

class Person:
    g = 50
    p = 2561341234123412341234123412341234123412341234

    def __init__(self):
        self.g = Person.g
        self.p = Person.p
        self.prime = erathosphene.generate_prime_number(n)
        print(f'Prime: {self.prime}')

    def get_remainder(self):
        print(self.g ** self.prime)
        remainder = (self.g ** self.prime) % self.p
        print(f'Remainder: {remainder}')
        return remainder

    def get_key(self, other_remainder):
        self.key = other_remainder ** self.prime % self.p
        print(f'Key: {self.key}')
        return self.key



if __name__ == '__main__':
    Alice = Person()
    Bob = Person()

    A = Alice.get_remainder()
    B = Bob.get_remainder()

    assert Alice.get_key(B) == Bob.get_key(A)