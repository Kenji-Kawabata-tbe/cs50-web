from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("listing/<int:listing_id>", views.listing_page, name="listing_page"),
    path("create", views.create_listing, name="create_listing"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("toggle_watchlist/<int:listing_id>", views.toggle_watchlist, name="toggle_watchlist"),
    path("category/<str:category_name>", views.category_list, name="category_list"),
    path("bid/<int:listing_id>", views.place_bid, name="place_bid"),
    path("comment/<int:listing_id>", views.add_comment, name="add_comment"),
    path("close/<int:listing_id>", views.close_auction, name="close_auction"),
]
