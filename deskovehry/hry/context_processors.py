def nick_context(request):
    return {
        'nick': request.session.get('nick', None)
    }
