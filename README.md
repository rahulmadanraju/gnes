<p align="center">
    <img src=".github/gnes-logo-tight.png?raw=true" width="300" alt="GNES Generic Neural Elastic Search, logo made by Han Xiao">
</p>

<p align="center">GNES is Generic Neural Elastic Search, a highly scalable semantic search system based on deep neural network.</p>

<p align="center">
<a href="#">
    <img src="http://badge.orange-ci.oa.com/ai-innersource/nes.svg" alt="building status">
</a>
<a href="https://github.com/hanxiao/bert-as-service/blob/master/LICENSE">
    <img src="https://img.shields.io/github/license/tensorflow/tensorflow.svg"
         alt="GitHub license">
</a>
</p>

<p align="center">
  <a href="#highlights">Highlights</a> •
  <a href="#what-is-it">What is it</a> •
  <a href="#install">Install</a> •
  <a href="#getting-started">Getting Started</a> •
  <a href="#server-and-client-api">API</a> •
  <a href="#book-tutorial">Tutorials</a> •
  <a href="#speech_balloon-faq">FAQ</a>  
</p>



<h2 align="center">Highlights</h2>

- :telescope: **State-of-the-art**: 
- :hatching_chick: **Easy-to-use on every level**: a YAML file is all you need to enable GNES.
- :zap: **Fast**: 
- :octopus: **Scalable**: built on Docker Swarm, GNES can be easily scaled up on multiple CPUs, GPUs and hosts.
- :gem: **Reliable**: serves on billion-level documents and queries; days of running without a break or OOM or any nasty exceptions.


<h2 align="center">Getting Started</h2>

### Using GNES with Docker Swarm

The easiest and the recommended way to use GNES is via Docker, which uses containers to create virtual environments that isolate a GNES installation from the rest of the system. You don't need to worry about dependencies, they are self-contained in the GNES docker image. Moreover, GNES relies on the Docker Swarm for managing, scaling and conducting orchestration tasks over multiple micro-services. 

#### 1. Prerequisites

- [Docker Engine>=1.13](https://docs.docker.com/install/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Docker Machine](https://docs.docker.com/machine/install-machine/)


#### 2. Start GNES with the wizard

If you are new to GNES, it is recommended to use the wizard to config and start GNES.

```bash
bash <(curl -s https://transfer.sh/yVeBa/gnes-wizard.sh)
```

At the last step, the wizard will generate a random name for the service, say `my-gnes-0531`. Keep that name in mind. If you miss that name, you can always use `docker stack ls` to checkout the name of your service.

To tell whether the service is running successfully or not, you can use `docker stack ps my-gnes-0531`. It should give you results as follows:
```bash
ID                  NAME                         IMAGE                                           NODE                DESIRED STATE       CURRENT STATE                ERROR               PORTS
zku2zm9deli9        my-gnes-0531_encoder.1      ccr.ccs.tencentyun.com/gnes/aipd-gnes:86c0a3a   VM-0-3-ubuntu       Running             Running about an hour ago
yc09pst6s7yt        my-gnes-0531_grpc_serve.1   ccr.ccs.tencentyun.com/gnes/aipd-gnes:86c0a3a   VM-0-3-ubuntu       Running             Running about an hour ago
```

Note, the running status under `CURRENT STATE` suggests everything is fine.

To stop a running GNES service, you can use `docker stack rm my-gnes-0531`.

- Having troubles to start GNES? Checkout our [troubleshooting guide](#).
- For pro-users/developers, you may want to use our `gnes-yaml.sh` tools to [generate a YAML config via CLI](#); or simply [handcraft your own `docker-compose.yml`](#).

#### 3. (optional) Train Mode: training a GNES system 

#### 4. Index Mode: adding new documents to GNES

#### 5. Query Mode: searching relevant documents for a given query  


<h2 align="center">:book: Documentation</h2>

The official documentation of GNES is hosted on Read the Docs. It is automatically built, updated and archived on every new release. 

### Building the documentation from scratch

To build the documentation by yourself, you need to first [install sphinx](http://www.sphinx-doc.org/en/master/usage/installation.html).

```bash
git clone https://github.com/tencent/gnes.git && cd gnes
sphinx-apidoc -o ./docs/ ./gnes
cd docs && make html
```

<h2 align="center">Tutorial</h2>

<h2 align="center">Contributing</h2>

<h2 align="center">TODO</h2>

<h2 align="center">Contact</h2>

<h2 align="center">License</h2>

[Apache License 2.0](./LICENSE)