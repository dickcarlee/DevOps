import pytest
pytest.main(['--html=report.html', '--junitxml=report.xml', '--browser=phantomjs',  'testcases/devops_login_test.py'])
