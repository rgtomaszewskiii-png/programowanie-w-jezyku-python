class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return (
            f"Library:\n"
            f"  Address: {self.street}, {self.zip_code} {self.city}\n"
            f"  Open hours: {self.open_hours}\n"
            f"  Phone: {self.phone}"
        )

    class Employee:
        def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
            self.first_name = first_name
            self.last_name = last_name
            self.hire_date = hire_date
            self.birth_date = birth_date
            self.city = city
            self.street = street
            self.zip_code = zip_code
            self.phone = phone

        def __str__(self):
            return (
                f"Employee: {self.first_name} {self.last_name}\n"
                f"  Hire date: {self.hire_date}\n"
                f"  Birth date: {self.birth_date}\n"
                f"  Address: {self.street}, {self.zip_code} {self.city}\n"
                f"  Phone: {self.phone}"
            )

        class Student:
            def __init__(self, first_name, last_name, student_id):
                self.first_name = first_name
                self.last_name = last_name
                self.student_id = student_id

            def __str__(self):
                return f"Student: {self.first_name} {self.last_name} (ID: {self.student_id})"

            class Book:
                def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
                    self.library = library
                    self.publication_date = publication_date
                    self.author_name = author_name
                    self.author_surname = author_surname
                    self.number_of_pages = number_of_pages

                def __str__(self):
                    return (
                        f"Book:\n"
                        f"  Author: {self.author_name} {self.author_surname}\n"
                        f"  Publication date: {self.publication_date}\n"
                        f"  Pages: {self.number_of_pages}\n"
                        f"  Available in:\n{self.library}"
                    )

                class Order:
                    def __init__(self, employee, student, books, order_date):
                        self.employee = employee
                        self.student = student
                        self.books = books
                        self.order_date = order_date

                    def __str__(self):
                        books_str = "\n".join(str(book) for book in self.books)
                        return (
                            f"Order date: {self.order_date}\n"
                            f"{self.student}\n"
                            f"Handled by:\n{self.employee}\n"
                            f"Books:\n{books_str}"
                        )

                    if __name__ == "__main__":
                        library1 = Library("Warsaw", "Main St 1", "00-001", "8-18", "123456789")
                        library2 = Library("Krakow", "Book St 5", "30-002", "9-17", "987654321")

                        books = [
                            Book(library1, "2010", "Adam", "Mickiewicz", 300),
                            Book(library1, "2015", "Henryk", "Sienkiewicz", 500),
                            Book(library2, "2000", "Juliusz", "Slowacki", 250),
                            Book(library2, "2020", "Olga", "Tokarczuk", 400),
                            Book(library1, "1999", "Boleslaw", "Prus", 350),
                        ]

                        employees = [
                            Employee("Anna", "Nowak", "2020-01-01", "1990-05-05", "Warsaw", "Main St 2", "00-002",
                                     "111222333"),
                            Employee("Jan", "Kowalski", "2019-02-02", "1985-03-03", "Krakow", "Book St 6", "30-003",
                                     "444555666"),
                            Employee("Ewa", "Zielinska", "2021-03-03", "1992-04-04", "Gdansk", "Sea St 1", "80-001",
                                     "777888999"),
                        ]

                        students = [
                            Student("Tom", "Smith", "S001"),
                            Student("Kate", "Brown", "S002"),
                            Student("Mark", "Taylor", "S003"),
                        ]

                        order1 = Order(employees[0], students[0], books[:3], "2024-01-10")
                        order2 = Order(employees[1], students[1], books[3:], "2024-01-11")

                        print(order1)
                        print("-" * 40)
                        print(order2)

                        class Property:
                            def __init__(self, area, rooms, price, address):
                                self.area = area
                                self.rooms = rooms
                                self.price = price
                                self.address = address

                                class House(Property):
                                    def __init__(self, area, rooms, price, address, plot):
                                        super().__init__(area, rooms, price, address)
                                        self.plot = plot

                                    def __str__(self):
                                        return (
                                            f"House:\n"
                                            f"  Area: {self.area} m2\n"
                                            f"  Rooms: {self.rooms}\n"
                                            f"  Plot: {self.plot} m2\n"
                                            f"  Price: {self.price}\n"
                                            f"  Address: {self.address}"
                                        )

                                    class Flat(Property):
                                        def __init__(self, area, rooms, price, address, floor):
                                            super().__init__(area, rooms, price, address)
                                            self.floor = floor

                                        def __str__(self):
                                            return (
                                                f"Flat:\n"
                                                f"  Area: {self.area} m2\n"
                                                f"  Rooms: {self.rooms}\n"
                                                f"  Floor: {self.floor}\n"
                                                f"  Price: {self.price}\n"
                                                f"  Address: {self.address}"
                                            )

                                        house = House(120, 5, 850000, "Green St 10", 600)
                                        flat = Flat(60, 3, 450000, "City Center 5", 3)

                                        print(house)
                                        print("-" * 40)
                                        print(flat)