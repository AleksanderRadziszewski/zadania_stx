from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.db.models import Q
import requests
from book.forms import SearchForm, AddUpdateBookForm, SearchApiForm
from book.models import Book

#Exercise 1a

class SearchBookListView(View):
    def get(self, request):
        part_books=None
        form=SearchForm(request.GET)
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
        return render(request, 'book/books_table.html', {'part_books': part_books,
                                                        'form': form})
#Exercise 1b

class AddUpdateBookView(View):
    def get(self,request,pk):
        book,created = Book.objects.get_or_create(pk=pk, defaults={'title': 'bla',
                                                           'author': 'bb',
                                                           'pub_date': 1940,
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

# Exercise 2

def ImportBook():
    request=requests.get("https://www.googleapis.com/books/v1/volumes?q=Hobbit").json()
    items_amount=len(request["items"])

    for item in range(items_amount):
        title = request['items'][item]['volumeInfo']['title']
        print(title)
        pub_date = request['items'][item]['volumeInfo']['publishedDate']
        page_amount = request['items'][item]['volumeInfo']['pageCount']
        isbn_num = request['items'][item]['volumeInfo']['industryIdentifiers'][0]['identifier']
        pub_language = request['items'][item]['volumeInfo']['language']
        link = request['items'][item]['selfLink']
        authors = request['items'][item]['volumeInfo']['authors']
        Book.objects.create(title=title,author=authors,pub_date=pub_date,pages_amount=page_amount,isbn_num=isbn_num,
                                 pub_language=pub_language,link=link)
#
#
# ImportBook()

# Exercise 3a

class SearchApiView(View):
    def get(self,request):
        form = SearchApiForm()
        return render(request, "book/search.html", {'form': form})
    def post(self,request):
        SearchApiForm(request.POST)
        search_input=request.POST.get('search_input')
        books = requests.get(f"https://www.googleapis.com/books/v1/volumes?q={search_input}&key=AIzaSyC7O8QkIp48tHEEXyE-vjbGMxq1N1ziW8Y").json()
        items_amount = len(books["items"])
        books_list=[]
        for item in range(items_amount):
            title = books['items'][item]['volumeInfo']['title']
            pub_date = books['items'][item]['volumeInfo']['publishedDate']
            page_amount = books['items'][item]['volumeInfo']['pageCount']
            isbn_num = books['items'][item]['volumeInfo']['industryIdentifiers'][0]['identifier']
            pub_language = books['items'][item]['volumeInfo']['language']
            link = books['items'][item]['selfLink']
            authors = books['items'][item]['volumeInfo']['authors']
            books_list.append({"title":title,
                               "authors":(",").join(authors),
                                "pub_date":pub_date,
                               "page_amount":page_amount,
                               "isbn_num":isbn_num,
                               "pub_lnguage":pub_language,
                               "link":link})

        return render(request,"book/search_api.html",{'book_list':books_list})

#Exercise 3b

class FilterView(View):
    def get(self,request):
        form=SearchApiForm()
        return render(request,"book/filter.html",{'form':form})
    def post(self,request):
        search_input=request.POST.get("search_input")
        cat_value = request.POST.get("value")
        books_list_search = []
        if cat_value is not None:
            book_search = requests.get(
                f"https://www.googleapis.com/books/v1/volumes?q={search_input}&filter={cat_value}&key=AIzaSyC7O8QkIp48tHEEXyE-vjbGMxq1N1ziW8Y").json()
            items_amount = len(book_search["items"])
        else:
            book_search = requests.get(
                f"https://www.googleapis.com/books/v1/volumes?q={search_input}&key=AIzaSyC7O8QkIp48tHEEXyE-vjbGMxq1N1ziW8Y").json()
            items_amount = len(book_search["items"])

        for item in range(items_amount):
                title = book_search['items'][item]['volumeInfo'].get('title') or "no title"
                pub_date = book_search['items'][item]['volumeInfo'].get('publishedDate') or "no date"
                page_amount = book_search['items'][item]['volumeInfo'].get("pageCount") or "no page count"
                pub_language = book_search['items'][item]['volumeInfo'].get('language') or "no publishing language"
                link = book_search['items'][item].get('selfLink') or "no link"
                authors = book_search['items'][item]['volumeInfo'].get('authors') or "no authors"
                books_list_search.append({"title": title,
                                          "authors": ("").join(authors),
                                          "pub_date": pub_date,
                                          "page_amount": page_amount,
                                          "pub_lnguage": pub_language,
                                          "link": link})

        return render(request, "book/book_search_api.html", {'book_list_searching': books_list_search})














