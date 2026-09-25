
def clean(s):
    from blueprints.ai_textbook_factory.purge.clean_n import clean_lines
    from blueprints.ai_textbook_factory.purge.clean_spaces import clean_spaces
    from blueprints.ai_textbook_factory.purge.clean import clean
    from blueprints.ai_textbook_factory.config import source_path

    s = clean_lines(s)
    s = clean_spaces(s)
    result = clean(s)

    print(result)

    return result