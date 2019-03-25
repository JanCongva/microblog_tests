from mt.base.application.implementations.web_ui import ViaWebUI


def test_login(application):
    view = ViaWebUI.navigate_to(application.web_ui, "LoggedIn")
    assert view.is_displayed


def test_edit_profile(application, request):
    profile = application.collections.profiles.instantiate(username=application.username)

    @request.addfinalizer
    def _revert():
        profile.update(username="user", about="")

    profile.update(username="new_user", about="My bio")
    view = ViaWebUI.navigate_to(profile, "Details")
    assert view.title.text == "User: new_user"


def test_post_create_delete(application):
    post = application.collections.posts.create(content="Hello world!")
    assert post.exists
    post.delete()
    assert not post.exists
