from screenpy_selenium import Target
from selenium.webdriver.common.by import By

ADD_TO_CART_BACKPAG_BUTTON = Target.the("add to cart backpag button").located(
    (By.ID, "add-to-cart-sauce-labs-backpack")
)
ADD_TO_CART_BIKE_BUTTON = Target.the("add to cart light button").located(
    (By.ID, "add-to-cart-sauce-labs-bike-light")
)
