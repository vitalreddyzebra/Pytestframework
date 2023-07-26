import pytest
from selenium import webdriver
import pytest_html
import pytest_metadata

@pytest.fixture()

def setup(browser):
    if browser=="chrome":
        print("Launching Chrome..........")
        driver=webdriver.Chrome()
    elif browser=="firefox":
        print("Launching Firefox..........")
        driver=webdriver.Firefox()
    else:
        driver = webdriver.Ie()

    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


####################### Pytest HTML reports ###############################

# It is a hook for adding environment info into html report

def pytest_configure(config):
    config._metadata={
        'Project Name' : 'Validator2',
        'Module Name' : 'Customer',
        'Tester' : 'Vital Reddy',

    }
# It is a hook for delete/modify Environment info into html report]

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)


