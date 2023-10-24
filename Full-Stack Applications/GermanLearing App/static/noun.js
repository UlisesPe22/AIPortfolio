document.addEventListener("DOMContentLoaded", function () {
    const hintButton = document.getElementById("hint-button");
    const badButton = document.getElementById("bad-button");
    const goodButton = document.getElementById("good-button");
    const sentenceDiv = document.getElementById("sentence");
    const definitionDiv = document.getElementById("definition");

    // Define a function to fetch noun data from the server
    function fetchNounData() {
    fetch("/get_all_noun_data")  // Replace with your Flask route for getting noun data
        .then(response => response.json())
        .then(data => {
            console.log(data);
            if (data.length > 0) {
                // Update the HTML elements with noun data
                const noun = data[0]; // Assuming you want the first noun in the list
                document.getElementById("noun-word").textContent = noun.word;
                document.getElementById("noun-plural").textContent = noun.plural;
                document.getElementById("noun-gender").textContent = noun.gender;
                document.getElementById("noun-sentence").textContent = noun.sentence;
                document.getElementById("noun-definition").textContent = noun.definition;
            } else {
                // Handle the case where there are no nouns in the response
                console.error("No nouns found in the response.");
            }
        })
        .catch(error => console.error("Error fetching noun data:", error));
}

    // Fetch noun data when the page loads
    fetchNounData();

    hintButton.addEventListener("click", function () {
        sentenceDiv.style.display = "block";
    });

    badButton.addEventListener("click", function () {
        sentenceDiv.style.display = "block";
        definitionDiv.style.display = "block";
    });

    goodButton.addEventListener("click", function () {
        // Fetch and display another noun when the "Good" button is clicked
        fetchNounData();
        sentenceDiv.style.display = "none";
        definitionDiv.style.display = "none";
    });
});
