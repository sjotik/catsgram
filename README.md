
<br/>
<p align="center">
  <a href="https://github.com/sjotik/kittygram_final">
    <img src="frontend/src/images/logo.svg" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">KITTYGRAM</h3>

  <p align="center">
    Instagram for cats
    <br/>
    <br/>
  </p>
</p>

![workflow](https://github.com/sjotik/kittygram_final/actions/workflows/main.yml/badge.svg)

## Table Of Contents

* [About the Project](#about-the-project)
* [Getting Started](#getting-started)
  * [Installation](#installation)
* [Technologies](#used-technologies)
* [License](#license)
* [Authors](#authors)

## About The Project

Social network for cats like instagram.
You can share images and achievements your pet cats.

## Getting Started

If you don't have Docker on your server, use manual from [Official page](https://docs.docker.com/engine/install/)

### Installation

1. [Clone](git@github.com:sjotik/kittygram_final.git) this project repo.

2. For starting this project locally use next command from project directory:

`docker compose up -d`

Open http://127.0.0.1:9000 in browser. **ENJOY**

### ENV variable

Project use PostgresQL database and for deploy you need create **.env** file in root directory with variables:
+ POSTGRES_DB=***set_name_for_DB***
+ POSTGRES_USER=***set_db_user***
+ POSTGRES_PASSWORD=***set_password***
+ DB_HOST=**db**
+ DB_PORT=**5432**

Also there is taken out django variables **SECREC_KEY** and **DEBUG**. You need to set them.

## Used Technologies

<table class="tg">
<thead>
  <tr>
    <th class="tg-wp8o"><a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a></th>
    <th class="tg-wp8o"><a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer"> <img src="https://cdn.worldvectorlogo.com/logos/django.svg" alt="django" width="40" height="40"/> </a></th>
    <th class="tg-wp8o"><a href="https://reactjs.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/react/react-original-wordmark.svg" alt="react" width="40" height="40"/> </a></th>
    <th class="tg-wp8o"><a href="https://www.postgresql.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/postgresql/postgresql-original-wordmark.svg" alt="postgresql" width="40" height="40"/> </a></th>
    <th class="tg-wp8o"><a href="https://www.docker.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original-wordmark.svg" alt="docker" width="40" height="40"/> </a></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-wp8o">Python</td>
    <td class="tg-wp8o">Django<br>RestFramework</td>
    <td class="tg-wp8o">React</td>
    <td class="tg-wp8o">Postgres</td>
    <td class="tg-wp8o">Docker</td>
  </tr>
</tbody>
</table>

## License

Distributed under the MIT License. See [LICENSE](https://github.com/sjotik/kittygram_final/blob/main/LICENSE.md) for more information.

## Authors

* [**Sjotik**](https://github.com/sjotik/)
