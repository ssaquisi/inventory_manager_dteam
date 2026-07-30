Feature: Inventory Management

Scenario: Remove product
    Given the inventory contains:
        | Product |
        | Coffee  |
        | Sugar   |
    When the user removes "Coffee"
    Then the inventory should not contain "Coffee"
