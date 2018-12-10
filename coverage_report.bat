call mkvirtualenv jenkins_test
pip install pytest
pip install coverage
coverage run script_test.py
coverage report -m
coverage xml -o coverage_report.xml
coverage html -d coverage
rmvirtualenv jenkins_test