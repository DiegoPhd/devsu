from faker import Faker
from petstore.data.model.request.user import CreateUser, UpdateUser


class User:
    @staticmethod
    def generate_data_for_creation() -> CreateUser:
        fake = Faker()
        return CreateUser(
            username=fake.user_name(),
            firtsName=fake.first_name(),
            lastName=fake.last_name(),
            email=fake.email(),
            password=fake.password(),
            phone=fake.phone_number(),
        )

    @staticmethod
    def generate_data_for_update(username: str) -> UpdateUser:
        fake = Faker()
        return UpdateUser(
            username=username,
            firtsName=fake.first_name(),
            lastName=fake.last_name(),
            email=fake.email(),
            password=fake.password(),
            phone=fake.phone_number(),
        )
