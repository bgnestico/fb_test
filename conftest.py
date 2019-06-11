import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def setup(request):
    web_driver = webdriver.Chrome()
    request.driver = web_driver
    yield
    web_driver.close()
