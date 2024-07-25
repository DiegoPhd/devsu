########## ONLY FOR LOCAL CONFIGURATION ##########
import sys
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
folder_a_directory = os.path.abspath(os.path.join(current_directory, os.pardir))
sys.path.append(folder_a_directory)

##################################################

from pytest_bdd import given, scenarios, then, when
from screenpy import AnActor, ReadsExactly, See
from screenpy_selenium import BrowseTheWeb, Open, Wait
from ui.page_home import LOGIN_BUTTON
from utils.constants import ORDER_COMPLETE, SAUCE_LABS_PAGE, TEN
from ui.page_checkout import (
    COMPLETE_ORDER_TEXT,
)
from tasks.login import Login
from tasks.buy_products import BuyProducts
from questions.the_confirm_order_text import TheConfirmOrderText

scenarios("../features/buy_products.feature")


@given("a user visits saucedemo.com")
def a_user_visits_saucedemo(Diego: AnActor) -> None:
    Diego.attempts_to(Open.browser_on(SAUCE_LABS_PAGE))
    Diego.attempts_to(Wait(TEN).second_for(LOGIN_BUTTON))


@given("the user logs in")
def the_user_logs_in(Diego: AnActor) -> None:
    Diego.attempts_to(Login())


@when("the user buy some products")
def the_user_buy_some_product(Diego: AnActor) -> None:
    Diego.attempts_to(BuyProducts())


@then("the user should see the order confirmation")
def the_user_should_see_the_order_confirmation(Diego: AnActor) -> None:
    Diego.attempts_to(Wait(TEN).second_for(COMPLETE_ORDER_TEXT))
    Diego.should(See.the(TheConfirmOrderText(), ReadsExactly(ORDER_COMPLETE)))
    Diego.ability_to(BrowseTheWeb).browser.close()
    Diego.exit_stage_left()
