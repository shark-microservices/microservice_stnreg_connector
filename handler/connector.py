#!/usr/bin/env python
# Copyright (c) 2022 SMHI, Swedish Meteorological and Hydrological Institute.
# License: MIT License (see LICENSE.txt or http://opensource.org/licenses/mit).
"""
Created on 2022-03-10 14:38

@author: johannes
"""
import requests


class Connector:
    """Connect to the REST-API of the national station register."""

    def post(*args, data=None, **kwargs):
        """Post a new station.

        Create a new station and get ID back.
        """
        raise NotImplementedError

    def put(*args, **kwargs):
        """Put and change station.

        Change a station attributes (eg. name, position, etc.).
        """
        raise NotImplementedError

    def delete(*args, **kwargs):
        """Delete a station.

        Erase a station from the national station register.
        """
        raise NotImplementedError
