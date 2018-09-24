from widgetastic.widget import GenericLocatorWidget, ParametrizedLocator, ParametrizedView


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
        return max(cls.all(browser))

    def delete(self):
        self.delete_link.click()

    @property
    def is_displayed(self):
        return self.delete_link.is_displayed
