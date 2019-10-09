# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BooksOnTheTable2(models.Model):
    id = models.IntegerField(primary_key=True)
    book_name = models.CharField(max_length=20, blank=True, null=True)
    the_author = models.CharField(max_length=20, blank=True, null=True)
    pricing = models.CharField(max_length=20, blank=True, null=True)
    dna_dan_jia = models.CharField(max_length=20, blank=True, null=True)
    version_of_the_club = models.CharField(max_length=20, blank=True, null=True)
    edition = models.CharField(max_length=20, blank=True, null=True)
    impression = models.CharField(max_length=20, blank=True, null=True)
    number_of_words = models.CharField(max_length=20, blank=True, null=True)
    number_of_pages = models.CharField(max_length=20, blank=True, null=True)
    size = models.CharField(max_length=20, blank=True, null=True)
    the_paper = models.CharField(max_length=20, blank=True, null=True)
    packaging = models.CharField(max_length=20, blank=True, null=True)
    printing_time = models.CharField(max_length=20, blank=True, null=True)
    the_editors_recommend = models.TextField(blank=True, null=True)
    plot_summary = models.TextField(blank=True, null=True)
    about_the_author = models.TextField(blank=True, null=True)
    catalogue = models.TextField(blank=True, null=True)
    meddia_comments = models.TextField(blank=True, null=True)
    highlights_illustrations = models.CharField(max_length=100, blank=True, null=True)
    whether_suit = models.CharField(max_length=20, blank=True, null=True)
    trying_to_read_online = models.TextField(blank=True, null=True)
    classify = models.CharField(max_length=20, blank=True, null=True)
    isbn_id = models.IntegerField(db_column='ISBN_id')  # Field name made lowercase.
    bei_4 = models.CharField(max_length=10, blank=True, null=True)
    bei_5 = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'books_on_the_table2'
        unique_together = (('id', 'isbn_id'),)


class County2(models.Model):
    id = models.IntegerField(primary_key=True)
    county_county = models.CharField(max_length=20, blank=True, null=True)
    province_id = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'county2'


class InTheClassification(models.Model):
    taxon = models.CharField(max_length=20, blank=True, null=True)
    id = models.IntegerField(primary_key=True)
    taxon_id = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'in_the_classification'


class OrderList(models.Model):
    id = models.IntegerField(primary_key=True)
    id_id = models.CharField(max_length=20, blank=True, null=True)
    order_reference = models.CharField(max_length=20, blank=True, null=True)
    order_time = models.CharField(max_length=20, blank=True, null=True)
    order_amount = models.CharField(max_length=20, blank=True, null=True)
    user_id = models.CharField(max_length=20, blank=True, null=True)
    shu = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'order_list'


class Province(models.Model):
    id = models.IntegerField(primary_key=True)
    province_city = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'province'


class Shopping(models.Model):
    id = models.IntegerField(primary_key=True)
    isbn_id = models.CharField(db_column='ISBN_id', max_length=20, blank=True, null=True)  # Field name made lowercase.
    id_id = models.CharField(max_length=20, blank=True, null=True)
    user_id = models.CharField(max_length=20)
    book_id = models.CharField(max_length=20)
    quantity = models.CharField(max_length=20, blank=True, null=True)
    get = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shopping'


class Site(models.Model):
    id = models.IntegerField(primary_key=True)
    consignee = models.CharField(max_length=20, blank=True, null=True)
    shipping_address = models.CharField(max_length=20, blank=True, null=True)
    detailed_address = models.CharField(max_length=20, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    cell_phone_number = models.CharField(max_length=20, blank=True, null=True)
    user_id = models.CharField(max_length=20)
    column_8 = models.CharField(db_column='Column_8', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'site'


class TheOrderContent(models.Model):
    id = models.IntegerField(primary_key=True)
    order_list_id = models.CharField(max_length=20)
    quantity = models.CharField(max_length=20, blank=True, null=True)
    price = models.CharField(max_length=20, blank=True, null=True)
    books_on_the_table2 = models.CharField(max_length=20)
    isbn_id = models.CharField(db_column='ISBN_id', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'the_order_content'


class Town(models.Model):
    id = models.IntegerField(primary_key=True)
    town_town = models.CharField(max_length=20, blank=True, null=True)
    village_id = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'town'


class User(models.Model):
    id = models.CharField(max_length=20,primary_key=True)
    pow = models.CharField(max_length=20, blank=True, null=True)
    id_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user'
        unique_together = (('id', 'id_id'),)


class Village(models.Model):
    id = models.IntegerField(primary_key=True)
    village_village = models.CharField(max_length=20, blank=True, null=True)
    county_id = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'village'
