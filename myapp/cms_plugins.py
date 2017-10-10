# _*_ coding:utf-8 _*_

__author__ = 'yanghao'
__date__ = '2017/9/25 21:17'

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _

from .models import Hello,ArticlePluginModel,AssociatedItem

class HelloPlugin(CMSPluginBase):
    model = Hello
    name = _("Hello Plugin")
    render_template = "hello_plugin.html"
    cache = False

    def render(self, context, instance, placeholder):
        context = super(HelloPlugin, self).render(context, instance, placeholder)
        return context

plugin_pool.register_plugin(HelloPlugin)


class TestPlugin(CMSPluginBase):
    model = CMSPlugin
    name = _("test Plugin")
    render_template = "test.html"
    cache = False

plugin_pool.register_plugin(TestPlugin)



from .admin import ItemInlineAdmin
class ArticlePlugin(CMSPluginBase):
    model = ArticlePluginModel
    name = _("Article Plugin")
    render_template = "article/index.html"
    inlines = (ItemInlineAdmin,)

    def render(self, context, instance, placeholder):
        context = super(ArticlePlugin, self).render(context, instance, placeholder)
        items = instance.associated_item.all()
        context.update({
            'items': items,
        })
        return context

plugin_pool.register_plugin(ArticlePlugin)


from .models import ParentPlugin, ChildPlugin

@plugin_pool.register_plugin
class ParentCMSPlugin(CMSPluginBase):
    render_template = 'parent.html'
    name = 'Parent'
    model = ParentPlugin
    allow_children = True  # This enables the parent plugin to accept child plugins
    # You can also specify a list of plugins that are accepted as children,
    # or leave it away completely to accept all
    # child_classes = ['ChildCMSPlugin']

    def render(self, context, instance, placeholder):
        context = super(ParentCMSPlugin, self).render(context, instance, placeholder)
        return context


@plugin_pool.register_plugin
class ChildCMSPlugin(CMSPluginBase):
    render_template = 'child.html'
    name = 'Child'
    model = ChildPlugin
    require_parent = True  # Is it required that this plugin is a child of another plugin?
    # You can also specify a list of plugins that are accepted as parents,
    # or leave it away completely to accept all
    # parent_classes = ['ParentCMSPlugin']

    def render(self, context, instance, placeholder):
        context = super(ChildCMSPlugin, self).render(context, instance, placeholder)
        return context