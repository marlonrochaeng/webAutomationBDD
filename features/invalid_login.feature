Feature: Login

    Scenario Outline: Invalid Login
        Given I open the "<url>" url
        When I go to "Login" page
        When I do the valid login with credentials "<username>" and "<password>"
        Then I should not be logged in
        Examples:
            | url                                           | username           | password                  |
            | https://the-internet.herokuapp.com            | tomsmith2          | SuperSecretPassword!2     |
