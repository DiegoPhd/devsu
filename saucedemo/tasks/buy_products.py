########## ONLY FOR LOCAL CONFIGURATION ##########
import sys
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
folder_a_directory = os.path.abspath(os.path.join(current_directory, os.pardir))
sys.path.append(folder_a_directory)

##################################################

from screenpy import Actor, beat
from screenpy_selenium import Click, Wait
from ui.header import SHOPPING_CART_BUTTON
from ui.page_cart import CHECKOUT_BUTTON
from ui.page_checkout import (
    CONTINUE_BUTTON,
    FINISH_BUTTON,
)
from ui.page_inventory import (
    ADD_TO_CART_BACKPAG_BUTTON,
    ADD_TO_CART_BIKE_BUTTON,
)
from utils.constants import TEN
from actions.add_product import Add
from data.factory.payer_data import Payer
from tasks.complete import Complete

class BuyProducts:

    @beat("{} buy some products")
    def perform_as(self, the_actor: Actor) -> None:
        the_actor.attempts_to(Wait(TEN).second_for(ADD_TO_CART_BACKPAG_BUTTON))
        the_actor.attempts_to(
            Add.the_product(ADD_TO_CART_BACKPAG_BUTTON),
            Add.the_product(ADD_TO_CART_BIKE_BUTTON),
        )
        the_actor.attempts_to(
            Click.on(SHOPPING_CART_BUTTON),
            Wait(TEN).second_for(CHECKOUT_BUTTON),
            Click.on(CHECKOUT_BUTTON),
            Wait(TEN).second_for(CONTINUE_BUTTON),
        )
        the_actor.tries_to(Complete.the_checkout_form(Payer.generate_data()))
        the_actor.attempts_to(
            Click.on(CONTINUE_BUTTON),
            Wait(TEN).second_for(FINISH_BUTTON),
            Click.on(FINISH_BUTTON),
        )
