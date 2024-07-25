from screenpy_selenium import Target
from selenium.webdriver.common.by import By

FIRTS_NAME_INPUT = Target.the("firts name input").located((By.ID, "first-name"))
LAST_NAME_INPUT = Target.the("last name input").located((By.ID, "last-name"))
ZIP_INPUT = Target.the("zip input").located((By.ID, "postal-code"))
CONTINUE_BUTTON = Target.the("continue button").located((By.ID, "continue"))
FINISH_BUTTON = Target.the("finish button").located((By.ID, "finish"))
COMPLETE_ORDER_TEXT = Target.the("complete order text").located(
    (By.CLASS_NAME, "complete-header")
)
