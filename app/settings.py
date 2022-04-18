import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.abspath(os.path.join(BASE_DIR, '.'))
sys.path.append(PROJECT_DIR)

APP_VERSION = '1.0.0'

# Test results
JUNIT_MERGE_FILES = 'junit_merge.xml'
JUNIT_TEST_RESULTS = os.getenv('JUNIT_TEST_RESULTS', "")
JACOCO_REPORTS = os.getenv("JACOCO_REPORTS", "")
SLACK_URL = os.getenv("SLACK_URL", "")



PASS_COLOR = "#3CB371"
FAIL_COLOR = "#DC143C"
