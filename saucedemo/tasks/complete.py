########## ONLY FOR LOCAL CONFIGURATION ##########
import sys
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
folder_a_directory = os.path.abspath(os.path.join(current_directory, os.pardir))
sys.path.append(folder_a_directory)

##################################################

from screenpy import Actor, beat
from screenpy_selenium import Enter
from data.model.payer_data_model import PayerData
from ui.page_checkout import FIRTS_NAME_INPUT, LAST_NAME_INPUT, ZIP_INPUT


class Complete:
    def __init__(self, payer_data: PayerData) -> None:
        self.payer_data: PayerData = payer_data

    @staticmethod
    def the_checkout_form(payer_data: PayerData) -> "Complete":
        return Complete(payer_data)

    @beat("{} complete the checkout form")
    def perform_as(self, the_actor: Actor) -> None:
        the_actor.attempts_to(
            Enter.the_text(self.payer_data.firts_name).into_the(FIRTS_NAME_INPUT)
        )
        the_actor.attempts_to(
            Enter.the_text(self.payer_data.last_name).into_the(LAST_NAME_INPUT)
        )
        the_actor.attempts_to(
            Enter.the_text(self.payer_data.zip_code).into_the(ZIP_INPUT)
        )
