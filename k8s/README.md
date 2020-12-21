# Kubernetes deployments

## Docker image

You'll need to build Docker image first, check [README](../README.md).

Then you'll need to push it to _aleksandrvin/vrcover-shop-eu-scraper_ docker
repo:

```bash
docker push aleksandrvin/vrcover-shop-eu-scraper:latest
```

## Deployment

You'll need to create a telegram bot and start a chat with him to obtain chat id.

```bash
kubectl create -f namespace.yaml
TELEGRAM_BOT_TOKEN=YOUR-TOKEN-HERE ./create-secrets.sh
kubectl create -f cronjob.yaml
```

## Check results

```
kubectl -n vrcover-shop-eu-scraper get cj
```

And logs.

And telegram.
