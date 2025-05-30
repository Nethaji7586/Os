import itertools

def entails(kb, query):
    syms = sorted(set("".join(kb + [query])) & set("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    for vals in itertools.product([True, False], repeat=len(syms)):
        model = dict(zip(syms, vals))
        if all(eval(s.replace('~','not ').replace('&',' and ').replace('|',' or ').replace('=>','<='), {}, model) for s in kb):
            if not eval(query.replace('~','not ').replace('&',' and ').replace('|',' or ').replace('=>','<='), {}, model):
                return False
    return True

# Example usage
kb = ["P => Q", "P"]
query = "Q"
print("Entails?" , entails(kb, query))
