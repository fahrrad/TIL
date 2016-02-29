
# Opening an url. Note that the setting here is to use a corporate firewall for everything, except basf.net stuff

from urllib.request import urlopen
import os 

os.environ['http_proxy']='http://someproxy:8080'
os.environ['no_proxy']='localhost,127.0.0.1,basf.net'
 
url = "http://pdeluh0001955.basfad.basf.net/MtxInterlayerWebServices/DirectDataExchangeLIMSDService/v1/Service.svc?wsdl"
doc = urlopen(url).read( )
print(doc)


