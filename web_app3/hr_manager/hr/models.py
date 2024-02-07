from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator  # PT VALIDAREA LA SALARIU WaGE

# modifici model, faci migrari 'makemigrations" sa vada migrarile din cod in db, executi migrarile cu manage.py migrate
AuthUserModel = get_user_model()  # selecteaza userii


# Create your models here.
class MyModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Employer(MyModel):
    class Meta:
        db_table = 'employers'

    name = models.CharField(max_length=255, unique=True, null=False)
    owner = models.ForeignKey(AuthUserModel, on_delete=models.CASCADE, null=False, default=1)
    employees = models.ManyToManyField(AuthUserModel, through='Employee', related_name='employees')

    def get_employees_nr(self):
        return self.employees.count()


class Employee(MyModel):
    class Meta:
        db_table = 'employees'

    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    user = models.ForeignKey(AuthUserModel, on_delete=models.CASCADE)

    wage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=100.00,
        null=False,
        validators=[MinValueValidator(0.00)]
    )

    def __str__(self):
        return self.user.email

    def first_name(self):
        return self.user.first_name

    first_name.short_description = 'First Name'
    first_name.order_field='user__first_name'

    def last_name(self):
        return self.user.last_name

    last_name.short_description = 'Last Name'
    last_name.order_field = 'user__last_name'

    def employer_name(self):
        return self.employer.name

    employer_name.short_description = 'Employer'
    employer_name.order_field = 'employer__name'


class Profile(MyModel):  # aici py manage.py makemigrate sa migreze si tabelu asta in db + py manage.py migrate salvezi
    class Meta:
        db_table = 'profiles'

    # facem profil din user in profile, daca stergi profil se sterge si user si invers
    user = models.OneToOneField(AuthUserModel, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='profiles', null=True, default=None)
