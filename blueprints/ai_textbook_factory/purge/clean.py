import re
from blueprints.ai_textbook_factory.config import logic_0,logic_1,logic_2


def clean(s):

    rmatches = re.findall(logic_1['find'],s)

    matches = []

    for m in rmatches:
        if(
#人文地理学去掉           re.search(r'\d',m[:5]) is not None and
            re.search(logic_1['clean'],m) is None
        ):
            matches.append(m)

    result = ''

    for m in matches:
        print(m.strip())
        result = result + '\n' + m.strip()

    return result