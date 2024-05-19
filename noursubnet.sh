for i in {1..254} ; for r in {1..254} ;do (proxychains4 ping -c 1 172.16.$i.$r > /dev/null 2>&1 | grep "bytes from" &) ;done
