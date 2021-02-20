Kuberenets manifests for Auto*mat z.s. internal infrastructure
-------------------------------------------------------------------

These manifests are used for `Auto*mat's <https://auto-mat.cz/>`_ internal infrastructure. These manifests, combined with manifests stored in our private AWS code commit repository (the secrets), allow for the deployment of much of Auto*mat's internal IT infrastructure.

Some of these manifests are written using the `ytt <https://get-ytt.io/>`_ In order to use these manifests you must first put them through the ytt prepocessor, here is an exmple of how:

``ytt -f mapa-test.yaml -f lib/ | kubectl apply -f -``

Databases are stored using digital ocean's managed database solution. When creating a new database, you should create a new user for that database, revoke the "doadmin" role for that user, and give it ownership of the database.

``ALTER DATABASE "klub-automat" OWNER TO "klub-automat";``

``REVOKE "klub-automat" from "doadmin";``

Connecting to internal services
-------------------------------------

You can connect to an internal service using kubectl to forward a port to your local machine. For example this command will allow you to connect to redis commander:

```
kubectl port-forward <redis-commander-pod> 8084:8081
firefox http://localhost:8084/
```
