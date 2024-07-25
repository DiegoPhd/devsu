from screenpy_selenium import Target
from selenium.webdriver.common.by import By

USERNAME_INPUT = Target.the("username input").located((By.ID, "user-name"))
PASSWORD_INPUT = Target.the("password input").located((By.ID, "password"))
LOGIN_BUTTON = Target.the("login button").located((By.ID, "login-button"))