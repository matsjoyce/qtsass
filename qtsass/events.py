# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2015 Yann Lanthony
# Copyright (c) 2017-2018 Spyder Project Contributors
#
# Licensed under the terms of the MIT License
# (See LICENSE.txt for details)
# -----------------------------------------------------------------------------
"""Source files event handler."""

# yapf: disable

import os

# Third party imports
from watchdog.events import FileSystemEventHandler


# yapf: enable


class SourceEventHandler(FileSystemEventHandler):
    """Source event hanlder."""

    def __init__(self, source, destination, compiler):
        """Source event hanlder."""
        super(SourceEventHandler, self).__init__()
        self._source = source
        self._destination = destination
        self._compiler = compiler

    def process_event_for_path(self, path):
        """Override watchdog method to handle on file modification events."""
        if os.path.isfile(self._source):
            if isinstance(path, bytes):
                path = path.decode()
            print(self._source, path)
            if path != self._source:
                return

        self._compiler(self._source, self._destination)

    def on_modified(self, event):
        return self.process_event_for_path(event.src_path)

    def on_moved(self, event):
        return self.process_event_for_path(event.dest_path)

    def on_created(self, event):
        return self.process_event_for_path(event.src_path)
