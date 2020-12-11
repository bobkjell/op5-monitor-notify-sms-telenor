# op5-monitor-notify-sms-telenor
Send SMS notifications from OP5 Monitor using Telenor SMS API

## Requirements
* Authentication details to Telenor SMS API
* python-requests
<br />

## Configure OP5 Montor with Commands for host- and service-notifications
host_notify_sms_telenor <br />
$USER1$/custom/notify_sms_telenor.py -P $CONTACTPAGER$ -H $HOSTNAME$ -ho $HOSTOUTPUT$ -hs $HOSTSTATE$ -c "customerid" -u "username basic auth" -px "password xml" -pb "password basic auth" -f "fromsender"
  
service_notify_sms_telenor <br />
$USER1$/custom/notify_sms_telenor.py -P $CONTACTPAGER$ -H $HOSTNAME$ -S $SERVICEDESC$ -so $SERVICEOUTPUT$ -ss $SERVICESTATE$ -c "customerid" -u "username basic auth" -px "password xml" -pb "password basic auth" -f "fromsender"

<br />

Use the configured Commands as host- and service-notifications cmds on contacts.
  
## More info
* Use /opt/monitor/etc/resource.cfg to hide auth-details from check_command.
* HTTP errors are logged in: /var/log/op5/sms_error.log
