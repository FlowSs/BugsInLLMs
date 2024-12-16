def fix_namespace_prefix_w(content):
    return re.sub(r'\s*w:st="(.*?)"', r'w-st="{}"'.format(WIDTH), content)
