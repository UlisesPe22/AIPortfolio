document.addEventListener("DOMContentLoaded", function () {
    const hintButton = document.getElementById("hint-button");
    const badButton = document.getElementById("bad-button");
    const goodButton = document.getElementById("good-button");
    const sentenceDiv = document.getElementById("sentence");
    const definitionDiv = document.getElementById("definition");

    // Define a function to fetch verb data from the server
    function fetchVerbData() {
        fetch("/get_all_verb_data")  // Replace with your Flask route for getting verb data
            .then(response => response.json())
            .then(data => {
                console.log(data);
                if (data.length > 0) {
                    // Update the HTML elements with verb data
                    const verb = data[0]; // Assuming you want the first verb in the list
                    document.getElementById("verb-word").textContent = verb.word;
                    document.getElementById("verb-past").textContent = verb.past;
                    document.getElementById("verb-sentence").textContent = verb.sentence;
                    document.getElementById("verb-definition").textContent = verb.definition;
                } else {
                    // Handle the case where there are no verbs in the response
                    console.error("No verbs found in the response.");
                }
            })
            .catch(error => console.error("Error fetching verb data:", error));
    }

    // Fetch verb data when the page loads
    fetchVerbData();

    hintButton.addEventListener("click", function () {
        sentenceDiv.style.display = "block";
    });

    badButton.addEventListener("click", function () {
        sentenceDiv.style.display = "block";
        definitionDiv.style.display = "block";
    });

    goodButton.addEventListener("click", function () {
        // Fetch and display another verb when the "Good" button is clicked
        fetchVerbData();
        sentenceDiv.style.display = "none";
        definitionDiv.style.display = "none";
    });
});
