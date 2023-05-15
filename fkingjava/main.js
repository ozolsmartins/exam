//kā piekļūstam HTML elementiem, izmantojot JS
const title=document.getElementById("virsraksts")
title.innerHTML="<i>Supreme</i>"
title.style.color="white"
title.style.backgroundColor="red"
//kā izveidojam elementus, kā nomainām elementu tekstuālo saturu vai stilojumu
const p_elements=document.createElement("p")
p_elements.innerHTML="checking"
document.body.append(p_elements)

const saraksts=document.createElement("ul")
const elemen1=document.createElement("li")
const elemen2=document.createElement("li")
elemen1.innerHTML="beta"
elemen2.innerHTML="alpha"
saraksts.append(elemen1)
saraksts.append(elemen2)
document.body.append(saraksts)
//zināt arī pogas un funkciju palaišanu, nospiežot pogu
let skaits=0
const count=document.getElementById("count")
count.innerHTML=skaits

function plusOne(){
    skaits+=1
    count.innerHTML=skaits
}
