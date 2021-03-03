Kuberenets manifests for Auto*mat z.s. internal infrastructure
-------------------------------------------------------------------

These manifests are used for [Auto*mat's](https://auto-mat.cz/) internal infrastructure. These manifests, combined with manifests stored in our private AWS code commit repository (the secrets), allow for the deployment of much of Auto*mat's internal IT infrastructure.

Currently these manifests are installed on a k8s cluster running on [DigitalOcean](https://cloud.digitalocean.com/projects?i=99d236). You'll need to [install kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/) and [configure it](https://www.digitalocean.com/docs/kubernetes/how-to/connect-to-cluster/) to work with DigitalOcean in order to update these configuration files.

Some of these manifests are written using the [ytt](https://get-ytt.io/) In order to use these manifests you must first put them through the ytt prepocessor, here is an exmple of how:

`ytt -f mapa-test.yaml -f lib/ | kubectl apply -f -`

Databases are stored using digital ocean's managed database solution. When creating a new database, you should create a new user for that database, revoke the "doadmin" role for that user, and give it ownership of the database.

`ALTER DATABASE "klub-automat" OWNER TO "klub-automat";`

`REVOKE "klub-automat" from "doadmin";`

Connecting to internal services
-------------------------------------

You can connect to an internal service using kubectl to forward a port to your local machine. For example this command will allow you to connect to redis commander:

```
kubectl port-forward <redis-commander-pod> 8084:8081
firefox http://localhost:8084/
```

Monitoring kubernetes
-------------------------

One way to see the state of kubernetes is to look in the [Dashboard](https://cloud.digitalocean.com/kubernetes/clusters/008342a2-fd75-46c7-b5dc-a84ed93f9a3e/db/99d23692-3f06-4cb4-a133-813c52e0e3ba/#/overview?namespace=_all). More detailed performance statistics can be found in grafana. To access grafana forward it's port.

```
kubectl port-forward   svc/doks-cluster-monitoring-grafana 8000:80
```

And go to the page that lists pod statistics: `http://localhost:8000/d/85a562078cdf77779eaa1add43ccec1e/kubernetes-compute-resources-namespace-pods?orgId=1&refresh=10s&var-datasource=default&var-cluster=&var-namespace=default`. If you are prompted to log in, the username is `admin` password can be found in the `k8s-secrets` repo on AWS CodeCommit.
