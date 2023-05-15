fetch('https://www.thecocktaildb.com/api/json/v1/1/random.php')
.then(response => response.json())
	.then(response =>
        {console.log(response)
    }
    )
	.catch(err => console.error(err));
function select_cocktail(){
    fetch('https://www.thecocktaildb.com/api/json/v1/1/random.php')
    .then(response => response.json())
	.then(response =>
        {

            var name=response.drinks[0].strDrink
            var ingredient1=response.drinks[0].strIngredient1
            var ingredient2=response.drinks[0].strIngredient2
            document.getElementById("ingredient").innerHTML="Ingredients:"+ingredient1+" "+"and"+" "+ingredient2
            document.getElementById("coktail").innerHTML=name
            document.getElementById("img").src=response.drinks[0].strDrinkThumb


            // document.getElementById("coktail").innerHTML=response["drinks"]
    }
    )
	.catch(err => console.error(err));
}

// function search_cocktail()

        function search_cocktail(){
            strDrink=document.getElementById("drink").value
            fetch('https://www.thecocktaildb.com/api/json/v1/1/search.php?s='+strDrink)
        
            .then(response => response.json())
            .then(response=>response.drinks.forEach(drink =>{
                document.getElementById("cocktail").innerHTML=drink.strDrink
                let alldrinks=document.createElement("p")
                alldrinks.innerHTML=drink.strDrink})
                )
            .catch(err => console.error(err))}
                