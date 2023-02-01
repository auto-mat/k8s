Followed:
-

[Caddy tutorial](https://github.com/caddyserver/ingress)

```
helm template caddy-ingress ./caddy-ingress-src/charts/caddy-ingress-controller \
  --namespace=caddy-system \
    > caddy-ingress.yaml

```
