from django.shortcuts import render
from cafesys.models import *
from django.contrib.auth.decorators import login_required

def get_reviews(request):
    reviews = Review.objects.all()
    context = {
        'reviews': reviews,
    }
    return render(request,
                'cafesys/reviews.html',
                context)

@login_required
def create_review(request):
    if request.method == 'POST':
        Review.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            author = request.user,
        )
        return get_reviews(request)
    else:
        return render(request,
                    'cafesys/create_review.html')

def get_review(request, pk):
    review = Review.objects.get(id=pk)
    context = {
        'review': review,
    }
    return render(request,
                'cafesys/review.html',
                context)