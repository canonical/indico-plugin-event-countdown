from flask import flash
from indico.modules.events.management.controllers import RHManageEventBase
from indico.web.forms.base import FormDefaults
from indico.web.rh import RH

from . import _
from .forms import EventCountdownSettingsForm
from .views import WPCountdown


class RHEditSettings(RH):
    def _process_args(self):
        RHManageEventBase._process_args(self)
        from .plugin import CountdownPlugin

        self.plugin = CountdownPlugin

    def _process(self):
        plugin_event_settings = self.plugin.event_settings.get_all(self.event)
        defaults = FormDefaults(
            {k: v for k, v in plugin_event_settings.items() if v is not None}
        )

        form = EventCountdownSettingsForm(obj=defaults)
        if form.validate_on_submit():
            self.plugin.event_settings.set_multi(self.event, form.data)
            flash(_("Countdown settings saved"), "success")

        return WPCountdown.render_template(
            "event_countdown_settings.html", self.event, form=form
        )
