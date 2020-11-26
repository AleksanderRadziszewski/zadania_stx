from datetime import date
import requests
from django.http import Http404
from django.core.exceptions import ValidationError
from django.db.models import Min, Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated



from book.forms import AddUpdateBookForm, SearchApiForm, SearchForm
from book.models import Book
from book.serializers import BookSerializer


class WelcomeView(View):
    def get(self, request):
        return render(request, "book/welcome.html")


# Exercise 1
class SearchBookListView(View):
    def get(self, request):
        form = SearchForm(initial={"pub_date_to": date.today().year})
        return render(request, "book/form.html", {"form": form})

    def post(self, request):
        form = SearchForm(request.POST)

        if form.is_valid():
            search_input = form.cleaned_data.get("search_input")
            pub_date_since = form.cleaned_data.get("pub_date_since")
            pub_date_to = form.cleaned_data.get("pub_date_to")

            if search_input:
                part_books = Book.objects.all().filter(
                    Q(title__icontains=search_input)
                    | Q(author__icontains=search_input)
                    | Q(pub_language__icontains=search_input)
                )
                if pub_date_since and pub_date_to:
                    part_books = part_books.filter(pub_date__range=[pub_date_since, pub_date_to])

                elif not pub_date_to:
                    pub_date_to = date.today().year
                    part_books = part_books.filter(pub_date__range=[pub_date_since, pub_date_to])

                elif not pub_date_since:
                    pub_date_since = part_books.aggregate(Min("pub_date")).get("pub_date__min")
                    part_books = part_books.filter(pub_date__range=[pub_date_since, pub_date_to])

                return render(request, "book/books_table.html", {"form": form, "part_books": part_books})

            elif not pub_date_to and not pub_date_since and not search_input:
                part_books = Book.objects.all()

                return render(request, "book/books_table.html", {"form": form, "part_books": part_books})
            part_books = Book.objects.all()
            part_books = part_books.filter(pub_date__range=[pub_date_since, pub_date_to])

            return render(request, "book/books_table.html", {"form": form, "part_books": part_books})

        return render(request, "book/books_table.html", {"form": form})


# Exercise 1b

class AddUpdateBookView(View):
    def get(self, request, pk=""):
        if not pk:
            form = AddUpdateBookForm()
        else:
            book = Book.objects.get(pk=pk)
            form = AddUpdateBookForm(instance=book)
        return render(request, "book/edit_book.html", {"form": form})

    def post(self, request, pk=""):
        form = AddUpdateBookForm(request.POST)
        text = "The book has already saved"
        try:
            if form.is_valid():
                if not pk:
                    book = Book.objects.get(pk=pk)
                else:
                    book = Book()
                book.title = form.cleaned_data.get("title")
                book.author = form.cleaned_data.get("author")
                book.pub_date = form.cleaned_data.get("pub_date")
                book.pages_amount = form.cleaned_data.get("pages_amount")
                book.pub_language = form.cleaned_data.get("pub_language")
                book.link = form.cleaned_data.get("link")
                book.isbn_num = form.cleaned_data.get("isbn_num")
                book.save()
        except KeyError:
            pass

            raise ValidationError("Invalid form")
        return render(request, "book/edit_book.html", {"form": form, "text": text})


# Exercise 2

class BooksImportView(View):
    def get(self, request):
        form = SearchApiForm()
        return render(request, "book/search_import.html", {"form": form})

    def post(self, request):
        search_input = request.POST.get("search_input")
        request_api = requests.get(f"https://www.googleapis.com/books/v1/volumes?q={search_input}").json()
        items_amount = len(request_api["items"])
        for item in range(items_amount):
            try:
                title = request_api["items"][item]["volumeInfo"]["title"]
                pub_date = request_api["items"][item]["volumeInfo"]["publishedDate"]
                page_amount = request_api["items"][item]["volumeInfo"]["pageCount"]
                pub_language = request_api["items"][item]["volumeInfo"]["language"]
                link = request_api["items"][item]["selfLink"]
                authors = request_api["items"][item]["volumeInfo"]["authors"]
                isbn_num = request_api["items"][item]["volumeInfo"]["industryIdentifiers"][0]["identifier"]
                Book.objects.create(
                    title=title,
                    author=",".join(authors),
                    pub_date=pub_date,
                    pages_amount=page_amount,
                    isbn_num=isbn_num,
                    pub_language=pub_language,
                    link=link,
                )
            except KeyError:
                pass

        return HttpResponse("")


# Exercise 3

class BookSearchFilterAPIView(generics.ListAPIView):
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        book_url = self.kwargs["title"]
        try:
            if book_url:
                queryset = Book.objects.all().filter(
                    Q(title__icontains=book_url)
                    | Q(author__icontains=book_url)
                    | Q(pub_language__icontains=book_url)
                )
                if not queryset:
                    raise Http404
                else:
                    return queryset

        except Book.DoesNotExist:
            raise Http404
