class User:
    # переменные класса
    user_count = 0
    default_password = "123456789"

    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
        self.password = User.default_password
        User.user_count += 1

    def test(self):
        print(self.name, "test")

    @classmethod
    def create_user(cls, name, phone_number):
        if not User.validate_phone(phone_number):
            raise ValueError("неправильный номер телефона")
        new_user = cls(name, phone_number)
        return new_user

    @classmethod
    def get_user_count(cls):
        return User.user_count

    @staticmethod
    def validate_phone(phone):
        if phone.isdigit():
            return True
        return False

print("Количество юзеров", User.user_count)
user_1 = User("Игорь", "996555000001")
print("Количество юзеров", User.user_count)
print(user_1.password)
User.default_password = "qwerty"
user_2 = User("Курманбек", "996555000002")
print(user_2.password)
user_3 = User.create_user("Дастан", "996555000003")
print(user_3.name, user_3.password, user_3.phone_number)
print("Количество юзеров", User.get_user_count())
