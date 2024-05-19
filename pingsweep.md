# shinra
Linux:

for i in {1..254} ;do (ping -c 1 192.168.1.$i | grep "bytes from" &) ;done


Windows CMD:

for /L %i in (1,1,255) do @ping -n 1 -w 200 192.168.1.%i > nul && echo 192.168.1.%i is up.


Powershell:

	
1..255 | % {"192.168.1.$($_): $(Test-Connection -count 1 -comp 192.168.1.$($_) -quiet)"}




from: https://www.rubyguides.com/2012/02/cli-ninja-ping-sweep/
