import pytest
from selenium import webdriver
from base.webdriverfactory import WebDriverFactory

@pytest.yield_fixture()
def setUp():
    print("Running method level setUp")
    yield
    print(" Running method level tearDown")


# @pytest.yield_fixture(scope="module")
@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser, website, osType, country):
    print("Running one time setUp")
    wdf = WebDriverFactory(browser, website)
    driver = wdf.getWebDriverInstance()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running one time tearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")
    parser.addoption("--country")
    parser.addoption("--website")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")

@pytest.fixture(scope="session")
def country(request):
    return request.config.getoption("--country")

@pytest.fixture(scope="session")
def website(request):
    return request.config.getoption("--website")
