# pyRelations
Small Python library for turning lists into relational record entries


## Example
```
>>> from pyrelations import Table
>>> table = Table(['ID','First','Last'])
>>> table.insert([1,'The','Name'])
>>> table.records
[[1, 'The', 'Name']]
>>> table.insert([2,'name','too','long'])
pyRecords error: Length of record does not match number of table columns
>>> table.records
[[1, 'The', 'Name']]
```