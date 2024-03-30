from django.db import models


COMPANY_SIZE = (
    ("1", "1-10" ),
    ("2", "11-50" ),
    ("3", "51-200" ),
    ("4", "201-500" ),

)


INDUSTRY = (
    ("1", "Agriculture"),
    ("2", "Banking & Finance"),
    ("3", "Business Services & Software"),
)


Job_Role = (
    ("1", "C-Suite"),
    ("2", "VP"),
)


COUNTRY = (
    ("us", "United States"),
    ("afghanistan", "Afghanistan"),
    ("albania", "Albania"),
    ("algeria", "Algeria"),
    ("american samoa", "American Samoa"),
)


class Subscribe(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email

class Customers(models.Model):
    image = models.FileField(upload_to="promoters/")
    white_logo = models.FileField(upload_to="promoters/", blank=True, null=True)

class Features(models.Model):
    image = models.ImageField(upload_to="testimonials/")
    icon = models.FileField(upload_to="testimonials/")
    icon_bg = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    testimonial_description = models.TextField()
    testimonial_author = models.CharField(max_length=255)
    author_designation = models.CharField(max_length=255)
    testimonial_logo = models.FileField(upload_to="testimonials/")


    def __str__(self):
        return self.title


class VideoBlog(models.Model):
    image = models.ImageField(upload_to="videoBlog/")
    title = models.CharField(max_length=255)
    logo = models.FileField(upload_to="videoBlog/")


    def __str__(self):
        return self.title
    

class Testimonial(models.Model):
    image=models.ImageField(upload_to="Testimonials1/")
    logo = models.FileField(upload_to="Testimonials1/", blank=True, null=True)
    description = models.TextField()
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    is_featured = models.BooleanField()


    def __str__(self):
        return self.name
    

class MarketingFeatures(models.Model):
    image=models.FileField(upload_to="features/")
    title = models.CharField(max_length=255)
    description = models.TextField()


    def __str__(self):
        return self.title
    

class Product (models.Model):
    bg_color = models.CharField(max_length=255)
    logo = models.FileField(upload_to="products/")
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField()
    btn_color = models.CharField(max_length=255)
    image = models.FileField(upload_to="products/")
    hero_image = models.FileField(upload_to="products/hero_images/")
    product_bg_color = models.CharField(max_length=255)


    def __str__(self):
        return self.title
    

class Blog (models.Model):
    image = models.ImageField(upload_to="blogs/")
    title = models.CharField(max_length = 128)
    content_type = models.CharField(max_length=255)


    def __str__(self):
        return self.content_type


class Contact (models.Model):
    email = models.EmailField(max_length=255)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    company = models.CharField(max_length=128)
    company_size = models.CharField(max_length=128, choices = COMPANY_SIZE)
    industry = models.CharField(max_length=128, choices = INDUSTRY)
    job_role = models.CharField(max_length=128, choices = Job_Role)
    country = models.CharField(max_length=128, choices = COUNTRY)
    user_agreement = models.BooleanField(default=False)

    class Meta:
        db_table = 'web_contact'
        ordering = ("-id",)

    def __str__(self):
        return self.first_name 

