import sys
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
folder_a_directory = os.path.abspath(os.path.join(current_directory, os.pardir))
sys.path.append(folder_a_directory)

from pytest_bdd import given, scenarios, then, when
from screenpy import AnActor, Pause
from screenpy_selenium import BrowseTheWeb, Click, Enter, Open, Wait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from ui.page_home import LOGIN_BUTTON, PASSWORD_INPUT, USERNAME_INPUT
from utils.constants import PASSWORD, TEN, USER


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
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
    the_actor.attempts_to(Pause.for_(TEN).second_because("yes"))


@when("the user buy some products")
def the_user_buy_some_product() -> None:
    b = 1


@then("the user should see the order confirmation")
def the_user_should_see_the_order_confirmation() -> None:
    c = 1
