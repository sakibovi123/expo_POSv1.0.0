from django.db import models


class Projects(models.Model):
    title = models.CharField(max_length=120)
    thumb = models.ImageField(upload_to="images/")
    desc = models.TextField(max_length=1000)
    
        
    def __str__(self):
        return self.title
    

class Department(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=120)
    
    def __str__(self):
        return self.title


class Employee(models.Model):
    emp_id = models.IntegerField()
    emp_name = models.CharField(max_length=120)
    emp_email = models.CharField(max_length=120, unique=True)
    emp_contact = models.CharField(max_length=120, null=True, blank=True)
    emp_img = models.ImageField(upload_to="images/")
    ongoing_projects = models.ForeignKey(Projects, on_delete=models.CASCADE, null=True)
    emp_department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    salary = models.FloatField()
    status = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.emp_name



class Brand(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=120)
    brand_img = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title


class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=120)
    cat_img = models.ImageField(upload_to="images/")


    def __str__(self):
        return self.title


class Product(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=120)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    buying_price = models.FloatField()
    stock_qty = models.IntegerField()
    stock_stat = models.BooleanField(default=True)


    def __str__(self):
        return self.title


class PaymentMethod(models.Model):
    title = models.CharField(max_length=120)


    def __str__(self):
        return self.title


class SellProducts(models.Model):
    customer_name = models.CharField(max_length=120)
    phone = models.CharField(max_length=120)
    method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE, null=True)
    products = models.ManyToManyField(Product, null=True)
    quantity = models.IntegerField()
    selling_price = models.FloatField()
    discount = models.FloatField()
    total = models.FloatField()


    def __str__(self):
        return self.customer_name

    