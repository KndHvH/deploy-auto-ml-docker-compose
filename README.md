# deploy-auto-ml-docker-compose
This project uses docker-compose to manage the deployment of a ML model trained on weather data. The app allows users to input weather data and receive a prediction for the weather condition. The app also stores user queries in a PostgreSQL database for later analysis.

 Technology and Resources

- [Python 3.10](https://www.python.org/downloads/release/python-31010/) - **pre-requisite**
- [Docker](https://www.docker.com/get-started) - **pre-requisite**
- [Docker Compose](https://docs.docker.com/compose/) - **pre-requisite**
- [Pipenv](https://github.com/pypa/pipenv)
- [Makefile](https://www.geeksforgeeks.org/how-to-install-make-on-ubuntu/) **pre-requisite**

*Please pay attention on **pre-requisites** resources that you must install/configure.*


### How to Build

```
make docker/build
make docker/up/database
```

### How to Run

```
make docker/run
```

*The project will be running at `http://localhost:8501/`*

The `entrypoint` of this project is the `main.py` file on the root path.

## Extras infos

- If you use the [vscode](https://code.visualstudio.com/) editor we have some examples of [launch.json](.docs/vscode.md) to speed up your tests.

    *Note: When you run the install command (using docker or locally), a .env file will be created automatically based on [env.template](env.template)*