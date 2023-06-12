from indico.core.plugins import WPJinjaMixinPlugin
from indico.modules.events.management.views import WPEventManagement


class WPCountdown(WPJinjaMixinPlugin, WPEventManagement):
    sidemenu_option = "countdown"
