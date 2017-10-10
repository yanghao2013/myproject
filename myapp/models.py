from django.db import models

# Create your models here.
from cms.models.pluginmodel import CMSPlugin

from django.db import models
from django.utils.translation import ugettext_lazy as _

class Hello(CMSPlugin):
    guest_name = models.CharField(max_length=50, default='Guest')


class SubjectCategory(models.Model):
    name = models.CharField(_('名称'),max_length=50)
    code = models.CharField(_('国标编码'), max_length=50, blank=True, null=True)
    order = models.IntegerField(_('排序'), default=0)
    show = models.BooleanField(_('是否展示'), default=True)

    class Meta:
        managed = True
        verbose_name = _('稿件学科分类')
        verbose_name_plural = _('稿件学科分类')
        # 联合索引
        index_together = [
            ("show",'order'),
        ]

    def __str__(self):
        return str(self.name_i18n)


class ArticlePluginModel(CMSPlugin):
    title = models.CharField(max_length=50)
    # sections = models.ManyToManyField(Section)

    def copy_relations(self, oldinstance):
        # Before copying related objects from the old instance, the ones
        # on the current one need to be deleted. Otherwise, duplicates may
        # appear on the public version of the page
        self.associated_item.all().delete()

        for associated_item in oldinstance.associated_item.all():
            # instance.pk = None; instance.pk.save() is the slightly odd but
            # standard Django way of copying a saved model instance
            associated_item.pk = None
            associated_item.plugin = self
            associated_item.save()

class AssociatedItem(models.Model):
    plugin = models.ForeignKey(
        ArticlePluginModel,
        related_name="associated_item"
    )


class ParentPlugin(CMSPlugin):
    name = models.CharField(_('名称'), max_length=50)

class ChildPlugin(CMSPlugin):
    name = models.CharField(_('名称'), max_length=50)