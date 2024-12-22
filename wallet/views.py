from django.shortcuts import redirect
from django.views.generic import CreateView

from wallet.models import Wallet


class WalletViewSet(CreateView):
    model = Wallet
    fields = ["wallet_name", "portfolio_value"]
    template_name = "wallet/wallet_view.html"
    success_url = "create_wallet"

    def form_valid(self, form):
        wallet = form.save(commit=False)
        wallet.user_id_id = self.request.user.id
        form.save()

        return redirect(self.success_url)

    # def form_invalid(self, form):
    #
    #     return self.render_to_response(self.get_context_data(form=form))


# class WalletViewSet(generics.CreateAPIView):
#     serializer_class = WalletSerializer
#     queryset = Wallet.objects.all()
#
#
# class GetAllWallet(generics.ListAPIView):
#     serializer_class = WalletSerializer
#     queryset = Wallet.objects.all()
#
#
# class DeleteWallet(generics.DestroyAPIView):
#     serializer_class = WalletSerializer
#     queryset = Wallet.objects.all()
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#
# class BankAccountViewSet(generics.CreateAPIView):
#     serializer_class = BankAccountSerializer
#     queryset = BankAccount.objects.all()
#
#
# class GetAllBankAccount(generics.ListAPIView):
#     serializer_class = BankAccountSerializer
#     queryset = BankAccount.objects.all()
#
#
# class DeleteBankAccount(generics.DestroyAPIView):
#     serializer_class = BankAccountSerializer
#     queryset = BankAccount.objects.all()
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
