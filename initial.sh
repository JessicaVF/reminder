export FLASK_APP=microblog.py
export MAIL_USERNAME=test
export MAIL_SERVER=smtp.googlemail.com
export MAIL_PORT=587
export MAIL_USE_TLS=1
export MAIL_PASSWORD=test
export FLASK_DEBUG=1
sudo /etc/init.d/elasticsearch start
export ELASTICSEARCH_URL=http://localhost:9200
