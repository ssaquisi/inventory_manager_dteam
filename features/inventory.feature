Feature: Inventory Management

Scenario: Add a product
    Given the inventory is empty
    When the user adds product "Coffee"
    Then the inventory should contain "Coffee"

Scenario: List products
    Given the inventory contains:
        | Product |
        | Coffee  |
        | Sugar   |
    When the user lists products
    Then the output should contain "Coffee"
    And the output should contain "Sugar"

Scenario: Update quantity
    Given the inventory contains:
        | Product | Quantity |
        | Coffee  | 10       |
    When the user updates "Coffee" to quantity "25"
    Then product "Coffee" should have quantity "25"

Scenario: Remove product
    Given the inventory contains:
        | Product |
        | Coffee  |
        | Sugar   |
    When the user removes "Coffee"
    Then the inventory should not contain "Coffee"

Scenario: Remove non-existing product
    Given the inventory is empty
    When the user removes "Coffee"
    Then the output should be "Product Coffee was not found"