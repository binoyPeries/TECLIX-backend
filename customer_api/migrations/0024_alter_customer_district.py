# Generated by Django 3.2.6 on 2021-09-22 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_api', '0023_alter_customer_district'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='district',
            field=models.CharField(choices=[('Puttalam', 'Puttalam'), ('Anuradhapura', 'Anuradhapura'), ('Gampaha', 'Gampaha'), ('Kalutara', 'Kalutara'), ('Matale', 'Matale'), ('Hambantota', 'Hambantota'), ('Kilinochchi', 'Kilinochchi'), ('Ratnapura', 'Ratnapura'), ('Trincomalee', 'Trincomalee'), ('Monaragala', 'Monaragala'), ('Galle', 'Galle'), ('Ampara', 'Ampara'), ('Polonnaruwa', 'Polonnaruwa'), ('Matara', 'Matara'), ('Kegalle', 'Kegalle'), ('Batticaloa', 'Batticaloa'), ('Mannar', 'Mannar'), ('Vavuniya', 'Vavuniya'), ('Colombo', 'Colombo'), ('Mullaitivu', 'Mullaitivu'), ('Jaffna', 'Jaffna'), ('Nuwara Eliya', 'Nuwara Eliya'), ('Kandy', 'Kandy'), ('Kurunegala', 'Kurunegala'), ('Badulla', 'Badulla')], max_length=100),
        ),
    ]
