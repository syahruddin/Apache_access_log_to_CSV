import shlex
from datetime import datetime
read = open("access.log", "r")
hasil = open("access.csv", "x")


hasil.write("ip_address,identd,userid,time,request_line,status_code,object_size,referrer,user_agent\n")
for line in read:
    #print(line)
    if "." in line:
        splited_line = shlex.split(line)
        splited_line[3] = splited_line[3] + " " + splited_line[4]
        splited_line.pop(4)
        splited_line.pop(9)

        splited_line[3] = splited_line[3].strip("[")
        splited_line[3] = splited_line[3].strip("]")
        splited_line[3] = datetime.strptime(splited_line[3],"%d/%b/%Y:%H:%M:%S %z").strftime("%Y-%m-%d %H:%M:%S")
        
        print(splited_line)
        converted_line = ""
        for word in splited_line:
            converted_line = converted_line + "\"" + word.strip() + "\"" + ","
        hasil.write(converted_line+"\n")

print("finish")