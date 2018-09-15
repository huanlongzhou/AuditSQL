# Generated by Django 2.1.1 on 2018-09-15 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sqlorders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MySQLQueryLog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='主键id')),
                ('user', models.CharField(max_length=30, verbose_name='用户名')),
                ('host', models.CharField(max_length=32, verbose_name='目标数据库地址')),
                ('database', models.CharField(max_length=32, verbose_name='目标数据库')),
                ('envi', models.SmallIntegerField(default=1, verbose_name='0：线上环境， 1：线下环境')),
                ('query_sql', models.TextField(default='', verbose_name='查询SQL')),
                ('query_time', models.CharField(default='', max_length=128, verbose_name='查询时间，单位s')),
                ('query_status', models.CharField(default='', max_length=2048, verbose_name='查询状态，成功或失败的原因')),
                ('affect_rows', models.IntegerField(default=0, verbose_name='影响行数')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='查询时间')),
            ],
            options={
                'verbose_name': 'mysql查询记录日志',
                'verbose_name_plural': 'mysql查询记录日志',
                'db_table': 'sqlaudit_sql_query_log',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='MysqlSchemasGrant',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='主键id')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('schema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sqlorders.MysqlSchemas', to_field='schema_join')),
            ],
            options={
                'verbose_name': 'SQL授权表',
                'verbose_name_plural': 'SQL授权表',
                'db_table': 'sqlaudit_schemas_grant',
                'default_permissions': (),
            },
        ),
    ]
