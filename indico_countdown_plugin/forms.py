from indico.web.forms.base import IndicoForm
from indico.web.forms.widgets import SwitchWidget
from wtforms.fields import BooleanField, SelectField

from . import _


class EventCountdownSettingsForm(IndicoForm):
    display_countdown = BooleanField(
        _("Display Countdown"),
        widget=SwitchWidget(),
        description=_("Display a countdown timer on the event home page"),
    )

    granularity = SelectField(
        _("Granularity"),
        choices=[
            ("second", _("Seconds")),
            ("minute", _("Minutes")),
            ("hour", _("Hours")),
            ("days", _("Days")),
        ],
    )
