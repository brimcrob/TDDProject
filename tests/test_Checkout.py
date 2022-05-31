import pytest
from Src.Checkout import Checkout


@pytest.fixture()
def checkout():
    checkout = Checkout()
    checkout.additemprice("a", 1)
    checkout.additemprice("b", 2)
    return checkout


# def test_CanAddItemPrice(checkout):
#    checkout.additemprice("a", 1)


# def test_CanAddItem(checkout):
#     checkout.additem("a")

def test_CanCalculateTotal(checkout):
    checkout.additem("a")
    assert checkout.calculateTotal() == 1


@pytest.mark.skip
def test_canApplyDiscount(checkout):
    checkout.addDiscount("a", 3, 2)
    checkout.additem("a")
    checkout.additem("a")
    checkout.additem("a")
    assert checkout.calculateTotal() == 2


def test_GetCorrectWithMultipleitems(checkout):
    checkout.additem("a")
    checkout.additem("b")
    assert checkout.calculateTotal() == 3


def test_canAddDiscountRule(checkout):
    checkout.addDiscount("a", 3, 2)
