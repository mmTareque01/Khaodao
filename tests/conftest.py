import pytest
from configuration.Configuration import configuration


@pytest.fixture(scope="class")
def init_driver(request):
    driver = configuration()
    driver.implicitly_wait(10)
    # driver.get()
    request.cls.driver = driver

    yield
    # driver.close()
