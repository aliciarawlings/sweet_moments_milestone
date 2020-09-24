#from django.db.models.signal import post_save, post_delete
#from django.dispatch import receiver
#from .models import OrderItem


#@receiver(post_delete, sender=OrderItem)
#def update_save(sender, instance, **kwargs):
 #   instance.order.update_total()



#@receiver(post_delete, sender=OrderItem)
#def update_on_save(sender, instance, **kwargs):
  
 #   instance.order.update_total()