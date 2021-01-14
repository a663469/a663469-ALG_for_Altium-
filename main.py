from df import dfp
from db import db_altium_lib
import re
import pandas as pd

def test_resis(name, type_comp, cont, n_cont):
    if name and cont:
        if ' ' in cont: cont = re.split(r' ', cont.lower())
        if ' ' in name: splname = re.split(r' ', name.lower())
        if any(word in splname for word in cont):
            if n_cont:
                if ' ' in n_cont: n_cont = re.split(r' ', n_cont.lower())
                if any(word in splname for word in cont):
                    return False
            return type_comp
        else
            return False

#dfp.components(0, dfp.storage(0), 'resistors')
#print(db_altium_lib.sorting_rules(0, 'resistors'))

db_altium_lib = db_altium_lib()
#print(db_altium_lib.sorting_rules('resistors')['contains'])
#print(db_altium_lib.sorting_rules('resistors')['not_contains'])

#tmp = db_altium_lib.sorting_rules('resistors')['not_contains']
#tmp = db_altium_lib.sorting_rules('resistors')['contains']


dfp = dfp()
dfp.components(dfp.storage(), db_altium_lib.sorting_rules('resistors'))


#df.type = df.name.apply(lambda x: test_resis(x))
#df = df.query("name != 'NaN'")
#print(db_altium_lib.type_components())

df = dfp.storage()
df['type'] = 'NaN'
for rul in db_altium_lib.type_components():
    type_comp = rul['group_name']
    cont = rul['contains']
    n_cont = rul['not_contains']
    df.type = df.name.apply(lambda x: test_resis(x, type_comp, cont, n_cont))
