Feature: User

    Scenario: Create, update and delete a user
        Given a new user
        When the user is search
        And the user is update
        And the user is search
        And the user is delete
        Then the user should not exist
