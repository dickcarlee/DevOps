import pytest
pytest.main(['--junitxml=report.xml', '--browser=phantomjs',  'testcases/*'])
