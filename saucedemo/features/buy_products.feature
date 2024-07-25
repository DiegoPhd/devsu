Feature: Buy some products in saucedemo.com

    Scenario: Buy products
        Given a user visits saucedemo.com
        And the user logs in
        When the user buy some products
        Then the user should see the order confirmation