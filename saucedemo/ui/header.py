from screenpy_selenium import Target
from selenium.webdriver.common.by import By

SHOPPING_CART_BUTTON = Target.the("shopping cart button").located(
    (By.ID, "shopping_cart_container")
)
