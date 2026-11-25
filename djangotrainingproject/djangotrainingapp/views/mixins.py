from typing import Any, cast
from django.conf import settings
from django.utils import timezone

from django.db.models import QuerySet
from django.http import HttpRequest

class OwnerQuerysetMixin:
  """ログインユーザー自身のデータだけを対象にする。他人の pk は 404 になる。
  ListView / DetailView / UpdateView / DeleteView の前(左側)に置くこと。"""
  request: HttpRequest

  def get_queryset(self) -> QuerySet[Any]:
    searchInputText = self.request.GET.get('search-text', '')

    if settings.DEBUG:
      print(f'*** 1: [{timezone.localtime()}] What is your search text: {searchInputText}')
    # print('*** [{timezone.localtime()}] What is your search text: ' + searchInputText)

    queryset = cast('QuerySet[Any]', super().get_queryset())  # pyright: ignore[reportUnknownMemberType, reportAttributeAccessIssue]
    result = queryset.filter(user=self.request.user)

    if searchInputText != '':
      if settings.DEBUG:
        print(f'*** 2: [{timezone.localtime()}] What is your search text: {searchInputText}')
      result = result.filter(title__icontains=searchInputText)

    return result
