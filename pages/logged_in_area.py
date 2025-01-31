import re
import time
from datetime import datetime
from playwright.sync_api import expect
from playwright.sync_api import Page
from conftest import current_date_time


class LoggedInArea:

    def __init__(self, page: Page):

        self.element_name = None
        # Login page
        self.navi_links = page.locator("//nav//li//a")
        self.login_email = page.locator("//input[@name='email']")
        self.login_password = page.locator("//input[@name='password']")
        self.login_button = page.locator("//button[@name='submit-form']")
        self.link_job_finder =  page.locator("//a[contains(@href, '/job-finder/job_kind/')]")
        self.link_forgot_password = page.locator("//a[contains(@href, '/auth/forgot-password')]")
        self.link_login_google = page.get_by_text("Login with Google")
        self.link_login_without_password = page.locator("//a[contains(@href, '/auth/magic-link')]")
        self.h3 = page.locator("//*[contains(@class, 'MuiGrid-root')]//h3")
        # Logged-in Area - Home
        # Side navigation links:
        self.side_navi_links = page.locator("//nav//li//a")
        self.link_dashboard = page.locator("//nav//li//a[@href='/dashboard']")
        #self.link_profile = page.locator("'Profil'")
        self.link_profile = page.locator("//nav//li//a[@href='/profile']")
        self.link_jobs = page.locator("//nav//li//a[@href='/jobs']")
        self.link_messenger = page.locator("//nav//li//a[@href='/messaging']")
        self.link_applications = page.locator("//nav//li//a[@href='/applications']")
        self.link_settings = page.locator("//nav//li//a[@href='/settings']")
        self.h1 = page.locator("//h1")
        self.h2 = page.locator("//h2")
        self.h4 = page.locator("//h4")
        self.h5 = page.locator("//h5")
        self.dialog_container = page.locator("//*[contains(@class, 'MuiDialog-container')]")
        self.dialog_title = page.locator("//*[@aria-labelledby='scroll-dialog-title']")
        self.dialog_message = page.locator("//*[@role='dialog']//p[contains(@class, 'MuiTypography')]")
        self.dialog_button_cta = page.locator("//*[contains(@class, 'MuiDialogActions-root')]//button")
        self.dialog_button_close = page.locator("//*[@role='dialog']//*[contains(@href, 'icon-close')]")
        self.link_medwing_friends = page.locator(
            "//a[@href='https://medwing.com/de/de/ueber-medwing/empfehlungsprogramm']"
        )
        #self.box_button = page.locator("//*[contains(@class, 'MuiBox')]//button")
        self.box_button = page.get_by_role("button", name="OK")
        #TODO: iframe - TikTok videos
        # Logged-in Area - Profile
        self.edit_personal_details = page.get_by_label("edit-personal-detail")
        self.add_job_search_status = page.locator("//a[@href='/profile?edit=job-search-status']")
        self.edit_profile_visibility = page.locator("//a[@aria-label='edit-Profile visibility']")
        self.edit_location = page.locator("//a[@aria-label='edit-Work Location']")
        #self.form_dropbox_option = page.locator("//*//ul//li//span")
        self.form_dropbox_option = page.locator("//*//ul//li")
        self.edit_facility_types = page.locator("//a[@aria-label='edit-Desired Facility Types']")
        self.add_facility_types = page.locator("//a[@href='/profile?edit=preferred-places']")
        self.add_departments = page.locator("//a[@href='/profile?edit=departments']")
        self.edit_contract_type = page.locator("//a[@href='/profile?edit=contract-type']")
        self.edit_working_hours = page.locator("//a[@aria-label='edit-Working Hours']")
        self.edit_shifts = page.locator("//a[@aria-label='edit-Possible Shifts']")
        self.edit_available_from = page.locator("//a[@aria-label='edit-Available from']")
        self.edit_years_experience = page.locator("//a[@aria-label='edit-Years of work experience']")
        self.edit_work_experience = page.locator("//a[@aria-label='edit-experience']")
        self.add_job = page.locator("//a[@href='/profile?add=work-experience']")
        self.edit_education = page.locator("[aria-label^='edit-education']")
        self.edit_relevant_education = page.locator("//a[@aria-label='edit-Relevant education']")
        self.add_education = page.locator("//a[@href='/profile?add=education']")
        self.add_skills = page.locator("//a[@href='/profile?edit=health-skills']")
        self.edit_it_skills = page.locator("//a[@aria-label='edit-IT skills']")
        self.edit_drivers_license = page.locator("//a[@aria-label='edit-Driver's license']")
        self.edit_german_skills = page.locator("//a[@aria-label='edit-German skills']")
        self.add_language = page.locator("//a[@href='/profile?add=language']")
        self.add_other_skills = page.locator("//a[@href='/profile?edit=other-skills']")
        self.upload_file = page.locator("//input[@data-testid='upload-document']")
        self.edit_document = page.locator("//a[contains(@href, '/profile?edit=document&id=']")
        self.add_motivation = page.locator("//a[@href='/profile?edit=motivation']")
        self.motivation_input = page.locator("//form//p")
        self.form_input = page.locator("//form//input")
        self.form_input_text = page.locator("//form//input[@type='text']")
        self.form_input_tel = page.locator("//form//input[@type='tel']")
        self.form_button_gender = page.locator("//*[contains(@class, 'MuiChip-clickable')]")
        self.form_button = page.locator("//form//button")
        self.form_role_button = page.locator("//form//div[@role='button']")
        self.form_button_submit = page.locator("//form//button[@type='submit']")
        self.form_combobox = page.locator("//*[@role='combobox']")
        self.dialog_birth = page.locator("//*[contains(@class, 'MuiPickersYear-root')]")
        self.form_calendar_year = page.get_by_role("radio", name="1987")
        self.form_calendar_month = page.get_by_role("radio", name="Mai")
        self.form_calendar_day = page.get_by_role("gridcell", name="17")
        self.form_input_disabled = page.locator("//form//input[contains(@class, 'Mui-disabled')]")
        self.form_location_nationwide = page.locator("//form//input[@name='nationWide']")
        self.form_checkbox = page.locator("//form//input[@type='checkbox']")
        self.form = page.locator("//form//ul//li")
        self.dropdown_list = page.locator("//*//ul//li[@data-value]")
        self.form_cancel_icon = page.get_by_test_id("CancelIcon")
        # TODO: Logged-in Area - Jobs
        # TODO: Logged-in Area - Messenger
        # Submit button (OK): -1
        self.dialog_date_button = page.locator("//*[contains(@class, 'MuiDialog-root')]//button[@role]")
        self.single_select_button = page.locator("//*[contains(@class, 'MuiBox-root')]//div[@role='button']")
        # Logged-in Area - Applications
        self.application = page.locator("//*[@data-testid='recommended-jobs-list-view']")
        # Calendar
        self.open_calendar_button = page.locator("//a[@href='/calendar']")
        self.calendar_radio = page.locator("//button[@role='radio']")
        self.calendar_checkbox = page.locator("//button[@role='checkbox']")
        self.calendar_add_availabilities = page.locator("//button[@data-id='create-availability-btn']")
        # Logged-in Area - Settings
        self.button_change_language = page.locator("//button[@aria-label='change-language']")
        self.popover_language = page.locator("//*[contains(@class, 'MuiPopover-paper')]//p")
        #self.popover_language = page.locator("//*[@href='#icon-de-flag-f9d525']")
        self.button_edit = page.locator("//button[@aria-label='edit']")   #email, password
        self.button_verify_email = page.locator("//*[@role='alert']//button")
        self.button_logout = page.locator("//button//*[contains(@href, '#icon-log-out')]")   # 2 buttons
        self.button_type_button = page.locator("button[type='button']")   # multiple (for ex., Logout)

        self.job_preferences_section = page.locator(
            "//div[1][contains(@class, 'MuiPaper-root')]"
        ).nth(1).locator("//*//p").nth(1)
        self.facility_types = page.locator("ul > li")
        self.job_preferences_facility = page.locator(
            "//div[1][contains(@class, 'MuiPaper-root')]"
        ).nth(1).locator("//div[2]/p[1]").nth(1)


    def verify_login_job_finder(self, page):
        self.link_job_finder.click()
        url = page.url
        page.expect()

    def enter_email(self, email):
        self.login_email.click()
        self.login_email.clear()
        self.login_email.fill(email)

    def enter_password(self, password):
        self.login_password.click()
        self.login_password.clear()
        self.login_password.fill(password)

    def click_login(self):
        self.login_button.click()

    def verify_h1_text(self, n, text):
        h1_text = self.h1.nth(n).text_content()
        print("h1_text: " + h1_text)
        print("expected_text: " + text)
        assert h1_text.startswith(text)
        #expect(expected_text).to_have_text(text)

    def verify_h1_text_settings(self, text, n):
        h1_text = self.h1.nth(n).text_content()
        print("h1:  " + h1_text)
        assert h1_text == text
        #expect(h1_text).to_contain_text(text)

    def verify_h2_text(self, text):
        h2_text = self.h2.text_content()
        print("h2:  " + h2_text)
        assert h2_text == text

    def verify_h3_text(self, text, n):
        h3_text = self.h3.nth(n).text_content()
        print("h3_text: " + h3_text)
        print("expected_text: " + text)
        assert h3_text.endswith(text)

    def verify_h4_text(self, n, text):
        h4_text = self.h4.nth(n).text_content()
        print("h4:  " + h4_text)
        assert h4_text == text

    def verify_h5_text(self, text):
        h5_text = self.h5.text_content()
        print("h5:  " + h5_text)
        assert h5_text == text

    def click_job_finder_link(self):
        self.link_job_finder.click()

    def click_forgot_password(self):
        self.link_forgot_password.click()

    def click_login_google(self):
        self.link_login_google.click()
        #TODO: verify google login page is opened in a new window

    def click_login_without_password(self):
        self.link_login_without_password.click()

    def click_side_navi_link(self, n):
        link = self.side_navi_links
        link.nth(n).click()

    def click_navi_side_link_dashboard(self):
        link = self.link_dashboard
        link.click()

    def click_navi_side_link_profile(self):
        link = self.link_profile
        link.click()

    def click_navi_side_link_jobs(self):
        link = self.link_jobs
        link.click()

    def click_navi_side_link_messenger(self):
        link = self.link_messenger
        link.click()

    def click_navi_side_link_applications(self):
        link = self.link_applications
        link.click()

    def click_navi_side_link_settings(self):
        link = self.link_settings
        link.click()

    def verify_dialog_title_text(self, text):
        dialog_title = self.dialog_title.text_content()
        expect(dialog_title).to_contain_text(text)

    def verify_dialog_message(self, text):
        dialog_message = self.dialog_message.text_content()
        expect(dialog_message).to_contain_text(text)

    def click_dialog_cta(self):
        button = self.dialog_button_cta
        button.click()
        expect(self.dialog_container).not_to_be_visible()

    def click_dialog_close(self):
        button = self.dialog_button_close
        button.click()
        expect(self.dialog_container).not_to_be_visible()

    def click_medwing_friends(self):
        link = self.link_medwing_friends
        link.click()
        #TODO: add switch to the other window, verify url, verify h1

    def click_box_button(self):
        button = self.box_button
        button.click()
        #TODO: add verify box is closed

    def click_button_type_button(self, n):
        button = self.button_type_button
        button.nth(n).click()

    def click_edit_personal_details(self, set_up):
        self.edit_personal_details.click()

    def click_add_job_search_status(self):
        button = self.add_job_search_status
        button.click()

    def click_edit_profile_visibility(self):
        button = self.edit_profile_visibility
        button.click()

    #def click_edit_work_location(self):
    #    button = self.edit_location
    #    button.scroll_into_view_if_needed()
    #    button.click()
    #    self.form_input_text.fill("Oland")
    #    time.sleep(3)
    #    self.form_dropbox_option.select_option()

    def click_edit_work_location(self):
        button = self.edit_location
        button.scroll_into_view_if_needed()
        button.click()

    def click_edit_facility_types(self):
        button = self.edit_facility_types
        button.click()

    def click_add_facility_types(self):
        button = self.add_facility_types
        button.click()

    def click_edit_contract_type(self):
        button = self.edit_contract_type
        button.click()

    def click_add_departments(self):
        button = self.add_departments
        button.click()

    def click_edit_working_hours(self):
        button = self.edit_working_hours
        button.click()

    def click_edit_shifts(self):
        button = self.edit_shifts
        button.click()

    def click_edit_available_from(self):
        button = self.edit_available_from
        button.click()

    def click_edit_years_experience(self):
        button = self.edit_years_experience
        button.click()

    def click_edit_work_experience(self, n):
        button = self.edit_work_experience
        button.nth(n).click()

    def click_add_work_experience(self):
        button = self.add_job
        expect(button).to_be_enabled()
        button.scroll_into_view_if_needed()
        button.click()

    def click_edit_education(self, n):
        button = self.edit_education
        button.nth(n).click()

    def click_edit_relevant_education(self):
        button = self.edit_relevant_education
        button.click()

    def click_add_education(self):
        button = self.add_education
        button.click()

    def click_add_skills(self):
        button = self.add_skills
        button.click()

    def click_edit_it_skills(self):
        button = self.edit_it_skills
        button.click()

    def click_edit_drivers_license(self):
        button = self.edit_drivers_license
        button.click()

    def click_edit_german_skills(self):
        button = self.edit_german_skills
        button.click()

    def click_add_language(self):
        button = self.add_language
        button.click()

    def select_german_language(self):
        dropdown = self.popover_language
        dropdown.first.click()

    def click_add_other_skills(self):
        button = self.add_other_skills
        button.click()

    def click_upload_file(self):
        button = self.upload_file
        button.click()

    def click_edit_document(self):
        button = self.edit_document
        button.click()

    def click_add_motivation(self):
        button = self.add_motivation
        button.scroll_into_view_if_needed()
        button.click()

    current_date_time = datetime.now().strftime('%Y%m%d-%H%M%S')

    def add_motivation_input(self):
        motivation = self.motivation_input
        motivation.fill("Test Motivation " + current_date_time)

    def click_form_button(self, n):
        button = self.form_button
        button.nth(n).click(timeout=5000)

    def click_form_role_button(self, n):
        button = self.form_role_button
        button.nth(n).click()

    def click_form_button_submit(self):
        button = self.form_button_submit
        button.click()

    def click_form_combobox(self, n):
        print("Combobox clicked")
        combobox_list = self.form_combobox
        combobox_list.nth(n).click()
        print("Combobox opened")
        #for combobox in combobox_list:
        #    combobox.nth(n).hover()
        #    combobox.nth(n).click()

    def click_dropdown_list(self):
        item = self.dropdown_list
        item.click()

    def click_dialog_date_button(self, n):
        date = self.dialog_date_button
        date.nth(n).click()

    def click_single_select_button(self, n):
        radio = self.single_select_button
        radio.nth(n).click()

    def click_application(self):
        item = self.application
        item.click()

    def click_open_calendar_button(self):
        calendar = self.open_calendar_button
        calendar.click()

    def add_calendar_date(self, n):
        radio = self.calendar_radio
        #radio.nth(n).scroll_into_view_if_needed()
        radio.nth(n).click()

    def form_check_checkbox(self, n):
        checkbox = self.calendar_checkbox
        checkbox.nth(n).check()

    def click_calendar_add_availabilities(self):
        availabilities = self.calendar_add_availabilities
        availabilities.click()

    def click_button_change_language(self, n):
        self.button_change_language.nth(n).click()

    def click_button_edit(self, n):
        button = self.button_edit
        button.nth(n).click()

    def click_button_verify_email(self):
        button = self.button_verify_email
        button.click()

    def click_button_logout(self):
        button = self.button_logout
        button.click()

    def change_language_german(self):
        self.click_button_change_language(1)
        self.select_german_language()

    def form_update_input_fields(self, set_up):
        page = set_up
        input_text = self.form_input_text
        input_tel = self.form_input_tel
        input_text.nth(0).fill("Test_" + current_date_time)
        input_text.nth(1).fill("Name_" + current_date_time)
        input_text.nth(2).fill("JobTitle_" + current_date_time)
        input_tel.clear()
        input_tel.fill(current_date_time)
        self.click_form_button_submit()
        time.sleep(1)
        page.reload()
        self.click_edit_personal_details(set_up)
        input_first_name = page.locator("#firstName").input_value()
        input_last_name = page.locator("#lastName").input_value()
        input_job_title = page.locator("#desiredJobPositionTitle").input_value()
        input_phone_draft = page.locator("#phone").input_value()
        input_phone = input_phone_draft.translate(str.maketrans('', '','_-@ !'))
        expected_first_name = "Test_" + current_date_time
        expected_last_name = "Name_" + current_date_time
        expected_job_title = "JobTitle_" + current_date_time
        expected_phone_draft = current_date_time
        expected_phone = expected_phone_draft.translate(str.maketrans('', '','_-@ !'))
        print("input_first_name: " + input_first_name)
        print("expected_first_name: " + expected_first_name)
        print("input_last_name: " + input_last_name)
        print("expected_last_name: " + expected_last_name)
        print("input_job_title: " + input_job_title)
        print("expected_job_title: " + expected_job_title)
        print("input_phone: " + input_phone)
        print("expected_phone: " + expected_phone)
        assert input_first_name == expected_first_name
        assert input_last_name == expected_last_name
        assert input_job_title == expected_job_title
        assert input_phone == expected_phone

    def form_text_fill(self, n, text):
        input_field = self.form_input_text
        input_field.nth(n).fill(text)

    def form_update_birth_date(self):
        date = self.form_input_text
        date.nth(4).scroll_into_view_if_needed()
        date.nth(4).click()
        self.add_calendar_date(55)
        self.add_calendar_date(6)
        self.select_calendar_day()
        self.click_box_button()
        self.click_form_button_submit()

    def select_calendar_year(self):
        radio = self.form_calendar_year
        radio.click()

    def select_calendar_month(self):
        radio = self.form_calendar_month
        radio.click()

    def select_calendar_day(self):
        day = self.form_calendar_day
        day.click()

    def update_gender(self):
        for button in self.form_button_gender.all():
            if button.first.is_checked():
                button.nth(1).check()
            elif button.nth(1).is_checked():
                button.first.check()
            else:
                button.nth(1).check()

    def add_work_experience(self):
        self.click_add_work_experience()
        input_text = self.form_input_text
        test_job_position = "Test Job Position " + current_date_time
        input_text.nth(0).fill(test_job_position)
        input_text.nth(1).fill("Test Employer " + current_date_time)
        input_text.nth(2).fill("Test Location " + current_date_time)
        input_text.nth(3).fill("Test Department " + current_date_time)
        input_text.nth(4).click()
        self.add_calendar_date(62)
        self.add_calendar_date(6)
        self.click_box_button()
        input_text.nth(5).click()
        self.add_calendar_date(5)
        self.add_calendar_date(4)
        self.click_box_button()
        self.click_form_button_submit()
        self.delete_work_experience()
        #time.sleep(1)

    def delete_work_experience(self):
        self.click_edit_work_experience(-1)
        self.click_form_button(0)

    def delete_education(self):
        self.click_edit_education(-1)
        self.click_form_button(0)

    def add_candidate_education(self):
        self.click_add_education()
        input_text = self.form_input_text
        test_job_title = "Test Title " + current_date_time
        input_text.nth(0).fill(test_job_title)
        input_text.nth(1).fill("Test Employer " + current_date_time)
        input_text.nth(2).fill("Test Location " + current_date_time)
        input_text.nth(3).click()
        self.add_calendar_date(62)
        self.add_calendar_date(6)
        self.click_box_button()
        input_text.nth(4).click()
        self.add_calendar_date(5)
        self.add_calendar_date(4)
        self.click_box_button()
        self.click_form_button_submit()
        self.delete_education()
        #time.sleep(1)

    def add_candidate_motivation(self):
        self.click_add_motivation()
        self.add_motivation_input()
        self.click_form_button(0)

    def logout(self):
        self.click_button_type_button(3)
        self.click_form_button_submit()
        time.sleep(1)

    def verify_input_disabled(self):
        input_disabled = self.form_input_disabled
        input_disabled.is_visible()

    def toggle_nationwide(self):
        location = self.form_location_nationwide
        location.click()

    def form_select_dropdown_option(self, n):
        print("Dropdown is opened")
        dropdown_options = self.form_dropbox_option
        dropdown_options.nth(n).scroll_into_view_if_needed()
        dropdown_options.nth(n).click()
        print("Dropdown option is selected")

    def verify_location_toggle(self):
        checkbox = self.form_checkbox
        input_disabled = self.form_input_disabled
        combobox = self.form_combobox
        cancel_icon = self.form_cancel_icon
        if checkbox.is_checked():
            print("Toggle is set to Worldwide")
            input_disabled.is_visible()
            checkbox.click()
            input_disabled.is_hidden()
        else:
            print("Toggle is NOT set to Worldwide")
            input_disabled.is_hidden()
            cancel_icon.click()
        combobox.fill("Baltrum")
        self.form_select_dropdown_option(0)
        self.click_form_button_submit()

    def get_work_location(self):
        location = self.job_preferences_section
        location_str = location.text_content()
        print("Location: " + location_str)
        assert location_str == "Baltrum"

    def verify_facility_types_list(self):
        facility_types_list = self.facility_types
        list_length = facility_types_list.count()
        print("list_length: " + str(list_length))
        assert list_length > 30
        #TODO: Update the list length with a relevant number

    def uncheck_form_checkboxes(self):
        checkbox_list = self.form_checkbox.all()
        for checkbox in checkbox_list:
            if checkbox.is_checked:
                checkbox.scroll_into_view_if_needed()
                checkbox.uncheck()
        print("Checkbox unchecked")

    def check_form_checkbox(self):
        checkbox_list = self.form_checkbox.all()
        for checkbox in checkbox_list:
            if not checkbox.is_checked():
                checkbox.check()
        print("Checkbox unchecked")

    def form_select_from_list(self):
        self.form_text_fill(0, "Day Clinic")
        checkbox_list = self.form_checkbox.all()
        for checkbox in checkbox_list:
            print("checkbox: " + checkbox.get_attribute(name='value'))
            if checkbox.get_attribute(name='value') == "dayclinic":
                checkbox.check()
        self.click_form_button_submit()

    def verify_preferred_facility(self):
        facility = self.job_preferences_facility.nth(0)
        facility_str = facility.text_content()
        print("Facility: " + facility_str)
        assert facility_str == "Day Clinic"

    def verify_update_facility_types(self):
        self.verify_h2_text("Desired Facility Types")
        self.verify_facility_types_list()
        self.uncheck_form_checkboxes()
        self.click_form_button_submit()
        self.click_add_facility_types()
        self.form_select_from_list()
        self.add_facility_types.is_hidden()

    def uncheck_form_departments(self):
        checkbox_list = self.form_checkbox.all()
        #print("List_len = " + str(len(checkbox_list)))
        form_items = self.form.all()
        for item in form_items:
            item.evaluate("e => e.scrollTop += 700")
            print("List_len = " + str(len(checkbox_list)))
        for checkbox in checkbox_list:
            if checkbox.is_checked:
                checkbox.scroll_into_view_if_needed()
                time.sleep(1)
                checkbox.uncheck()
        print("Checkbox unchecked")
        self.click_add_departments()

    def verify_update_departments(self):
        self.verify_h2_text("Departments")
        self.uncheck_form_departments()
        self.click_form_button_submit()

    # flaky - sometimes the button's state is not saved after being clicked
    def deselect_all_contract_types(self):
        cancel_buttons = self.form_cancel_icon.all()
        for button in cancel_buttons:
            if button.is_visible():
                button.click()
                time.sleep(1)   # because of flakiness
            elif button.is_hidden():
                self.form_button.wait_for(timeout=5000)
                self.click_form_button(0)
            else:
                self.form_button.wait_for(timeout=5000)
                self.click_form_button(0)

    def select_contract_type(self):
        cancel_buttons = self.form_cancel_icon.all()
        for button in cancel_buttons:
            if button.is_hidden:
                button = self.form_role_button
                button.nth(0).click(timeout=5000)
            elif button.is_visible():
                self.deselect_all_contract_types()

    def update_contract_type(self):
        self.deselect_all_contract_types()
        time.sleep(1)
        if self.form_button.is_hidden():
            self.click_edit_contract_type()
            self.select_contract_type()
            self.click_form_button(0)

    def verify_update_contract_type(self):
        self.verify_h2_text("Contract Type")
        self.select_contract_type()

    def verify_working_hours(self):
        self.verify_h2_text("Working Hours")

    def verify_shifts(self):
        self.verify_h2_text("Possible shifts")

    def select_available_from(self):
        input_text = self.form_input_text
        input_text.click()
        time.sleep(3)

    def verify_available_from(self):
        self.verify_h2_text("Earliest Start Date")
        self.select_available_from()
        self.add_calendar_date(0)
        self.add_calendar_date(11)
        self.select_calendar_day()
        self.click_box_button()
        self.uncheck_form_checkboxes()
        time.sleep(1)
        self.click_form_combobox(0)
        self.form_select_dropdown_option(5)
        self.click_form_combobox(1)
        self.form_select_dropdown_option(1)
        self.click_form_button_submit()

    def verify_notice_period(self):
        form_input = self.form_input
        notice_units = form_input.nth(1).get_attribute("value")
        notice_type = form_input.nth(2).get_attribute("value")
        print("combobox_content_units: " + notice_units)
        print("combobox_content_type: " + notice_type)
        assert notice_units == "6"
        assert notice_type == "weeks"
