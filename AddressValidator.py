name: Deploy to EC2

on:
  push:
    branches:
      - main 

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Set up SSH
      uses: webfactory/ssh-agent@v0.5.3
      with:
        ssh-private-key: ${{ secrets.EC2_SSH_KEY }}

    - name: Copy files to EC2
  run: |
    scp -o StrictHostKeyChecking=no -r AddressValidator.py ${USERNAME}@${{ secrets.EC2_INSTANCE_IP }}:/home/ec2-user/


    - name: Execute commands on EC2
      run: |
        ssh -o StrictHostKeyChecking=no ${USERNAME}@${{ secrets.EC2_INSTANCE_IP }} 'bash -s' < ./path/to/your/deployment/script.sh
