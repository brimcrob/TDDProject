import pytest
from Src.Checkout import Checkout
def test_CanInstatiateCheckout():
    co = Checkout

def test_CanAddItemPrice():
    co = Checkout()
    co.additemprice("a", 1)

def test_CanAddItem():
    co = Checkout()
    co.additem("a")



