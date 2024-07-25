from screenpy_selenium import Target
from selenium.webdriver.common.by import By

CHECKOUT_BUTTON = Target.the("checkout button").located((By.ID, "checkout"))
