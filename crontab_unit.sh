# Run the bandwidth monitor emailer script at 8 AM and 8 PM daily and log output.
# SMTP variables are assumed to be set at the top of the crontab file.
0 8 * * * /root/bandwidth-monitor-emailer/run.sh >> /var/log/cron/bandwidth_monitor.log 2>&1