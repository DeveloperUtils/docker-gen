# docker-gen-nxt

## run

0. `./build.sh`
1. `docker run -it --rm -v $(pwd):/usr/src/app -v "/var/run/docker.sock:/tmp/docker.sock:ro" -e DOCKER_HOST='unix://tmp/docker.sock' devtools/docker-gen:latest`


## Links
* https://github.com/jwilder/docker-gen
* https://github.com/nginx-proxy/nginx-proxy
* https://docker-py.readthedocs.io/en/stable/index.html
