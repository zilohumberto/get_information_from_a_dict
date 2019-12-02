build:
	docker build -t truestart-humberto .

create:
	docker run -itd --name cont-truestart-humberto truestart-humberto

start:
	docker container start cont-truestart-humberto

stop:
	docker container stop cont-truestart-humberto

restart:
	docker container restart cont-truestart-humberto

bash:
	docker exec -it cont-truestart-humberto bash

rm:
	docker rm cont-truestart-humberto