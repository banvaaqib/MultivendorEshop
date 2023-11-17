from django.db import models
from ckeditor.fields import RichTextField # isko humne admin panel me text box acha mile yani zayada feture vala
from django.utils.text import slugify      # slugify ko humne slug fild ke liye import kiya he
from django.db.models.signals import pre_save # pre_save ko bhi humne slug fild ke liye import kiya he




# Create your models here.

# slider model Code Start

class slider(models.Model):
    DISCOUNT_DEAL =(
        ('HOT DEALS', 'HOT DEALS'),
        ('New Arraivels', 'New Arraivels'),

    )

    Image = models.ImageField(upload_to='media/slider_imgs')
    Discount_Deal =models.CharField(choices=DISCOUNT_DEAL,max_length=100)
    Sale = models.IntegerField()
    Brand_Name =models.CharField(max_length=200)
    Discount = models.CharField(max_length=200)
    Link = models.CharField(max_length=300)

    def __str__(self):
        return self.Brand_Name

# slider model Code End


# banner_area model Code Start

class banner_area(models.Model):
    Image = models.ImageField(upload_to='media/banner_imgs')
    banner_title1 = models.CharField(max_length=100)
    banner_title2 = models.CharField(max_length=100)
    Discount_Deal =models.CharField(max_length=100)
    Link = models.CharField(max_length=300, null=True)


    def __str__(self):
        return self

# banner_area model Code End


# Main_Category model Code Start

class Main_Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Main_Category model Code End


# Category model Code Start

class Category(models.Model):
    main_category = models.ForeignKey(Main_Category,on_delete=models.CASCADE)
    name= models.CharField(max_length=100)

    def __str__(self):
        return self.name + "--" + self.main_category.name

# Category model Code End


# Sub_Category model Code Start

class Sub_Category(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.category.main_category.name + " -- " + self.category.name + " -- " + self.name

# Sub_Category model Code End

# Section model Code Start

class Section(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Section model Code End

# Product model Code Start

class Product(models.Model):
    total_quantity = models.IntegerField()
    Availability = models.IntegerField()
    featured_image = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    price = models.IntegerField()
    Discount = models.IntegerField()
    # Product_Information = models.TextField()
    Product_information = RichTextField(null=True)
    model_Name = models.CharField(max_length=100)
    Categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    Tags = models.CharField(max_length=200)
    # Discription = models.TextField()
    Discription = RichTextField()

    section = models.ForeignKey(Section,on_delete=models.DO_NOTHING)
    slug = models.SlugField(default='', max_length=500, null=True, blank=True)

    def __str__(self):
        return self.product_name

# Product model Code End

    # slug fild code start
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("product_detail", kwargs={'slug': self.slug})

    class Meta:
        db_table = "app_Product"

def create_slug(instance, new_slug=None):
    slug = slugify(instance.product_name)
    if new_slug is not None:
        slug = new_slug
    qs = Product.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, Product)

# slug fild code End

# Product_Image model Code Start

class Product_Image(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    Image_url = models.CharField(max_length=200)

# Product_Image model Code End


# Additional_Information model Code Start

class Additional_Information(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    specification = models.CharField(max_length=200)
    details = models.CharField(max_length=200)

# Additional_Information model Code End









