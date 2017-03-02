# azuer88:  from https://lincolnloop.com/blog/2008/may/10/getting-requestcontext-your-templates/
from django.shortcuts import render_to_response


def render_to(template_name):
    def renderer(func):
        def wrapper(request, *args, **kw):
            output = func(request, *args, **kw)
            if not isinstance(output, dict):
                return output
            return render_to_response(request, template_name, output)
        return wrapper
    return renderer

