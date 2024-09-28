# features/add_party.feature

Feature: addParty
    Add a Party to MDM

Scenario: Add a new party
    Given I have an XML request file "addParty.xml"
    When I send a PUT request to the endpoint
    Then I should receive a valid response
    And I should validate Last_Name is "Lion"
