document.addEventListener("DOMContentLoaded", function () {
    var titleInput = document.getElementById("titleInput");
    var bodyInput = document.getElementById("bodyInput");
    var aiBodyBtn = document.getElementById("aiBodyBtn");
    var aiStatus = document.getElementById("aiStatus");

    if (!titleInput || !bodyInput || !aiBodyBtn) {
        return;
    }

    function buildBody(title) {
        var topic = (title || "").trim();
        return [
            "Introduction",
            topic + " is an important topic that affects daily life and long-term growth.",
            "",
            "Main Discussion",
            "First, understanding " + topic + " helps build a clear foundation.",
            "Second, practical use of " + topic + " improves results over time.",
            "Third, challenges in " + topic + " can be reduced through planning and consistency.",
            "",
            "Conclusion",
            "In summary, " + topic + " offers strong value when approached with the right strategy."
        ].join("\n");
    }

    aiBodyBtn.addEventListener("click", function (event) {
        event.preventDefault();
        var enteredTitle = (titleInput.value || "").trim();
        if (!enteredTitle) {
            if (aiStatus) {
                aiStatus.textContent = "Enter a title first, then click AI button.";
            }
            titleInput.focus();
            return;
        }
        bodyInput.value = buildBody(enteredTitle);
        bodyInput.focus();
        if (aiStatus) {
            aiStatus.textContent = "AI body generated from your title.";
        }
    });
});
