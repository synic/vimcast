from django.db import models

DEPARTMENTS = ( # {{{
    ('sales',       'Sales'),
    ('executive',   'Executive'),
    ('developers',  'Developers'),
    ('support',     'Customer Support'),
) # }}}

class Employee(models.Model):
    """
    This model represents employees in the company
    """
    employee_first_name = models.CharField(max_length=100)
    employee_last_name = models.CharField(max_length=100)
    employee_phone = models.CharField(max_length=40)
    employee_department = models.CharField(max_length=20, db_index=True,
        help_text="Department, leave null if you don't see the correct "
        "option here.", null=True, blank=True)

    address = models.CharField("Address, Line 1", max_length=255)
    address_two = models.CharField("Address, Line 2", max_length=255)
