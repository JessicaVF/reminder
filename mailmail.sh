export MAIL_PORT=8025
export MAIL_SERVER=localhost
python -m smtpd -n -c DebuggingServer localhost:8025
