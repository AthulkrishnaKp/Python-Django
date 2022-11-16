var courses=[
    {cname:"django",fee:35000,durasion:5,teqs:[
        "python","javascript","html","css","bootstrap","django","angular"
    ]},
    {cname:"MEARN",fee:55000,durasion:6,teqs:[
        "javascript","html","css","bootstrap","node","express","angular","react"
    ]},
    {cname:"bigdata",fee:75000,durasion:7,teqs:[
        "python","pig","hive","sqoop","pyspark","ml"
    ]},
    {cname:"ASP.net",fee:35000,durasion:5,teqs:[
        "c#","javascript","html","css","bootstrap"
    ]},
]

// courses.map(c=>c.cname).forEach(n=>console.log(n))
// courses.map(c=>console.log(c.cname))


// courses whose fees greater than 40000
// courses.filter(c=>c.fee>40000).forEach(n=>console.log(n.cname))

// var costly_course=courses.reduce((c1,c2)=>c1.fee>c2.fee?c1:c2)
// console.log(costly_course.cname);

// // descending order sorting by duration of courses.
// courses.sort((c1,c2)=>c2.durasion-c1.durasion).forEach(c=>console.log(c.cname))



// ******************************************************************************

//   Find Function .....................

// var bdata=courses.find(c=>c.cname=="bigdata")
// console.log(bdata.cname);


// ******************************************************************************

// Some function :

// is Testing available? result will be a bolean value ,ie True or False there we use some function:

// var isAvailable=courses.some(c=>c.cname=="bigdata")
// console.log(isAvailable);

// var arr=[10,11,12]
// console.log(arr.includes(10));

// print courses which has Javascript in teqs :
//  includes can only be used for arrays

courses.filter(c=>c.teqs.includes("javascript")).forEach(c=>console.log(c.cname))