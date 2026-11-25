from typing import Any, cast

from django.db.models import QuerySet
from django.http import HttpRequest

class OwnerQuerysetMixin:
  """ログインユーザー自身のデータだけを対象にする。他人の pk は 404 になる。
  ListView / DetailView / UpdateView / DeleteView の前(左側)に置くこと。"""
  request: HttpRequest

  def get_queryset(self) -> QuerySet[Any]:
    queryset = cast('QuerySet[Any]', super().get_queryset())  # pyright: ignore[reportUnknownMemberType, reportAttributeAccessIssue]
    result = queryset.filter(user=self.request.user)
    return result
