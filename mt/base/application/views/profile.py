from widgetastic_bootstrap import Button
from widgetastic.widget import GenericLocatorWidget, Text, TextInput, View


class ProfileDetialsView(View):
    title = Text(".//h1")
    edit = GenericLocatorWidget(".//a[normalize-space(.)='Edit your profile']")

    @property
    def is_displayed(self):
        return title.text == "User: {}".format(self.context["object"].username)


class ProfileEditView(View):
    username = TextInput(name="username")
    about = TextInput(name="about_me")
    submit = Button("Submit")
