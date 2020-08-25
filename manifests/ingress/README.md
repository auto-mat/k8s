Followed:
-

[DO tutorial](https://www.digitalocean.com/community/tutorials/how-to-set-up-an-nginx-ingress-on-digitalocean-kubernetes-using-helm)

```
helm install nginx-ingress stable/nginx-ingress --set controller.publishService.enabled=true
```
