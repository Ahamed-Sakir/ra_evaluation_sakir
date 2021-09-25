def visit_dirct(path):
    folder = []
    file_ = []
    try:
        folder = os.listdir(str(path))
    except:
        pass

    for x in folder:
        file_.append(x)
        file = visit_dirct(path + '/' + x)
        for y in file:
            file_.append(y)

    return file_


print(visit_dirct('test/'))