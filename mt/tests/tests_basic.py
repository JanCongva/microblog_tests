from wait_for import wait_for

from mt.base.application.implementations.web_ui import ViaWebUI


def test_login(application):
    view = ViaWebUI.navigate_to(application.web_ui, "LoggedIn")
    assert view.is_displayed


def test_edit_profile(application, request):
    profile = application.collections.profiles.instantiate(username=application.username)

    @request.addfinalizer
    def _revert():
        profile.update(username="misharov", about="")

    profile.update(username="misharov2", about="My bio", address="Some address")
    view = ViaWebUI.navigate_to(profile, "Details")
    wait_for(lambda: view.is_displayed)
    assert view.title.text == "User: misharov2"
