########## ONLY FOR LOCAL CONFIGURATION ##########
import sys
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
folder_a_directory = os.path.abspath(os.path.join(current_directory, os.pardir))
sys.path.append(folder_a_directory)

##################################################

from screenpy import Actor, MakeNote, beat
from screenpy_requests import SendPUTRequest
from data.model.request.user import UpdateUserModel
from utils.endpoints import UPDATE_USER, URL
from utils.note_constants import USER


class UpdateAUser:

    def __init__(self, user: UpdateUserModel) -> None:
        self.user: UpdateUserModel = user

    @staticmethod
    def with_data(user: UpdateUserModel) -> "UpdateAUser":
        return UpdateAUser(user)

    @beat("{} updates the user")
    def perform_as(self, the_actor: Actor) -> None:
        endpoint = URL + UPDATE_USER.format(username=self.user)
        the_actor.attempts_to(
            SendPUTRequest.to(endpoint).with_(json=self.user.__dict__)
        )
        the_actor.attempts_to(MakeNote.of(self.user).as_(USER))
