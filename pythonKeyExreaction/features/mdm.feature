# features/mdm.feature

Feature: MDM Integration
  Scenario: Send XML Request to MDM
    Given I have an XML request
    When I send the XML request to MDM
    Then I should receive a valid response
