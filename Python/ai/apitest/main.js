const options = {
	method: 'GET',
	headers: {
		'X-RapidAPI-Key': '0b73437c2bmsh4ecc30ef11ff701p1a3afcjsn179baf7d5939',
		'X-RapidAPI-Host': 'love-calculator.p.rapidapi.com'
	}
};

function calculate(){
   male=document.getElementById("male").value
   female=document.getElementById("female").value
   fetch('https://love-calculator.p.rapidapi.com/getPercentage?sname='+ male +'&fname='+female, options)
	.then(response => response.json())
	.then(response => {
		document.getElementById("result").innerHTML=response["percentage"]+'%'
		document.getElementById("recommend").innerHTML=response["result"]
		console.log(response)
	})
	.catch(err => console.error(err));
    
}