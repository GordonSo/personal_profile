class BasePage():
    _driver = None
    _uri = None

    def __init__(self, driver, uri):
        self._driver = driver
        self._uri = uri

    def open(self):
        self._driver.get("localhost:8080\{uri}".format(uri=self._uri))
        return self

    def get_title(self):
        return self._driver.title

