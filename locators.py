from selenium.webdriver.common.by import By

class LoginPageLocators():
    USER_EMAIL = (By.XPATH, '//*[@id="user-email"]')
    USER_PASSWORD = (By.XPATH, '//input[@id="pass"]')
    NEXT_BUTTON = (By.XPATH, '//input[@value="Next"]')
    SIGNIN_BUTTON = (By.XPATH, '//input[@value="Sign in"]')
    INFO_BANNER_TEXT = (By.XPATH, '//div[@id="flash_notice"]')

class DealsPageLocators():
    LEFT_NAV_MENU = (By.XPATH, '//div[@class="aside-content slim-scroll"]')
    LEADS_TAB = (By.XPATH, '//a[@href="/leads"]')
    FIRST_DEAL_IN_LIST = (By.XPATH, '//*[@id="data-table"]/tbody/tr[1]/td[1]/a')
    FIRST_DEAL_IN_LIST_COSIGNER_NAME = (By.XPATH, '//*[@id="data-table"]/tbody/tr[1]/td[3]')

    #Filter
    FILTER = (By.XPATH, '//a[contains(text(), "Show search form")]')
    FILTER_COSIGNER_NAME = (By.XPATH,'//input[@id="cosigner_name" and @type="text"]')
    SEARCH_BUTTON = (By.XPATH, "//button[@name='button']")

class LeadsPageLocators():
    NEW_LEAD_BUTTON = (By.XPATH, '//a[@href="/leads/new"]')
    FIRST_LEAD_IN_LIST = (By.XPATH, '//*[@id="data-table"]/tbody/tr[1]/td[1]/a')

class CompaniesPageLocators():
    FIRST_COMPANY_IN_LIST = (By.XPATH, '//*[@id="data-table"]/tbody/tr[1]/td[1]/a')



class OneLeadPageLocators():
    COMPANY_NAME_FIELD = (By.XPATH, '//input[@id="lead_name"]')
    SAVE_BUTTON = (By.XPATH, '//div[@class="float-right"]/input[@name="commit"]')
    INFO_MODAL = (By.XPATH, '//div[@id="flash_notice"]')
    COMPANY_ADDRESS_FIELD = (By.XPATH, '//input[@id="lead_addresses_attributes_0_address_1"]')
    COSIGNER_ADDRESS_FIELD = (By.XPATH, '//input[@id="lead_people_attributes_0_addresses_attributes_0_address_1"]')
    CONVERT_BUTTON = (By.XPATH,'//a[contains(text(), "Convert")]')


