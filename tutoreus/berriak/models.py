from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from datetime import datetime
from tutoreus.utils import post_to_twitter

class Berria(models.Model):
    izenburua = models.CharField(max_length=64)
    slug = models.SlugField(db_index=True, help_text="Eremu honetan berri honen URL helbidea zehazten ari zara.")
    desk = models.TextField(max_length=256)
    
    erabiltzailea = models.ForeignKey(User)   
    publikoa_da = models.BooleanField() 
    pub_date = models.DateTimeField('publikazio data', default=datetime.now)
    mod_date = models.DateTimeField('modifikazio data', default=datetime.now)
    

    def get_desk_txikia(self):
    	return self.desk[:400]+'...'    
    
    
    class Meta:    
        verbose_name = "berria"
        verbose_name_plural = "berriak"

    def __unicode__(self):
        return u'%s' % (self.izenburua)

    def get_absolute_url(self):
        return "/azken-berriak/feed/"

post_save.connect(post_to_twitter, sender=Berria)