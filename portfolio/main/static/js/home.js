document.addEventListener("DOMContentLoaded", function () {
    try {
        const nameSearch = document.getElementById("name-search");
        const tags = document.querySelectorAll(".tag");
        const projects = document.querySelectorAll(".project");

        if (!nameSearch || !tags.length || !projects.length) {
            throw new Error("Required elements not found in the DOM");
        }

        let selectedTags = [];

        function filterProjects() {
            try {
                const nameQuery = nameSearch.value.toLowerCase().trim();

                projects.forEach(project => {
                    const name = project.getAttribute("data-name");
                    const projectTags = project.getAttribute("data-tags");

                    if (!name || !projectTags) {
                        throw new Error("Project is missing required data attributes");
                    }

                    const matchesNameSearch = nameQuery === "" || name.toLowerCase().includes(nameQuery);
                    const projectTagsArray = projectTags.toLowerCase().split(",");
                    const matchesSelectedTags = selectedTags.length === 0 || 
                        selectedTags.every(tag => projectTagsArray.includes(tag));

                    project.style.display = (matchesNameSearch && matchesSelectedTags) ? "" : "none";
                });
            } catch (error) {
                console.error("Error in filterProjects:", error);
            }
        }

        tags.forEach(tag => {
            tag.addEventListener("click", function () {
                try {
                    const selectedTag = this.getAttribute("data-tag");
                    if (!selectedTag) {
                        throw new Error("Tag is missing data-tag attribute");
                    }

                    const index = selectedTags.indexOf(selectedTag.toLowerCase());

                    if (index === -1) {
                        selectedTags.push(selectedTag.toLowerCase());
                        this.classList.add("selected");
                    } else {
                        selectedTags.splice(index, 1);
                        this.classList.remove("selected");
                    }

                    filterProjects();
                } catch (error) {
                    console.error("Error in tag click handler:", error);
                }
            });
        });

        nameSearch.addEventListener("keyup", filterProjects);
    } catch (error) {
        console.error("Error initializing home.js:", error);
    }
});
