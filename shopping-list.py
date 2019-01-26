#!/usr/bin/env python3
import os

from flask import Flask, request
import gkeepapi


app = Flask(__name__)


class ShoppingList:
    SHOPPING_LIST_ID = "1524845248826.648002074"

    def __init__(self):
        self._keep = gkeepapi.Keep()
        self._login()

    def _login(self):
        user_name = "ronan_murfy@hotmail.com"
        password = os.environ.get("GOOGLE_KEEP_TOKEN")
        self._keep.resume(user_name, password)

    def _get_sort_value_needed_for_end_of_list(self, shopping_list):
        try:
            return str(int(shopping_list.unchecked[-1].sort) - 1)
        except IndexError:
            # The shopping list is empty, any sorting will do.
            return 0

    def add(self, grocery):
        shopping_list = self._keep.get(self.SHOPPING_LIST_ID)
        sort_value = self._get_sort_value_needed_for_end_of_list(shopping_list)
        shopping_list.add(grocery, sort=sort_value)
        self._keep.sync()


def is_valid_token(token):
    # App password
    return os.environ.get("SHOPPING_LIST_TOKEN") == token


@app.route("/grocery/", methods=["POST"])
def hello_world():
    payload = request.get_json()
    if not is_valid_token(payload["token"]):
        return "Invalid token, forbidden!", 403

    grocery = payload["grocery"]
    shopping_list.add(grocery)

    return "{} added!".format(grocery)


shopping_list = ShoppingList()
