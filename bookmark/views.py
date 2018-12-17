# 테이블 형태로 북마크 리스트를 출력하는 함수형 뷰
from django.shortcuts import render
from .models import Bookmark # from bookmark.models import Bookmark # 같은 표현

def tabularBookmark(request):
    bookmarks = Bookmark.objects.all().order_by('id')
    return render(request, 'bookmark/tabular_list.html', {'bookmarks': bookmarks})

# 클래스형 제네릭 뷰를 사용하기 위한 임포트
from django.views.generic import ListView, DetailView
# 모델 클래스 임포트
from bookmark.models import Bookmark

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from mysite.views import LoginRequiredMixin

# 북마크 테이블의 전체 레코드 리스트 출력을 위한 뷰
class BookmarkLV(ListView):
    model = Bookmark
    # 1) 디폴트 컨텍스트 변수 object_list를 적용
    # 2) 디폴트 템플릿 파일명 소문자모델명_list.html = bookmark_list.html

# 북마크 테이블의 특정 레코드 상세 출력을 위한 뷰
class BookmarkDV(DetailView):
    model = Bookmark
    # 1) 디폴트 컨텍스트 변수 object를 적용
    # 2) 디폴트 템플릿 파일명 소문자모델명_detail.html = bookmark_detail.html
    #    기본 키로 조회하는 경우, 모델 클래스 명만 지정하면,
    #    r'^bookmark/(?P<pk>)\d+)/$'에 따라서 기본 키 값이 자동으로 인수 전달됨

class BookmarkCreateView(LoginRequiredMixin, CreateView):
    model = Bookmark
    fields = ['title', 'url']
    success_url = reverse_lazy('bookmark:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(BookmarkCreateView, self).form_valid(form)

# class BookmarkChangeLV(LoginRequiredMixin, ListView):
#     template_name = 'bookmark/bookmark_change_list.html'
#
#     def get_queryset(self):
#         return id
#
# class BookmarkUpdateView(LoginRequiredMixin, UpdateView):
#     model = Bookmark
#     fields = ['title', 'url']
#     success_url = reverse_lazy('bookmark:index')
#
# class BookmarkDeleteView(LoginRequiredMixin, DeleteView):
#     model = Bookmark
#     success_url = reverse_lazy('bookmark:index')

