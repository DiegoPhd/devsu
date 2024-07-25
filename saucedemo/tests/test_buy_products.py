########## ONLY FOR LOCAL CONFIGURATION ##########
import sys
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
folder_a_directory = os.path.abspath(os.path.join(current_directory, os.pardir))
sys.path.append(folder_a_directory)

##################################################

from pytest_bdd import given, scenarios, then, when
from screenpy import AnActor, ReadsExactly, See
from screenpy_selenium import BrowseTheWeb, Click, Enter, Open, Text, Wait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from ui.page_home import LOGIN_BUTTON, PASSWORD_INPUT, USERNAME_INPUT
from ui.page_inventory import ADD_TO_CART_BACKPAG_BUTTON, ADD_TO_CART_BIKE_BUTTON
from utils.constants import ORDER_COMPLETE, PASSWORD, TEN, USER
from data.factory.payer_data import Payer
from data.model.payer_data_model import PayerData
from ui.page_checkout import (
    COMPLETE_ORDER_TEXT,
    CONTINUE_BUTTON,
    FINISH_BUTTON,
    FIRTS_NAME_INPUT,
    LAST_NAME_INPUT,
    ZIP_INPUT,
)
from ui.header import SHOPPING_CART_BUTTON
from ui.page_cart import CHECKOUT_BUTTON

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.set_window_size(1920, 1080)
the_actor = AnActor.named("Diego").who_can(BrowseTheWeb.using(driver))

scenarios("../features/buy_products.feature")


@given("a user visits saucedemo.com")
def a_user_visits_saucedemo() -> None:
    the_actor.attempts_to(Open.browser_on("https://www.saucedemo.com/"))
    the_actor.attempts_to(Wait(TEN).second_for(LOGIN_BUTTON))


@given("the user logs in")
def the_user_logs_in() -> None:
    the_actor.attempts_to(Enter.the_text(USER).into_the(USERNAME_INPUT))
    the_actor.attempts_to(Enter.the_text(PASSWORD).into_the(PASSWORD_INPUT))
    the_actor.attempts_to(Click.on(LOGIN_BUTTON))


@when("the user buy some products")
def the_user_buy_some_product() -> None:
    the_actor.attempts_to(Wait(TEN).second_for(ADD_TO_CART_BACKPAG_BUTTON))
    the_actor.attempts_to(Click.on(ADD_TO_CART_BACKPAG_BUTTON))
    the_actor.attempts_to(Click.on(ADD_TO_CART_BIKE_BUTTON))
    the_actor.attempts_to(Click.on(SHOPPING_CART_BUTTON))
    the_actor.attempts_to(Wait(TEN).second_for(CHECKOUT_BUTTON))
    the_actor.attempts_to(Click.on(CHECKOUT_BUTTON))
    the_actor.attempts_to(Wait(TEN).second_for(CONTINUE_BUTTON))
    payer_data: PayerData = Payer.generate_data()
    the_actor.attempts_to(
        Enter.the_text(payer_data.firts_name).into_the(FIRTS_NAME_INPUT)
    )
    the_actor.attempts_to(
        Enter.the_text(payer_data.last_name).into_the(LAST_NAME_INPUT)
    )
    the_actor.attempts_to(Enter.the_text(payer_data.zip_code).into_the(ZIP_INPUT))
    the_actor.attempts_to(Click.on(CONTINUE_BUTTON))
    the_actor.attempts_to(Wait(TEN).second_for(FINISH_BUTTON))
    the_actor.attempts_to(Click.on(FINISH_BUTTON))


@then("the user should see the order confirmation")
def the_user_should_see_the_order_confirmation() -> None:
    the_actor.attempts_to(Wait(TEN).second_for(COMPLETE_ORDER_TEXT))
    the_actor.should(
        See.the(Text.of(COMPLETE_ORDER_TEXT), ReadsExactly(ORDER_COMPLETE))
    )
    driver.quit()
