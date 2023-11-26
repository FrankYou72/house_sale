from django.shortcuts import render

from ..models.buyer import Buyer
from ..models.item import Item
from ..models.payment import Payment
from utils.connection import execute_query
from ..queries.buyer_debt import query as buyer_debt


def base_view(request):
    return render(request, "base.html")


def list_buyers(request):
    buyers = execute_query(buyer_debt)
    context = {"buyers": buyers}
    print(buyers)
    return render(request, "buyer.html", context=context)


def list_offers(request, buyer_id):
    buyer = Buyer.objects.get(id=buyer_id)
    offers = buyer.offer_set.all()
    accepted_offers = offers.filter(accepted=True)
    total = sum([offer.item.start_price for offer in accepted_offers])
    payments = buyer.payment_set.all()
    total_paid = sum([payment.value for payment in payments])
    total_debt = total - total_paid
    context = {
        "buyer": buyer,
        "offers": offers,
        "total": total,
        "total_paid": total_paid,
        "total_debt": total_debt
    }
    print(context)

    return render(request, "offer.html", context=context)


def dashboard(request):
    items = Item.objects.all()
    payments = Payment.objects.all()
    total_expected = sum([item.start_price for item in items])
    total_sold = sum([item.start_price for item in items if item.bought])
    total_paid = sum([payment.value for payment in payments])

    percentage = round(100*total_sold/total_expected, 2)
    percentage_paid = round(100*total_paid/total_expected, 2)
    context = {
        "total_expected": total_expected,
        "total_sold": total_sold,
        "percentage": percentage,
        "total_paid": total_paid,
        "percentage_paid": percentage_paid
    }

    return render(request, "dashboard.html", context=context)


def payment(request, buyer_id):
    buyer = Buyer.objects.get(id=buyer_id)
    offers = buyer.offer_set.all()
    accepted_offers = offers.filter(accepted=True)
    total = sum([offer.item.start_price for offer in accepted_offers])
    payments = buyer.payment_set.all()
    total_paid = sum([payment.value for payment in payments])
    total_debt = total - total_paid
    context = {
        "buyer": buyer,
        "payments": payments,
        "total": total,
        "total_paid": total_paid,
        "total_debt": total_debt
    }

    return render(request, "payment.html", context)
