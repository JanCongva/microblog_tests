from widgetastic.widget import GenericLocatorWidget, ParametrizedView, Text, TextInput, View

from mt.base.application.views.post import PostView


class ProfileDetialsView(View):
    title = Text(".//h1")
    edit = GenericLocatorWidget(".//a[normalize-space(.)='Edit your profile']")
    posts = ParametrizedView.nested(PostView)

    @property
    def is_displayed(self):
        return self.title.text == "User: {}".format(self.context["object"].username)


class ProfileEditView(View):
    title = Text(".//h1")
    username = TextInput(name="username")
    city = TextInput(name="city")
    about = TextInput(name="about_me")
    submit = GenericLocatorWidget(".//input[@name='submit']")

    @property
    def is_displayed(self):
        return self.title.text == "Edit Profile"
