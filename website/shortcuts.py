from django.shortcuts import (
    render as original_render,
    redirect,
    resolve_url,
    HttpResponseRedirect,
)

def render(request, template, context=None, content_type=None, status=None, using=None):
    """
    Render with some automatically added context variables
    """
    defaults = {
        'request': request,
    }
    if request.user.is_authenticated:
        defaults['user'] = request.user
    return original_render(
        request,
        template,
        { **defaults, **context } if context else defaults, content_type, status, using
    )

def redirect_back(request):
    """
    Return a redirect to the previous page
    """
    try:
        return redirect(request.headers['Referer'])
    except KeyError:
        return redirect('home')

def redirect_hash(to, hash, *args, **kwargs):
    """
    Return a redirect to the location with an added hash
    """
    return HttpResponseRedirect(f'{resolve_url(to, *args, **kwargs)}#{hash}')