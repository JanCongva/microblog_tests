import attr
from navmazing import NavigateToAttribute

from mt.base.application.entities import BaseCollection, BaseEntity
from mt.base.application.implementations.web_ui import MtNavigateStep, ViaWebUI
from mt.base.application.views.post import AllPostsView


@attr.s
class Post(BaseEntity):
    post_id = attr.ib()

    def delete(self):
        profile = self.parent.filters.get("parent")
        if profile:
            view = ViaWebUI.navigate_to(profile, "Details")
        else:
            view = ViaWebUI.navigate_to(self.parent, "All")
        view.posts(self.post_id).delete()

    @property
    def exists(self):
        profile = self.parent.filters.get("parent")
        if profile:
            view = ViaWebUI.navigate_to(profile, "Details")
        else:
            view = ViaWebUI.navigate_to(self.parent, "All")
        return view.posts(self.post_id).is_displayed


@attr.s
class PostsCollection(BaseCollection):
    ENTITY = Post

    @property
    def all(self):
        profile = self.filters.get("parent")
        if profile:
            view = ViaWebUI.navigate_to(profile, "Details")
        else:
            view = ViaWebUI.navigate_to(self, "All")
        posts = []
        for post_id in view.posts.view_class.all(view.browser):
            posts.append(self.instantiate(post_id[0]))
        return posts

    def create(self, content):
        view = ViaWebUI.navigate_to(self, "All")
        changed = view.fill({"text_area": content})
        if changed:
            post = self.instantiate(view.posts.view_class._last_post_id(view.browser)[0] + 1)
            view.submit.click()
            return post

    def delete(self, *post_ids):
        profile = self.filters.get("profile")
        ViaWebUI.navigate_to(profile, "Details") if profile else ViaWebUI.navigate_to(self, "All")
        for post_id in post_ids:
            post = self.instantiate(post_id)
            post.delete()


@ViaWebUI.register_destination_for(PostsCollection, "All")
class PostsAll(MtNavigateStep):
    VIEW = AllPostsView
    prerequisite = NavigateToAttribute("application.web_ui", "LoginScreen")

    def step(self):
        self.parent.navbar.home.click()
