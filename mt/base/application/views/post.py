from widgetastic.widget import (GenericLocatorWidget, ParametrizedLocator, ParametrizedView, Text,
                                TextInput)

from mt.base.application.views.common import BaseLoggedInView


class PostView(ParametrizedView):
    PARAMETERS = ("post_id",)
    ALL_POSTS = ".//span[contains(@id, 'post')]"
    delete_link = GenericLocatorWidget(
        ParametrizedLocator(".//a[@href='/delete/{post_id}']"))

    @classmethod
    def all(cls, browser):
        return [(int(e.get_attribute("id").lstrip("post")),)
                for e in browser.elements(cls.ALL_POSTS)]

    @classmethod
    def _last_post_id(cls, browser):
        try:
            return max(cls.all(browser))
        except ValueError:
            return 0,

    def delete(self):
        self.delete_link.click()

    @property
    def is_displayed(self):
        return self.delete_link.is_displayed


class AllPostsView(BaseLoggedInView):
    greeting = Text(".//h1")
    text_area = TextInput(name="post")
    submit = GenericLocatorWidget('.//input[@name="submit"]')
    posts = ParametrizedView.nested(PostView)

    @property
    def is_displayed(self):
        return (
            self.logged_in and
            self.greeting.text == "Hi, {}!".format(self.context["object"].username)
        )
