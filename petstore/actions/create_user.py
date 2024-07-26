########## ONLY FOR LOCAL CONFIGURATION ##########
import sys
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
folder_a_directory = os.path.abspath(os.path.join(current_directory, os.pardir))
sys.path.append(folder_a_directory)

##################################################

from screenpy import Actor, MakeNote, beat
from screenpy_requests import SendPOSTRequest
from data.model.request.user import CreateUserModel
from utils.endpoints import CREATE_USER, URL
from utils.note_constants import USER


class CreateAUser:

    def __init__(self, user: CreateUserModel) -> None:
        self.user: CreateUserModel = user

    @staticmethod
    def with_data(user: CreateUserModel) -> "CreateAUser":
        return CreateAUser(user)

    @beat("{} creates a new user")
    def perform_as(self, the_actor: Actor) -> None:
        endpoint = URL + CREATE_USER
        the_actor.attempts_to(
            SendPOSTRequest.to(endpoint).with_(json=self.user.__dict__)
        )
        the_actor.attempts_to(MakeNote.of(self.user).as_(USER))
