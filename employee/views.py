import jinja2
import os
import webapp2
from google.appengine.api import users
from google.appengine.ext import ndb
from .models import Employee, Role, SalarySheet, SalaryHistory


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader("templates"),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class EmployeePage(webapp2.RequestHandler):

    def get(self):
        employee_query = Employee.query()
        employees = employee_query.fetch(10)

        role_query = Role.query()
        roles = role_query.fetch(10)

        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        template_values = {
            'user': user,
            'employees': employees,
            'roles': roles,
            'url': url,
            'url_linktext': url_linktext,
        }

        template = JINJA_ENVIRONMENT.get_template('employee.html')
        self.response.write(template.render(template_values))

    def post(self):
        employe = Employee()
        role = Role.get_or_insert(self.request.get('role'))
        role.role = self.request.get('role')
        role.put()
        employe.name = self.request.get('name')
        employe.salary = float(self.request.get('salary'))
        # employe.role = Role(role=self.request.get('role'))
        employe.role = role
        # employe.hire_date = request.POST.get('hire_date')
        employe.new_hire_training_completed = True
        employe.put()

        employee_query = Employee().query()
        employees = employee_query.fetch(10)

        role_query = Role.query()
        roles = role_query.fetch(10)

        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        template_values = {
            'user': user,
            'employees': employees,
            'roles': roles,
            'url': url,
            'url_linktext': url_linktext,
        }

        template = JINJA_ENVIRONMENT.get_template('employee.html')
        self.response.write(template.render(template_values))


class SalaryPage(webapp2.RequestHandler):

    def get(self, employee_id):
        employee_id = self.request.get('employee_id')
        salary_query = SalaryHistory().query(SalaryHistory.employee.name=='rrrr')
        salaries = salary_query.fetch()

        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        template_values = {
            'user': user,
            'salaries': salaries,
            'employee_id': employee_id,
            'url': url,
            'url_linktext': url_linktext,
        }

        template = JINJA_ENVIRONMENT.get_template('salary.html')
        self.response.write(template.render(template_values))

    def post(self, employee_id):
        salary_history = SalaryHistory()
        # role = Role.get_or_insert(self.request.get('role'))
        # role.name = self.request.get('role')
        # role.put()
        salary_history.salary = float(self.request.get('salary'))
        # salary_history.date = self.request.get('date')
        # self.request.route_kwargs
        emp = Employee(id=employee_id)
        salary_history.employee = emp

        salary_history.put()
        salary_query = SalaryHistory(employee = Employee.get_by_id(employee_id)).query()
        salaries = salary_query.fetch()

        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        template_values = {
            'user': user,
            'salaries': salaries,
            'employee_id': Employee.get_or_insert(name='rrrr'),
            'url': url,
            'url_linktext': url_linktext,
        }

        template = JINJA_ENVIRONMENT.get_template('salary.html')
        self.response.write(template.render(template_values))