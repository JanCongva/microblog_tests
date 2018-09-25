from widgetastic.widget import GenericLocatorWidget, Text, TextInput, View
from widgetastic_bootstrap import Tab


class ProfileDetialsView(View):
    title = Text(".//h1")
    edit = GenericLocatorWidget(".//a[normalize-space(.)='Edit your profile']")

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
