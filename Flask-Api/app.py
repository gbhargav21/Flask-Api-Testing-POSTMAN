from flask import Flask
from flask import jsonify
from flask import Flask, request

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def welcome():
    return "Server is Running!!"
@app.route('/json', methods=['POST'])
def json_example():
    jsondata = request.get_json()
    costs_total = []
    delivery_cost=[]
    delivery_slabs = [[0, 10, 50], [10, 20, 100],[20, 50, 500], [50, 500, 1000]]
    for i in jsondata["order_items"]:
    # name minmum length=50
    # quantity 500
    # price 10000
        quantity = i["quantity"]
        price = i["price"]
        name = i["name"]
        if len(name) <= 0 or len(name) >= 50:
            return jsonify({"Message":"The length of the item is Out of Range......"})
        elif price <= 0 or price >= 10000:
            return jsonify({"Message":"Price Out of Range......"})
        elif quantity <= 0 or quantity >= 500:
            return jsonify({"Message":"Quantity  Out of Range!!! "})
        else:
            tot = quantity*price
            costs_total.append(tot)
    j = jsondata['distance']
    for i in delivery_slabs:
         o = i[0]*1000
         f = i[1]*1000
         if j>=0 or j<=500000:
            if j>=o and j<=f:
                charge=i[2]*100
                delivery_cost.append(charge)
            else:
                return jsonify({"Message":"Distance Out of Range...."}) 

         else:
             return jsonify({"Message":"Distance Out of Range...."}) 

    offer=jsondata["offer"]
    typ=offer.get("offer_type").lower()
    value=offer.get("offer_val")
    if typ=="flat":
        total=sum(costs_total)
        jsa=delivery_cost[0]
        z=total+jsa
        z=z-value
        return jsonify({"order_total":z})
    elif typ=="delivery":
        s=sum(costs_total)
        return jsonify({"order_total":s})
    else:
        total=sum(costs_total)
        jsa=delivery_cost[0]
        z=total+jsa
        return jsonify({"Order_total":z})

if __name__ == '__main__':
    app.run()