from widgetastic_bootstrap import Button
from widgetastic.widget import Checkbox, GenericLocatorWidget, Text, TextInput, View


class Navbar(View):
    ROOT = ".//nav[@class='navbar navbar-expand-lg navbar-light bg-light']"
    title = Text(".//a[@class='navbar-brand']")
    home = Text(".//a[normalize-space(.)='Home']")
    explore = Text(".//a[normalize-space(.)='Explore']")
    search = TextInput(name="q")
    messages = Text(".//a[normalize-space(.)='Messages']")
    profile = Text(".//a[normalize-space(.)='Profile']")
    login = Text(".//a[normalize-space(.)='Login']")
    logout = Text(".//a[normalize-space(.)='Logout']")


class LoginPage(View):
    navbar = View.nested(Navbar)
    username = TextInput(id="username")
    password = TextInput(id="password")
    remember_me = Checkbox(id="remember_me")
    login_button = Text(locator='.//input[@name="submit"]')
    register = GenericLocatorWidget(".//a[@href='/auth/register']")


class BaseLoggedInView(View):
    navbar = View.nested(Navbar)
    greeting = Text(".//h1")
    text_area = TextInput(name="post")
    submit = Button("Submit")
    newer_posts = Text(".//a[normalize-space(.)='Newer posts']")
    older_posts = Text(".//a[normalize-space(.)='Older posts']")

    @property
    def is_displayed(self):
        return self.greeting.text == "Hi, {}!".format(self.context["object"].application.username)
