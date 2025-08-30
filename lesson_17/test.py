import sys, inspect
from pathlib import Path
BASE = Path(__file__).resolve().parent / "randominfo" / "randominfo-master"
sys.path.insert(0, str(BASE))

import randominfo
print("USING:", randominfo.__file__)
print("HAS idx check? ->", "addr[i]" in inspect.getsource(randominfo.get_address))

p = randominfo.Person()
print(p.full_name, p.gender, p.country, p.address)



