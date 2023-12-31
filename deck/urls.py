from django.urls import path
from . import views


urlpatterns = [
    path('decks', views.deck_list, name='home'),
    path('decks/add', views.new_deck, name='new-deck'),
    # path('decks/<int:pk>', views.DeckDetailsView.as_view(), name='deck-details'),
    path('decks/<int:pk>', views.card_details, name='deck-details'),
    path('decks/<int:pk>/edit', views.edit_deck, name='edit-deck'),
    path('decks/<int:pk>/delete', views.delete_deck, name='delete-deck'),
    path('decks/<int:pk>/new_card', views.new_card, name='new-card'),
    path('decks/<int:pk>/card<int:card_pk>/edit', views.edit_card, name='edit-card'),
    path('decks/<int:pk>/card<int:card_pk>/delete', views.delete_card, name='delete-card'),
]