function showAlert(msg) {
  const ele = document.getElementById("alert");
  ele.innerHTML = msg;
  ele.classList.remove("d-none");
}

function hideAlert() {
  const ele = document.getElementById("alert");
  ele.innerHTML = "";
  ele.classList.add("d-none");
}

function searching() {
  const btn = document.getElementById("search-btn");
  btn.value = "Searching...";

  const txtBox = document.getElementById("text-box");
  txtBox.setAttribute("disabled", "true");
}

function searchingComplete() {
  const btn = document.getElementById("search-btn");
  btn.value = "Search";

  const txtBox = document.getElementById("text-box");
  txtBox.removeAttribute("disabled");
}

document.getElementById("search-btn").addEventListener("click", function () {
  const searchText = document.getElementById("text-box").value;
  searching();
  hideAlert();
  fetch(`/search/${searchText}`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then((response) => {
      searchingComplete();
      return response.json();
    })
    .then((data) => {
      const itemContainer = document.getElementById("item-container");
      itemContainer.innerHTML = "";
      if (searchText in data) {
        list = data[searchText];
        list.forEach((obj) => {
          const col = document.createElement("div");
          col.className = "col";

          const card = document.createElement("div");
          card.className = "card mt-3";
          card.innerHTML = `<h5 class="card-header">
          ${obj.title}
      </h5>
      <img src="https://${obj.image}" class="card-img-bottom">`;
          col.appendChild(card);
          itemContainer.appendChild(col);
        });
      } else {
        showAlert("no result found...");
      }
    })
    .catch((error) => {
      console.error("Error:", error);
      showAlert(error);
    });
});
