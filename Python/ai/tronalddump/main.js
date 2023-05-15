const options = {
	method: 'GET',
	headers: {
		Accept: 'application/hal+json',
		'X-RapidAPI-Key': '0b73437c2bmsh4ecc30ef11ff701p1a3afcjsn179baf7d5939',
		'X-RapidAPI-Host': 'matchilling-tronald-dump-v1.p.rapidapi.com'
	}
};

fetch('https://matchilling-tronald-dump-v1.p.rapidapi.com/random/quote', options)
	.then(response => response.json())
	.then(response =>
        {document.getElementById("quote").innerHTML=response["value"]})
	.catch(err => console.error(err));

function select_quote(){
    fetch('https://matchilling-tronald-dump-v1.p.rapidapi.com/random/quote', options)
	.then(response => response.json())
	.then(response =>
        { 
            document.getElementById("quote").innerHTML=response["value"]
        })
	.catch(err => console.error(err));
}

