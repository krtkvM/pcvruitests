from datetime import datetime
from faker import Faker
from selenium.webdriver.support.select import Select
from Pages.base_page import BasePage
from locators import CompanyPageLocators, DealsPageLocators


class CompanyPage(BasePage):

    def create_new_blank_deal(self):
        add_new_deal = self.browser.find_element(*CompanyPageLocators.ADD_NEW_DEAL_BUTTON)
        add_new_deal.click()
        create_new_blank_deal = self.browser.find_element(*CompanyPageLocators.CREATE_NEW_BLANK_DEAL_BUTTON)
        create_new_blank_deal.click()

    def open_add_a_note(self):
        add_a_note = self.browser.find_element(*CompanyPageLocators.ADD_A_NOTE_BUTTON)
        add_a_note.click()

    def select_category_in_note_form(self):
        category_for_note = self.browser.find_element(*CompanyPageLocators.NOTE_CATEGORY_SELECT)
        select_category_for_note = Select(category_for_note)
        select_category_for_note.select_by_value("4")

    def enter_current_date_and_time_in_note_form(self):
        date_time_for_reminder = self.browser.find_element(*CompanyPageLocators.TIME_HOLDER_FOR_NOTE_REMINDER)
        date_time_for_reminder.click()
        current_date = datetime.today().strftime('%m/%d/%Y %I:%M %p')
        date_time_for_reminder.send_keys(current_date)

    def select_priority_in_note_form(self):
        medium_priority_input = self.browser.find_element(*CompanyPageLocators.MEDIUM_PRIORITY_INPUT)
        medium_priority_input.click()

    def enter_note_text_in_note_form(self, text):
        note_body = self.browser.find_element(*CompanyPageLocators.NOTE_BODY)
        note_body.send_keys(text)

    def press_add_note_button(self):
        add_note = self.browser.find_element(*CompanyPageLocators.ADD_NOTE_BOTTON)
        add_note.click()

    def assert_adding_new_note(self):
        activities_tab = self.browser.find_element(*CompanyPageLocators.ACTIVITIES_TAB)
        activities_tab.click()
        first_note = self.browser.find_element(*CompanyPageLocators.FIRST_NOTE_TEXT)
        first_note_text = first_note.text
        assert "test/qa-Mk" in str(first_note_text)

    # Company tab Editing

    def select_owner_account(self):
        owner_account = self.browser.find_element(*CompanyPageLocators.COMPANY_ACCOUNT_OWNER_FIELD)
        select_owner_account = Select(owner_account)
        select_owner_account.select_by_value("4")

    def edit_company_name(self, text):
        company_name = self.browser.find_element(*CompanyPageLocators.COMPANY_NAME_FIELD)
        company_name.clear()
        company_name.send_keys(text)

    def edit_company_address(self, text):
        company_address = self.browser.find_element(*CompanyPageLocators.COMPANY_ADDRESS_FIELD)
        company_address.clear()
        company_address.send_keys(text)

    def edit_company_email(self, text):# как то передавать атрибут в самом тесте и задавать значение там
        company_email = self.browser.find_element(*CompanyPageLocators.COMPANY_EMAIL_FIELD)
        company_email.clear()
        company_email.send_keys(text)

    def edit_company_phone(self, text):
        company_phone = self.browser.find_element(*CompanyPageLocators.COMPANY_PHONE_FIELD)
        company_phone.clear()
        company_phone.send_keys(text)

    def edit_company_website(self, text):
        company_website = self.browser.find_element(*CompanyPageLocators.COMPANY_WEBSITE_FIELD)
        company_website.clear()
        company_website.send_keys(text)

    def go_to_companies_list(self):
        link_to_companies_list = self.browser.find_element(*CompanyPageLocators.LINK_TO_DEALS_LIST)
        link_to_companies_list.click()

    # Deal tab Editing

    def go_to_first_deal_tab(self):
        first_deal_tab = self.browser.find_element(*CompanyPageLocators.FIRST_DEAL_TAB)
        first_deal_tab.click()

    def edit_stage_selector(self):
        stage_selector = self.browser.find_element(*CompanyPageLocators.DEAL_STAGE_FIELD)
        select_deal_stage = Select(stage_selector)
        select_deal_stage.select_by_value("11")

    def edit_vendor_selector(self):
        vendor_selector_field = self.browser.find_element(*CompanyPageLocators.VENDOR_FIELD)
        select_vendor = Select(vendor_selector_field)
        select_vendor.select_by_value("2")

    def edit_time_frame(self):
        time_frame_field = self.browser.find_element(*CompanyPageLocators.TIME_FRAME_FIELD)
        select_time_frame = Select(time_frame_field)
        select_time_frame.select_by_value("1")

    def edit_cosigners_first_name(self, text):
        cosigners_name = self.browser.find_element(*CompanyPageLocators.COSIGNERS_FIRST_NAME)
        cosigners_name.clear()
        cosigners_name.send_keys(text)

    # def add_cosigners_email(self, text):
    #     add_email_button = self.browser.find_element(*CompanyPageLocators.ADD_ANOTHER_COSIGNERS_EMAIL_BUTTON)
    #     add_email_button.click()
    #     email_field_label = self.browser.find_element(*CompanyPageLocators.NEW_COSIGNERS_EMAIL_FIELD_LABEL)
    #     email_field_label.click()
    #     email_field = self.browser.find_element(*CompanyPageLocators.NEW_COSIGNERS_EMAIL_FIELD)
    #     email_field.send_keys(text)

    def edit_lender(self):
        lender_field = self.browser.find_element(*CompanyPageLocators.LENDER_NAME_SELECT)
        select_lender_field = Select(lender_field)
        select_lender_field.select_by_value("2")

    def assert_editing_deal(self):
        first_deal_cosigner_name = self.browser.find_element(*DealsPageLocators.FIRST_DEAL_IN_LIST_COSIGNER_NAME)
        first_deal_cosigner_name_text = first_deal_cosigner_name.text
        assert "qa/cosigners_name" in str(first_deal_cosigner_name_text)

    ### Send Email form ###
    def open_send_email_form(self):
        send_email_button = self.browser.find_element(*CompanyPageLocators.SEND_EMAIL_BUTTON)
        send_email_button.click()

    def select_deal_for_send_email_form(self):
        select_deal_field = self.browser.find_element(*CompanyPageLocators.SELECT_EMAILS_FROM_DEAL_FIELD)
        select_deal = Select(select_deal_field)
        select_deal.select_by_value("8")

    def enter_additional_email(self, text):
        additional_email_field = self.browser.find_element(*CompanyPageLocators.ADDITIONAL_EMAILS)
        additional_email_field.send_keys(text)

    def enter_email_subject(self, text):
        email_subject = self.browser.find_element(*CompanyPageLocators.EMAIL_SUBJECT)
        email_subject.send_keys(text)

    def enter_email_text(self, text):
        email_text_field = self.browser.find_element(*CompanyPageLocators.EMAIL_BODY)
        email_text_field.send_keys(text)

    def send_email(self):
        send_email_button = self.browser.find_element(*CompanyPageLocators.SEND_EMAIL_BUTTON_IN_FORM)
        send_email_button.click()

    ### Document Requests form ###
    def open_document_requests_form(self):
        document_requests_button = self.browser.find_element(*CompanyPageLocators.DOCUMENT_REQUESTS_BUTTON)
        document_requests_button.click()

    def select_deal_document_requests_form(self):
        select_deal_document_requests_form = self.browser.find_element(*CompanyPageLocators.SELECT_DEAL_FOR_DOCUMENT_REQUESTS_FORM)
        deal_document_requests_form = Select(select_deal_document_requests_form)
        deal_document_requests_form.select_by_value("8")

    def select_cosigner_document_requests_form(self):
        select_cosigner_document_requests_form = self.browser.find_element(*CompanyPageLocators.SELECT_COSIGNER_FOR_DOCUMENT_REQUESTS_FORM)
        cosigner_document_requests_form = Select(select_cosigner_document_requests_form)
        cosigner_document_requests_form.select_by_value("8")

    def select_several_checkboxes(self):
        checkbox_1 = self.browser.find_element(*CompanyPageLocators.CHECKBOX_DRIVER_LICENSE)
        checkbox_1.click()
        checkbox_2 = self.browser.find_element(*CompanyPageLocators.CHECKBOX_INVOICE_FROM_VENDOR)
        checkbox_2.click()
        checkbox_4 = self.browser.find_element(*CompanyPageLocators.CHECKBOX_LAST_SIX_BUSINESS_BANK_STATEMENTS)
        checkbox_4.click()
        checkbox_7 = self.browser.find_element(*CompanyPageLocators.CHECKBOX_2020_BUSINESS_TAX_RETURNS)
        checkbox_7.click()
        checkbox_10 = self.browser.find_element(*CompanyPageLocators.CHECKBOX_2020_PERSONAL_TAX_RETURNS)
        checkbox_10.click()

    def enter_additional_documents(self, text):
        additional_documents = self.browser.find_element(*CompanyPageLocators.ADDITIONAL_DOCUMENTS_FIELD)
        additional_documents.send_keys(text)

    def send_request_for_documents(self):
        send_request_button = self.browser.find_element(*CompanyPageLocators.SEND_REQUEST_BUTTON)
        send_request_button.click()

    def assert_document_requests(self):
        success_string = self.browser.find_element(*CompanyPageLocators.SUCCESS_STRING)
        success_string_text = success_string.text
        assert "Success!" in str(success_string_text)

