import time
from playwright.sync_api import expect
from pages.heyflow import HeyFlow
from tests_ui.conftest import current_date_time
from pages.base_page import BasePage

#@pytest.mark.regression
def test_apply_for_job(set_up):
    page = BasePage(set_up)
    frame = HeyFlow(set_up)
    page.accept_cookie_banner()
    page.click_register(set_up)
    page.click_job_finder_link(1)
    frame.heyflow_create_candidate('#hey__iframe-soft_registration_v7_7_qa')
    page.accept_cookie_banner()
    page.navigate_to_jobs()
    page.apply_for_job(set_up)
