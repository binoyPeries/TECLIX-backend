# Generated by Django 3.2.6 on 2021-09-26 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_api', '0027_merge_20210924_0754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='district',
            field=models.CharField(choices=[('Kalutara', 'Kalutara'), ('Batticaloa', 'Batticaloa'), ('Hambantota', 'Hambantota'), ('Kurunegala', 'Kurunegala'), ('Mannar', 'Mannar'), ('Monaragala', 'Monaragala'), ('Colombo', 'Colombo'), ('Anuradhapura', 'Anuradhapura'), ('Galle', 'Galle'), ('Jaffna', 'Jaffna'), ('Gampaha', 'Gampaha'), ('Ratnapura', 'Ratnapura'), ('Mullaitivu', 'Mullaitivu'), ('Kilinochchi', 'Kilinochchi'), ('Puttalam', 'Puttalam'), ('Nuwara Eliya', 'Nuwara Eliya'), ('Polonnaruwa', 'Polonnaruwa'), ('Kegalle', 'Kegalle'), ('Vavuniya', 'Vavuniya'), ('Badulla', 'Badulla'), ('Matale', 'Matale'), ('Ampara', 'Ampara'), ('Matara', 'Matara'), ('Kandy', 'Kandy'), ('Trincomalee', 'Trincomalee')], max_length=100),
        ),
        migrations.AlterField(
            model_name='customerlatepay',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
