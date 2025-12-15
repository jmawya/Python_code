const a=[1,2,3]
const person={
    name:"Jannatul",
     age:23,
     institution:"DMCC"
}
console.log(person.age)

const ab=[1,2,3];
ab.push(80);
ab.unshift(0);
console.log(ab);

ab.forEach(element =>{
  console.log(element)
})

const dd=ab.map(element => element * 2)
console.log(dd);

//const dd=ab.map(element=>{
// return element*2  // it's create a new array where every element is two fold
// }) 
// console.log(dd);
// we will filter number enormous then 50 and we will not take it
const de=ab.filter(element => element>50 )
console.log(de);

//find
const da=[20,30,40, 80,70]

const e=da.find(element => element>20)
console.log(e)


const erosion=[{
    name:"Jannatul",
     age:23,
     institution:"DMCC"
},
 {
    name:"Rafi",
    age:20,
    institution:"VAS"
},
{
    name:"Raha",
    age:60,
    institution:"dAS"
}

]
const sn=erosion.find(erosion => erosion.age > 20);
console.log(sn); 

//is the data exist or not
const an=[20,30,40, 80,70];
console.log(an.includes(40));

const dsa=da.every(element=> element>800)
console.log(dsa);