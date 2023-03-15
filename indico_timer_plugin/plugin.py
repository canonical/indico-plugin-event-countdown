from indico.core.plugins import IndicoPlugin
from indico.web.views import WPBase
from indico.web.forms.base import IndicoForm
from indico.web.forms.widgets import SwitchWidget
from wtforms.fields import BooleanField
from flask_pluginengine import render_plugin_template


class TimerPlugin(IndicoPlugin):
    """Example Plugin

    An example plugin that demonstrates the capabilities of the new Indico plugin system.
    """

    def init(self):
        super(TimerPlugin, self).init()
        self.template_hook('conference-home-info',
                render_plugin_template('timer_plugin_clock.html'))

