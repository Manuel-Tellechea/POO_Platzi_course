class Person:
    def __init__(self, name):
        self.name = name

    def get_moving(self):
        print(f"I'm walking")


class Cyclist(Person):
    def __init__(self, name):
        super().__init__(name)

    def get_moving(self):
        print(f"I'm ridding my bike")


def main():
    person = Person('Ignazio')
    person.get_moving()

    cyclist = Cyclist('Lucía')
    cyclist.get_moving()


if __name__ == '__main__':
    main()
