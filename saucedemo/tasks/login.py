########## ONLY FOR LOCAL CONFIGURATION ##########
import sys
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
folder_a_directory = os.path.abspath(os.path.join(current_directory, os.pardir))
sys.path.append(folder_a_directory)

##################################################

from screenpy import Actor, beat
from screenpy_selenium import Click, Enter

from ui.page_home import LOGIN_BUTTON, PASSWORD_INPUT, USERNAME_INPUT
from utils.constants import PASSWORD, USER


class Login:
    @beat("{} logs in into saucelabs.com")
    def perform_as(self, the_actor: Actor) -> None:
        the_actor.attempts_to(
            Enter.the_text(USER).into_the(USERNAME_INPUT),
            Enter.the_text(PASSWORD).into_the(PASSWORD_INPUT),
            Click.on(LOGIN_BUTTON),
        )
