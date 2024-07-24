#!/usr/bin/env python3

from aws_cdk import App
from ec2.ec2_stack import EC2Stack

app = App()

ec2_stack = EC2Stack(app, "EC2Stack")

app.synth()
