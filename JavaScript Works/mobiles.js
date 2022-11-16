// # number of mobiles 
// # print 5g mobile names
// # costly mobile
// # cheapest mobile
// # print AMOLED display mobile names
// # sort mobiles based on price
// # print samsung 5g mobiles
// # print costly samsung mobile

mobiles = [
    { "id": 1000, "name": "samsungA52", "band": "4g",
     "display": "AMOLED", "price": 27000, "brand": "samsung" },
    { "id": 1001, "name": "samsungA52s", "band": "5g",
     "display":"AMOLED", "price": 32000, "brand": "samsung" },
    { "id": 1002, "name": "redminote10", "band": "4g",
     "display": "led", "price": 17000, "brand": "redmi" },
    { "id": 1003, "name": "redminote11pro", "band": "5g",
     "display": "superAMOLED", "price": 20000, "brand": "redmi" },
    { "id": 1004, "name": "samsungA72", "band": "5g",
     "display": "AMOLED", "price": 27000, "brand": "samsung" },
    { "id": 1005, "name": "samsungA53", "band": "5g",
     "display": "AMOLED", "price": 27000, "brand": "samsung" },
    { "id": 1006, "name": "samsungm52", "band": "5g",
     "display": "AMOLED", "price": 27000, "brand": "samsung" },
    { "id": 1007, "name": "samsungm53", "band": "5g",
     "display": "AMOLED", "price": 27000, "brand": "samsung" },
    { "id": 1008, "name": "samsungA22", "band": "5g",
     "display": "AMOLED", "price": 27000, "brand": "samsung" }
]


// console.log(mobiles.length);

// mobiles.filter(n=>n.band=='5g').forEach(n=>console.log(n.name))

// a=mobiles.reduce((n1,n2)=>n1.price>n2.price?n1:n2)
// console.log(a.name);

// a=mobiles.reduce((n1,n2)=>n1.price<n2.price?n1:n2)
// console.log(a.name);

// mobiles.filter(n=>n.display=="AMOLED").forEach(n=>console.log(n.name))

// m=mobiles.sort((n1,n2)=>n1.price<n2.price?-1:1)
// console.log(m);

// mobiles.filter(n=>n.band=='5g' && n.brand=="samsung").forEach(n=>console.log(n.name))

// max=mobiles.filter(n=>n.brand=="samsung").reduce((n1,n2)=>n1.price>n2.price?n1:n2)
// console.log(max.name);