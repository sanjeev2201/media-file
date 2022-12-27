# code
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import Teacher,Student


@receiver(post_save, sender=Teacher)
def create_profile(sender, instance, created, **kwargs):
    if created:
        print('instance:',instance)
        print("Teacher table created")
		#Teacher.objects.create(user=instance)
    else:
        print("teacher instance not created")
        
    

@receiver(post_save, sender=Student)
def save_profile(sender, instance,created,**kwargs):
    if created:
        print('Instance:',instance)
        print('Student table created')
    else:
        print('student data not created')
