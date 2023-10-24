document.addEventListener("DOMContentLoaded", function () {
    const hintButton = document.getElementById("hint-button");
    const badButton = document.getElementById("bad-button");
    const goodButton = document.getElementById("good-button");
    const sentenceDiv = document.getElementById("sentence");
    const definitionDiv = document.getElementById("definition");

    // Define a function to fetch adjective data from the server
    function fetchAdjectiveData() {
        fetch("/get_all_adjective_data")  // Replace with your Flask route for getting adjective data
            .then(response => response.json())
            .then(data => {
                console.log(data);
                if (data.length > 0) {
                    // Update the HTML elements with adjective data
                    const adjective = data[0]; // Assuming you want the first adjective in the list
                    document.getElementById("adjective-word").textContent = adjective.word;
                    document.getElementById("adjective-sentence").textContent = adjective.sentence;
                    document.getElementById("adjective-definition").textContent = adjective.definition;
                } else {
                    // Handle the case where there are no adjectives in the response
                    console.error("No adjectives found in the response.");
                }
            })
            .catch(error => console.error("Error fetching adjective data:", error));
    }

    // Fetch adjective data when the page loads
    fetchAdjectiveData();

    hintButton.addEventListener("click", function () {
        sentenceDiv.style.display = "block";
    });

    badButton.addEventListener("click", function () {
        sentenceDiv.style.display = "block";
        definitionDiv.style.display = "block";
    });

    goodButton.addEventListener("click", function () {
        // Fetch and display another adjective when the "Good" button is clicked
        fetchAdjectiveData();
        sentenceDiv.style.display = "none";
        definitionDiv.style.display = "none";
    });
});
    