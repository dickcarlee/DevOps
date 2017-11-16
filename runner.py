import pytest
pytest.main(['--junitxml=report.xml', '--browser=phantomjs',  'testcases/devops_login_test.py'])
