from django.shortcuts import get_object_or_404 ,render
from django.http import Http404
from .models import Book
from django.db.models import Avg

# Create your views here.

def index(request):
    books = Book.objects.all().order_by("title")
    num_books = books.count()
    avg_rating = books.aggregate(Avg("rating"))

    return render(request, "index.html",{
        "books": books,
        "total_number_of_books" : num_books,
        "average_rating": avg_rating
        }) 


def book_datail(request, slug):
#   try:
#       book= Book.objects.get(pk=id)
#   except:
#       raise Http404()
    book = get_object_or_404(Book, slug=slug)
    return render(request, "book_detail.html",{
        "title": book.title,
        "author": book.author,
        "rating": book.rating, 
        "is_bestseller": book.is_bestselling,
        "published_countries":book.published_countries.all()
        }) 
