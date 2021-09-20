# Generated by Django 3.2.6 on 2021-09-20 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_api', '0018_alter_customer_district'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='district',
            field=models.CharField(choices=[('Badulla', 'Badulla'), ('Ampara', 'Ampara'), ('Nuwara Eliya', 'Nuwara Eliya'), ('Ratnapura', 'Ratnapura'), ('Monaragala', 'Monaragala'), ('Mullaitivu', 'Mullaitivu'), ('Gampaha', 'Gampaha'), ('Kandy', 'Kandy'), ('Hambantota', 'Hambantota'), ('Anuradhapura', 'Anuradhapura'), ('Batticaloa', 'Batticaloa'), ('Puttalam', 'Puttalam'), ('Galle', 'Galle'), ('Polonnaruwa', 'Polonnaruwa'), ('Colombo', 'Colombo'), ('Matara', 'Matara'), ('Mannar', 'Mannar'), ('Trincomalee', 'Trincomalee'), ('Vavuniya', 'Vavuniya'), ('Jaffna', 'Jaffna'), ('Kalutara', 'Kalutara'), ('Matale', 'Matale'), ('Kilinochchi', 'Kilinochchi'), ('Kegalle', 'Kegalle'), ('Kurunegala', 'Kurunegala')], max_length=100),
        ),
    ]
