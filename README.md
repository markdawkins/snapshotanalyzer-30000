# snapshotanalyzer-30000

Demo project to manage  AWS EC2 instances snapshots

## About

This  project is a demo, and uses Boto3 to manage AWS EC2 instance snapshots.

## Configuring

shotty uses the configuration file created by the AWS CLI. e.g.

'aws configure --profile shotty'

##Running

'pipenv run "python shotty/shotty.py <command>
<--project=PROJECT>"''
*command* is list, start, or stop
*project* is opional 
