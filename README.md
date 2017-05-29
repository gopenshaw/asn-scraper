Example usage:

As a python module:
```python
import asn_scraper
asns = asn_scraper.get_all_asns()
asns[36375]
# {'Country': u'US',
# 'Name': u'University of Michigan',
# 'Routes v4': 14,
# 'Routes v6': 1}
```

From command line:
```
# write json data to out.txt
python asn_scraper.py out.txt
head out.txt
# {
#      "1": {
#         "Country": "US", 
#         "Name": "Level 3 Communications, Inc.", 
#         "Routes v4": 11, 
#         "Routes v6": 0
#     }, 
#     "2": {
#         "Country": "US", 
#         "Name": "University of Delaware", 
```
