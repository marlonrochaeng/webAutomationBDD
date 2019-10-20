from behave import fixture, use_fixture
from selenium import webdriver
import os
from datetime import datetime
import pytest
from behave import fixture
from utilities.evidence_generator import EvidenceGenerator

SCREENSHOT = 'screenshots/'


def before_all(context):
    print("Executing before all")

def before_feature(context, feature):
    print("Before feature\n")

def before_scenario(context, scenario):
    print("Before scenario:")
    use_fixture(BrowserSetUp, context)
    use_fixture(GenerateEvidence, context, scenario)

def after_scenario(context, scenario):
    print("after scenario")
    context.driver.quit()

def after_feature(context, feature):
    print("\nAfter Feature")

def after_all(context):
    print("After scenario")


@fixture
def BrowserSetUp(context):
    """
        Esse método cria o browser através do parâmetro informado pela linha de comando
        parâmetro: --browser chrome (ou firefox)
    """
    print("Running browser setUp")
    if context.config.userdata['browser'] == 'firefox':
        print("Tests will be executed on Firefox")
        context.driver = webdriver.Firefox()
    elif context.config.userdata['browser'] == 'chrome':
        print("Tests will be executed on Chrome")
        context.driver = webdriver.Chrome(os.path.join("framework", "chromedriver.exe"))
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)

    yield context.driver
    

@fixture
def GenerateEvidence(context, scenario):
    """
        Esse método gera o documento de report geral após a execução dos casos de teste
    """
    pytest.time_start = datetime.now()
    pytest.time_start_format = "Test_Suit_Executed_At_" + pytest.time_start.strftime("%d_%m_%Y_%H_%M_%S")
    yield
    result = str(scenario.status)
    pytest.time_end = datetime.now()
    pytest.time_end_format = pytest.time_end.strftime("%d_%m_%Y_%H_%M_%S")
    doc = EvidenceGenerator("Test Automation Framework",
                            str((pytest.time_end - pytest.time_start).seconds) + 's', result)
    TEST_DIR = os.path.join(SCREENSHOT, str(pytest.time_start_format))
    if not os.path.exists(TEST_DIR):
        os.makedirs(TEST_DIR, exist_ok=True)
    dirs = os.listdir(TEST_DIR)
    for subdir in dirs:
        evidences = os.listdir(os.path.join(TEST_DIR, subdir))
        for e in evidences:
            doc.AddEvidence(subdir, e, os.path.join(TEST_DIR, subdir, e))
        doc.CreateDocument(os.path.join(TEST_DIR,subdir, "doc.docx"))
#behave -D browser=chrome