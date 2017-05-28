from django.db import models

class Topic(models.Model):
    text = models.CharField(max_length = 200)
    data_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text     #returns whatever text was inputted into the topic entry
'''
takes text for the Topic instance with length of up to 200.
'''
# Create your models here.

class Entry(models.Model):
    topic3333 = models.ForeignKey(Topic)   #topic is from foreign key. makes a connection to Topic. Relates topic to the Entry instance created.
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name_plural = 'Entries'  #Changes the name to Entries instead of Entrys.

    def __str__(self):
        if len(self.text)>50:
            return self.text[:50] + '...'
        else:
            return self.text[:]

'''
allows for the text to not be ellipsed off. text is able to be returned fully as long as it's
not greater than 50 docstring lengths long.
'''