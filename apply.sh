#!/bin/bash
if [ ! -z "$KUBERNETES_CLUSTER_CERTIFICATE" ]
then
    echo "$KUBERNETES_CLUSTER_CERTIFICATE" | base64 --decode > cert.crt
fi

kubecmd (){
    if [ -z "$KUBERNETES_TOKEN" ]
    then
        kubectl $@
    else
        kubectl \
            --kubeconfig=/dev/null \
            --server=$KUBERNETES_SERVER \
            --certificate-authority=cert.crt \
            --token=$KUBERNETES_TOKEN \
            $@
    fi
}
kubecmd apply -f manifests/config-maps/
kubecmd apply -f manifests/ingress/
kubecmd apply -f manifests/
ytt -f manifests/ytt/ -f  manifests/ytt/lib/ | kubecmd apply -f -
