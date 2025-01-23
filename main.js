// The API
const api = "https://pokeapi.co/api/v2/pokemon/";

// Document Elements
const searchBar = document.querySelector("input");
const images = document.getElementById("pokemonimages");
const table = document.getElementById("poketable");
const failmessage = document.getElementById("resultsnotfound");

// Pokemon Table Elements
const pokemonFrontImage = document.getElementById("pokemonfront");
const pokemonBackImage = document.getElementById("pokemonback");
const pokemonName = document.getElementById("pokemonname");
const pokemonType = document.getElementById("pokemontype");
const pokemonAbilitiesList = document.getElementById("pokemonabiltieslist");

const pokemonHPName = document.getElementById("pokestat1");
const pokemonATKName = document.getElementById("pokestat2");
const pokemonDEFName = document.getElementById("pokestat3");
const pokemonSPATKName = document.getElementById("pokestat4");
const pokemonSPDEFName = document.getElementById("pokestat5");
const pokemonSPDName = document.getElementById("pokestat6");

const pokemonHP = document.getElementById("pokemonhp");
const pokemonATK = document.getElementById("pokemonatk");
const pokemonDEF = document.getElementById("pokemondef");
const pokemonSPATK = document.getElementById("pokemonspatk");
const pokemonSPDEF = document.getElementById("pokemonspdef");
const pokemonSPD = document.getElementById("pokemonspd");



// Add immediately after script loaded. 
searchBar.addEventListener("keydown", function (e) {
    // Press Enter in order to load script.
    if (e.code === "Enter") {
        getPokemonData(e);
    }
});

/**
 * The entire string is converted to a Sentence Case format. Also removes dashes.
 * @param {string} s - The String that will be Sentence Cased.
 */
function sentenceCase(s) {
    return s.replace("-", " ")
            .toLowerCase()
            .split(' ')
            .map(word => word.charAt(0).toUpperCase() + word.slice(1))
            .join(' ');
}

/**
 * Requests for data from the API and sends them to setPokemonData().
 * @param {string} pokeName - The requested name of the Pokemon.
 */
async function getPokemonData(pokeName) {
    // Making sure that the following URL request is case-insensitive.
    const newURLRequest = api.concat('', pokeName.target.value.toLowerCase());
        
    // Requesting URL.
    const request = new Request(newURLRequest, {method: "GET"});

    // Check for possible errors.
    try {
        const response = await fetch(request);
        if (!response.ok) {
        throw new Error(`Response status: ${response.status}`);
        }
        const json = await response.json();
        
        // JSON Obtained, proceed to change.
        console.log(json["name"]);

        // Change table data.
        setPokemonData(json);

        // Change hidden properties of elements.
        images.hidden = false;
        table.hidden = false;
        failmessage.hidden = true;
    }
    
    // If not found, hide table.
    catch (error) {
        console.error(error.message);

        // Change hidden properties of elements.
        images.hidden = true;
        table.hidden = true;
        failmessage.hidden = false;

    }
}

/**
 * Sets Pokemon data for viewing in a tabular form.
 * @param {json} json - The Pokemon's Data retrieved from PokeAPI in JSON format.
 */
function setPokemonData(json){
    // Resetting types and abilities for iteration.
    pokemonAbilitiesList.innerHTML = "";
    pokemonType.innerHTML = "";

    // Set image and name.
    pokemonFrontImage.src       = json.sprites.front_default;
    pokemonBackImage.src        = json.sprites.back_default;
    pokemonName.innerHTML       = sentenceCase(json.name) + "<br/><small>#" + json.id + "</small>";

    // Iterate over types.
    for (let index = 0;  index < json.types.length; index++) {
        const typeName = json.types[index].type.name;

        // Title case the noun.
        pokemonType.innerHTML += sentenceCase(typeName);

        // If there are more types, add a comma.
        if ((index + 1) != json.types.length) {
            pokemonType.innerHTML += "/"
        }
    }

    // Iterate over abilties.
    for (let index = 0;  index < json.abilities.length; index++) {
        const abilityName = json.abilities[index].ability.name;

        // Title case the noun. titleCase(s)
        //pokemonAbilitiesList.innerHTML += abilityName[0].toUpperCase() + abilityName.substring(1);
        pokemonAbilitiesList.innerHTML += sentenceCase(abilityName);

        // Check if hidden. If hidden, then print the following.
        if (json.abilities[index].is_hidden){
            pokemonAbilitiesList.innerHTML += " (hidden)"
        }

        // If there are more abilities, add a comma.
        if ((index + 1) != json.abilities.length) {
            pokemonAbilitiesList.innerHTML += ", "
        }
    }

    // Set remaining base stats and names..
    pokemonHPName.innerHTML     = json.stats[0].stat.name.toUpperCase();
    pokemonATKName.innerHTML    = sentenceCase(json.stats[1].stat.name);
    pokemonDEFName.innerHTML    = sentenceCase(json.stats[2].stat.name);
    pokemonSPATKName.innerHTML  = sentenceCase(json.stats[3].stat.name);
    pokemonSPDEFName.innerHTML  = sentenceCase(json.stats[4].stat.name);
    pokemonSPDName.innerHTML    = sentenceCase(json.stats[5].stat.name);

    pokemonHP.innerHTML         = json.stats[0].base_stat;
    pokemonATK.innerHTML        = json.stats[1].base_stat;
    pokemonDEF.innerHTML        = json.stats[2].base_stat;
    pokemonSPATK.innerHTML      = json.stats[3].base_stat;
    pokemonSPDEF.innerHTML      = json.stats[4].base_stat;
    pokemonSPD.innerHTML        = json.stats[5].base_stat;
}