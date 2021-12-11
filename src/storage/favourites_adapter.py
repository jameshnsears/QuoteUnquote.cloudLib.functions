from cloud.determine_cloud_env import using_gcp
from cloud.gcp import gcp_firestore


def favourites_send(request):
    if using_gcp():
        return gcp_firestore.favourites_send(request.json.get('code'), request.json.get('digests'))


def favourites_retrieve(request):
    if using_gcp():
        return gcp_firestore.favourites_retrieve(request.json.get('code'))
