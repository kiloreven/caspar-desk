from random import getrandbits

from django.db import models
from django.contrib.postgres.fields import JSONField


class Template(models.Model):
    """
    The contents of a single table. This is the user-submitted
    HTML that is rendered in the player. Must include a JS hook
    of some sort (TBD)
    """
    name = models.CharField(max_length=128)
    html = models.TextField()


class Player(models.Model):
    """
    An instance of a player. A player consists of a template, and controls and
    renders the template. A player spawns an admin interface and the actual
    player website, which can be rendered inside CasparCG.
    """
    name = models.CharField(max_length=128)
    template = models.ForeignKey(Template)
    slug = models.CharField(max_length=8, unique=True)

    def save(self, *args, **kwargs):
        if not self.digest:
            # Create random slug that we are sure does not currently exist
            digest = '%8x' % random.getrandbits(64)
            while self.objects.filter(slug=slug):
                slug = '%8x' % random.getrandbits(64)

            self.slug = slug

        super(Player, self).save(*args, **kwargs)


class Table(models.Model):
    """
    A table of data.
    """
    name = models.CharField(max_length=128)
    head = JSONField()
    body = JSONField()

#     def create(self, *args, **kwargs, data=data):
#         """
#         Handle the creation of a table by cataloging all available headers
#         and saving the data as the table body.
#         """
        
    

class TemplateField(models.Model):
    """
    A field in the template -- used for transferring data from the admin
    interface to the rendered template. Each field is given a hook variable
    (which is handled by the template-side Websocket hook), a table object
    and the name of a field in the table from which data will be procured.

    When the template hook is called with a row from the table, the system
    will use this model to determine the destination variable name of the data
    that is procured from the table.

    If the template field is not bound to a table, data is not procured from a
    table but rather only the input from a form is used.
    """
    template = models.ForeignKey(Template)
    hook_variable = models.CharField(max_length=128)
    table = models.ForeignKey(Table, null=True)
    table_header = models.CharField(max_length=128)
