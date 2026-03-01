document.addEventListener("DOMContentLoaded", function () {
    var titleInput = document.getElementById("titleInput");
    var bodyInput = document.getElementById("bodyInput");
    var aiBodyBtn = document.getElementById("aiBodyBtn");
    var aiStatus = document.getElementById("aiStatus");

    if (!titleInput || !bodyInput || !aiBodyBtn) {
        return;
    }

    function buildBody(title) {
        var topic = (title || "").trim() || "Modern technology";
        return [
            "Introduction",
            topic + " is changing the way people learn, work, and solve daily problems.",
            "",
            "Main Discussion",
            "First, " + topic + " helps improve speed and consistency in everyday tasks.",
            "Second, it creates new opportunities for creativity and collaboration.",
            "Finally, using " + topic + " responsibly is important for long-term benefits.",
            "",
            "Conclusion",
            "In summary, " + topic + " has strong potential when applied with clear goals and balance."
        ].join("\n");
    }

    aiBodyBtn.addEventListener("click", function (event) {
        event.preventDefault();
        bodyInput.value = buildBody(titleInput.value);
        bodyInput.focus();
        if (aiStatus) {
            aiStatus.textContent = "AI draft generated. You can edit it before submitting.";
        }
    });
});
