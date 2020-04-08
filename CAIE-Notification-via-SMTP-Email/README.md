### If you want to keep this file runing on the remote server when close your ssh connection, the following command will help you!
```
cd .../CAIE-Notification-via-SMTP-Email
nohup sudo python  -u CAIE-Notification.py > caie.log 2>&1 &
```
### If you want to watch the logs:

``` cat caie.log```