class CompanyPageLocators():

    COMPANY_INFO_TAB = (By.XPATH,'//ul[@id="app-tabs"]//a[@href="#company"]')
    ACTIVITIES_TAB = (By.XPATH,'//ul[@id="app-tabs"]//a[@href="#activities"]')
    FIRST_DEAL_TAB = (By.XPATH, '//ul[@id="app-tabs"]/li[4]')
    ADD_NEW_DEAL_BUTTON = (By.XPATH, '//button[@data-target="#add-deal"]')
    CREATE_NEW_BLANK_DEAL_BUTTON = (By.XPATH, '//button[contains(text(), "Create new blank deal")]')
    ADD_A_NOTE_BUTTON = (By.XPATH, '//button[@data-target="#create-note"]')
    SEND_EMAIL_BUTTON = (By.XPATH, "//button[@data-target='#send-email']")
    DOCUMENT_REQUESTS_BUTTON = (By.XPATH, "//button[@data-target='#document-requests']")

    # Notes  locators
    NOTE_CATEGORY_SELECT = (By.XPATH, '//select[@id="note_note_category_id"]')
    TIME_HOLDER_FOR_NOTE_REMINDER = (By.XPATH, "//input[@id='note_reminder_time_holder']")
    MEDIUM_PRIORITY_INPUT = (By.XPATH, "//input[@id='note_reminder_attributes_priority_medium']")
    NOTE_BODY = (By.XPATH, "//trix-editor[@id='note_body']")
    ADD_NOTE_BOTTON = (By.XPATH, "//button[@id='create_note']")

    # Send email form
    SELECT_EMAILS_FROM_DEAL_FIELD = (By.XPATH, '//select[@id="email_deal_id"]')
    ADDITIONAL_EMAILS = (By.XPATH, "//input[@id='additional_emails']")
    EMAIL_SUBJECT = (By.XPATH, "//input[@id='subject']")
    EMAIL_BODY = (By.XPATH, '//trix-editor[@id="body"]')
    SEND_EMAIL_BUTTON_IN_FORM = (By.XPATH, "//button[@id='send-email-button']")

    # Activities tab
    FIRST_NOTE_TEXT = (By.XPATH, "//div[@id='notes']/ul/li[1]//div[@class='trix-content']/div")

    # Company tab
    COMPANY_ADDRESS_FIELD = (By.XPATH, '//input[@id="company_addresses_attributes_0_address_1"]')
    COMPANY_PHONE_FIELD = (By.XPATH, '//input[@id="company_phones_attributes_0_phone_number"]')
    COMPANY_EMAIL_FIELD = (By.XPATH, '//input[@id="company_emails_attributes_0_email"]')
    COMPANY_WEBSITE_FIELD = (By.XPATH, '//input[@id="company_websites_attributes_0_url"]')
    COMPANY_NAME_FIELD = (By.XPATH, '//input[@id="company_account_name"]')
    COMPANY_ACCOUNT_OWNER_FIELD = (By.XPATH, '//select[@id="company_account_id"]')
    LINK_TO_DEALS_LIST = (By.XPATH, '//nav//a[@href="/deals"]')

    # Deal tab
    DEAL_STAGE_FIELD = (By.XPATH, '//select[@id="company_deals_attributes_0_stage_id"]')#company_deals_attributes_0_stage_id
    VENDOR_FIELD = (By.XPATH, '//select[@id="company_deals_attributes_0_vendor_id"]')
    TIME_FRAME_FIELD = (By.XPATH, '//select[@id="company_deals_attributes_0_time_frame_id"]')
    COSIGNERS_FIRST_NAME = (By.XPATH, '//input[@id="company_deals_attributes_0_cosigners_attributes_0_person_attributes_first_name"]')
    ADD_ANOTHER_COSIGNERS_EMAIL_BUTTON = (By.XPATH, '//*[@id="cosigners-wrapper"]/div[1]/div[2]/div[2]/div[3]') #WORST selector ever
    LENDER_NAME_SELECT = (By.XPATH,'//select[@id="company_deals_attributes_0_deals_lenders_attributes_0_lender_id"]')
    LENDER_RESPONSE = (By.XPATH,'//select[@id="company_deals_attributes_0_deals_lenders_attributes_0_feedback_option_id"]')
    LENDER_CONDITION_NEED_TO_CLOSE =(By.XPATH, "//textarea[@id='company_deals_attributes_0_deals_lenders_attributes_0_conditions']")
    NEW_COSIGNERS_EMAIL_FIELD = (By.XPATH, "/html//div[@id='cosigners-wrapper']/div[1]/div[2]/div[2]//input[@name='company[deals_attributes][0][cosigners_attributes][0][person_attributes][emails_attributes][1650438491866][email]']")
    NEW_COSIGNERS_EMAIL_FIELD_LABEL = (By.XPATH, "//label[@for='company_emails_attributes_0_email']")

    # Document Requests Form
    SELECT_DEAL_FOR_DOCUMENT_REQUESTS_FORM = (By.XPATH, "//select[@id='document_request_deal_id']")
    SELECT_COSIGNER_FOR_DOCUMENT_REQUESTS_FORM = (By.XPATH, "//select[@id='cosigner-select']")
    CHECKBOX_DRIVER_LICENSE = (By.XPATH, "//input[@value='type_1']")
    CHECKBOX_INVOICE_FROM_VENDOR = (By.XPATH, "//input[@value='type_2']")
    CHECKBOX_LAST_SIX_BUSINESS_BANK_STATEMENTS = (By.XPATH, "//input[@value='type_4']")
    CHECKBOX_2020_BUSINESS_TAX_RETURNS = (By.XPATH, "//input[@value='type_7']")
    CHECKBOX_2020_PERSONAL_TAX_RETURNS = (By.XPATH, "//input[@value='type_10']")
    ADDITIONAL_DOCUMENTS_FIELD = (By.XPATH, "//input[@id='freehand_request']")
    SEND_REQUEST_BUTTON = (By.XPATH, "//button[@id='save-document-request']")

    # Popup after activities
    SUCCESS_STRING = (By.XPATH, "//h2[@id='swal2-title']")

    #//h2[@id='swal2-title']
    #//a[@id='deal-add-button' and @data-association='email']/i[]

class GmailPageLocators():
    LOGIN_FIELD = (By.XPATH, "//input[@id='identifierId']")
    NEXT_BUTTON_LOGIN_PAGE = (By.XPATH, "//div[@id='identifierNext']//button[@type='button']")
    PASSWORD_FIELD = (By.XPATH, "//input[@name='password']")
    NEXT_BUTTON_PASSWORD_PAGE = (By.XPATH, "//div[@id='passwordNext']//button[@type='button']")
