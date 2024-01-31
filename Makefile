push_dockerhub:
	docker build -t http_monitoring_system:1.0 .
	docker tag http_monitoring_system:1.0 mohammad330a/http_monitoring_system:1.0
	docker push mohammad330a/http_monitoring_system:1.0

