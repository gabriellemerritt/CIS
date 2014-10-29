// setting default symbol for first time look up 
var defaultSymbol = "AAPL";
var Symbol = defaultSymbol;
var click = 0; 

var xhrRequest = function (url, type, callback) {
  var xhr = new XMLHttpRequest();
  xhr.onload = function () {
    callback(this.responseText);
  };
  xhr.open(type, url);
  xhr.send();
};



function retrieveStock(stock,firstMsg) {
	var url = "http://dev.markitondemand.com/Api/v2/Quote/json?symbol="+stock;
	//send stock request to markit ondemand 
	xhrRequest(url, 'GET',
		function(responseText){
			// scan json and load in data into these variables
			var json = JSON.parse(responseText); 
			var stockName = json.Name; 
			var stockSymbol = json.Symbol;
			var LastPrice = Math.round(json.LastPrice * 100);
			var stockChange = Math.round(json.Change *100)/100;
			var changePercent = Math.round(json.ChangePercent *100); 
			console.log(stockSymbol);
			console.log("Last price is" + LastPrice);
			console.log("Change in percent since yesterday"+ changePercent);
			// create a dictionary that contains symbol, current price, and change in percent
			var stockDictionary = { 
				"Symbol": stockSymbol, 
				"LastPrice": LastPrice,
				"ChangePercent": changePercent
			};
			// hardcode stock to microsoft if there is no previous symbol
			// if (firstMsg){
			// 	stockDictionary.stockSymbol = symbol;
				
			// }
			// send to pebble  
			Pebble.sendAppMessage(stockDictionary, 
				function(e){
					console.log("Stock info sent to pebble successfully!");
				},
				function(e){
					console.log("Error Sending Stock data to pebble");
				}
			);
		}
	);	
}

// function stockError(err) {
//   console.log("Error requesting Stock!");
// }

// function getStock() {
// 	var name = window.localStorage.getItem('stock');
// 	retrieveStock(name);
// }


// Listen for when the watchface is opened
Pebble.addEventListener('ready', 
  function(e) {
    console.log("PebbleKit JS ready!");
    //Get Apple Stock
    console.log("what symbol is from local storage " + Symbol);
    if (!Symbol) { Symbol = "AAPL";}
    var firstMsg = true;
    retrieveStock(Symbol,firstMsg); 
  }
);

// Listen for when an AppMessage is received
Pebble.addEventListener('appmessage',
  function(e) {
    console.log("AppMessage received!");
    // variable to record how many times i've clicked select
	    // symbol = e.payload.symbol; // load the symbol from dictionary
	    // localStorage.setItem("symbol", symbol); // store the symbol
	    // firstMsg = false;  // we have recieved amessage so we dont have to hardcode symbol
	    //Symbol = window.e.payload[100];
	    if ((click % 2) ==0 ) { Symbol = "GOOG";}
	    else { Symbol = "AAPL";}
	    console.log("what symbol is from local storage " + Symbol);
	    console.log(click); 
	    
	    retrieveStock(Symbol,true);
	click = click +1; 
	if (click > 100){click = 1;}
	}
  );
