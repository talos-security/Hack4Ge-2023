if [ $# -eq 0 ]
  then
    IP="127.0.0.1" 
else
    IP=$1
fi

docker build -t sqli2 .
docker run -p $IP:5001:5001 sqli2