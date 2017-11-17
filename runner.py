import pytest
pytest.main(['--junitxml=report.xml', '--html=report.html', '--browser=phantomjs',  'testcases'])
