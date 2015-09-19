from google.appengine.ext import ndb


class Role(ndb.Model):
    role = ndb.StringProperty()


class Employee(ndb.Model):
  name = ndb.StringProperty()
  role = ndb.StructuredProperty(Role)
  hire_date = ndb.DateProperty(indexed=False)
  new_hire_training_completed = ndb.BooleanProperty(indexed=False)
  email = ndb.StringProperty()
  salary = ndb.FloatProperty()


class SalaryHistory(ndb.Model):
    employee = ndb.StructuredProperty(Employee)
    salary = ndb.FloatProperty()
    date = ndb.DateProperty(auto_now_add=True)

class SalarySheet(ndb.Model):
    employee = ndb.StructuredProperty(Employee)
    absent_days = ndb.IntegerProperty()
    year = ndb.IntegerProperty()
    month = ndb.IntegerProperty()
    date = ndb.DateProperty(indexed=False)