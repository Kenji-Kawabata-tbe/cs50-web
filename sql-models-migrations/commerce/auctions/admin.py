from django.contrib import admin
from .models import Listing, Bid, Comment, Watchlist, Category

# Register your models here.
# Listingモデルを管理画面で表示
@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "starting_bid", "is_active", "category")
    search_fields = ("title", "description")
    list_filter = ("is_active", "category")
    ordering = ("-id",)

# Bidモデルを管理画面で表示
@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    list_display = ("listing", "user", "amount", "timestamp")
    list_filter = ("listing", "user")
    ordering = ("-timestamp",)

# Commentモデルを管理画面で表示
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("listing", "user", "timestamp")
    search_fields = ("content",)

# その他のモデルも登録
admin.site.register(Watchlist)
admin.site.register(Category)


