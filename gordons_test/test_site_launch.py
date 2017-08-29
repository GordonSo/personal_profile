from .page_objects import home

def test_site_launch(given_a_browser):
    driver = given_a_browser
    home_page = home.HomePage(driver=driver).open()
    assert 'Django' in home_page.get_title()

