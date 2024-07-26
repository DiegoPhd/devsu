########## ONLY FOR LOCAL CONFIGURATION ##########
import sys
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
folder_a_directory = os.path.abspath(os.path.join(current_directory, os.pardir))
sys.path.append(folder_a_directory)

##################################################

from screenpy import Actor, beat
from screenpy_requests import SendGETRequest
from utils.endpoints import SEARCH_USER, URL


class Search:

    def __init__(self, user: str) -> None:
        self.user: str = user

    @staticmethod
    def the_user(user: str) -> "Search":
        return Search(user)

    @beat("{} searches the user")
    def perform_as(self, the_actor: Actor) -> None:
        endpoint = URL + SEARCH_USER.format(username=self.user)
        the_actor.attempts_to(SendGETRequest.to(endpoint))
