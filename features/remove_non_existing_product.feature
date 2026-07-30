Feature: Inventory Management

Scenario: Remove non-existing product
    Given the inventory is empty
    When the user removes "Coffee"
    Then the output should be "Product Coffee was not found"
