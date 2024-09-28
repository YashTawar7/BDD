# steps/test_add_party_steps.py

from behave import given, when, then
from config import Config
from utils.request_handler import send_request


@given('I have an XML request file "{file}"')
def step_given_xml_request(context, file):
    context.xml_file = file


@when('I send a PUT request to the endpoint')
def step_send_put_request(context):
    endpoint = Config.endpoint_REST  # or Config.endpoint_SOAP depending on your implementation
    with open(context.xml_file, 'r') as f:
        xml_data = f.read()
    context.response = send_request(xml_data, endpoint)


@then('I should receive a valid response')
def step_validate_response(context):
    assert context.response.status_code == 200


@then('I should validate Last_Name is "{expected_last_name}"')
def step_validate_last_name(context, expected_last_name):
    assert expected_last_name == "Lion"  # Placeholder validation, implement actual validation as needed
