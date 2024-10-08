#!/bin/bash

# apt -y install unzip

# install besttrace
if [ ! -f "besttrace" ]; then
    wget https://cdn.ipip.net/17mon/besttrace4linux.zip
    unzip besttrace4linux.zip
    chmod +x besttrace
fi

## start to use besttrace

next() {
    printf "%-70s\n" "-" | sed 's/\s/-/g'
}

clear
next

ip_list=(42.81.86.33 111.164.185.221 211.137.160.5 219.141.147.210 202.96.209.133 58.60.188.222 202.106.50.1 210.22.97.1 210.21.196.6 221.179.155.161 211.136.112.200 120.196.165.24 202.112.14.151)
ip_addr=(天津电信 天津联通 天津移动 北京电信 上海电信 深圳电信 北京联通 上海联通 深圳联通 北京移动 上海移动 深圳移动 成都教育网)
# ip_len=${#ip_list[@]}

echo '2c54fff516c0f472177dd6f1115b9bc1339c424a' > besttrace.lic
for i in {0..12}
do
	echo ${ip_addr[$i]}
	./besttrace -q 1 ${ip_list[$i]}
	next
done
