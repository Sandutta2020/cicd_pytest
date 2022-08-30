import importlib
import pandas as pd
from  classfile.pass_check import check_password_strength
import pytest
import warnings
warnings.filterwarnings("ignore")
interface_component = importlib.import_module('classfile.' + 'class_loading')
my_class = getattr(interface_component, 'class_loading')
my_instance = my_class()
df =my_instance.run()
print(df.values)
@pytest.mark.skip
def test_password():
   num = check_password_strength('santanu1')
   assert num == 'Medium'
@pytest.mark.skip
@pytest.mark.parametrize("passd, strength",[('san','Medium'),('Passwords1','Strong')])
def test_passwords_params(passd, strength):
    num = check_password_strength(passd)
    assert num == strength
@pytest.mark.parametrize("passd, strength",list(df.itertuples(index=False)))
def test_passwords_df(passd, strength):
    num = check_password_strength(passd)
    assert num == strength