#!/bin/bash
kubectl apply -f manifests/config-maps/
kubectl apply -f manifests/ingress/
kubectl apply -f manifests/
ytt -f manifests/ytt/ -f manifests/ytt/lib/ -f manifests/ytt/config-maps/ -f manifests/ytt/data/ | kubectl apply -f -
