######### MODULES
from web3 import Web3,HTTPProvider
from web3.middleware import geth_poa, geth_poa_middleware
import json
from flask import Flask,request

######### SETTING OBJECTS
w3 = Web3(Web3.HTTPProvider("https://mainnet-rpc.thundercore.com"))
app = Flask(__name__)
private_key = "3754287ebaf7a8e73a79d74430d77af682d30d060266194b6cb8556cae906587"
mainAddress = "0xA44eB9298E017e3e174478B135c5bBF4b86813A1"
nonce = w3.eth.getTransactionCount(mainAddress)

######## SETTING UP FUNCTION
def sendThunderToken(to, value):
  nonce = w3.eth.getTransactionCount(mainAddress)
  tx = {
  'nonce' : nonce,
  'to' : to,
  'value' : w3.toWei(value , 'ether'),
  'gas' : 21000,
  'gasPrice' : w3.toWei('50', 'gwei')
  }
  sign_tx = w3.eth.account.signTransaction(tx, private_key)
  tran_hash = w3.eth.sendRawTransaction(sign_tx.rawTransaction)
  txn = w3.toHex(tran_hash)
  return txn

####### CREATEING API
@app.route('/test')
def setuphandler():
	nonce = w3.eth.getTransactionCount(mainAddress)
	return str(nonce)

@app.route('/sendThunderToken', methods = ['POST'])
def sendZilHandler():
	index = request.json
	address = index["address"]
	amount = index["amount"]
	tx = sendThunderToken(address, amount)
	return tx
