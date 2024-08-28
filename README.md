# `Amazon Web Service`

[`Question 1`]()

Create an EC2 instance at Amazon Web Service (AWS) with the following configuration:

    * Name: 		new-instance
    * Region:		ap-south-1
    * Image: 		Ubuntu Server 22.04 (HVM), SSD Volume Type
    * Architecture: 	64-bit (x86)
    * Instance Type: 	t2.micro, 1v CPU, 1GB Memory
    * Key-pair:		RSA type
    * Network Settings: Allow SSH traffic from Anywhere.

[`Question 2`](instance.py)

Write a python script to start, stop and reboot AWS EC2 instances using Boto3.

[`Question 3`](s3.py)

Write a python script to upload any sample file to AWS S3 bucket using Boto3.
