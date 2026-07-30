Feature: Inventory Management

Scenario: List products
    Given the inventory contains:
        | Product |
        | Coffee  |
        | Sugar   |
    When the user lists products
    Then the output should contain "Coffee"
    And the output should contain "Sugar"
