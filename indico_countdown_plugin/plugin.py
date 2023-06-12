from datetime import datetime, timezone

from flask_pluginengine import render_plugin_template
from indico.core import signals
from indico.core.plugins import IndicoPlugin, IndicoPluginBlueprint, url_for_plugin
from indico.web.menu import SideMenuItem

from . import _
from .controllers import RHEditSettings


class CountdownPlugin(IndicoPlugin):
    """Countdown Plugin

    A plugin that shows a countdown timer on the main page
    """

    default_event_settings = {"display_countdown": False, "granularity": "second"}

    def init(self):
        super().init()
        self.template_hook("conference-home-info", self._inject_plugin_template)
        # self.inject_bundle('main.js', WPBase)
        self.connect(
            signals.menu.items,
            self._inject_menuitems,
            sender="event-management-sidemenu",
        )

    def get_blueprints(self):
        blueprint = IndicoPluginBlueprint(
            "countdown", __name__, url_prefix="/event/<int:event_id>/manage/countdown"
        )
        blueprint.add_url_rule("/", "edit", RHEditSettings, methods=("GET", "POST"))
        return blueprint

    def _inject_plugin_template(self, event):
        display_countdown = self.event_settings.get(event, "display_countdown")
        if not display_countdown:
            return

        if datetime.now(timezone.utc) >= (event.start_dt_override or event.start_dt):
            return

        granularity = self.event_settings.get(event, "granularity")
        return render_plugin_template(
            "countdown_display.html", event=event, granularity=granularity
        )

    def _inject_menuitems(self, sender, event, **kwargs):
        return SideMenuItem(
            "countdown",
            _("Countdown"),
            url_for_plugin("countdown.edit", event),
            section="customization",
        )
