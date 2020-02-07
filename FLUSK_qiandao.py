#-*-coding:utf-8-*-
from flask import Flask,render_template
#import urlib.request
from flask import request
from flask import redirect
from flask import jsonify
import argparse
import json
import glob
import pickle
import os
import time

app=Flask(__name__)
app.config["JSON_AS_ASCII"]=False
@app.route("/qiandao",methods=["POST","GET"])
def main():
    if request.method=="GET":
        names=get_names_today()
        return render_template("_app.html",names=names)
    else:
        this_name=request.form.get("name")
        this_state=request.form.get("state")
        this_is_out=request.form.get("is_out")
        print(this_is_out)
        this_ip= request.remote_addr
        time_now= time.strftime('%Y-%m-%d %H:%M:%S')
        insert(this_name,this_state,this_is_out,this_ip,time_now)    
        return 'suc'

@app.route("/save",methods=["POST","GET"])
def save():
    now=time.strftime('%Y-%m-%d',time.localtime(time.time()))
    with open("qiandao_file","wb")as f:
        pickle.dump(t_global,f)
    os.system("python3 get_result.py")
    ret="static/qiandao_"+now+".txt"
    return ret

def insert(name,state,is_out,ip,time_now):
    now=time.strftime('%Y-%m-%d',time.localtime(time.time()))
    if now not in t_global:
        t_global[now]={}
    t_global[now][name]={"state":state,"ip":ip,"is_out":is_out,"time_now":time_now}
    
def get_names_today():
    now=time.strftime('%Y-%m-%d',time.localtime(time.time()))
    if now not in t_global:
        names=load_all_names()
        return names
    else:
        ret=[]
        for name in all_names:
            if name in t_global[now]:
                continue
            else:
                ret.append(name)
        return ret

def load_all_names():
    names=[]
    for line in open(all_name_file,"r",encoding="utf-8"):
        names.append(line.strip())
    return names

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', default=9100, type=int, help='开启服务的端口号')
    args = parser.parse_args()
    dir_path = os.path.dirname(os.path.abspath(__file__))    
    all_name_file=os.path.join(dir_path,"all_name")
    now=time.strftime('%Y-%m-%d',time.localtime(time.time()))
    all_names=load_all_names()
    if glob.glob("qiandao_file")==[]:
        t_global={}
    else:
        with open("qiandao_file","rb")as f:
            t_global=pickle.load(f)


    app.run(host="0.0.0.0",port=args.port,debug=True,threaded=True)
    #print test("ST烯碳董事郭社乐辞职曾任公司财务总监遭深交所通报批评")
