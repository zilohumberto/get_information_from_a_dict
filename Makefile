build:
	docker build -t trustart-humberto .

create:
	docker run -itd --name cont-trustart-humberto trustart-humberto

start:
	docker container start cont-trustart-humberto

stop:
	docker container stop cont-trustart-humberto

restart:
	docker container restart cont-trustart-humberto

bash:
	docker exec -it cont-trustart-humberto bash

rm:
	docker rm cont-trustart-humberto