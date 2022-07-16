from cloud.determine_cloud_env import using_gcp
from cloud.gcp import gcp_firestore


def transfer_backup(request):
    if using_gcp():
        return gcp_firestore.transfer_backup(request.json.get('code'), request.json)


def transfer_restore(request):
    if using_gcp():
        return gcp_firestore.transfer_restore(request.json.get('code'))
