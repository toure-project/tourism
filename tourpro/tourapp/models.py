from django.db import models


class hotels(models.Model):
  H_Name =models.CharField( 'hotel name', max_length=120, default='3')
  Email =models.CharField( 'hotel name', max_length=120, default='3')
  Phon_Number =models.CharField( 'hotel name', max_length=120, default='3')
  H_Locaation =models.CharField( 'hotel addres', max_length=120, default='3')
  Superior_Room= models.CharField(max_length=30, default='3')
  Deluxe_Room= models.CharField(max_length=30, default='3')
  single_Occupation= models.CharField(max_length=30, default='3')
  Double_Occupation= models.CharField(max_length=30, default='3')  
  Photo = models.ImageField(null=True, blank=True, upload_to="images/")
def __str__(self):
    return self.H_Name


  