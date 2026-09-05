// Catalog rendering. Edit products.js to add or change products.
const starterImages = {
  "products-reference.png#mega": "crop-one",
  "products-reference.png#super": "crop-two",
  "products-reference.png#baseball": "crop-three"
};
const grid = document.getElementById("products");
const currency = new Intl.NumberFormat("en-US", { style: "currency", currency: "USD" });
const category = new URLSearchParams(location.search).get("category") || "Football";
const heading = category === "All" ? "Catalog" : category;
document.getElementById("collection-title").textContent = heading;
document.getElementById("breadcrumb").textContent = heading;
document.title = heading + " | KSC";
document.querySelectorAll("[data-category]").forEach(link => {
  if (link.dataset.category === category) link.setAttribute("aria-current", "page");
});
function render() {
  const query = document.getElementById("search").value.trim().toLowerCase();
  let list = products.filter(product => (category === "All" || product.category === category) && product.title.toLowerCase().includes(query));
  const sorts = {
    az: (a, b) => a.title.localeCompare(b.title),
    za: (a, b) => b.title.localeCompare(a.title),
    low: (a, b) => a.price - b.price,
    high: (a, b) => b.price - a.price
  };
  const sort = sorts[document.getElementById("sort").value];
  if (sort) list.sort(sort);
  grid.replaceChildren();
  list.forEach(product => {
    const card = document.createElement("article");
    card.className = "product";
    const imageArea = document.createElement("div");
    imageArea.className = "product-image";
    if (product.image) {
      const image = document.createElement("img");
      image.src = product.image;
      image.alt = product.title;
      image.loading = "lazy";
      image.addEventListener("error", () => { imageArea.replaceChildren(); imageArea.classList.add("blank"); imageArea.setAttribute("aria-label", "Image unavailable"); });
      if (starterImages[product.image]) {
        const crop = document.createElement("div");
        crop.className = "crop " + starterImages[product.image];
        crop.append(image);
        imageArea.append(crop);
      } else imageArea.append(image);
    } else {
      imageArea.classList.add("blank");
      imageArea.setAttribute("role", "img");
      imageArea.setAttribute("aria-label", "Product image placeholder");
    }
    const title = document.createElement("h2");
    title.textContent = product.title;
    const price = document.createElement("p");
    price.className = "price";
    price.textContent = currency.format(product.price);
    card.append(imageArea, title, price);
    grid.append(card);
  });
  document.getElementById("product-count").textContent = list.length + (list.length === 1 ? " product" : " products");
  document.getElementById("empty").hidden = list.length > 0;
}
document.getElementById("sort").addEventListener("change", render);
document.getElementById("search").addEventListener("input", render);
document.getElementById("search-form").addEventListener("submit", event => { event.preventDefault(); render(); document.getElementById("collection").scrollIntoView({behavior:"smooth"}); });
const messages = {
  account: ["Customer accounts", "This is a sample KSC storefront. Customer accounts are not connected yet."],
  cart: ["Your bag is empty", "This sample catalog does not accept orders yet."],
  policies: ["Store policies", "KSC store policies will be added before the shop opens. This is a sample catalog; orders are not available yet."]
};
document.querySelectorAll("[data-info]").forEach(button => button.addEventListener("click", () => {
  const [title, text] = messages[button.dataset.info];
  document.getElementById("info-title").textContent = title;
  document.getElementById("info-text").textContent = text;
  document.getElementById("info").showModal();
}));
render();

