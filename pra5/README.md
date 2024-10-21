# PRA5:Deploying an ML APP to the Cloud

## Setting up AWS Beanstalk Application

1. Sign up for [AWS Account](https://aws.amazon.com/free/)
2. Create an App in AWS Elastic Beanstalk

    Make sure region is the same using us-east-1 (N. Virginia).

    Video reference: https://www.youtube.com/watch?v=2BoVhej0QVI&t=504s&ab_channel=TinyTechnicalTutorials

    On IAM console, create a role for EC2, `1ec2-beanstalk` with the following permission policies
    - AWSElasticBeanstalkMulticontainerDocker
    - AWSElasticBeanstalkWebTier
    - AWSElasticBeanstalkWorkerTier

    Use the following options when configuring application and environment.

    | | | | 
    --- | --- | ---
    Application Name | `test-app`
    Environment | Test-app-env
    Platform | Python
    Service access > Service role | aws-elasticbeanstalk-service-role
    Service access > EC2 instance profile | ec2-beanstalk
    Root volume (boot device) > Root volume type | General Purpose 3(SSD)
    IMDSv1 | Check Deactivated
    Capacity > Fleet composition | Check Spot Instance

    Note, a **Service role** will be automatically(?) created for you, but you need to create your own **EC2 instance profile**.

    Launch configurations are mentioned here: https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environments-cfg-autoscaling-launch-templates.html#environments-cfg-autoscaling-launch-templates-options.



    
