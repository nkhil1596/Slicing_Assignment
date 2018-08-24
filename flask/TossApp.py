from flask import Flask,json,jsonify
app = Flask(__name__)
users = [{

	'Requester':'Nidhi',
	'status': 'requested',
	'Item': 'Biryani',
	'Id':'01',
	'cost':'00',
	'Bidder1':{'Name':'karan','age':'30','price':'100'},
	'Bidder2':{'Name':'vipul','age':'35','price':'150'},
	'Bidder3':{'Name':'Arnav','age':'21','price':'80'},
	'Bidder4':{'Name':'Chauhan','age':'25','price':'120'},
	'Grabber':{'Name':'Arnav','Type_of_delievery':'Home_Delievery_Delievered through someone else'}},
	{'Requester':'Nikhil',
	'status': 'requested',
	'Item': 'Pizza',
	'Id':'02',
	'cost':'00',
	'Bidder1':{'Name':'Sumit','age':'32','price':'200'},
	'Bidder2':{'Name':'Amit','age':'37','price':'250'},
	'Bidder3':{'Name':'Ronit','age':'38','price':'175'},
	'Bidder4':{'Name':'Vinnet','age':'31','price':'150'},
	'Grabber':{'Name':'Vinnet','Type_of_delievery':'Home Delievery'}},
	{'Requester':'Nirav',
	'status': 'requested',
	'Item': 'Momos',
	'Id':'03',
	'cost':'00',
	'Bidder1':{'Name':'Ajay','age':'21','price':'20'},
	'Bidder2':{'Name':'Ajit','age':'23','price':'25'},
	'Bidder3':{'Name':'Abhay','age':'26','price':'80'},
	'Bidder4':{'Name':'Abhi','age':'28','price':'120'},
	'Grabber':{'Name':'Ajit','Type_of_delievery':'Home Delievery'}},
]
@app.route('/CreateRequestByName/<string:Requester>/Provider', methods=['GET'])
def returnUsername(Requester):
	detail = [user for user in users if user['Requester'] == Requester]
	return jsonify({'user' : detail[0]})
	for detail in data['users']:
		print(detail)
		return (json.dumps(detail))



if __name__ == '__main__':

    app.run(debug=True)