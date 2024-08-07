import pytest
from web_agent import WebAgent

@pytest.fixture(scope="module")
def agent():
    # Initialize the helper
    agent = WebAgent()
    yield agent
    agent.close_browser()
    
    

def test_login(agent):
    """Test login functionality"""
    # Open the website
    agent.navigate_to("https://app.digemp.net/")

    # Log in to the website
    agent.enter_input_value(WebAgent.SELECTOR.ID, "email", "admin.owner@mailinator.com")
    agent.enter_input_value(WebAgent.SELECTOR.ID,  "password", "click123")
    agent.click_button(WebAgent.SELECTOR.CSS,  "div.login-box button[type='submit']", wait=3)

def test_navigate_to_user_page(agent):
    """Test navigation to user page"""
    # Navigate to the user insertion page
    agent.navigate_to("https://app.digemp.net/admin/user")
    # Insert user details
    agent.click_button(WebAgent.SELECTOR.CSS, "#user-list-view .jDataTable-form-button", wait=3)

def test_insert_user_details(agent):
    """Test inserting user details"""
    # Navigate to the user insertion page
    agent.navigate_to("https://app.digemp.net/admin/user")
    # Insert user details
    agent.click_button(WebAgent.SELECTOR.CSS, "#user-list-view .jDataTable-form-button", wait=3)
    
    # Click on the anchor tag to show the password fields
    agent.click_button(WebAgent.SELECTOR.CSS, "a[href='#tab-user-general']", wait=2)

    name = agent.enter_input_value(WebAgent.SELECTOR.ID, "name", agent.generate_name())
    email = agent.enter_input_value(WebAgent.SELECTOR.ID, "email", agent.generate_email())
    roles = agent.select_dropdown_value(WebAgent.SELECTOR.NAME, "roles[]", select_count=2)
    agent.wait(1)

    # Click on the anchor tag to show the password fields
    agent.click_button(WebAgent.SELECTOR.CSS, "a[href='#tab-user-security']")

    # Add password to the password field and password confirmation field
    password_value = "click123"
    password = agent.enter_input_value(WebAgent.SELECTOR.ID, "password", password_value)
    confirm_password = agent.enter_input_value(WebAgent.SELECTOR.ID, "password_confirmation", password_value)
    agent.wait(1)

    # Click on the anchor tag to show the password fields
    agent.click_button(WebAgent.SELECTOR.CSS, "a[href='#tab-user-detail']")

    # Select a random option from the select element with ID "user_group_id"
    user_group = agent.select_dropdown_value(WebAgent.SELECTOR.ID, "user_group_id", select_count=1)

    # Select a random option from the select element with ID "department_head"
    department_head = agent.select_dropdown_value(WebAgent.SELECTOR.ID, "department_head", select_count=1)

    # Select a random option from the select element with ID "supervisor_id"
    supervisor = agent.select_dropdown_value(WebAgent.SELECTOR.ID, "supervisor_id", select_count=1)

    # Wait for the page to load
    agent.wait(2)

    # Submit the form
    agent.click_button(WebAgent.SELECTOR.CSS, "#user-modal button[type='submit']")

    # Wait for the page to load
    agent.wait(10)
