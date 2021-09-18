# Generated by Django 3.2.6 on 2021-09-18 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asset_api', '0003_alter_product_category'),
        ('customer_api', '0007_auto_20210918_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='district',
            field=models.CharField(choices=[('Gampaha', 'Gampaha'), ('Ratnapura', 'Ratnapura'), ('Kurunegala', 'Kurunegala'), ('Mullaitivu', 'Mullaitivu'), ('Puttalam', 'Puttalam'), ('Galle', 'Galle'), ('Ampara', 'Ampara'), ('Nuwara Eliya', 'Nuwara Eliya'), ('Polonnaruwa', 'Polonnaruwa'), ('Kegalle', 'Kegalle'), ('Kalutara', 'Kalutara'), ('Vavuniya', 'Vavuniya'), ('Matara', 'Matara'), ('Kandy', 'Kandy'), ('Trincomalee', 'Trincomalee'), ('Anuradhapura', 'Anuradhapura'), ('Matale', 'Matale'), ('Colombo', 'Colombo'), ('Mannar', 'Mannar'), ('Batticaloa', 'Batticaloa'), ('Hambantota', 'Hambantota'), ('Jaffna', 'Jaffna'), ('Kilinochchi', 'Kilinochchi'), ('Monaragala', 'Monaragala'), ('Badulla', 'Badulla')], max_length=100),
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer_api.serviceorder')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asset_api.product')),
            ],
        ),
    ]