document.addEventListener("DOMContentLoaded", function () {
    const nameSearch = document.getElementById("name-search");
    const tags = document.querySelectorAll(".tag");
    const projects = document.querySelectorAll(".project");

    let selectedTags = [];

    function filterProjects() {
        const nameQuery = nameSearch.value.toLowerCase().trim();

        projects.forEach(project => {
            const name = project.getAttribute("data-name").toLowerCase();
            const projectTags = project.getAttribute("data-tags").toLowerCase().split(",");
            const matchesNameSearch = nameQuery === "" || name.includes(nameQuery);
            const matchesSelectedTags = selectedTags.length === 0 || 
                selectedTags.every(tag => projectTags.includes(tag));

            console.log("project tags: " + projectTags, "\nselected tags: " + selectedTags);

            if (matchesNameSearch && matchesSelectedTags) {
                project.style.display = "";
            } else {
                project.style.display = "none";
            }
        });
    }

    tags.forEach(tag => {
        tag.addEventListener("click", function () {
            const selectedTag = this.getAttribute("data-tag").toLowerCase();
            const index = selectedTags.indexOf(selectedTag);

            if (index === -1) {
                selectedTags.push(selectedTag);
                this.classList.add("selected");
            } else {
                selectedTags.splice(index, 1);
                this.classList.remove("selected");
            }

            filterProjects();

            console.log(selectedTags);
        });
    });

    nameSearch.addEventListener("keyup", filterProjects);
});
