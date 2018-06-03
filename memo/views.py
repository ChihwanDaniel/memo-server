from django.shortcuts import render
from .models import memo

def memo_list(request):
    qs = memo.objects.all()
    return render(request, 'memo/memo_list.html', {'memos': qs})
