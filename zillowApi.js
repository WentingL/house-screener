const zillow = require('node-zillow');

// get key from environment variable
const z = new zillow();

const params = {
  // address: '2512 Mapleton Ave.',
  // citystatezip: '80304',
  zpid: 1111111,
};

// prints the results
 z.get('GetZestimate', params)
 .then(function(results) {
    //handle your results here for instance
    console.log(results) 
  })
 .catch(err =>{
 	console.log("We encountered an error")
 });
