from faker import Faker


def show_greeting():
    faker = Faker()
    first_name = faker.first_name()
    print(f"Hello {first_name}!")
