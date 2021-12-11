from endpoint import favourites, transfer


def save(request):
    return favourites.favourites_send(request)


def receive(request):
    return favourites.favourites_receive(request)


def transfer_backup(request):
    return transfer.transfer_backup(request)


def transfer_restore(request):
    return transfer.transfer_restore(request)
