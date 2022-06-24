import time
from faker import Faker
from Pages.companies_page import CompaniesPage
from Pages.company_page import CompanyPage

from Pages.login_page import LoginPage
from Pages.deals_page import DealsPage

fake=Faker()
fake_email = fake.email()

def test_add_new_deal(browser):
    link = "https://guloans-staging.herokuapp.com/"
    page = LoginPage(browser, link)
    page.open()
    page.login_in_westfield()
    deals_page = DealsPage(browser, link)
    deals_page.select_first_deal_in_list()

    company_page = CompanyPage(browser, link)
    company_page.create_new_blank_deal()

def test_add_new_note(browser):
    link = "https://guloans-staging.herokuapp.com/"
    page = LoginPage(browser, link)
    page.open()
    page.login_in_westfield()

    deals_page = DealsPage(browser, link)
    deals_page.select_first_deal_in_list()

    company_page = CompanyPage(browser, link)
    company_page.open_add_a_note()
    company_page.select_category_in_note_form()
    company_page.enter_current_date_and_time_in_note_form()
    company_page.select_priority_in_note_form()
    company_page.enter_note_text_in_note_form(fake.text() + " test/qa-Mk ")
    company_page.press_add_note_button()
    company_page.assert_adding_new_note()

def test_edit_company (browser):
    link = "https://guloans-staging.herokuapp.com/"
    page = LoginPage(browser, link)
    page.open()
    page.login_in_westfield()

    deals_page = DealsPage(browser, link)
    deals_page.select_first_deal_in_list()

    company_page = CompanyPage(browser, link)
    company_page.select_owner_account()
    company_page.edit_company_name(fake.company() + " qa/comp_name")
    company_page.edit_company_address(fake.address())
    company_page.edit_company_phone(fake.phone_number())
    company_page.edit_company_email(fake.email())
    company_page.edit_company_website()
    company_page.go_to_companies_list()

    companies_page = CompaniesPage(browser, link)
    companies_page.assert_name_first_company_in_list()

def test_edit_deal(browser):
    link = "https://guloans-staging.herokuapp.com/"
    page = LoginPage(browser, link)
    page.open()
    page.login_in_westfield()

    deals_page = DealsPage(browser, link)
    deals_page.select_first_deal_in_list()

    company_page = CompanyPage(browser, link)
    company_page.go_to_first_deal_tab()
    company_page.edit_stage_selector()
    company_page.edit_vendor_selector()
    company_page.edit_time_frame()
    company_page.edit_cosigners_first_name(fake.company() + " qa/cosigners_name")
    company_page.edit_lender()
    company_page.go_to_companies_list()
    company_page.assert_editing_deal()

def test_send_email(browser):
    link = "https://guloans-staging.herokuapp.com/"
    page = LoginPage(browser, link)
    page.open()
    page.login_in_westfield()

    deals_page = DealsPage(browser, link)
    deals_page.open_filter()
    deals_page.enter_cosigners_name_in_filter("qa-mkr4")
    deals_page.press_search_button()
    deals_page.select_first_deal_in_list()

    company_page = CompanyPage(browser, link)
    company_page.open_send_email_form()
    company_page.select_deal_for_send_email_form()
    # company_page.select_company_email() #we need check to companie's email correct and selected
    # company_page.select_cosigner_email()
    company_page.enter_additional_email("mkrtkv3@gmail.com,mkrtkv5@gmail.com")
    
    company_page.enter_email_subject("Hi autotest")
    company_page.enter_email_text("Олавом Белым звали одного конунга. Он был сыном конунга Ингьяльда, сына Хельги, сына Олава, сына Гудрёда, сына Хальвдана Белая Нога, конунга уппландцев.")
    company_page.send_email()

    # gmail_page = GmailPage(browser, link)
    # gmail_page.open()


def test_document_requests(browser):
    link = "https://guloans-staging.herokuapp.com/"
    page = LoginPage(browser, link)
    page.open()
    page.login_in_westfield()

    deals_page = DealsPage(browser, link)
    deals_page.open_filter()
    deals_page.enter_cosigners_name_in_filter("qa-mkr4")
    deals_page.press_search_button()
    deals_page.select_first_deal_in_list()

    company_page = CompanyPage(browser, link)
    company_page.open_document_requests_form()
    company_page.select_deal_document_requests_form()
    company_page.select_cosigner_document_requests_form()
    company_page.select_several_checkboxes()
    company_page.enter_additional_documents(fake.name()+","+fake.name())
    company_page.send_request_for_documents()
    company_page.assert_document_requests()