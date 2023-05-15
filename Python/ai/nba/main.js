const options = {
	method: 'GET',
	headers: {
		'X-RapidAPI-Key': '0b73437c2bmsh4ecc30ef11ff701p1a3afcjsn179baf7d5939',
		'X-RapidAPI-Host': 'free-nba.p.rapidapi.com'
	}
};

let data=[]
function load_data(response_data){
	data=response_data
	let dropdown=document.getElementById("players")
	console.log(response_data)
	response_data.forEach(player => {
		let option_element=document.createElement("option")
		option_element.innerHTML=player.first_name+" "+player.last_name
		option_element.value=player.id
		dropdown.append(option_element)
	});
}
fetch('https://free-nba.p.rapidapi.com/players?page=0&per_page=100', options)
	.then(response => response.json())
	.then(response => load_data(response.data))
	// .then(response => console.log(response.data[0].team)) izvada 1 elem komandu
	.catch(err => console.error(err));
function select_player(){
	select=document.getElementById("players")
	i=select.selectedIndex
	console.log(select.options[i].value)
	console.log(data[i])
	name_element=document.getElementById("name")
	team_element=document.getElementById("team")
	name_element.innerHTML=data[i].first_name+" "+data[i].last_name
	team_element.innerHTML="Player for "+ data[i].team.full_name
}
