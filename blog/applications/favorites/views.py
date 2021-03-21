
from django.shortcuts import render
#
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
#
from django.views.generic import (
    View,
    ListView,
    DeleteView
)

from applications.entry.models import Entry

#
from .models import Favorites
# Create your views here.

class UserPageView(LoginRequiredMixin, ListView):
    template_name = "favorites/profil.html"
    context_object_name = 'entries-user'
    login_url = reverse_lazy('users_app:user-login')

    def get_queryset(self):
        return Favorites.objects.entries_user(self.request.user)


class AddFavoritesView(LoginRequiredMixin, View):
    login_url = reverse_lazy('users_app:user-login')

    def post(self, request, *args, **kwargs):
        user = self.request.user
        entry = Entry.objects.get(id=self.kwargs['pk'])

        Favorites.objects.create(
            user=user,
            entry=entry,
        )
        return HttpResponseRedirect(
            reverse(
                'favorites_app:profil'
            )
        )

class FavoritesDeleteView(DeleteView):
    model = Favorites
    success_url = reverse_lazy('favoritos_app:perfil')

