Feature: Dropdown

    Scenario Outline: Select menu
        Given I open the "<url>" url
        When I go to "Dropdown" page
        When I select the <item> from the menu
        Then The selected <item> should be visible

        Examples:
            | url                                           | item      |
            | https://the-internet.herokuapp.com            | Option 1  |
 