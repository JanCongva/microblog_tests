import attr
from navmazing import NavigateToAttribute, NavigateToSibling

from mt.base.application.entities import BaseCollection, BaseEntity
from mt.base.application.implementations.web_ui import MtNavigateStep, ViaWebUI
from mt.base.application.views.profile import ProfileDetialsView, ProfileEditView


@attr.s
class Profile(BaseEntity):
    username = attr.ib()

    def update(self, username=None, about=None, city=None):
        view = ViaWebUI.navigate_to(self, "Edit")
        changed = view.fill({
            "basic_info": {"username": username, "about": about},
            "additional_info": {"city": city}
        })
        if changed:
            self.username = username
            view.basic_info.submit.click()
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
        self.parent.actions.item_select("Edit your profile")
