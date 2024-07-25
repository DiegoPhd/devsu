from typing import Generator
import pytest

from screenpy import AnActor
from screenpy.pacing import the_narrator
from screenpy_adapter_allure import AllureAdapter
from screenpy_selenium import BrowseTheWeb
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

the_narrator.adapters.append(AllureAdapter())


@pytest.fixture
def Diego() -> Generator:
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.set_window_size(1920, 1080)
    the_actor = AnActor.named("Diego").who_can(BrowseTheWeb.using(driver))
    yield the_actor
    the_actor.exit()
