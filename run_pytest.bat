call mkvirtualenv jenkins_test
pip install pytest
pytest
call deactivate jenkins_test
call rmvirtualenv jenkins_test