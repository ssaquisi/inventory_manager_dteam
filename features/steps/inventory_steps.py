from behave import given, when, then

@given('the inventory is empty')
def step_impl(context):
    context.inventory = {}
    context.output = ""

@when('the user adds product "{product}"')
def step_impl(context, product):
    context.inventory[product] = 0

@then('the inventory should contain "{product}"')
def step_impl(context, product):
    assert product in context.inventory, \
        f'{product} was not found in the inventory'

@given('the inventory contains:')
def step_impl(context):
    context.inventory = {}

    for row in context.table:
        product = row["Product"]

        if "Quantity" in row.headings:
            quantity = int(row["Quantity"])
        else:
            quantity = 0

        context.inventory[product] = quantity

    context.output = ""

@when('the user updates "{product}" to quantity "{quantity}"')
def step_impl(context, product, quantity):
    if product in context.inventory:
        context.inventory[product] = int(quantity)

@then('product "{product}" should have quantity "{quantity}"')
def step_impl(context, product, quantity):
    assert product in context.inventory, \
        f'{product} was not found'

    assert context.inventory[product] == int(quantity), \
        f'Expected quantity {quantity} but got {context.inventory[product]}'