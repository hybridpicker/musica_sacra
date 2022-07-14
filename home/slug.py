from django.utils.text import slugify
import datetime

def create_slug_text(title):
    # Remove space and make every character low #
    title =  title.lower()
    # Checking for special characters and transform #
    chars = {'ö':'oe','ä':'ae','ü':'ue', 'ß':'ss',}
    for char in chars:
        title = title.replace(char,chars[char])
    # Check for other special characters #
    title = slugify(title)
    return title

def get_year_presentation(self):
    year = datetime.datetime.strptime(self, "%d.%m.%Y").date()
    year = int(year.year)
    return year