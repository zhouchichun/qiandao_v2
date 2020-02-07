import pickle

with open("qiandao_file","rb")as f:
    t=pickle.load(f)

for time,con in t.items():
#    print(time)
    with open("static/qiandao_%s.txt"%time,"w",encoding="utf-8")as f:

        for ll,name_content in enumerate(con.items()):
             name,content=name_content
 #           print(name)
  #          print("健康状况:%s"%content["state"])
   #         print("ip:%s"%content["ip"])
    #        print("--------------------------------------------------------")
             f.write("%s\t%s\t%s\t%s\t%s\t%s\n"%(ll+1,name,content["state"],content["ip"],content["is_out"],content["time_now"]))
