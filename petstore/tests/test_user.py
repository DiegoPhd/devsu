########## ONLY FOR LOCAL CONFIGURATION ##########
import sys
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
folder_a_directory = os.path.abspath(os.path.join(current_directory, os.pardir))
sys.path.append(folder_a_directory)

##################################################

from http import HTTPStatus
from pytest_bdd import given, scenarios, then, when
from screenpy import AnActor, IsEqualTo, MakeNote, See, SeeAllOf, noted_under
from screenpy_requests import BodyOfTheLastResponse, StatusCodeOfTheLastResponse

from actions.create_user import CreateAUser
from actions.delete_user import Delete
from actions.search_user import Search
from actions.update_user import UpdateAUser
from data.model.request.factory.user_data import User
from data.model.request.user import CreateUserModel
from utils.note_constants import ID, USER


scenarios("../features/user.feature")


@given("a new user")
def a_new_user(Diego: AnActor) -> None:
    Diego.attempts_to(CreateAUser.with_data(User.generate_data_for_creation()))
    Diego.should(See(StatusCodeOfTheLastResponse(), IsEqualTo(HTTPStatus.OK)))


@when("the user is search")
def the_user_is_search(Diego: AnActor) -> None:
    user: CreateUserModel = noted_under(USER)
    Diego.attempts_to(Search.the_user(user.username))
    Diego.should(See(StatusCodeOfTheLastResponse(), IsEqualTo(HTTPStatus.OK)))

    result_user = BodyOfTheLastResponse().answered_by(Diego)
    Diego.attempts_to(MakeNote.of(result_user["id"]).as_(ID))

    print("---------------------")
    print(result_user)
    print("---------------------")
    print(user)
    Diego.should(
        SeeAllOf(
            (result_user["username"], IsEqualTo(user.username)),
            (result_user["firstName"], IsEqualTo(user.firstName)),
            (result_user["lastName"], IsEqualTo(user.lastName)),
            (result_user["email"], IsEqualTo(user.email)),
            (result_user["password"], IsEqualTo(user.password)),
            (result_user["phone"], IsEqualTo(user.phone)),
        )
    )


@when("the user is update")
def the_user_is_update(Diego: AnActor) -> None:
    user: CreateUserModel = noted_under(USER)
    user.id = noted_under(ID)
    Diego.attempts_to(
        UpdateAUser.with_data(
            User.generate_data_for_update(
                id=user.id,
                username=user.username,
                lastName=user.lastName,
                password=user.password,
                phone=user.phone,
            )
        )
    )
    Diego.should(See(StatusCodeOfTheLastResponse(), IsEqualTo(HTTPStatus.OK)))


@when("the user is delete")
def the_user_is_delete(Diego: AnActor) -> None:
    user: CreateUserModel = noted_under(USER)
    Diego.attempts_to(Delete.the_user(user.username))
    Diego.should(See(StatusCodeOfTheLastResponse(), IsEqualTo(HTTPStatus.OK)))


@then("the user should not exist")
def the_user_should_not_exist(Diego: AnActor) -> None:
    user: CreateUserModel = noted_under(USER)
    Diego.attempts_to(Search.the_user(user.username))
    Diego.should(See(StatusCodeOfTheLastResponse(), IsEqualTo(HTTPStatus.NOT_FOUND)))
