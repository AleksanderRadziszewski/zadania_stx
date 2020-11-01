from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.db.models import Q
from datetime import date

from django.views.generic import UpdateView

from book.forms import SearchForm, AddUpdateBookForm
from book.models import Book


class SearchBookListView(View):
    def get(self, request):
        part_books=None
        form=SearchForm(request.GET,initial={"pub_date_to":date.today()})
        form.is_valid()
        search_input=form.cleaned_data.get('search_input')
        pub_date_since=form.cleaned_data.get('pub_date_since')
        pub_date_to = form.cleaned_data.get('pub_date_to')
        if search_input is not None:
            part_books = Book.objects.all().filter(
                Q(title__icontains=search_input) | Q(author__icontains=search_input)
                | Q(pub_language__icontains=search_input))
        elif pub_date_to and pub_date_since is not None:
            part_books = part_books.filter(pub_date__range=[pub_date_since, pub_date_to])
        else:
            part_books = Book.objects.all()
        return render(request, 'book/books_list.html', {'part_books': part_books,
                                                        'form': form})

class AddUpdateBookView(View):
    def get(self,request,pk):
        book,created = Book.objects.get_or_create(pk=pk, defaults={'title': 'bla',
                                                           'author': 'bb',
                                                           'pub_date': date(1940, 10, 1),
                                                           'pages_amount': 80,
                                                           'pub_language': 'English',
                                                           'isbn_num': '222-444-444',
                                                           'link': 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.barnesandnoble.com%2Fw%2Fharry-potter-i-komnata-tajemnic-j-k-rowling%2F1116540470&psig=AOvVaw3la-vaVjRPIpCZgD7o0T3q&ust=1604313551353000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCJDh6OyT4ewCFQAAAAAdAAAAABAG'})

        form=AddUpdateBookForm(instance=book)
        return render(request, "book/edit_book.html", {"form":form})
    def post(self,request,pk):
        form=AddUpdateBookForm(request.POST)
        if form.is_valid():
            book=Book.objects.get(pk=pk)
            book.title=form.cleaned_data.get('title')
            book.author = form.cleaned_data.get('author')
            book.pub_date = form.cleaned_data.get('pub_date')
            book.pages_amount = form.cleaned_data.get('pages_amount')
            book.pub_language = form.cleaned_data.get('pub_language')
            book.link = form.cleaned_data.get('link')
            book.isbn_num = form.cleaned_data.get('isbn_num')
            book.save()
        return redirect(reverse("search"))









# Create your views here.
