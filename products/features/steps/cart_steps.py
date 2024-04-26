from behave import given, when, then

@given('I am on the product list page')
def step_impl(context):
    context.browser.visit(context.get_url('product_list'))

@when('I click on "Add to cart" for "Product A"')
def step_impl(context):
    context.browser.find_by_text('Add to cart')[0].click()

@then('"Product A" should be added to my cart')
def step_impl(context):
    cart_link = context.browser.find_by_id('cart_link')
    cart_link.click()
    assert "Product A" in context.browser.html
