from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Institution, Review
from .forms import ReviewForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q

def index(request):
    page = request.GET.get('page', '1')
    kw = request.GET.get('kw', '')  # 검색어
    institution_list = Institution.objects.order_by('-create_date')
    if kw:
        institution_list = institution_list.filter(
            Q(subject__icontains=kw) |  # 제목 검색
            Q(content__icontains=kw)  # 내용 검색
        ).distinct()
    paginator = Paginator(institution_list, 8)
    page_obj = paginator.get_page(page)
    context = {'institution_list': page_obj, 'page': page, 'kw': kw}
    return render(request, 'review/institution_list.html', context)

def detail(request, institution_id):
    institution = get_object_or_404(Institution, pk=institution_id)
    context = {'institution': institution}
    return render(request, 'review/institution_detail.html', context)

@login_required(login_url='common:login')
def review_create(request, institution_id):
    institution = get_object_or_404(Institution, pk=institution_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.create_date = timezone.now()
            review.institution = institution
            review.save()
            return redirect('review:detail', institution_id=institution.id)
    else:
        form = ReviewForm()
    context = {'institution': institution, 'form': form}
    return render(request, 'review/institution_detail.html', context)

@login_required(login_url='common:login')
def review_modify(request, institution_id):
    review = get_object_or_404(Review, pk=institution_id)
    if request.user != review.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('review:detail', institution_id=review.institution.id)
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.save()
            return redirect('review:detail', institution_id=review.institution.id)
    else:
        form = ReviewForm(instance=review)
    context = {'review': review, 'form': form}
    return render(request, 'review/review_form.html', context)

@login_required(login_url='common:login')
def review_delete(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.user != review.author:
        messages.error(request, '삭제권한이 없습니다')
    else:
        review.delete()
    return redirect('review:detail', institution_id=review.institution.id)