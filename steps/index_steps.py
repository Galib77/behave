from behave import given, when, then
from app import index

@given('the application is running')
def step_given_application_running(context):
    pass

@when('I call the index function')
def step_when_call_index_function(context):
    context.result = index()

@then('it should return "Hello, world!"')
def step_then_should_return_hello(context):
    assert context.result == "Hello, world!"
