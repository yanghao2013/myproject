# _*_ coding:utf-8 _*_

__author__ = 'yanghao'
__date__ = '2017/10/8 21:49'

from menus.base import Menu, NavigationNode
from menus.menu_pool import menu_pool
from django.utils.translation import ugettext_lazy as _

class TestMenu(Menu):

    def get_nodes(self, request):
        nodes = []
        n = NavigationNode(_('sample root page'), "/", 1)
        n2 = NavigationNode(_('sample settings page'), "/bye/", 2)
        n3 = NavigationNode(_('sample account page'), "/hello/", 3)
        n4 = NavigationNode(_('sample my profile page'), "/hello/world/", 4, 3)
        nodes.append(n)
        nodes.append(n2)
        nodes.append(n3)
        nodes.append(n4)
        return nodes

menu_pool.register_menu(TestMenu)


from menus.base import Modifier
from menus.menu_pool import menu_pool

from cms.models import Page

class MyExampleModifier(Modifier):
    """
    This modifier makes the changed_by attribute of a page
    accessible for the menu system.
    """
    def modify(self, request, nodes, namespace, root_id, post_cut, breadcrumb):
        # only do something when the menu has already been cut
        if post_cut:
            # only consider nodes that refer to cms pages
            # and put them in a dict for efficient access
            page_nodes = {n.id: n for n in nodes if n.attr["is_page"]}
            # retrieve the attributes of interest from the relevant pages
            pages = Page.objects.filter(id__in=page_nodes.keys()).values('id', 'changed_by')
            # loop over all relevant pages
            for page in pages:
                # take the node referring to the page
                node = page_nodes[page['id']]
                # put the changed_by attribute on the node
                node.attr["changed_by"] = page['changed_by']
        return nodes

menu_pool.register_modifier(MyExampleModifier)