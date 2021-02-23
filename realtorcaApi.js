const realtor = require('realtorca');

let opts = {
  LongitudeMin: -79.6758985519409,
  LongitudeMax: -79.6079635620117,
  LatitudeMin: 43.57601549736786,
  LatitudeMax: 43.602250137362276,
  PriceMin: 100000,
  PriceMax: 410000
};


var queryUrl = realtor.buildUrl(opts);
console.log( queryUrl );
//https://www.realtor.ca/Residential/Map.aspx#LongitudeMin=-79.6758985519409&LongitudeMax=-79.6079635620117&LatitudeMin=43.57601549736786&LatitudeMax=43.602250137362276&PriceMin=100000&PriceMax=425000

// Parse options from url
var options = realtor.optionsFromUrl(queryUrl);
console.log(options);


realtor.post(opts)
  .then(function(data) {
      //json response
      console.log(data)
  })
  .catch(err => {
      console.log(err)
  });