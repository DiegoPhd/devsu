########## ONLY FOR LOCAL CONFIGURATION ##########
import sys
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
folder_a_directory = os.path.abspath(os.path.join(current_directory, os.pardir))
sys.path.append(folder_a_directory)

##################################################

from faker import Faker
from data.model.request.user import CreateUserModel, UpdateUserModel


class User:
    @staticmethod
    def generate_data_for_creation() -> CreateUserModel:
        fake = Faker()
        return CreateUserModel(
            username=fake.user_name(),
            firstName=fake.first_name(),
            lastName=fake.last_name(),
            email=fake.email(),
            password=fake.password(),
            phone=fake.phone_number(),
        )

    @staticmethod
    def generate_data_for_update(
        id: int, username: str, lastName: str, password: str, phone: str
    ) -> UpdateUserModel:
        fake = Faker()
        return UpdateUserModel(
            id=id,
            username=username,
            firstName=fake.first_name(),
            lastName=lastName,
            email=fake.email(),
            password=password,
            phone=phone,
        )
