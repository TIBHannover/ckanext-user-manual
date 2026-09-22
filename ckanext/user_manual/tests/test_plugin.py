"""
Tests for plugin.py.

Tests are written using the pytest library (https://docs.pytest.org), and you
should read the testing guidelines in the CKAN docs:
https://docs.ckan.org/en/2.9/contributing/testing.html

To write tests for your extension you should install the pytest-ckan package:

    pip install pytest-ckan

This will allow you to use CKAN specific fixtures on your tests.

For instance, if your test involves database access you can use `clean_db` to
reset the database:

    import pytest

    from ckan.tests import factories

    @pytest.mark.usefixtures("clean_db")
    def test_some_action():

        dataset = factories.Dataset()

        # ...

For functional tests that involve requests to the application, you can use the
`app` fixture:

    from ckan.plugins import toolkit

    def test_some_endpoint(app):

        url = toolkit.url_for('myblueprint.some_endpoint')

        response = app.get(url)

        assert response.status_code == 200


To temporary patch the CKAN configuration for the duration of a test you can use:

    import pytest

    @pytest.mark.ckan_config("ckanext.myext.some_key", "some_value")
    def test_some_action():
        pass
"""
import logging

import pytest
from ckan.exceptions import CkanConfigurationException
from ckan.plugins import toolkit

import ckanext.user_manual.plugin as plugin

@pytest.mark.ckan_config("ckan.plugins", "user_manual")
@pytest.mark.ckan_config("SECRET_KEY", "test_secret")
@pytest.mark.usefixtures("with_plugins")
def test_help_page_and_assets_render_on_ckan_211(app, caplog):
    from ckan.lib.webassets_tools import include_asset

    caplog.set_level(logging.ERROR, logger="ckan.lib.webassets_tools")
    response = app.get(toolkit.url_for("user_manual.help"))
    with app.flask_app.test_request_context("/"):
        include_asset("ckanext-user-manual/help-js")

    assert response.status_code == 200
    assert "CKAN" in response.body
    assert "Trying to include unknown asset" not in caplog.text


def test_plugin_detection_matches_complete_names(monkeypatch):
    monkeypatch.setitem(
        toolkit.config, "ckan.plugins", "user_manual_extra datastore"
    )

    assert plugin.check_plugin_enabled("user_manual") is False
    assert plugin.check_plugin_enabled("datastore") is True


def test_help_video_requires_storage_configuration(app, monkeypatch):
    monkeypatch.delitem(toolkit.config, "ckan.storage_path", raising=False)

    with app.flask_app.test_request_context("/user_manual/video"):
        with pytest.raises(CkanConfigurationException, match="ckan.storage_path"):
            plugin.get_help_video()


def test_help_video_uses_configured_storage_path(app, monkeypatch, tmp_path):
    video_dir = tmp_path / "storage" / "uploads" / "admin"
    video_dir.mkdir(parents=True)
    (video_dir / "help.mp4").write_bytes(b"video-data")
    monkeypatch.setitem(toolkit.config, "ckan.storage_path", str(tmp_path))

    with app.flask_app.test_request_context("/user_manual/video"):
        response = plugin.get_help_video()

    response.direct_passthrough = False
    assert response.get_data() == b"video-data"
