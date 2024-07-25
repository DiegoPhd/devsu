########## ONLY FOR LOCAL CONFIGURATION ##########
import sys
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
folder_a_directory = os.path.abspath(os.path.join(current_directory, os.pardir))
sys.path.append(folder_a_directory)

##################################################

from screenpy import Actor, beat

from ui.page_checkout import COMPLETE_ORDER_TEXT


class TheConfirmOrderText:

    @beat("{} reads the confirm order text")
    def answered_by(self, the_actor: Actor) -> str:
        return COMPLETE_ORDER_TEXT.found_by(the_actor).text
