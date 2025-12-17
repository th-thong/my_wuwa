from urllib.parse import urlparse, parse_qs

def get_params(url: str):
    parse_result = urlparse(url)

    query_string = parse_result.query

    if not query_string and parse_result.fragment:

        if '?' in parse_result.fragment:
            query_string = parse_result.fragment.split('?')[1]

    params = parse_qs(query_string)

    clean_params = {k: v[0] for k, v in params.items()}

    return clean_params