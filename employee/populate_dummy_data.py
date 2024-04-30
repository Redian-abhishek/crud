from django.core.management.base import BaseCommand
from faker import Faker
from employee.models import Employee  # Import your Employee model

fake = Faker()

class Command(BaseCommand):
    help = 'Populate the database with dummy employee data'

    def add_arguments(self, parser):
        parser.add_argument('num_records', type=int, help='Number of dummy records to create')

    def handle(self, *args, **options):
        num_records = options['num_records']
        
        for _ in range(num_records):
            eid = fake.uuid4()[:8]  # Generate a random 8-character ID
            ename = fake.name()
            eemail = fake.email()
            econtact = fake.phone_number()

            employee = Employee(eid=eid, ename=ename, eemail=eemail, econtact=econtact)
            employee.save()

        self.stdout.write(self.style.SUCCESS(f'Successfully populated {num_records} employee records'))
