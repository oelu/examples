"""
Fabric Snippets.
"""
from fabric.api import hide, run, get, local

def hide_output():
    """
    Should test if output is omitted.
    """
    with hide('output'):
        lsout = local("ls -l", capture=True)


def hide_output_and_running():
    """
    Should test if output is omitted.
    """
    with hide('output', 'running'):
        lsout = local("ls -l", capture=True)
