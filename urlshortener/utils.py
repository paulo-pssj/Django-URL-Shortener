"""
Utilities for Shortener
"""
from django.conf import settings
from random import choice
from string import ascii_letters, digits

SIZE = getattr(settings, "MAXIMUM_URL_CHARS", 7)

AVALIABLE_CHARS = ascii_letters + digits

def create_random_code(chars=AVALIABLE_CHARS):
    """
    Creates a random string with the predetermined size
    """
    return "".join(
        [choice(chars) for _ in range(SIZE)]
    )
    
def create_shortened_url(model_instance):
    random_code = create_random_code()
    
    # Gets the model class
    model_class = model_instance.__class__
    
    if model_class.objects.filter(short_url=random_code).exists():
        # run the function again
        return create_shortened_url(model_instance)
    
    return random_code