Feature: Inventory Management

Scenario: Add a product
    Given the inventory is empty
    When the user adds product "Coffee"
    Then the inventory should contain "Coffee"
