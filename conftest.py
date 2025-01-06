from _pydatetime import datetime
import pytest
#from configuration.config import medwing_web_config as cfg

headless_bool = True
slowmo_value = 300

current_date_time = datetime.now().strftime('%Y%m%d-%H%M%S')

@pytest.fixture(scope='session')
def context_creation(playwright):
    browser = playwright.chromium.launch(headless=headless_bool, slow_mo=slowmo_value)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://my.mdwng.dev")
    page.set_default_timeout(3000)

@pytest.fixture
def set_up(context_creation, browser):
    #context = browser.new_context(storage_state="state.json")
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://mdwng.dev")
    #page.goto(cfg.qa('base_url'))
    page.set_default_timeout(3000)

    yield page
    page.close()

@pytest.fixture
def url_set_up(page):
    page.goto("https://mdwng.dev/")
    page.locator("//*[@id='onetrust-policy-title']").click()
    page.locator("//button[@id='onetrust-accept-btn-handler']").click()

    yield page
    page.close()
