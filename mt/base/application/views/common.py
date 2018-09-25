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
    login_button = GenericLocatorWidget('.//input[@name="submit"]')
    register = GenericLocatorWidget(".//a[@href='/auth/register']")

    @property
    def is_displayed(self):
        return False


class BaseLoggedInView(View):
    navbar = View.nested(Navbar)
    newer_posts = Text(".//a[contains(normalize-space(.), 'Newer posts')]")
    older_posts = Text(".//a[contains(normalize-space(.), 'Older posts')]")

    @property
    def logged_in(self):
        return self.newer_posts.is_displayed and self.older_posts.is_displayed
    
    @property
    def is_displayed(self):
        return self.logged_in
