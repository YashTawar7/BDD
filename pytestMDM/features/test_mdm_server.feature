Feature: Add Party Feature

  Scenario: Send PUT request to the endpoint
    Given I have an XML request file "<xml_file>"
    When I send a PUT request to the endpoint
    Then I should receive a valid response
