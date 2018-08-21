import logging

from . import MessageTypes
from .command import Command

logger = logging.getLogger(__name__)

class CommandWebsite(Command):
    """
    AA5RObot command to create a link to DStar XReflectors.
    """
    def __init__(self):
        self.command = "website"
        self.syntax = None
        self.help = "Get a link to DStar XReflectors"

    def do_command(self, data):
        return (MessageTypes.RTM_MESSAGE, "Here is the site for DStar XReflectors: http://xrefl.net/")
