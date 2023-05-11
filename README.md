# LOTR SDK
The LOTR SDK is a Python library for accessing the Lord of the Rings API. It provides a simple and easy-to-use interface for retrieving data from the API.

## Installation
You can install the LOTR SDK using pip:

```pip install gmurtaza-lotr-sdk```



## Usage

```python
from lotr_sdk import LOTR_SDK

bearer_token = "your_bearer_token_here"
lotr_sdk = LOTR_SDK(bearer_token)

movies = lotr_sdk.get_movies()
print(movies)

movie = lotr_sdk.get_movie("5cd95395de30eff6ebccde5b")
print(movie)

movie_quotes = lotr_sdk.get_movie_quotes("5cd95395de30eff6ebccde5b")
print(movie_quotes)

quotes = lotr_sdk.get_quotes()
print(quotes)

quote = lotr_sdk.get_quote("5cd99d4bde30eff6ebccde5c")
print(quote)