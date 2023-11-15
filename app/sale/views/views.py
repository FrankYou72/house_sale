from django.shortcuts import render

from ..models.buyer import Buyer
from ..models.offer import Offer, OfferSerializer
from ..models.item import Item

def base_view(request):
    return render(request, "base.html")


def list_buyers(request):
    buyers = Buyer.objects.all().order_by('name')
    return render(request, "buyer.html", context={"buyers": buyers})


def list_offers(request, buyer_id):
    buyer = Buyer.objects.get(id=buyer_id)
    offers = buyer.offer_set.all()
    accepted_offers = offers.filter(accepted=True)
    total = sum([offer.item.start_price for offer in accepted_offers])

    return render(request, "offer.html", context={"buyer": buyer, "offers": offers, "total": total})


def dashboard(request):
    items = Item.objects.all()
    total_expected = sum([item.start_price for item in items])
    total_sold = sum([item.start_price for item in items if item.bought])
    percentage = round(100*total_sold/total_expected, 2)

    return render(request, "dashboard.html", context={
        "total_expected": total_expected,
        "total_sold": total_sold,
        "percentage": percentage
    })


def payment(request, buyer_id):
    buyer = Buyer.objects.get(id=buyer_id)
    offers = buyer.offer_set.all()
    accepted_offers = offers.filter(accepted=True)
    total_bought = sum([offer.item.start_price for offer in accepted_offers])
    payments = buyer.payment_set.all()
    total_paid = sum([payment.value for payment in payments])
    total_debt = total_bought - total_paid

    return render(
        request,
        "payment.html",
        context={
            "buyer": buyer,
            "payments": payments,
            "total_bought": total_bought,
            "total_paid": total_paid,
            "total_debt": total_debt
        })



