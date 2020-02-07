sh kill.sh $1
echo "old process killed"
nohup python3 FLUSK_qiandao.py  --port $1 &
echo "new started at port 9600"
