def _inline_r_setup(code: str) -> str:
    """
    Some behaviour of R cannot be configured via env variables, but can
    only be configured via R options once R has started. These are set here.
    """
    with_option = f"""\
    options(install.packages.compile.from.source = "never")
    {code}
    """
    return with_option
