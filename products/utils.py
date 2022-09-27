import random
import string
from django.utils.text import slugify

def random_string_generator(size=10, chrs=string.ascii_lowercase + string.digits):
  return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, new_slug=None):
  if new_slug in not None:
    slug = new_slug
  else:
    slug = slugify(instance.title)
    
  Klass = instance.__class__
  qs_exists = Klass.objects.filter(slug=slug).exists()
  if qs_exists:
    new_slug = "{slug}-{srandstr}".format(slug=slug, randstr=random_string_generator(size=4))
    return unique_slug_generator(instance, new_slug=new_slug)
  return slug
