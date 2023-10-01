# Meme Search

View your favorite memes with this crappy app! Not to be used by anyone. JavaScript free.

## Docker Hub Image

Find it on the Docker Hub: [sanoti5896/meme-search](https://hub.docker.com/r/sanoti5896/meme-search)

Image contains instructions on how to configure this app with your sacred meme collection.

## Running Locally (Python)

This portion will assume you have Python already configured.

Make a folder in this repo called `SearchItems`. This will be ignored by default in git.

#### Development Build

```shell
python app.py
```

#### Production App

```shell
gunicorn -b 0.0.0.0:5000 app:app
```

Alternatively you can provide the `FLASK_ENV=production` in PyCharm or similar IDE.

## Running Locally (Docker) 

### Docker Compose (preferred)

Modify the volume in `docker-compose.yml` to match your host folder. Run the following command:

```shell
docker-compose up --build -d
```

Once finished use this to stop:

```shell
docker-compose down
```

### Docker (alternate manual instructions)

#### Build the Docker image

```shell
docker build -t meme-search .
```

####  Run the Docker container

Exposes port 5000 and maps it to a local port 5432.
Replace `./SearchItems` with a folder of your choice.

```shell
docker run -d -p 5432:5000 -v ./SearchItems:/app/SearchItems meme-search
```