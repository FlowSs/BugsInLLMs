import textwrap
def oneline(script, seperator=" && "):
    """
    converts a script to one line command.
    THis is useful to run a single ssh command and pass a one line script.

    :param script:
    :return:
    """
    return seperator.join(textwrap.dedent(script).strip().splitlines())
