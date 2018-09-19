import attr
from navmazing import NavigateToAttribute, NavigateToSibling

from mt.base.application.entities import BaseCollection, BaseEntity
from mt.base.application.implementations.web_ui import MtNavigateStep, ViaWebUI
from mt.base.application.views.profile import ProfileDetialsView, ProfileEditView


@attr.s
class Profile(BaseEntity):
    username = attr.ib()

    def update(self, username=None, about=None):
        view = ViaWebUI.navigate_to(self, "Edit")
        view.fill({"username": username, "about": about})
        view.submit.click()
        ViaWebUI.navigate_to(self, "Details")


@attr.s
class ProfilesCollection(BaseCollection):
    ENTITY = Profile


@ViaWebUI.register_destination_for(Profile, "Details")
class ProfileDetails(MtNavigateStep):
    VIEW = ProfileDetialsView
    prerequisite = NavigateToAttribute("application.web_ui", "LoggedIn")

    def step(self):
        self.parent.navbar.profile.click()


@ViaWebUI.register_destination_for(Profile, "Edit")
class ProfileEdit(MtNavigateStep):
    VIEW = ProfileEditView
    prerequisite = NavigateToSibling("Details")

    def step(self):
        self.parent.edit.click()
