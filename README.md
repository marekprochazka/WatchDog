# WatchDog


<image src="static/logo.png" alt="watchod_logo" style="width: 50%;" />

### How to run the project locally:
* [Install docker](https://docs.docker.com/engine/install/)
* Clone this repository (via [cli](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository) or tools such as [github desktop](https://desktop.github.com/) or [gitkraken](https://www.gitkraken.com/))
* Open project in your favorite IDE
* In root folder create `.env` file from `.env.example`
* run `scripts/init_git.bash` (skip if ends with error)
* run `docker compose build`
* run `docker compose up`
  * the app is served at port 8000
* for intellisense inside IDE you might need to install node dependencies locally which you can do by `cd` into `services/frontend` and running `npm i` 

### Updating dependencies
* run `docker compose run --rm --user root django bash`
* for python run `poetry add ...`
* for frontend go to `services/frontend` and run `npm i ...`

### Formatting
* ./scripts/format.sh or ./scripts/format.bat

### Linting
* ./scripts/lint.sh or ./scripts/lint.bat

### BE tests
* docker compose --file docker-compose.test.yml  up

### Project description

Webscraper controlling prices of (mostly) supplements on various e-shops. The goal is to provide users with the best price for the product they are looking for. The app will also provide price history for each product and more.

### Technologies used
  * Template: [django-vue-base](https://github.com/marekprochazka/django-vue-base)
  * Scraper: TBD
  * Backend: [Django](https://www.djangoproject.com/)
  * Frontend: [Vue.js](https://vuejs.org/)
  * Database: [PostgreSQL](https://www.postgresql.org/)
  * Database hosting: [Supabase](https://supabase.io/)
  * Hosting: TBD
  * [Docker](https://www.docker.com/)
  * [Poetry](https://python-poetry.org/)
  * [Vite](https://vitejs.dev/)
  * Backend testing: [pytest](https://docs.pytest.org/en/6.2.x/)
  * Frontend testing: TBD
  * CI/CD: [Github Actions](https://github.com/features/actions)
  * API documentation: [drf-spectacular](https://drf-spectacular.readthedocs.io/en/latest/)
  * Code formatting: [black](https://pypi.org/project/black/)




