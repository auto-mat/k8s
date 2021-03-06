#!/bin/bash
kubectl apply -f manifests/config-maps/
kubectl apply -f manifests/ingress/
kubectl apply -f manifests/
ytt -f manifests/ytt/ -f  manifests/ytt/lib/ | kubectl apply -f -
