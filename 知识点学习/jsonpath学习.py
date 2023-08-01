import json
import jsonpath

book = {
  "store": {
    "book":[
      { "category": "reference",
        "author": "Nigel Rees",
        "title": "Sayings of the Century",
        "price": 8.95
      },
      { "category": "fiction",
        "author": "J. R. R. Tolkien",
        "title": "The Lord of the Rings",
        "isbn": "0-395-19395-8",
        "price": 22.99
      }
    ],
    "bicycle": {
      "color": "red",
      "price": 19.95
    }
  }
}
print(book)
json.dumps(book)
print(book)

checkurl = "$.store.book.price"
print(jsonpath.jsonpath(book, checkurl))

