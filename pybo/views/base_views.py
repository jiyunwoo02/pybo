from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from ..models import Question


def index(request):
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어

    question_list = Question.objects.order_by('-create_date') # 작성일시 역순 정렬, - 붙으면 역방향, 없으면 순방향

    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 제목 검색, ※ subject__contains=kw 대신 subject__icontains=kw을 사용하면 대소문자를 가리지 않고 찾아 준다.
            Q(content__icontains=kw) |  # 내용 검색
            Q(answer__content__icontains=kw) |  # 답변 내용 검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이 검색
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이 검색
        ).distinct()

    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj, 'page': page, 'kw': kw}
    return render(request, 'pybo/question_list.html', context)
    # --> 질문 목록으로 조회한 question_list 데이터를
    # pybo/question_list.html (Template: 파이썬 데이터 읽어서 사용 가능한 html 파일) 파일에 적용하여 HTML을 생성한 후 리턴
    # render 함수는 파이썬 데이터를 템플릿에 적용하여 HTML로 반환하는 함수

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)
