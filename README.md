Kuberenets manifests for Auto*mat z.s. internal infrastructure
-------------------------------------------------------------------

These manifests are used for `Auto*mat's <https://auto-mat.cz/>`_ internal infrastructure. These manifests, combined with manifests stored in our private AWS code commit repository (the secrets), allow for the deployment of much of Auto*mat's internal IT infrastructure.

Some of these manifests are written using the `ytt <https://get-ytt.io/>`_ In order to use these manifests you must first put them through the ytt prepocessor, here is an exmple of how:

``ytt -f mapa-test.yaml -f lib/ | kubectl apply -f -``
