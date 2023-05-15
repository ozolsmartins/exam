const options = {
	method: 'GET',
	headers: {
		'X-RapidAPI-Key': '0b73437c2bmsh4ecc30ef11ff701p1a3afcjsn179baf7d5939',
		'X-RapidAPI-Host': 'instagram-profile1.p.rapidapi.com'
	}
};
function setImage(image_url){
    document.getElementById("image").src=image_url
}
function getUserData(){
    username=document.getElementById("name").value
    const options = {
        method: 'GET',
        headers: {
            'X-RapidAPI-Key': '0b73437c2bmsh4ecc30ef11ff701p1a3afcjsn179baf7d5939',
            'X-RapidAPI-Host': 'instagram-profile1.p.rapidapi.com'
        }
    };
    
    fetch('https://instagram-profile1.p.rapidapi.com/getprofile/'+username, options)
        .then(response => response.json())
        .then(response => {
            console.log(response)
            setImage(response["profile_pic_url_hd"])
        })
        .catch(err => console.error(err));}