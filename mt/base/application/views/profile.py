from widgetastic.widget import GenericLocatorWidget, ParametrizedView, Text, TextInput, View
from widgetastic_bootstrap import Dropdown, Tab

from mt.base.application.views.post import PostView


class ProfileDetialsView(View):
    title = Text(".//h1")
    actions = Dropdown("Profile actions")
    posts = ParametrizedView.nested(PostView)

    @property
    def is_displayed(self):
        return self.title.text == "User: {}".format(self.context["object"].username)


class ProfileEditView(View):
    title = Text(".//h1")

    @View.nested
    class basic_info(Tab):
        ROOT = ".//div[@id='basic']"
        TAB_NAME = "Basic info"
        username = TextInput(name="username")
        about = TextInput(name="about_me")
        submit = GenericLocatorWidget(".//input[@name='submit']")

    @View.nested
    class additional_info(Tab):
        ROOT = ".//div[@id='additional']"
        TAB_NAME = "Additional info"
        city = TextInput(name="city")

    @property
    def is_displayed(self):
        return self.title.text == "Edit Profile"
