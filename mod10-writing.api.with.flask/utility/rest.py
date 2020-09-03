def convert_request_to_dictionary(request, fields):
    emp = {}
    for field in fields:
        if field in request.json:
            emp[field] = request.json[field]
    del emp["identity"]
    return emp