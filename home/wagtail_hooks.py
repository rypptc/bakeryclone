from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup

from home.models import FooterText, Person
from breads.models import BreadIngredient, BreadType, Country


from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    ModelAdminGroup,
    modeladmin_register,
)



class BreadIngredientAdmin(ModelAdmin):
    # These stub classes allow us to put various models into the custom "Wagtail Bakery" menu item
    # rather than under the default Snippets section.
    model = BreadIngredient
    search_fields = ("name",)
    inspect_view_enabled = True


class BreadTypeAdmin(ModelAdmin):
    model = BreadType
    search_fields = ("title",)


class BreadCountryAdmin(ModelAdmin):
    model = Country
    search_fields = ("title",)


class BreadModelAdminGroup(ModelAdminGroup):
    menu_label = "Bread Categories"
    menu_icon = "suitcase"  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    items = (BreadIngredientAdmin, BreadTypeAdmin, BreadCountryAdmin)

class PersonViewSet(SnippetViewSet):
    model = Person
    menu_label = "People"  # ditch this to use verbose_name_plural from model
    icon = "group"  # change as required
    list_display = ("first_name", "last_name", "job_title", "thumb_image")
    list_filter = {
        "job_title": ["icontains"],
    }

class FooterTextViewSet(SnippetViewSet):
    model = FooterText
    search_fields = ("body",)


class BakerySnippetViewSetGroup(SnippetViewSetGroup):
    menu_label = "Bakery Misc"
    menu_icon = "utensils"  # change as required
    menu_order = 300  # will put in 4th place (000 being 1st, 100 2nd)
    items = (PersonViewSet, FooterTextViewSet)


# When using a ModelAdminGroup class to group several ModelAdmin classes together,
# you only need to register the ModelAdminGroup class with Wagtail:
modeladmin_register(BreadModelAdminGroup)
register_snippet(BakerySnippetViewSetGroup)