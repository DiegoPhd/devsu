from typing import Generator
import pytest

from screenpy import AnActor
from screenpy.pacing import the_narrator
from screenpy_adapter_allure import AllureAdapter
from screenpy_requests import MakeAPIRequests

the_narrator.adapters.append(AllureAdapter())


@pytest.fixture
def Diego() -> Generator:
    the_actor = AnActor.named("Diego").who_can(MakeAPIRequests())
    yield the_actor
    the_actor.exit()
