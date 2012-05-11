#!/usr/bin/env python
#encoding:utf-8
#author:dbr/Ben
#project:tvdb_api
#repository:http://github.com/dbr/tvdb_api
#license:unlicense (http://unlicense.org/)

"""Custom exceptions used or raised by tvdb_api
"""

__author__ = "dbr/Ben"
__version__ = "1.7.1"

__all__ = ["tvdb_error", "tvdb_userabort", "tvdb_shownotfound",
"tvdb_seasonnotfound", "tvdb_episodenotfound", "tvdb_attributenotfound"]

class tvdb_exception(Exception):
    """Any exception generated by tvdb_api
    """
    pass

class tvdb_error(tvdb_exception):
    """An error with www.thetvdb.com (Cannot connect, for example)
    """
    pass

class tvdb_userabort(tvdb_exception):
    """User aborted the interactive selection (via
    the q command, ^c etc)
    """
    pass

class tvdb_shownotfound(tvdb_exception):
    """Show cannot be found on www.thetvdb.com (non-existant show)
    """
    pass

class tvdb_seasonnotfound(tvdb_exception):
    """Season cannot be found on www.thetvdb.com
    """
    pass

class tvdb_episodenotfound(tvdb_exception):
    """Episode cannot be found on www.thetvdb.com
    """
    pass

class tvdb_attributenotfound(tvdb_exception):
    """Raised if an episode does not have the requested
    attribute (such as a episode name)
    """
    pass
