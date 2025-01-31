import re
import time
from playwright.sync_api import expect
from pytest_playwright.pytest_playwright import new_context
from pages.heyflow import HeyFlow
from pages.base_page import BasePage
from pages.logged_in_area import LoggedInArea

#@pytest.mark.regression
def est_apply_for_job(set_up):
    page = BasePage(set_up)
    frame = HeyFlow(set_up)
    page.accept_cookie_banner()
    page.click_register(set_up)
    page.click_job_finder_link(1)
    frame.heyflow_create_candidate_v7_7('#hey__iframe-soft_registration_v7_6_qa')
    page.accept_cookie_banner()
    page.navigate_to_jobs()
    page.apply_for_job(set_up)

def test_login_existing_user(set_up):
    page = BasePage(set_up)
    page.accept_cookie_banner()
    logged_in_area = LoggedInArea(set_up)
    page.goto_url(set_up, "https://my.mdwng.dev/auth/login")
    page.accept_cookie_banner()
    #TODO: use fixtures to get the credentials
    logged_in_area.enter_email("testautomations+2024test@medwing.com")
    logged_in_area.enter_password("Med1205+")
    logged_in_area.click_form_button_submit()
    time.sleep(2)
    logged_in_area.verify_h4_text(0, "Your Profile is almost ready")

def test_update_profile_info(set_up):
    page = set_up
    base_page = BasePage(set_up)
    logged_in_area = LoggedInArea(set_up)
    base_page.login_existing_user(set_up)
    page.wait_for_load_state(timeout='networkidle')
    logged_in_area.click_navi_side_link_profile()
    page.wait_for_load_state(timeout='networkidle')
    logged_in_area.click_edit_personal_details(set_up)
    logged_in_area.form_update_input_fields(set_up)
    logged_in_area.form_update_birth_date()

def test_navigation(set_up):
    page = set_up
    base_page = BasePage(set_up)
    logged_in_area = LoggedInArea(set_up)
    base_page.login_existing_user(set_up)
    page.wait_for_load_state(timeout='networkidle')
    logged_in_area.click_navi_side_link_settings()
    logged_in_area.verify_h1_text_settings("Settings", 1)
    logged_in_area.click_navi_side_link_dashboard()
    logged_in_area.verify_h1_text(0, re.compile(r"Welcome .*"))
    logged_in_area.click_navi_side_link_profile()
    logged_in_area.verify_h1_text(0, "Profile")
    logged_in_area.click_navi_side_link_jobs()
    expect(logged_in_area.verify_h1_text(0, re.compile(r"Welcome .*"))).not_to_be_visible()
    logged_in_area.click_navi_side_link_applications()
    logged_in_area.verify_h1_text(0, "Applications")
    logged_in_area.click_navi_side_link_messenger()
    logged_in_area.verify_h2_text("Messages")

def test_settings_change_language(set_up):
    page = set_up
    base_page = BasePage(set_up)
    logged_in_area = LoggedInArea(set_up)
    base_page.login_existing_user(set_up)
    page.wait_for_load_state(timeout='networkidle')
    logged_in_area.click_navi_side_link_settings()
    logged_in_area.change_language_german()
    page.wait_for_load_state('networkidle')
    page.reload()
    page.wait_for_load_state('networkidle')
    logged_in_area.verify_h1_text_settings("Einstellungen", 1)

def test_add_work_experience(set_up):
    page = set_up
    base_page = BasePage(set_up)
    logged_in_area = LoggedInArea(set_up)
    base_page.login_existing_user(set_up)
    page.wait_for_load_state(timeout='networkidle')
    logged_in_area.click_navi_side_link_profile()
    page.wait_for_load_state(timeout='networkidle')
    logged_in_area.add_work_experience()

def test_add_education(set_up):
    page = set_up
    base_page = BasePage(set_up)
    logged_in_area = LoggedInArea(set_up)
    base_page.login_existing_user(set_up)
    page.wait_for_load_state(timeout='networkidle')
    logged_in_area.click_navi_side_link_profile()
    logged_in_area.add_candidate_education()

def test_add_motivation(set_up):
    page = set_up
    base_page = BasePage(set_up)
    logged_in_area = LoggedInArea(set_up)
    base_page.login_existing_user(set_up)
    page.wait_for_load_state(timeout='networkidle')
    logged_in_area.click_navi_side_link_profile()
    logged_in_area.add_candidate_motivation()

def test_logout(set_up):
    page = set_up
    base_page = BasePage(set_up)
    logged_in_area = LoggedInArea(set_up)
    base_page.login_existing_user(set_up)
    page.wait_for_load_state(timeout='networkidle')
    logged_in_area.click_navi_side_link_settings()
    logged_in_area.logout()
