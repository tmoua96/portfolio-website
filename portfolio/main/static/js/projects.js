document.addEventListener("DOMContentLoaded", function () {
    try {
        const tags = document.querySelectorAll(".tag-btn");
        const projects = document.querySelectorAll(".project-card");

        if (!tags.length || !projects.length) {
            throw new Error("Required elements not found in the DOM");
        }

        let selectedTags = [];

        function filterProjects() {
            try {
                projects.forEach(project => {
                    const projectTags = project.getAttribute("data-tags");

                    if (!projectTags) {
                        throw new Error("Project is missing required data attributes");
                    }

                    const projectTagsArray = projectTags.toLowerCase().split(", ");
                    const matchesSelectedTags = selectedTags.length === 0 || 
                        selectedTags.some(tag => projectTagsArray.includes(tag));

                    project.style.display = matchesSelectedTags ? "" : "none";
                });
            } catch (error) {
                console.error("Error with filtering projects:", error);
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
                        this.classList.add("btn-dark");
                        this.classList.remove("btn-outline-dark");
                    } else {
                        selectedTags.splice(index, 1);
                        this.classList.remove("btn-dark");
                        this.classList.add("btn-outline-dark");
                    }

                    console.log("selectedTags: ", selectedTags);

                    filterProjects();
                } catch (error) {
                    console.error("Error in tag click handler:", error);
                }
            });
        });
    } catch (error) {
        console.error("Error initializing projects.js:", error);
    }
});
