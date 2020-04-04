from django.db import models

# Create your models here.

class Tag(models.Model):
    Name = models.CharField(max_length=200, null=True, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Name

class Customer(models.Model):
    FirstName = models.CharField(max_length=200, null=True)
    LastName = models.CharField(max_length=200, null=True)
    Email = models.EmailField(max_length=254, unique=True)
    Phone = models.CharField(max_length=200, null=True, unique=True)
    Notes = models.TextField(max_length=500, null=True)
    Tags = models.ManyToManyField(Tag)
    Enabled = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.FirstName + ' ' + self.LastName

class Message(models.Model):
    MessageTypeOptions = (
        ('Promo', 'Promo'),
        ('Notification', 'Notification'),
    )
    DiscountTypeOptions = (
        ('Percent','Percent'),
        ('Money', 'Money'),

    )

    Type = models.CharField(max_length=200, null=True, choices=MessageTypeOptions)
    Name = models.CharField(max_length=200, null=True)
    Display = models.CharField(max_length=200, null=True)
    MessageText = models.TextField(max_length=500, null=True)
    Discount = models.BooleanField(default=False)
    DiscountType = models.CharField(max_length=200, null=True, choices=DiscountTypeOptions)
    DiscountAmount = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Name

class MessageLog(models.Model):
    Customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    Message = models.ForeignKey(Message, null=True, on_delete=models.SET_NULL)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.Customer) + ' - ' + str(self.Message) + ' On: ' + str(self.created_at)



