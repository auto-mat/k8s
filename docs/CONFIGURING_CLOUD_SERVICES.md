AWS
=====


Currently we are using AWS for S3, cloudfront, and SES.

Billing on AWS
-------------

It is important to have [properly configured billing allarms](https://us-east-1.console.aws.amazon.com/cloudwatch/home?region=us-east-1#alarmsV2:?) because costs can sometimes be unexpected:

![image](https://user-images.githubusercontent.com/1391608/176616396-2e85abfb-7d80-4a5a-83cb-40a25f70e5bf.png)

You can also use [the cost explorer](https://us-east-1.console.aws.amazon.com/cost-management/home?region=eu-west-1#/dashboard) to see where the money is going.

SES (Send Email Service)
------------------------

It is important to occasionally check the [configuration of SES and the reputation metrics](https://eu-west-1.console.aws.amazon.com/ses/home?region=eu-west-1#/reputation). If reputation gets too low, the account can be susspended and also our emails can end up in SPAM.

![image](https://user-images.githubusercontent.com/1391608/176617439-ae5875c3-0279-498c-8be5-8be24ad7c394.png)

S3
--

Here is a link to [the S3 admin](https://s3.console.aws.amazon.com/s3/buckets?region=eu-west-1).

Digital ocean
==========

We run k8s on digital ocean.

k8s services are accessed via a (completely pointless other than costing us money) load balancer which imediately redirects to nginx which does the actual load balancing in k8s.

[load balancers](https://cloud.digitalocean.com/networking/load_balancers?i=99d236&preserveScrollPosition=true)

Sometimes DO will automatically create a second even more pointless load balancer which will cost us even more money. This should be deleted (TODO: figure out how to stop this).

Here is a link to the k8s cluster where you can [scale the size of the cluster](https://cloud.digitalocean.com/kubernetes/clusters/008342a2-fd75-46c7-b5dc-a84ed93f9a3e/resources?expand=398385&i=99d236).
