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

## Python Application

### Start venv and install dependencies

```bash
# create the virtual env
python3 -m venv venv    

# activate the environment
source venv/bin/activate    # on wsl
venv\Scripts\activate       # on windows

# install dependencies
pip install -r requirements.txt
```

```bash
# run the flask app
export FLASK_APP=app.py          # wsl
$env:FLASK_APP="application.py"  # windows (powershell)
$env:FLASK_ENV = "development"
flask run
```

```bash
# you can grab all dependencies with
pip freeze
```

### Upload Flask App to Elastic Beanstalk App

Elastic Beanstalk App accessible here: http://test-app-env.eba-fctwsrc4.us-east-1.elasticbeanstalk.com/

Reference for elastic beanstalk config: [video](https://youtu.be/dhHOzye-Rms?si=yz6kkZtbdzNxz2UF)

1. zip relevant files 
    - .ebextensions
    - models/
    - templates/
    - application.py
    - requirements.txt
2. Upload zip file to Elastic Beanstalk App
