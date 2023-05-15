// 1. ievērojot pareizu tabulas HTML struktūru, aizpildīt tabulu ar vienu rindu, kas satur
// 3 šūnas - vārdu, uzvārdu, klasi
const tabula=document.getElementById("name")
const row=document.createElement("tr")
console.log(row)
const data1=document.createElement("td")
const data2=document.createElement("td")
const data3=document.createElement("td")
data1.innerHTML="Martins"
data2.innerHTML="Ozols"
data3.innerHTML="11"
row.append(data1)
row.append(data2)
row.append(data3)
tabula.append(row)

// 2. klikšķinot abas pogas, attiecīgā count elementa saturam jāpalielinās par 1
let summa=0
const sum=document.getElementById("sum")
sum.innerHTML=summa
let skaits=0
const count1=document.getElementById("count1")
count1.innerHTML=skaits
function plusOne1(){
    skaits+=1
    count1.innerHTML=skaits
    summa+=1
    sum.innerHTML=summa
}

let skaits2=0
const count2=document.getElementById("count2")
count2.innerHTML=skaits2
function plusOne2(){
    skaits2+=1
    count2.innerHTML=skaits2
    summa+=1
    sum.innerHTML=summa
}

// 3. summas elementā uzrādīt abu count elementu summu

// 4. switch theme nomaina lapas motīvu, ja fons ir balts un teksts melns -
// nomaina fonu un melnu un tekstu uz baltu un otrādi.
const colors=["white","black"]
let selected=0
colorSet=["white","black"]

function switchTheme(){
    if(selected===1){
        selected=0;
        document.body.style.color=colors[1]
    }
    else{
        selected+=1;
        document.body.style.color=colors[0]
    }
    document.body.style.backgroundColor=colors[selected];
    

}






