from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_iam as iam,
)

class EC2Stack(Stack):

    def __init__(self, scope, construct_id, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        # Create a VPC
        vpc = ec2.Vpc(self, "VPC",
            max_azs=2,
        )

        # User Data Script
        user_data_script = """#!/bin/bash
echo 'User data script executed' > /var/log/user-data.log
"""
        
        # Create an EC2 instance
        instance = ec2.Instance( self, "TestInstance",
            instance_name="TestInstance",
            instance_type=ec2.InstanceType("t4g.micro"),
            machine_image=ec2.MachineImage.latest_amazon_linux2023(
                cpu_type=ec2.AmazonLinuxCpuType.ARM_64
            ),
            vpc=vpc,
            user_data=ec2.UserData.custom(user_data_script)
        )
        
        instance.role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name("AmazonSSMManagedInstanceCore")
        )