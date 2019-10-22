Feature: Alerts

    Scenario Outline: Dealing with alerts
        Given I open the "<url>" url
        When I go to "Alerts" page
        When I click on the first alert
        And I accept the alert
        Then Should be possible to click on the second alert
        And I accept the alert
        Examples:
            | url                                |
            | https://the-internet.herokuapp.com |
