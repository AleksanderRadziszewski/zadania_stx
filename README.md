# Project Name: Zadania_stx

### This project aims to provide some basic search, filter and import functionality like:

- filtering and searching by particular fields of Book model
- searching and filtering by keyword in Google Api book
- editing and adding books
- importing books from Goofle Api book

Moreover application has been tested through unittest and  deployed on public Heroku server.

# Project Structure:

### Project contains one application with one model:

Book:

- title
- author
- isbn_number
- publishing_language
- publishing_date
- pages_amount
- link

# Project status:

Finished

# Usage illustrations:

## 1. Books model records
a) empty title

<img width="1279" alt="Zrzut ekranu 2020-11-8 o 21 08 32" src="https://user-images.githubusercontent.com/56914063/98483188-94692900-2206-11eb-9881-bc49c3f8c633.png">


b)filtering only by author

<img width="1280" alt="Zrzut ekranu 2020-11-8 o 21 09 27" src="https://user-images.githubusercontent.com/56914063/98483205-bcf12300-2206-11eb-8b31-5a0eabfa0d57.png">

c)filtering by publishing language

<img width="1280" alt="Zrzut ekranu 2020-11-8 o 21 11 32" src="https://user-images.githubusercontent.com/56914063/98483258-0b062680-2207-11eb-89ca-cd10bd05b348.png">

d)filtering by publishing dates and title

<img width="660" alt="Zrzut ekranu 2020-11-8 o 21 12 51" src="https://user-images.githubusercontent.com/56914063/98483290-44d72d00-2207-11eb-956c-022b53bc672b.png">

e)filtering by only dates

<img width="1280" alt="Zrzut ekranu 2020-11-8 o 21 15 00" src="https://user-images.githubusercontent.com/56914063/98483323-8962c880-2207-11eb-80a0-19be83607087.png">

f)Filtering by nothing

<img width="1280" alt="Zrzut ekranu 2020-11-8 o 21 27 00" src="https://user-images.githubusercontent.com/56914063/98483494-2d993f00-2209-11eb-8079-3af64e404aa8.png">

## 2.Searching using Google Api books

<img width="1275" alt="Zrzut ekranu 2020-11-8 o 21 43 13" src="https://user-images.githubusercontent.com/56914063/98483813-7f42c900-220b-11eb-998d-3c01a2c00996.png">

## 3.Filtering using Google Api books

a) Without checking filter type

<img width="1280" alt="Zrzut ekranu 2020-11-8 o 21 54 54" src="https://user-images.githubusercontent.com/56914063/98484063-3855d300-220d-11eb-91f6-be6af358ce2c.png">

b)With checking filter type

<img width="1280" alt="Zrzut ekranu 2020-11-8 o 21 55 58" src="https://user-images.githubusercontent.com/56914063/98484065-3b50c380-220d-11eb-8f49-da61514d386b.png">

## 4.Import Google Api

<img width="496" alt="Zrzut ekranu 2020-11-9 o 11 10 35" src="https://user-images.githubusercontent.com/56914063/98528413-8b1aa380-227c-11eb-80a5-53693e6a073d.png">

<img width="1280" alt="Zrzut ekranu 2020-11-9 o 11 11 25" src="https://user-images.githubusercontent.com/56914063/98528419-8eae2a80-227c-11eb-9038-c059ddf2ca91.png">

## 5. Edit and add book

a) before editing

<img width="447" alt="Zrzut ekranu 2020-11-9 o 12 40 12" src="https://user-images.githubusercontent.com/56914063/98536911-d3d85980-2288-11eb-89f9-f60e9f5e65cc.png">

b) Page amount has changed

<img width="532" alt="Zrzut ekranu 2020-11-9 o 12 40 23" src="https://user-images.githubusercontent.com/56914063/98536915-d5a21d00-2288-11eb-8324-aa767fc3230d.png">


c) View in database

<img width="1280" alt="Zrzut ekranu 2020-11-9 o 12 43 18" src="https://user-images.githubusercontent.com/56914063/98537202-329dd300-2289-11eb-958d-6ca898f2f03a.png">


d) add book

<img width="686" alt="Zrzut ekranu 2020-11-9 o 18 33 34" src="https://user-images.githubusercontent.com/56914063/98576653-26326e00-22bb-11eb-8d51-27dadb148716.png">

<img width="538" alt="Zrzut ekranu 2020-11-9 o 18 38 47" src="https://user-images.githubusercontent.com/56914063/98576659-2894c800-22bb-11eb-9506-34bb916b6654.png">

<img width="1275" alt="Zrzut ekranu 2020-11-9 o 18 40 21" src="https://user-images.githubusercontent.com/56914063/98576661-29c5f500-22bb-11eb-90e4-84b6f9a1d39b.png">

## 6. Rest Api Views

a) Book List Api View

![Zrzut ekranu 2020-12-4 o 13 21 50](https://user-images.githubusercontent.com/56914063/101163539-04b37080-3634-11eb-904f-ad9e1ebf9a7d.png)

b) Book Created Api View

![Zrzut ekranu 2020-12-4 o 13 22 08](https://user-images.githubusercontent.com/56914063/101163717-48a67580-3634-11eb-98a4-2e72027f7ebe.png)

![Zrzut ekranu 2020-12-4 o 13 37 19](https://user-images.githubusercontent.com/56914063/101164801-e2baed80-3635-11eb-8727-e7d7e4fc417d.png)

c) Book Update Api View

![Zrzut ekranu 2020-12-4 o 13 40 01](https://user-images.githubusercontent.com/56914063/101165020-3dece000-3636-11eb-9961-994899cc5386.png)

d) Book Delete Api View

![Zrzut ekranu 2020-12-4 o 13 41 45](https://user-images.githubusercontent.com/56914063/101165203-86a49900-3636-11eb-9c3c-57f0a16835bb.png)



## 7. Unit tests

a) Test 


# Sources:

https://developers.google.com/books

https://docs.djangoproject.com/en/3.1/

https://stackoverflow.com/

https://dashboard.heroku.com/


