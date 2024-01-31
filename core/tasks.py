import urllib.request
from celery import shared_task
from core.models import Server


@shared_task
def check_servers():
    servers = Server.objects.all()
    for server in servers:
        url = server.address
        try:
            result = str(urllib.request.urlopen(url).getcode())
            print(url, result)
            if result.startswith('2'):
                server.success += 1
            else:
                server.failure += 1
        except Exception as e:
            server.failure += 1
            print("ERROR: ", e)
        server.save()

