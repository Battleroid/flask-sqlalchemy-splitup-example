flask-sqlalchemy-splitup-example
================================

Example for my own sanity. Split up models and blueprints. Went crazy temporarily trying to make sure this worked properly.

Need to create database on initial start, using manager? Can't remember. Either way do:

```python
>>> from thing import db
>>> db.create_all()
```
