## Psifos Docker

### Description

Psifos is a web application for electronic voting led by the Participa Uchile team.

### How to execute

The repository has three submodules, `psifos-frontend`, `psifos-backend-op`, and `psifos-backend-info`. These three are necessary to run the application.

The application has two modes, production and development. For this there are different docker-compose.yml files. Also, each submodule has Dockerfiles for production and development.

* Production: `docker-compose.prod-yml` / `Dockerfile.prod`
* Development: `docker-compose.dev-yml` / `Dockerfile.dev`

To run the application you must run: `docker-compose -f [yml file] up -d --build`

To stop the application you must run: `docker-compose -f [yml file] stop`

In development, you should run the first migration and create the admin user manually:
```
$ docker compose -f docker-compose.dev.yml exec back-op-dev alembic upgrade head
$ docker compose -f docker-compose.dev.yml exec back-op-dev python create_debug_admin.py
```
Now, you can go to `http://localhost:3000/psifos` and enter with the following credentials:
- user: `admin`
- pass: `12345`

### Environment Variables

The application has environment variables for its operation. These must go in an .env located in the `psifos-dockerized` directory

| Variable  | Description  |
|-----------|--------------|
| DATABASE_USER | Database admin user |
| DATABASE_PASS | Database user password |
| DATABASE_HOST    | Database container id |
| DATABASE_NAME  | Name of the database on which to work |
| SECRET_KEY  | A secret phrase that will perform hash |
| APP_FRONTEND_URL  | URL where the frontend will be hosted |
| APP_BACKEND_OP_URL  | URL where the back-op will be hosted |
| APP_BACKEND_INFO_URL  | URL where the back-info will be hosted |
| TYPE_AUTH  | Authentication type (cas or oauth) |
| CAS_URL  | Authentication server URL |
| OAUTH_TOKEN_URL  | Oauth2 token url |
| OAUTH_AUTHORIZE_URL  | Oauth2 Authorize URL |
| OAUTH_CLIENT_ID  | Oauth2 client id |
| OAUTH_CLIENT_SECRET  | Oauth2 client secret |
| OAUTH_USER_INFO_URL  | Oauth2 url for info user |
| CELERY_BROKER_URL  | Celery broker container id |
| CELERY_RESULT_BACKEND  | Celery result  container id |



