# Flask-Api-Testing-POSTMAN
**Contains POST API to provide input to the server**

## **Installation Instructions**
<li>git clone https://github.com/gbhargav21/Flask-Api-Testing-POSTMAN.git</li>
 <li>cd Flask-Api-Testing-POSTMAN</li>
  <li>pip install -r requirements.txt</li>
  <li>python app.py</li>
  <li>In Postman add the URL( http://127.0.0.1:5000/json) and change the type to POST.</li>
  <li>On the body tab, change to raw and select JSON from the drop-down. </li>
 <li>Click Send</li>
 
  
## usage
### POST Request for order total
<li>Send a POST request to  http://127.0.0.1:5000/json
</li>


```json
{
  "order_items": [
    {
      "name": "bread",
      "quantity": 2,
      "price": 2200
    },
    {
      "name": "butter",
      "quantity": 1,
      "price": 5900
    }
  ],
  "distance": 1200,
  "offer": {
    "offer_type": "FLAT",
    "offer_val": 1000
  }
}
```
<li>Response From the Server</li>

```json
{
    "order_total": 14300
}
```
## ASSUMPTIONS
- Maximum Name length = 50
- Maximum item quantity = 500
- Maximum item price(paisa) = 10000
- distance range(min, max) (metre) = (0, 500000)
- Initial Delivery Slab (lower, upper, cost) (lower and upper bound in Km) = [[0, 10, 50], [10, 20, 100],[20, 50, 500], [50, 500, 1000]]
## Required Additional Tools
<li>POSTMAN for testing API
<li> Download and Install from here -https://www.postman.com/downloads/

