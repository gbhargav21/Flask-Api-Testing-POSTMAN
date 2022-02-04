# Flask-Api-Testing-POSTMAN
**Contains POST API to provide input to the server**

## **Installation Instructions**
<li>1.git clone https://github.com/mornville/flask-api.git</li>
 <li>2.cd Flask-Api-Testing-POSTMAN</li>
  <li>3.pip install -r requirements.txt</li>
  <li>4.python app.py</li>
  <li>5.In Postman add the URL( http://127.0.0.1:5000/json) and change the type to POST.</li>
  <li>6.On the body tab, change to raw and select JSON from the drop-down. </li>
 <li> 7.Click Send</li>
 
  
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

