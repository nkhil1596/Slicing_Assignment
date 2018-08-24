from flask import Flask,json,jsonify
app = Flask(__name__)
@app.route('/CreateRequestByName/<string:Requester>/Provider', methods=['GET'])
def returnUsername(Requester):

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
	string_data =json.dumps(users)
	database_file = open("store.py","w+")
	database_file.write(string_data)
	print (string_data)
	return jsonify({"users": string_data})
@app.route('/CreateRequestByName/<string:Requester>/Provider', methods=["POST"])
def new_names():
    database_file = open("store.py", "r")
    read_file = database_file.read()
    # print read_file
    object_name =json.loads(read_file)

    if not request.json and not 'name' in request.json:
       abort(400)
       
       name ={
       "Requester": request.json['Requester']
}
       object_name.append(Requester)
       print (object_name)

    string_object_name =json.dumps(object_name)
    print (string_object_name)
    open_database_file = open("store.py", "w")
    open_database_file.write(  string_object_name)
    print (open_database_file)
    return jsonify({"all_data": open_database_file})

if __name__ == '__main__':


    app.run(debug=True)