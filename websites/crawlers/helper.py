
def condition(title, name):
    return (title in name) or (name in title) or (title in (''.join(e for e in name if e.isalnum() or e == " "))) or ((''.join(e for e in name if e.isalnum() or e == " ")) in title) or (''.join(e for e in name if e.isalnum() or e == " ")) in (''.join(e for e in title if e.isalnum() or e == " ")) or (''.join(e for e in title if e.isalnum() or e == " ")) in (''.join(e for e in name if e.isalnum() or e == " "))

# def search(title, name, tmdb_year, fetched_year, year_key, result):
