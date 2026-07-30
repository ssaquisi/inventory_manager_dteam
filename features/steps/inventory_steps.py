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
