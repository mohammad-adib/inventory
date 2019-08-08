from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime

# Create your models here.


class Product(models.Model):


    ######## S A I L  P R O P E R T I E S  &  A V A I L A B I L I T Y ########


    def __str__(self):
        return self.ahz_serial_number

    #  Product Code (if available)
    sku = models.CharField(max_length=200,null=True,blank=True)
    
    # Product Serial Number by Company
    ahz_serial_number = models.CharField(default='Some Serial****',max_length=200)

    # Product Serial Number by Brand (if available)
    product_serial_number = models.CharField(default='Some Serial****',max_length=200,null=True,blank=True)

    # Price
    price = models.IntegerField(default=0)

    # Discounted Price
    price_offer = models.IntegerField(default=0)

    # Brand [I added this myself.]
    brand = models.CharField(max_length=200,default="new brand")


    # Exists in store?
    is_in_store = models.BooleanField(default=True)


    ######## F E A T U R E S  &  S P E C I F I C A T I O N S ########


    buckle = models.CharField(default='Some Feature****',max_length=200)                   # Didn't know the type, Assumed a string

    color = models.CharField(default='Some Feature****',max_length=200)                    # Didn't know the type, Assumed a string 

    case_material = models.CharField(default='Some Feature****',max_length=200)            # Didn't know the type, Assumed a string   

    case_shape = models.CharField(default='Some Feature****',max_length=200)               # Didn't know the type, Assumed a string   

    case_thickness = models.FloatField(default=0.0)

    chronograph = models.CharField(default='Some Feature****',max_length=200)              # Didn't know the type, Assumed a string

    country_of_manufacture = models.CharField(default='Some Feature****',max_length=50)

    dial_color = models.CharField(default='Some Feature****',max_length=200)               # Didn't know the type, Assumed a string

    feature = models.CharField(default='Some Feature****',max_length=200)                  # Didn't know the type, Assumed a string

    movement = models.CharField(default='Some Feature****',max_length=200)                 # Didn't know the type, Assumed a string

    M = "Men"; W = "Women"; sex_group = ( (M,'Men') , (W,'Women'))
    sex = models.CharField(max_length=5, choices=sex_group, default=M)

    strap = models.CharField(default='Some Feature****',max_length=200)                    # Didn't know the type, Assumed a string

    strap_color = models.CharField(default='Some Feature****',max_length=200)              # Didn't know the type, Assumed a string

    strap_width = models.FloatField(default=0.0)

    warranty = models.CharField(default='Some Feature****',max_length=200)                 # Didn't know the type, Assumed a string

    water_resistance = models.BooleanField(default=False)

    weight = models.FloatField(default=0.0)

    _category = models.CharField(default='Some Feature****',max_length=200)                # Didn't know the type, Assumed a string

    application = models.CharField(default='Some Feature****',max_length=200)              # Didn't know the type, Assumed a string

    short_description =  models.TextField(default='Some Text****',blank=True, null=True)

    case_diameter = models.FloatField(default=0.0)

    glass = models.CharField(default='Some Feature****',max_length=200)                    # Didn't know the type, Assumed a string

    case_back = models.CharField(default='Some Feature****',max_length=200)                # Didn't know the type, Assumed a string

    bezel = models.CharField(default='Some Feature****',max_length=200)                    # Didn't know the type, Assumed a string

    bezel_color = models.CharField(default='Some Feature****',max_length=200)              # Didn't know the type, Assumed a string

    movement_energy = models.CharField(default='Some Feature****',max_length=200)          # Didn't know the type, Assumed a string

    product_family = models.CharField(default='Some Feature****',max_length=200)           # Didn't know the type, Assumed a string

    watches_gifts = models.CharField(default='Some Feature****',max_length=200)            # Didn't know the type, Assumed a string

    luminous = models.BooleanField(default=False)               # Didn't know the type, Assumed a boolean

    stopwatches = models.BooleanField(default=False)            # Didn't know the type, Assumed a boolean

    countdown_timer = models.BooleanField(default=False)        # Didn't know the type, Assumed a boolean

    impact_resistant = models.BooleanField(default=False)       # Didn't know the type, Assumed a boolean

    moon_phase = models.BooleanField(default=False)             # Didn't know the type, Assumed a boolean

    skeleton = models.CharField(default='Some Feature****',max_length=200)                 # Didn't know the type, Assumed a string

    mother_of_pearl = models.CharField(default='Some Feature****',max_length=200)          # Didn't know the type, Assumed a string

    day = models.CharField(default='Some Feature****',max_length=200)                      # Didn't know the type, Assumed a string

    date = models.CharField(default='Some Feature****',max_length=200)                     # Didn't know the type, Assumed a string

    month = models.CharField(default='Some Feature****',max_length=200)                    # Didn't know the type, Assumed a string

    limited_number = models.CharField(default='Some Feature****',max_length=200)           # Didn't know the type, Assumed a string

    gold = models.BooleanField(default=False)                   # Didn't know the type, Assumed a boolean

    diamond = models.BooleanField(default=False)                # Didn't know the type, Assumed a boolean

    jewellery = models.BooleanField(default=False)              # Didn't know the type, Assumed a boolean

    open_heart = models.BooleanField(default=False)             # Didn't know the type, Assumed a boolean

    hour_24 = models.BooleanField(default=False)                # Didn't know the type, Assumed a boolean

    dual_time = models.BooleanField(default=False)              # Didn't know the type, Assumed a boolean

    tachymeter = models.BooleanField(default=False)             # Didn't know the type, Assumed a boolean

    big_date = models.BooleanField(default=False)               # Didn't know the type, Assumed a boolean

    gmt = models.BooleanField(default=False)                    # Didn't know the type, Assumed a boolean

    light = models.BooleanField(default=False)                  # Didn't know the type, Assumed a boolean

    alarm = models.BooleanField(default=False)                  # Didn't know the type, Assumed a boolean

    compass = models.BooleanField(default=False)                # Didn't know the type, Assumed a boolean 

    altimeter = models.BooleanField(default=False)              # Didn't know the type, Assumed a boolean

    barometric = models.BooleanField(default=False)             # Didn't know the type, Assumed a boolean

    thermometer = models.BooleanField(default=False)            # Didn't know the type, Assumed a boolean

    gps_atomic_solar_hybrid = models.BooleanField(default=False) # Didn't know the type, Assumed a boolean


class Store(models.Model):
    
    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)

    serial = models.CharField(max_length=200)

    number_of_visitors = models.IntegerField(default=0)

    products = models.ManyToManyField(Product,through = 'Availability')


class Availability(models.Model):

    number_of_products=models.IntegerField(default=1)

    ######## R E L A T I O N S H I P S ########
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
