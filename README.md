# Online shops watchers collection

## Installation

```
pipx install git+https://github.com/aleksandr-vin/shops-watcher.git
```

## Gopro shop

Running:

```
check-gopro-shop "
  https://gopro.com/en/nl/shop/mounts-accessories/ultra-wide-lens-mod/AEWAL-001.html
  https://gopro.com/en/nl/shop/mounts-accessories/macro-lens-mod/AEWAL-021.html
"
```

Will give you result, like:

```
NOT_AVAILABLE - Macro Lens Mod - €111.99
ORDERABLE - Ultra Wide Lens Mod - €87.99
```

## vrcover-shop

Build Docker image, then try locally or [deploy in k8s](k8s/README.md).

```
docker build -t aleksandrvin/vrcover-shop-eu-scraper .
```
