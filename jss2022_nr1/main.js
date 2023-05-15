// const luksofors=document.getElementById("luksofors");
// const colors=["#cc3232","#e7b416","#2dc937"];
// let selected=0;
// luksofors.style.backgroundColor=colors[selected];


colorSet=[["#cc3232","black","black"],
["#cc3232","#e7b416","black"],
["black","black","#2dc937"],
["black","#e7b416","black"]]

let selected=0
setState(selected)


function setState(selected){
    for(let i=0;i<3;i++){
        const luks=document.getElementById("a"+(i+1))
        luks.style.backgroundColor=colorSet[selected][i]

    }
}
function changeColor(){
    if(selected===3){
        selected=0;
    }
    else{
        selected+=1;
    }
    setState(selected);
}
