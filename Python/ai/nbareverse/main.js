const options = {
	method: 'GET',
	headers: {
		'X-RapidAPI-Key': '0b73437c2bmsh4ecc30ef11ff701p1a3afcjsn179baf7d5939',
		'X-RapidAPI-Host': 'free-nba.p.rapidapi.com'
	}
};

let data=[]
let players=[]
function load_data(response_data){
	data=response_data
	let dropdown=document.getElementById("teams")
	console.log(response_data)
	response_data.forEach(teams => {
		let option_element=document.createElement("option")
		option_element.innerHTML=teams.full_name
		dropdown.append(option_element)
	});
}
fetch('https://free-nba.p.rapidapi.com/teams?page=0&per_page=100', options)
	.then(response => response.json())
	.then(response => load_data(response.data))
	// .then(response => console.log(response.data[0].team)) izvada 1 elem komandu
	.catch(err => console.error(err));

fetch('https://free-nba.p.rapidapi.com/players?page=0&per_page=100', options)
	.then(response => response.json())
	.then(response => load_players(response.data))
	// .then(response => console.log(response.data[0].team)) izvada 1 elem komandu
	.catch(err => console.error(err));
function load_players(response_data){
		players=response_data
		console.log(response_data)
	}



function select_team(){
	list=document.getElementById("player")
	list.innerHTML=" "
	console.log(players)
	select=document.getElementById("teams")
	i=select.selectedIndex
	// console.log(select.options[i].value)
	// console.log(data[i])
	team_element=document.getElementById("player")
	players.forEach(player => {
		// console.log(player.first_name+" "+player.team.id+" "+data[i].id)
		if (player.team.id==data[i].id){
			let list_element=document.createElement("li")
			list=document.getElementById("player")
			console.log(player)
			list_element.innerHTML=player.first_name+" "+player.last_name
			list.append(list_element)}
	})

	
	// if (players.team.full_name=teams.full_name)
	// team_element.innerHTML=data[i].id
}
