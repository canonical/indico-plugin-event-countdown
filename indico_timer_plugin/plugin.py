from indico.core.plugins import IndicoPlugin
from indico.web.views import WPBase
from indico.web.forms.base import IndicoForm
from indico.web.forms.widgets import SwitchWidget
from wtforms.fields import BooleanField
from flask_pluginengine import render_plugin_template
from datetime import datetime, timezone
from indico.util.i18n import _

class EventTimerSettingsForm(IndicoForm):
    display_timer = BooleanField(
        _('Display Timer'),
        widget=SwitchWidget(),
        description=_('Display a countdown timer on the event home page')
    )

class TimerEventSettingsFormBase(IndicoForm):
    display_timer = BooleanField(
        _('Display Timer'),
        widget=SwitchWidget(),
        description=_('Display a countdown timer on the event home page')
    )

    def __init__(self, *args, **kwargs):
        # Provide the plugin settings in case a plugin needs them for more complex form fields.
        self._plugin_settings = kwargs.pop('plugin_settings')
        super().__init__(*args, **kwargs)



class TimerPlugin(IndicoPlugin):
    """Example Plugin

    An example plugin that demonstrates the capabilities of the new Indico plugin system.
    """

    configurable = True
    default_settings = {
        'display_timer': False
    }
    default_event_settings = {
        'display_timer': True
    }
    event_settings_form = TimerEventSettingsFormBase
    
    def init(self):
        super(TimerPlugin, self).init()
        self.template_hook('conference-home-info', self._inject_plugin_template)
        self.inject_bundle('main.js', WPBase)
        print("init working")

    def _inject_plugin_template(self, event=None):
        print(self.default_event_settings)
        # print(self.event_settings)
        # print(self.event_settings_form)
        # print(event_settings.get_all(event))
        # enabled = self.event_settings.get('display_timer')
        # if enabled:
        time_to_event = event.start_dt - datetime.now(event.tzinfo) 
        print(time_to_event)
        return render_plugin_template('timer_plugin_clock.html',
                time_to_event=time_to_event.total_seconds(), event=event)


