Feature: Download

    Scenario Outline: File download
        Given I open the "<url>" url
        When I go to "Download" page
        Then I select the "<download>" file to download


        Examples:
            | url                                | download      |
            | https://the-internet.herokuapp.com | some-file.txt |
