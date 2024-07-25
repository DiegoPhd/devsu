########## ONLY FOR LOCAL CONFIGURATION ##########
import sys
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
folder_a_directory = os.path.abspath(os.path.join(current_directory, os.pardir))
sys.path.append(folder_a_directory)

##################################################

from data.model.payer_data_model import PayerData
from faker import Faker


class Payer:
    @staticmethod
    def generate_data() -> PayerData:
        fake = Faker()
        return PayerData(
            firts_name=fake.name(), last_name=fake.last_name(), zip_code=fake.zipcode()
        )
