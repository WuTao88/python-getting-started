from django.shortcuts import render

def PermissionDenied(request):
    return render(request, '403.html')
def PageNotFound(request):
    ''' 
    404、500处理函数
    '''
    return render(request, '404.html')

def ServerError(request):
    ''' 
    404、500处理函数
    '''
    return render(request, '500.html')