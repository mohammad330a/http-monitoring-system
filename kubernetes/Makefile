run_kube:
	kubectl apply   -f  http-monitor/templates/secret.yml
	kubectl apply   -f  http-monitor/templates/config-map.yml
	kubectl apply   -f  http-monitor/templates/mariadb-statefulset.yml
	kubectl apply   -f  http-monitor/templates/deployment.yml
	kubectl apply   -f  http-monitor/templates/celery_deployment.yml
	kubectl apply   -f  http-monitor/templates/celery_beat_deployment.yml
	kubectl apply   -f  http-monitor/templates/redis_deployment.yml
	kubectl apply   -f  http-monitor/templates/mariadb-write-service.yml
	kubectl apply   -f  http-monitor/templates/mariadb-read-service.yml
	kubectl apply   -f  http-monitor/templates/service.yml
	kubectl apply   -f  http-monitor/templates/redis_service.yml
