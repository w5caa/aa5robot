import logging

from . import MessageTypes
from .command import Command

logger = logging.getLogger(__name__)

class CommandPota(Command):
    """
    AA5RObot command to create a link to the POTA.us website.
    """
    def __init__(self):
        self.command = "pota"
        self.syntax = None
        self.help = "Get a link to the POTA spotter website (Parks on the Air)"

    def do_command(self, data):
        return (MessageTypes.RTM_MESSAGE, "The POTA spotter website is at https://pota.us/")
