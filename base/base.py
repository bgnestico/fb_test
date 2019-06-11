# Base object class declaration for the POM


class Base(object):

    def __init__(self, setup):
        self.driver = setup.web_driver

    # Creates a model to instantiate a web driver
    def get_page(self, url=""):
        self.driver.get(url)
