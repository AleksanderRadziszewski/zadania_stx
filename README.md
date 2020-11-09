# Project Name: Zadania_stx

This project aims to provide some basic search, filter and import functionality like:

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

Ongoing

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

<img width="353" alt="Zrzut ekranu 2020-11-9 o 11 15 31" src="https://user-images.githubusercontent.com/56914063/98528705-f795a280-227c-11eb-95b5-159cd044cb65.png">

b) Page amount has changed

<img width="514" alt="Zrzut ekranu 2020-11-9 o 11 17 20" src="https://user-images.githubusercontent.com/56914063/98528872-30ce1280-227d-11eb-922c-a693219348a7.png">

c) View in database

<img width="1280" alt="Zrzut ekranu 2020-11-9 o 11 20 34" src="https://user-images.githubusercontent.com/56914063/98529233-a9cd6a00-227d-11eb-8b33-59d9f3e4e679.png">










# Sources:

https://developers.google.com/books

https://docs.djangoproject.com/en/3.1/

https://stackoverflow.com/

https://dashboard.heroku.com/


