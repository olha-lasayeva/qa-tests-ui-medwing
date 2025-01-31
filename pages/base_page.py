import time
import pytest
from playwright.sync_api import expect
from conftest import set_up
from pages.logged_in_area import LoggedInArea


class BasePage:

    def __init__(self, page):

        self.element_name = None
        self.cookie_banner_title = page.locator("//*[@id='onetrust-policy-title']")
        self.cookie_banner_accept = page.locator("//button[@id='onetrust-accept-btn-handler']")

        self.register_button = page.locator("//*[@class='fbl-nav-button-1']//a")
        self.job_finder_link = page.locator("//*[@data-cy='link-box']")
        self.side_navigation_links = page.locator("//nav//li//a")
        self.button_apply = page.locator("//a[@data-id='job-recommendations-apply']")

        #apply for job form
        self.form_input = page.locator("//form//input")
        self.form_submit = page.locator("//button[@type='submit']")
        self.form_button = page.get_by_role("button")
        self.form_phone = page.locator("//*[@name='phone']")
        self.form_experience = page.locator("//*[@id='years-of-experience']")
        self.form_experience_years = page.locator("//ul//li[@data-value]")
        self.form_shifts = page.locator("//*[@name='shift']")
        self.date_picker_value = page.locator("//*[contains(@class, 'MuiDialog-root')]//button")
        self.date_picker_submit = page.locator("'OK'")
        self.form_education = page.locator("//*[@id='mui-component-select-relevantEducation']")
        self.form_education_select = page.locator("//ul//li[@data-value='basic_nursing_course']")
        self.form_work_experience = page.locator(
            "//*[contains(@class, 'MuiDialogContent-root')]//button[@type='button']"
        )

        #heyflow
        self.heyflow_id = page.locator("#hey__iframe-soft_registration_v7_7_qa")

# Common functions
    def goto_url(self, set_up, url) -> None:
        page = set_up
        page.goto(url)

    def accept_cookie_banner(self):
        expect(self.cookie_banner_title).to_be_visible()
        self.cookie_banner_accept.click()

    def click_register(self, set_up):
        page = set_up
        self.register_button.nth(-1).click()
        #NOTE: currently on qa env the same heyflow variant for a and b
        if (page.url == "https://medwing.com/de/de/a/job-finder/job_kind" or
                page.url == "https://medwing.com/de/de/b/job-finder/job_kind"):
            page.goto("https://mdwng.dev/de/de/b/job-finder/job_kind")
            self.accept_cookie_banner()

    def click_job_finder_link(self, n):
        self.job_finder_link.nth(n).click()

    def navigate_to_jobs(self):
        self.side_navigation_links.nth(2).click()

    def apply_for_job(self, set_up):
        page = set_up
        self.button_apply.click()
        expect(self.form_phone).to_be_visible()
        self.form_phone.click()
        self.form_phone.fill('1771453335')
        self.form_submit.click()
        self.form_button.first.click()
        self.form_submit.click()  # citizenship
        self.form_button.nth(1).click()
        self.form_submit.click()  # language skills
        time.sleep(2)
        self.form_experience.click()
        self.form_experience_years.nth(2).click()
        self.form_submit.click()  # work experience
        self.form_button.first.click()
        self.form_submit.click()  # driving license
        self.form_shifts.first.click()
        self.form_submit.click()  # shifts
        self.form_input.first.click()
        page.wait_for_load_state(timeout=5000)
        self.date_picker_value.get_by_text('2025').click()
        self.date_picker_value.get_by_text('Jan.').click()
        self.date_picker_submit.click()
        self.form_submit.click()  # availability
        self.form_education.click()
        self.form_education_select.click()
        self.form_submit.click()  # qualifications
        self.form_work_experience.nth(1).click()
        self.form_input.nth(0).fill("Test Position")
        self.form_input.nth(1).fill("Test Employer")
        self.form_input.nth(2).fill("Test Location")
        self.form_input.nth(3).fill("Test Department")
        self.form_input.nth(4).click()
        self.date_picker_value.get_by_text('2022').click()
        self.date_picker_value.get_by_text('Jan.').click()
        self.date_picker_value.nth(4).click()  # month
        self.date_picker_submit.click()
        self.form_input.nth(5).click()
        self.date_picker_value.get_by_text('2024').click()
        self.date_picker_value.get_by_text('Dez.').click()
        #page.wait_for_load_state(timeout=5000)
        self.date_picker_submit.click()
        self.form_submit.click()
        self.form_input.nth(0).fill("Test Title")
        self.form_input.nth(1).fill("Test Institution")
        self.form_input.nth(2).fill("Test City")
        self.form_input.nth(3).click()
        self.date_picker_value.get_by_text('2020').click()
        self.date_picker_value.get_by_text('Sept.').click()
        self.date_picker_submit.click()
        self.form_input.nth(4).click()
        self.date_picker_value.get_by_text('2023').click()
        self.date_picker_value.get_by_text('Mai').click()
        #page.wait_for_load_state(timeout=5000)
        self.date_picker_submit.click()
        self.form_submit.click()
        #self.form_submit.click()

    def login_existing_user(self, set_up):
        #page = set_up
        self.accept_cookie_banner()
        logged_in_area = LoggedInArea(set_up)
        self.goto_url(set_up, "https://my.mdwng.dev/auth/login")
        self.accept_cookie_banner()
        # TODO: use fixtures to get the credentials
        logged_in_area.enter_email("testautomations+2024test@medwing.com")
        logged_in_area.enter_password("Med1205+")
        logged_in_area.click_form_button_submit()
        logged_in_area.verify_h1_text(0, "Welcome")
