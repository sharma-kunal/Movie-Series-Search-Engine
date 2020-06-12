
def condition(title, name):
    return (title in name) or (name in title) or (title in (''.join(e for e in name if e.isalnum()))) or ((''.join(e for e in name if e.isalnum())) in title) or (''.join(e for e in name if e.isalnum())) in (''.join(e for e in title if e.isalnum())) or (''.join(e for e in title if e.isalnum())) in (''.join(e for e in name if e.isalnum()))

# def search(title, name, tmdb_year, fetched_year, year_key, result):
