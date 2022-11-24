This is test password strength.
The following module will be tested :
1) SQLITE
2) Pytest
3) Jenkins

The following package must be installed:
1) pip install pytest-html


To Run pytest Please use the following commands:
pytest run_python.py

Generate Report :
pytest run_python.py --html=Report.html

This is thr basic test testing password strength 
if password can consists  of any catagory like  alphabet,number, special charactor,and upper case charactor .
we can consider password stength "Strong","Medium" or "Poor".
  1) if only 1 catagory then poor
  2) if more than 1 catagory then medium
  3) if more than 2 category then Strong

Activate python conda create environment:

conda create -n pytest_env python=3.8
conda activate pytest_env
pip install -r requirements.txt


How to open Jenkins:
java -jar jenkins.war