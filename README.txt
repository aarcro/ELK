Use the following to setup the ELK stack after staring the Vagrant Box.

It's based on precise64-minimal-datagrok-2, the same box as moreau, so you
should already have it. This box will join the same hostbased network as moreau
but if they aren't talking to each other, take a look at your networking
settings in vbox.

To test everything:
1) log into moreau
2) telnet 192.168.56.102 5959
3) Type a message, and abort telnet
4) On the host machine browse to http://localhost:9999/local
5) Click on the default logstash dashboard and see your test message


wget -qO - http://packages.elasticsearch.org/GPG-KEY-elasticsearch | sudo apt-key add -
echo 'deb http://packages.elasticsearch.org/elasticsearch/1.3/debian stable main' |sudo tee /etc/apt/sources.list.d/elasticsearch.list
echo 'deb http://packages.elasticsearch.org/logstash/1.4/debian stable main' | sudo tee /etc/apt/sources.list.d/logstash.list

apt-get update
apt-get install elasticsearch logstash unzip openjdk-7-jre-headless nginx

wget http://download.elasticsearch.org/kibana/kibana/kibana-latest.zip
unzip kibana-latest.zip

cp -a kibana-latest /usr/share/nginx/www/prod
cp -a kibana-latest /usr/share/nginx/www/local

# Edit prod/config.js
# elasticsearch: "http://elsvipprd1.ddtc.cmgdigital.com:9200",

cp confs/logstash.conf /etc/logstash/conf.d/
# merge confs/mysettings.py with mysettings.py in medley

update-rc.d elasticsearch defaults 95 10
update-rc.d logstash defaults 95 10

service elasticsearch start
service logstash start
service nginx start

# /opt/logstash/bin/logstash -f config.conf
