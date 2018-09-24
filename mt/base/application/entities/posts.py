import attr
from navmazing import NavigateToAttribute
from wait_for import wait_for

from mt.base.application.entities import BaseCollection, BaseEntity
from mt.base.application.implementations.web_ui import MtNavigateStep, ViaWebUI
from mt.base.application.views.common import BaseLoggedInView


@attr.s
class Post(BaseEntity):
    post_id = attr.ib()

    def delete(self):
        view = ViaWebUI.navigate_to(self.parent, "All")
        view.posts(self.post_id).delete()

    @property
    def exists(self):
        view = ViaWebUI.navigate_to(self.parent, "All")
        return view.posts(self.post_id).is_displayed


@attr.s
class PostsCollection(BaseCollection):
    ENTITY = Post

    def create(self, content):
        view = ViaWebUI.navigate_to(self, "All")
        changed = view.fill({"text_area": content})
        if changed:
            view.submit.click()
            return self.instantiate(view.posts.view_class._last_post_id(view.browser)[0] + 1)

    def delete(self, *post_ids):
        ViaWebUI.navigate_to(self, "All")
        for post_id in post_ids:
            post = self.instantiate(post_id)
            post.delete()


@ViaWebUI.register_destination_for(PostsCollection, "All")
class LoggedIn(MtNavigateStep):
    VIEW = BaseLoggedInView
    prerequisite = NavigateToAttribute("application.web_ui", "LoginScreen")

    def step(self):
        self.application.web_ui.do_login()
        wait_for(lambda: self.view.is_displayed)
