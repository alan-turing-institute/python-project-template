"""
{{ project_name }}: {{ project_short_description }}
"""

from __future__ import annotations

from importlib.metadata import version

__all__ = ("__version__",)
__version__ = version(__name__)
