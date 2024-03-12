def _replace_url_args(url, url_args):
    
    
    for arg in url_args:
        if isinstance(url_args[arg], six.string_types):
            url = url.replace(arg, url_args[arg])
    return url
