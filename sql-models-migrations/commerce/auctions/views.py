from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import User, Listing, Bid, Comment, Watchlist, Category
from django.contrib import messages

def index(request):
    listings = Listing.objects.filter(is_active=True)
    return render(request, "auctions/index.html", {"listings": listings})


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def listing_page(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id)
    highest_bid = listing.bids.order_by('-amount').first()
    is_watching = Watchlist.objects.filter(user=request.user, listing=listing).exists() if request.user.is_authenticated else False

    return render(request, "auctions/listing.html", {
        "listing": listing,
        "highest_bid": highest_bid,
        "is_watching": is_watching
    })

@login_required
def create_listing(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        starting_bid = request.POST["starting_bid"]
        category_name = request.POST.get("category")
        image_url = request.POST.get("image_url")

        category, _ = Category.objects.get_or_create(name=category_name)

        listing = Listing.objects.create(
            title=title,
            description=description,
            starting_bid=starting_bid,
            category=category,
            image_url=image_url,
            owner=request.user
        )
        return HttpResponseRedirect(reverse("index"))

    categories = Category.objects.all()
    return render(request, "auctions/create.html", {"categories": categories})

@login_required
def place_bid(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id)
    bid_amount = float(request.POST["bid"])

    highest_bid = listing.bids.order_by('-amount').first()
    if bid_amount < listing.starting_bid or (highest_bid and bid_amount <= highest_bid.amount):
        messages.error(request, "Your bid must be higher than the current highest bid.")
    else:
        Bid.objects.create(listing=listing, user=request.user, amount=bid_amount)
        messages.success(request, "Bid placed successfully!")

    return HttpResponseRedirect(reverse("listing_page", args=[listing_id]))

@login_required
def watchlist(request):
    watchlist_items = Watchlist.objects.filter(user=request.user)
    return render(request, "auctions/watchlist.html", {"watchlist_items": watchlist_items})

@login_required
def add_comment(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id)
    content = request.POST["comment"]
    Comment.objects.create(listing=listing, user=request.user, content=content)
    return HttpResponseRedirect(reverse("listing_page", args=[listing_id]))

@login_required
def close_auction(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id)
    if request.user == listing.owner:
        listing.is_active = False
        listing.save()
        messages.success(request, "Auction closed successfully.")
    return HttpResponseRedirect(reverse("listing_page", args=[listing_id]))

def category_list(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    listings = Listing.objects.filter(category=category, is_active=True)
    return render(request, "auctions/category.html", {"listings": listings, "category": category})

@login_required
def toggle_watchlist(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id)

    # 既にウォッチリストにあるかどうかを確認
    watchlist_item = Watchlist.objects.filter(user=request.user, listing=listing).first()

    if watchlist_item:
        # 既にウォッチリストにある場合は削除
        watchlist_item.delete()
        messages.success(request, "Removed from Watchlist!")
    else:
        # なければ新規作成
        Watchlist.objects.create(user=request.user, listing=listing)
        messages.success(request, "Added to Watchlist!")

    return HttpResponseRedirect(reverse("listing_page", args=[listing_id]))
