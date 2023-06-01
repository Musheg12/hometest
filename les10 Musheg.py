"""Создать класс Human c атрибутами name, surname, birth_year и двумя методами full_name(),
 который будет  возвращать полное имя:
 Name Surname и get_age(), возвращающий возраст, созданного экземпляра."""
class Human:
    def __init__(self, name, surname, birth_year):
        self.name = name
        self.surname = surname
        self.birth_year = birth_year

    def full_name(self):
        self.full_name = self.name + ' ' + self.surname
        return self.full_name

    def get_age(self):
        return f"Возраст: {2023 - self.birth_year}"

hum = Human("Axel", "Fouli", 1963)

print(f"{hum.full_name()}\n{hum.get_age()}")