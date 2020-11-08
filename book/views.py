from datetime import date
import requests
from django.core.exceptions import ValidationError
from django.db.models import Q, Min
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from book.forms import AddUpdateBookForm, SearchApiForm, SearchForm
from book.models import Book


class WelcomeView(View):
    def get(self, request):
        return render(request, "book/welcome.html")


# Exercise 1a


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
                    pub_date_since = part_books.aggregate(Min('pub_date')).get("pub_date__min")
                    part_books = part_books.filter(pub_date__range=[pub_date_since, pub_date_to])
                return render(request, "book/books_table.html", {"form": form,
                                                                 "part_books": part_books})
            else:
                part_books = Book.objects.all()
            return render(request, "book/books_table.html", {"form": form,
                                                                 "part_books": part_books})
        return render(request, "book/books_table.html", {"form": form})


# Exercise 1b


class AddUpdateBookView(View):
    def get(self, request, pk):
        book, created = Book.objects.get_or_create(
            pk=pk,
            defaults={
                "title": "bla",
                "author": "bb",
                "pub_date": 1940,
                "pages_amount": 80,
                "pub_language": "English",
                "isbn_num": "222-444-444",
                "link": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.barnesandnoble.com%"
                        "2Fw%2Fharry-potter-i-komnata-tajemnic-j-k-rowling%2F1116540470&psig="
                        "AOvVaw3la-vaVjRPIpCZgD7o0T3q&ust=1604313551353000&source=images&cd=vfe&ved="
                        "0CAIQjRxqFwoTCJDh6OyT4ewCFQAAAAAdAAAAABAG",
            },
        )

        form = AddUpdateBookForm(instance=book)
        return render(request, "book/edit_book.html", {"form": form})

    def post(self, request, pk):
        form = AddUpdateBookForm(request.POST)
        if form.is_valid():
            book = Book.objects.get(pk=pk)
            book.title = form.cleaned_data.get("title")
            book.author = form.cleaned_data.get("author")
            book.pub_date = form.cleaned_data.get("pub_date")
            book.pages_amount = form.cleaned_data.get("pages_amount")
            book.pub_language = form.cleaned_data.get("pub_language")
            book.link = form.cleaned_data.get("link")
            book.isbn_num = form.cleaned_data.get("isbn_num")
            book.save()
        else:
            raise ValidationError("Invalid form")
        return redirect(reverse("update", kwargs={"pk": pk}))


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


# Exercise 3a


class SearchApiView(View):
    def get(self, request):
        form = SearchApiForm()
        return render(request, "book/book_search_api.html", {"form": form})

    def post(self, request):
        SearchApiForm(request.POST)
        search_input = request.POST.get("search_input")
        books = requests.get(
            f"https://www.googleapis.com/books/v1/volumes?q={search_input}"
            f"&key=AIzaSyC7O8QkIp48tHEEXyE-vjbGMxq1N1ziW8Y"
        ).json()
        items_amount = len(books["items"])
        books_list = []
        for item in range(items_amount):
            try:
                title = books["items"][item]["volumeInfo"]["title"]
                pub_date = books["items"][item]["volumeInfo"]["publishedDate"]
                page_amount = books["items"][item]["volumeInfo"]["pageCount"]
                pub_language = books["items"][item]["volumeInfo"]["language"]
                link = books["items"][item]["selfLink"]
                authors = books["items"][item]["volumeInfo"]["authors"]
                isbn_num = books["items"][item]["volumeInfo"]["industryIdentifiers"][0].get("identifier")
                books_list.append(

                    {
                        "title": title,
                        "authors": ",".join(authors),
                        "pub_date": pub_date,
                        "page_amount": page_amount,
                        "isbn_num": isbn_num,
                        "pub_lnguage": pub_language,
                        "link": link,
                    })
            except KeyError:
                pass

        return render(request, "book/book_list.html", {"book_list": books_list})


# Exercise 3b


class FilterView(View):
    def get(self, request):
        form = SearchApiForm()
        return render(request, "book/filter.html", {"form": form})

    def post(self, request):
        search_input = request.POST.get("search_input")
        cat_value = request.POST.get("value")
        books_list_search = []
        if cat_value is not None:
            book_search = requests.get(
                f"https://www.googleapis.com/books/v1/volumes?q={search_input}&"
                f"filter={cat_value}&key=AIzaSyC7O8QkIp48tHEEXyE-vjbGMxq1N1ziW8Y"
            ).json()
            items_amount = len(book_search["items"])
        else:
            book_search = requests.get(
                f"https://www.googleapis.com/books/v1/volumes?q="
                f"{search_input}&key=AIzaSyC7O8QkIp48tHEEXyE-vjbGMxq1N1ziW8Y"
            ).json()
            items_amount = len(book_search["items"])

        for item in range(items_amount):
            title = book_search["items"][item]["volumeInfo"].get("title") or "no title"
            pub_date = book_search["items"][item]["volumeInfo"].get("publishedDate") or "no date"
            page_amount = book_search["items"][item]["volumeInfo"].get("pageCount") or "no page count"
            pub_language = book_search["items"][item]["volumeInfo"].get("language") or "no publishing language"
            link = book_search["items"][item].get("selfLink") or "no link"
            authors = book_search["items"][item]["volumeInfo"].get("authors") or "no authors"
            books_list_search.append(
                {
                    "title": title,
                    "authors": ",".join(authors),
                    "pub_date": pub_date,
                    "page_amount": page_amount,
                    "pub_language": pub_language,
                    "link": link,
                }
            )

        return render(request, "book/filter_book_api.html", {"books_list_search": books_list_search})
