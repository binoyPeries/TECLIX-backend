# Generated by Django 3.2.6 on 2021-09-23 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_api', '0020_auto_20210920_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='district',
            field=models.CharField(choices=[('Polonnaruwa', 'Polonnaruwa'), ('Kandy', 'Kandy'), ('Kurunegala', 'Kurunegala'), ('Jaffna', 'Jaffna'), ('Mannar', 'Mannar'), ('Matara', 'Matara'), ('Gampaha', 'Gampaha'), ('Ampara', 'Ampara'), ('Trincomalee', 'Trincomalee'), ('Matale', 'Matale'), ('Ratnapura', 'Ratnapura'), ('Hambantota', 'Hambantota'), ('Kalutara', 'Kalutara'), ('Batticaloa', 'Batticaloa'), ('Galle', 'Galle'), ('Monaragala', 'Monaragala'), ('Badulla', 'Badulla'), ('Kegalle', 'Kegalle'), ('Anuradhapura', 'Anuradhapura'), ('Kilinochchi', 'Kilinochchi'), ('Colombo', 'Colombo'), ('Puttalam', 'Puttalam'), ('Nuwara Eliya', 'Nuwara Eliya'), ('Vavuniya', 'Vavuniya'), ('Mullaitivu', 'Mullaitivu')], max_length=100),
        ),
        migrations.AlterField(
            model_name='customer',
            name='loyalty_points',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='customer',
            name='outstanding',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='customer',
            name='profile_picture',
            field=models.ImageField(blank=True, max_length=255, upload_to='customer/'),
        ),
    ]