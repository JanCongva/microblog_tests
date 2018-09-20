from widgetastic.widget import GenericLocatorWidget, Text, TextInput, View


class ProfileDetialsView(View):
    title = Text(".//h1")
    edit = GenericLocatorWidget(".//a[normalize-space(.)='Edit your profile']")

    @property
    def is_displayed(self):
        return self.title.text == "User: {}".format(self.context["object"].username)


class ProfileEditView(View):
    title = Text(".//h1")
    username = TextInput(name="username")
    about = TextInput(name="about_me")
    submit = GenericLocatorWidget(".//input[@name='submit']")

    @property
    def is_displayed(self):
        return self.title.text == "Edit Profile"
