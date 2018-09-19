# OVStat
Python OvChipkaart API Wrapper Package

Install with: 
```bash
python setup.py install
```
This will install the ovstat package.

####Example
```python
from ovstat.OvApi import OvApi
import json
o = OvApi("username", "password")
cards = o.get_cards_list()
for card in cards:
    records = o.get_transaction_list(card['mediumId'])
    card['transactions'] = records
print(json.dumps(cards))
```
