from flask import Flask, jsonify, request


app = Flask(__name__)

books = [
    {
        "id": 1,
        "title": "Titanic",
    },
    {
        "id": 2,
        "title": "Troia",
    },
    {
        "id": 3,
        "title": "Eva",
    },
]


@app.route("/books", methods=["GET"])
def get_books():
    return jsonify(books)


@app.route("/books/<int:id>", methods=["GET"])
def get_book_by_id(id: int):
    book = None
    for b in books:
        if b.get("id") == id:
            book = b

    return jsonify(book)


@app.route("/books/<int:id>", methods=["PUT"])
def update_book(id: int):
    updated_book = request.get_json()

    for i, book in enumerate(books):
        if book.get("id") == id:
            books[i].update(updated_book)
            return jsonify(books[i])

    return jsonify(None)


@app.route("/books/<int:id>", methods=["DELETE"])
def remove_book(id: int):
    for i, book in enumerate(books):
        if book.get("id") == id:
            del books[i]

    return jsonify(books)


@app.route("/books", methods=["POST"])
def insert_book():
    new_book = request.get_json()
    books.append(new_book)
    return jsonify(new_book)


app.run(port=5000, host="localhost", debug=True)
