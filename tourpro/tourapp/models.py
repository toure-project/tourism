from django.db import models

class reat(models.Model):
  title = models.CharField(max_length=120)

  def __str__(self):
    return self.title


class hotels(models.Model):
  H_Name =models.CharField( 'hotel name', max_length=120)
  level = models.ForeignKey(reat,blank= True, null=True, on_delete=models.CASCADE)
  H_Locaation =models.CharField( 'hotel addres', max_length=120)
  Discreption = models.TextField(max_length=200)
  Payment =models.CharField(max_length =120)
  #photo =
def __str__(self):
    return self.name
