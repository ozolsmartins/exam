let x;
x=8;
const y=23;
console.log(x)

if(x>5){console.log("ok")}
else{console.log("no")}
for(let i=0; i<5;i++){
    let c=6;
    console.log(i)
}
while(x>0){
    console.log(x)
    x--;
}
const a=[1,4,2,7,2]
console.log(a.length)
console.log(a[3])
for(const item of a){
    console.log(item)
}
let obj={
    name:"vards",
    age:17
}
console.log(obj.age)
function funkcijas_nosauk(a,b){
    return a+b
}
console.log(funkcijas_nosauk(2,3))

const page=document.createElement("p"); //izveido elementu
page.id="page";
page.innerHTML="<h1>hello world</h1>"; //elementa ieksejo saturu
page.classList.add("red"); //pievieno klasi .red
document.body.appendChild(page); //pievieno elementu body beigas

const list=document.createElement("ul");
boys=["Mārcis","Toms","Tomass"];
for(const boy of boys){
    list.innerHTML+="<li>"+boy+"</li>";
};
document.body.appendChild(list);
const people=[
    {
        name:"Atis",
        surname:"Ozols",
        age:21
    },
    {
        name:"Mārcis",
        surname:"Mārcovs",
        age:12
    },
    {
        name:"Jānis",
        surname:"Paraudziņš",
        age:4
    },
    {
        name:"Mārtiņs",
        surname:"Ozols",
        age:17
    },
];
const table=document.createElement("table");

for(const person of people){
    const row=document.createElement("tr");
    row.innerHTML="<td>"+person.name+"<td></td>"+person.surname+"</td>";
    table.appendChild(row);
};
table.style.border="1px solid black"
document.body.appendChild(table)