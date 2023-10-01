# Meme Search

View your favorite memes with this crappy app! Not to be used by anyone. JavaScript free.

## Run Production App

```shell
gunicorn -b 0.0.0.0:5000 app:app
```

## Docker Compose (preferred)

### Start app

```shell
docker-compose up --build -d
```

### Stop app

```shell
docker-compose down
```

## Docker (alternate manual instructions)

### Build the Docker image

```shell
docker build -t meme-search .
```

###  Run the Docker container

Exposes port 5000 and maps it to a local port 5432.
Replace `./SearchItems` with a folder of your choice.

```shell
docker run -d -p 5432:5000 -v ./SearchItems:/app/SearchItems meme-search
```