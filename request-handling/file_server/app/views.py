from datetime import datetime
from os import listdir, path

from django.conf import settings
from django.shortcuts import render


def file_list(request, date=None):
    template_name = 'index.html'
    files = [{
        'name': f,
        'ctime': datetime.fromtimestamp(
            path.getctime(
                path.join(settings.FILES_PATH, f)
            )
        ),
        'mtime': datetime.fromtimestamp(
            path.getmtime(
                path.join(settings.FILES_PATH, f)
            )
        ),
    } for f in listdir(settings.FILES_PATH)]

    context = {
        'files': files,
        'date': date
    }

    return render(request, template_name, context)


def file_content(request, name):
    print(name)
    with open(f'files/{name}', encoding='utf8') as f:
        data = f.read()
    return render(
        request,
        'file_content.html',
        context={'file_name': name, 'file_content': data}
    )
