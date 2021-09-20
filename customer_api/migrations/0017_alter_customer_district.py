# Generated by Django 3.2.6 on 2021-09-20 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_api', '0016_auto_20210919_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='district',
            field=models.CharField(choices=[('Matale', 'Matale'), ('Ratnapura', 'Ratnapura'), ('Batticaloa', 'Batticaloa'), ('Ampara', 'Ampara'), ('Kalutara', 'Kalutara'), ('Monaragala', 'Monaragala'), ('Trincomalee', 'Trincomalee'), ('Kegalle', 'Kegalle'), ('Mullaitivu', 'Mullaitivu'), ('Gampaha', 'Gampaha'), ('Matara', 'Matara'), ('Polonnaruwa', 'Polonnaruwa'), ('Kandy', 'Kandy'), ('Nuwara Eliya', 'Nuwara Eliya'), ('Puttalam', 'Puttalam'), ('Jaffna', 'Jaffna'), ('Galle', 'Galle'), ('Colombo', 'Colombo'), ('Hambantota', 'Hambantota'), ('Vavuniya', 'Vavuniya'), ('Badulla', 'Badulla'), ('Kurunegala', 'Kurunegala'), ('Mannar', 'Mannar'), ('Anuradhapura', 'Anuradhapura'), ('Kilinochchi', 'Kilinochchi')], max_length=100),
        ),
    ]
