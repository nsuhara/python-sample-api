# sample-api

## develop

| category       | item          | detail                   | note |
| :------------- | :------------ | :----------------------- | :--- |
| environment    | github-branch | develop                  |      |
|                | ecs-cluster   | ms-sandbox-a-dev-cluster |      |
|                | healthcheck   | /sandbox-a/healthcheck   |      |
| rds            | host          | {rds:host}               |      |
|                | port          | 5432                     |      |
|                | database      | sandbox_a                |      |
|                | user          | postgres                 |      |
|                | password      | postgres                 |      |
| bastion server | pem           | ms-dev-ec2.pem           |      |
|                | host          | {bastion server:host}    |      |

## api

| service  | method | example                                  | note |
| :------- | :----- | :--------------------------------------- | :--- |
| read all | get    | [link](app/apis/client/get_read_all.py)  |      |
| read one | get    | [link](app/apis/client/get_read_one.py)  |      |
| upsert   | post   | [link](app/apis/client/post_upsert.py)   |      |
| update   | put    | [link](app/apis/client/put_update.py)    |      |
| delete   | delete | [link](app/apis/client/delete_delete.py) |      |

## check code

```command.sh
source config/{localhost | develop | release}
python -B -m pylint --rcfile=.pylintrc -f parseable `find app -name "*.py" -not -path "app/tests"`
```

## unit test

```command.sh
source config/{localhost | develop | release}
python -B -m unittest discover tests
```

## launch docker

```command.sh
Dockerfiles/docker_compose_up.sh
```

## launch flask

```command.sh
brew services start postgresql
source config/{localhost | develop | release}
flask db init
flask db migrate
flask db upgrade
flask run
```

## migrate error

```command.sh
# ERROR [root] Error: Can't locate revision identified by {id}
flask db revision --rev-id {id}
```

## connect to rds

```command.sh
psql -h {rds:host} -p {rds:port} -d {rds:database} -U {rds:user}
```

## connect to rds using port forwarding

```command.sh
ssh -N -L 15432:{rds:host}:{rds:port} -i "{bastion server:pem}" -p 22 {bastion server:host}
psql -h localhost -p 15432 -d {rds:database} -U {rds:user}
```

## commit without updating

```command.sh
git commit --allow-empty -m "empty commit"
git push origin {environment:branch}
```

## docker login

```command.sh
docker ps
# CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                    NAMES
# 0af68012c7c9        app_app             "/code/entrypoint.sh"    38 seconds ago      Up 37 seconds       0.0.0.0:8000->8000/tcp   app_app_1
# 9901a105e8d5        postgres:11.5       "docker-entrypoint.s…"   39 seconds ago      Up 37 seconds       0.0.0.0:5432->5432/tcp   app_postgres_1

docker exec -i -t {app_app:CONTAINER ID} /bin/bash
```

## example

### flask run

```command.sh
source config/development
flask run
```

### docker compose up

```command.sh
Dockerfiles/docker_compose_up.sh
```

### port forwarding

```command.sh
ssh -N -L 15432:{rds:host}:5432 -i "ms-dev-ec2.pem" -p 22 {bastion server:host}
psql -h localhost -p 15432 -d sandbox_a -U postgres
```
