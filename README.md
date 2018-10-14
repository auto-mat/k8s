followed: http://blog.arungupta.me/gossip-kubernetes-aws-kops/
followed: https://medium.com/@markgituma/kubernetes-local-to-production-with-django-1-introduction-d73adc9ce4b4
read: https://medium.com/google-cloud/kubernetes-nodeport-vs-loadbalancer-vs-ingress-when-should-i-use-what-922f010849e0

Create cluster

    kops --state s3://kubernetes-auto-mat create cluster cluster.k8s.local --yes --vpc vpc-9263eaf7 --zones eu-west-1a --subnets subnet-6862270d,subnet-9b630eec,subnet-bae364e3   --networking=weave

Validate cluster

    kops validate cluster

Install dashboard

    kubectl create -f https://raw.githubusercontent.com/kubernetes/dashboard/master/src/deploy/recommended/kubernetes-dashboard.yaml
    kubectl apply -f k8s-dashboard-admin-user.yaml
    kubectl apply -f heapster-influxdb-grafana.yaml

Get login token

    kubectl describe sa admin-user -n kube-system
    kubectl describe secret {token id} -n kube-system

Install autoscaler

    https://github.com/kubernetes/autoscaler/tree/master/cluster-autoscaler/cloudprovider/aws
