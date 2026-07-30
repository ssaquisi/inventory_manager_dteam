Feature: Inventory Management

Scenario: Update quantity
    Given the inventory contains:
        | Product | Quantity |
        | Coffee  | 10       |
    When the user updates "Coffee" to quantity "25"
    Then product "Coffee" should have quantity "25"
