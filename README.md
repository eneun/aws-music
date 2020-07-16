# aws-music
## Instruction
1. Launch one EC2 instance (free tier, e.g., t2.micro), using the following `user data` command, and open 80 port from the `security group`.

```
#include
https://raw.githubusercontent.com/eneun/aws-music/master/start.sh
```
2. Check if the website works through the public IP address.
3. Make an **S3)) bucket and make it public.
4. Set up the IAM role to EC2 with full S3 access.
5. Submit the S3 information on the website that we launched.
6. Check if posting function works.