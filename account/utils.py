import random
import string
from django.utils.text import slugify

def random_string_generator(size=5, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))



def unique_slug_generator(instance, new_slug=None):

    if new_slug is not None:
        slug = new_slug
    else:
        if hasattr(instance,'title') :
            slug = slugify(instance.title)
        elif hasattr(instance,'subjet') :
            slug = slugify(instance.subject)
        elif hasattr(instance,'name') :
            slug = slugify(instance.name)
        elif hasattr(instance,'student'):
            slug = slugify(instance.student.user.username)
        else :
            slug = slugify(instance.user.username)
    Model = instance.__class__
    qs_exists = Model.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
                    slug=slug,
                    randstr=random_string_generator(size=4)
                )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug