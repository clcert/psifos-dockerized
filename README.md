## Psifos Docker

### Description

Psifos is a web application for electronic voting led by the Participa Uchile team.

### How to execute

The repository has three submodules, `psifos-frontend`, `psifos-backend-op`, and `psifos-backend-info`. These three are necessary to run the application.

The application has two modes, production and development. For this there are different docker-compose.yml files. Also, each submodule has Dockerfiles for production and development.

* Production: `docker-compose-prod-yml` / `Dockerfile.prod`
* Development: `docker-compose-dev-yml` / `Dockerfile.dev`

To run the application you must run: `docker-compose -f [yml file] up -d --build`

To stop the application you must run: `docker-compose -f [yml file] stop`


The app works with a Caddy web server

