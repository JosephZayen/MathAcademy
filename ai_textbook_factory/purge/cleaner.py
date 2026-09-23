
def clean(s):
    from purge.clean_n import clean_lines
    from purge.clean_spaces import clean_spaces
    from purge.clean import clean
    from config import source_path

    s = clean_lines(s)
    s = clean_spaces(s)
    result = clean(s)

    print(result)

    return result