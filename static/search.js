document.getElementById("search-btn").addEventListener("click", function () {
  const searchText = document.getElementById("text-box").value;
  fetch(`/search/${searchText}`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      const itemContainer = document.getElementById("item-container");
      itemContainer.innerHTML = "";
      data.forEach((obj) => {
        const item = document.createElement("div");
        card.className = "item";
        card.innerHTML = `<img src="https://dummyimage.com/600x400/">
            <div class="title">${obj.title}</div>`;
        cardContainer.appendChild(card);
      });
    })
    .catch((error) => console.error("Error:", error));
});
