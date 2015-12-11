def get_assignments(desc, codebook):
    code=codebook.predict(desc)
    return code