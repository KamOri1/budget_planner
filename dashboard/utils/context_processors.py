def get_title(request):
    path_title = request.path.strip("/")

    return {"path_title": path_title}
