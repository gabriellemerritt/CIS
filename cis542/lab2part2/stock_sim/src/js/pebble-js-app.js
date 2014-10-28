// setting default symbol for first time look up 
var defaultSymbol = "AAPL";
var symbol = defaultSymbol;

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
			var json = JSON.parse(responseText); 
			var stockName = json.Data.Name; 
			var stockSymbol = json.Data.Symbol;
			var LastPrice = Math.round(json.Data.LastPrice);
			var stockChange = Math.round(json.Data.Change);
			var changePercent = Math.round(json.Data.ChangePercent); 
			console.log("Last price is" + LastPrice);
			console.log("Change in percent since yesterday"+ changePercent);

			var stockDictionary = { 
				"Symbol": stockSymbol 
				"LastPrice": lastPrice
				"ChangePercent": changePercent

			};
			if (firstMsg){
				stockDictionary.stockSymbol = symbol;
				
			}
			// send to pebs 
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
    symbol = localStorage.getItem("symbol");
    if (!symbol) { symbol = "AAPL";}
    var firstMsg = true;
    retrieveStock(symbol,firstMsg); 
  }
);

// Listen for when an AppMessage is received
Pebble.addEventListener('appmessage',
  function(e) {
    console.log("AppMessage received!");
 //    var firstMsg;
	// if (e.payload.init) 
	// {
	//     firstMsg = true;
	//     retrieveStock(symbol,firstMsg);
	// }
	//   else if (e.payload.fetch) {
	//     firstMsg = false;
	//     retrieveStock(symbol,firstMsg);
	//   }
	//   else if 
	    e.payload.symbol
	    symbol = e.payload.symbol;
	    localStorage.setItem("symbol", symbol);
	    firstMsg = false;
	    retrieveStock(symbol,firstMsg);
	  
  });
