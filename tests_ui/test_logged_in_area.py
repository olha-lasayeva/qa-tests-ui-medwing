import time
from pytest_playwright.pytest_playwright import new_context
from pages.heyflow import HeyFlow
from pages.base_page import BasePage
from pages.logged_in_area import LoggedInArea

#@pytest.mark.regression
#TODO: Activate when heyflow test is updated to the uptodate version
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

#@pytest.mark.regression
def test_login_existing_user(set_up):
    base_page = BasePage(set_up)
    base_page.login_existing_user(set_up)

def test_profile_info_update(set_up):
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
    base_page = BasePage(set_up)
    logged_in_area = LoggedInArea(set_up)
    base_page.login_existing_user(set_up)
    logged_in_area.click_navi_side_link_settings()
    logged_in_area.verify_h1_text_settings("Settings", 1)
    logged_in_area.click_navi_side_link_dashboard()
    logged_in_area.verify_h1_text(0, "Welcome")
    logged_in_area.click_navi_side_link_jobs()
    logged_in_area.verify_h3_text("jobs found", 0)
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

def test_profile_add_work_experience(set_up):
    page = set_up
    base_page = BasePage(set_up)
    logged_in_area = LoggedInArea(set_up)
    base_page.login_existing_user(set_up)
    page.wait_for_load_state(timeout='networkidle')
    logged_in_area.click_navi_side_link_profile()
    #page.wait_for_load_state(timeout='networkidle')
    logged_in_area.add_work_experience()
    page.wait_for_load_state(timeout='networkidle')

def test_profile_add_education(set_up):
    page = set_up
    base_page = BasePage(set_up)
    logged_in_area = LoggedInArea(set_up)
    base_page.login_existing_user(set_up)
    page.wait_for_load_state(timeout='networkidle')
    logged_in_area.click_navi_side_link_profile()
    logged_in_area.add_candidate_education()
    page.wait_for_load_state(timeout='networkidle')

def test_profile_add_motivation(set_up):
    page = set_up
    base_page = BasePage(set_up)
    logged_in_area = LoggedInArea(set_up)
    base_page.login_existing_user(set_up)
    page.wait_for_load_state(timeout='networkidle')
    logged_in_area.click_navi_side_link_profile()
    logged_in_area.add_candidate_motivation()

def test_settings_logout(set_up):
    page = set_up
    base_page = BasePage(set_up)
    logged_in_area = LoggedInArea(set_up)
    base_page.login_existing_user(set_up)
    page.wait_for_load_state(timeout='networkidle')
    logged_in_area.click_navi_side_link_settings()
    logged_in_area.logout()

def test_preferences_work_location(set_up):
    page = set_up
    base_page = BasePage(set_up)
    logged_in_area = LoggedInArea(set_up)
    base_page.login_existing_user(set_up)
    page.wait_for_load_state(timeout='networkidle')
    logged_in_area.click_navi_side_link_profile()
    logged_in_area.click_edit_work_location()
    logged_in_area.verify_location_toggle()
    logged_in_area.get_work_location()

def test_preferences_facility_types(set_up):
    page = set_up
    base_page = BasePage(set_up)
    logged_in_area = LoggedInArea(set_up)
    base_page.login_existing_user(set_up)
    page.wait_for_load_state(timeout='networkidle')
    logged_in_area.click_navi_side_link_profile()
    logged_in_area.click_edit_facility_types()
    logged_in_area.verify_update_facility_types()
    page.wait_for_load_state('networkidle')   # need to wait till the results are saved after clicking Submit

def test_preferences_departments(set_up):
    page = set_up
    base_page = BasePage(set_up)
    logged_in_area = LoggedInArea(set_up)
    base_page.login_existing_user(set_up)
    page.wait_for_load_state(timeout='networkidle')
    logged_in_area.click_navi_side_link_profile()
    logged_in_area.click_add_departments()
    logged_in_area.verify_update_departments()

def test_preferences_contract_type(set_up):
    page = set_up
    base_page = BasePage(set_up)
    logged_in_area = LoggedInArea(set_up)
    base_page.login_existing_user(set_up)
    page.wait_for_load_state(timeout='networkidle')
    logged_in_area.click_navi_side_link_profile()
    logged_in_area.click_edit_contract_type()
    logged_in_area.update_contract_type()

def est_preferences_working_hours():
    pass
    # TODO

def est_preferences_shifts():
    pass
    # TODO

def test_preferences_available_from(set_up):
    page = set_up
    base_page = BasePage(set_up)
    logged_in_area = LoggedInArea(set_up)
    base_page.login_existing_user(set_up)
    page.wait_for_load_state(timeout='networkidle')
    logged_in_area.click_navi_side_link_profile()
    logged_in_area.click_edit_available_from()
    logged_in_area.verify_available_from()
    logged_in_area.click_edit_available_from()
    logged_in_area.verify_notice_period()
    logged_in_area.check_form_checkbox()
    logged_in_area.click_form_button_submit()
