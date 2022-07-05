#!/usr/bin/python3
#0-lookup.py
"""Defines an object attribute lookup function."""


def lookup(obj):
    """Return a list of object available attributes."""
    return (dir(obj))
