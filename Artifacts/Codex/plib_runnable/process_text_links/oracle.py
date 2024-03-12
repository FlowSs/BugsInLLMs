def process_text_links(text):
    """Process links in text, adding some attributes and linkifying textual links."""
    link_callbacks = [callbacks.nofollow, callbacks.target_blank]

    def link_attributes(attrs, new=False):
        """Run standard callbacks except for internal links."""
        href_key = (None, "href")
        if attrs.get(href_key).startswith("/"):
            return attrs

        # Run the standard callbacks
        for callback in link_callbacks:
            attrs = callback(attrs, new)
        return attrs

    return bleach.linkify(
        text,
        callbacks=[link_attributes],
        parse_email=False,
        skip_tags=["code"],
    )
