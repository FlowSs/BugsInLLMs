import re
def make_find_paths(find_paths):
    '''
    Given a sequence of path fragments or patterns as passed to `--find`, transform all path
    fragments into glob patterns. Pass through existing patterns untouched.

    For example, given find_paths of:

      ['foo.txt', 'pp:root/somedir']

    ... transform that into:

      ['sh:**/*foo.txt*/**', 'pp:root/somedir']
    '''

    return tuple(
        find_path
        if re.compile(r'([-!+RrPp] )|(\w\w:)').match(find_path)
        else f'sh:**/*{find_path}*/**'
        for find_path in find_paths
    )
