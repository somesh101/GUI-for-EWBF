# Author https://github.com/somesh101
# Free in all senses to be modified and distributed :D 
# as long as above two line stays and you can add yours below this line.

import json,requests
import datetime
#i am using nanopool but otherpool does provide api for such output. 
out1=requests.get("https://api.cryptonator.com/api/ticker/btc-usd").json()
out2=requests.get("https://api.cryptonator.com/api/ticker/zec-usd").json()
out3=requests.get("https://api.cryptonator.com/api/ticker/eth-usd").json()
#change this for your Pool 
out4=requests.get("https://api.nanopool.org/v1/zec/user/t1RL3nmwnLhBpX9n1ZrRKgZXac4Pp7aCvYB").json()
out5=requests.get("http://api.fixer.io/latest?base=USD").json()

res="1 USD       : INR "
res+=str(out5['rates']['INR'])+ '\n'
res+="1 BTC       : USD "
res+=out1['ticker']['price'] + '\n'
res+="1 ZEC       : USD "
res+=out2['ticker']['price'] + '\n'
res+="1 ETH       : USD "
res+=out3['ticker']['price'] + '\n'



res+="UnConfirmed : Z   "+ out4['data']['unconfirmed_balance'] + '\n'
res+="Balance     : Z   " + out4['data']['balance'] +'\n' 
res+="Hash Rate   : Sol/s " + out4['data']['hashrate']

try:
	fp=open("balance.log",'r+')
	for each in fp:
		each=each.strip()
	tail=each.split(',')
  #this function still needs improvements. buggy in some senses
	if(float(out4['data']['balance'])<float(tail[1])+float(tail[2])):
		fp.write("---- Flag -----")
except:
	fp=fp=open("balance.log",'a+')


fp.write('\n'+str(datetime.datetime.now())+','+str(out4['data']['balance'])+','+str(out4['data']['unconfirmed_balance']))
fp.close()
print(res)
