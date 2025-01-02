import time
from playwright.sync_api import expect
from tests_ui.conftest import current_date_time


class HeyFlow:

    def __init__(self, page):

        self.heyflow_id = page.locator("#hey__iframe-soft_registration_v7_7_qa")

    def heyflow_create_candidate(self, set_up):
        page = set_up
        frame = self.heyflow_id
        frame.content_frame.get_by_text("Krankenhaus").nth(1).click()
        # page.wait_for_load_state()
        frame.content_frame.get_by_text("Exam. Altenpfleger/in").first.click()
        frame.content_frame.get_by_text("Gynäkologie").click()
        frame.content_frame.get_by_role("button", name="Weiter").click()
        frame.content_frame.get_by_text("-jährige Ausbildung").click()
        frame.content_frame.get_by_text("Festanstellung", exact=True).click()
        frame.content_frame.get_by_text("Vollzeit").click()
        frame.content_frame.get_by_placeholder(
            "z.B. 12053 oder Berlin").fill("berlin")
        frame.content_frame.get_by_role("option", name="Berlin", exact=True).click()
        frame.content_frame.get_by_label("PLZ oder Stadt").click()
        frame.content_frame.get_by_label("PLZ oder Stadt").fill("13086")
        frame.content_frame.get_by_role("option", name="Berlin, 13086", exact=True).click(timeout=500)
        frame.content_frame.get_by_role("button", name="Weiter").click()
        time.sleep(3)  # TODO: Add expect screen is loaded
        expect(frame.content_frame.get_by_label("E-MAIL-ADRESSE")).to_be_visible(timeout=2000)
        frame.content_frame.get_by_label("E-MAIL-ADRESSE").click()
        frame.content_frame.get_by_label("E-MAIL-ADRESSE").fill(
            "testautomations+" + current_date_time + "test@medwing.com")
        frame.content_frame.get_by_role("button", name="Weiter").click()
        frame.content_frame.get_by_text("Ab sofort").click()
        frame.content_frame.get_by_text("Frau", exact=True).click()
        frame.content_frame.get_by_text("Herr").click()
        frame.content_frame.get_by_text("Frau", exact=True).click()
        frame.content_frame.get_by_label("VORNAME").click()
        frame.content_frame.get_by_label("VORNAME").fill("Test_202412121")
        frame.content_frame.get_by_label("NACHNAME").click()
        frame.content_frame.get_by_label("NACHNAME").fill("Test")
        frame.content_frame.get_by_role("button", name="Weiter").click()
        frame.content_frame.get_by_placeholder("3456789").fill("1771450000")
        frame.content_frame.get_by_role("button", name="Weiter").click()

