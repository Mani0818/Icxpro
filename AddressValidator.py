name: Deploy to EC2

on:
  push:
    branches:
      - main  # Change this to your main branch name if it's different

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
        scp -o StrictHostKeyChecking=no -r ./path/to/your/files ${USERNAME}@${{ secrets.EC2_INSTANCE_IP }}:/path/on/ec2

    - name: Execute commands on EC2
      run: |
        ssh -o StrictHostKeyChecking=no ${USERNAME}@${{ secrets.EC2_INSTANCE_IP }} 'bash -s' < ./path/to/your/deployment/script.sh
