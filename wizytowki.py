from faker import Faker
fake = Faker('en_US')

class Card:
    card_set = []
    def __init__(self, name, last_name, position, email):
        self.name = name
        self.last_name = last_name
        self.position = position
        self.email = email
        self.card_set.append(self)

    def __str__(self):
        return f"{self.name} {self.last_name} {self.email}"

    def create_card(n):
        for number in range(n):
            new_card = Card(name=fake.first_name(), last_name=fake.last_name(), email=fake.email())
            print(new_card)
        return card_set

create_card(5)



