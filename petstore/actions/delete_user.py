########## ONLY FOR LOCAL CONFIGURATION ##########
import sys
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
folder_a_directory = os.path.abspath(os.path.join(current_directory, os.pardir))
sys.path.append(folder_a_directory)

##################################################

from screenpy import Actor, beat
from screenpy_requests import SendDELETERequest
from utils.endpoints import DELETE_USER, URL


class Delete:

    def __init__(self, user: str) -> None:
        self.user: str = user

    @staticmethod
    def the_user(user: str) -> "Delete":
        return Delete(user)

    @beat("{} deletes the user")
    def perform_as(self, the_actor: Actor) -> None:
        endpoint = URL + DELETE_USER.format(username=self.user)
        the_actor.attempts_to(SendDELETERequest.to(endpoint))
