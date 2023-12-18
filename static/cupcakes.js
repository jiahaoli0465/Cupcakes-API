const BASE_URL = "api";

class CupcakeManager {
  constructor() {
    this.$cupcakesList = $("#cupcakes-list");
    this.$form = $("#new-cupcake-form");
    this.init();
  }

  init() {
    this.showInitialCupcakes();
    this.addEventListeners();
  }

  addEventListeners() {
    this.$form.on("submit", this.handleFormSubmit.bind(this));
    this.$cupcakesList.on("click", ".delete-button", this.handleDelete.bind(this));
  }

  generateCupcakeHTML(cupcake) {
    return `
      <div data-cupcake-id=${cupcake.id}>
        <li>
          flavor: ${cupcake.flavor} / ${cupcake.size} / rating: ${cupcake.rating}
          <button class="delete-button">X</button>
        </li>
        <img class="Cupcake-img"
              src="${cupcake.image}"
              alt="(no image provided)">
      </div>
    `;
  }

  async showInitialCupcakes() {
    const response = await axios.get(`${BASE_URL}/cupcakes`);
    for (let cupcakeData of response.data.cupcakes) {
      let newCupcake = $(this.generateCupcakeHTML(cupcakeData));
      this.$cupcakesList.append(newCupcake);
    }
  }

  async handleFormSubmit(evt) {
    evt.preventDefault();
    let flavor = $("#form-flavor").val();
    let rating = $("#form-rating").val();
    let size = $("#form-size").val();
    let image = $("#form-image").val();

    const newCupcakeResponse = await axios.post(`${BASE_URL}/cupcakes`, {
      flavor,
      rating,
      size,
      image
    });

    let newCupcake = $(this.generateCupcakeHTML(newCupcakeResponse.data.cupcake));
    this.$cupcakesList.append(newCupcake);
    this.$form.trigger("reset");
  }

  async handleDelete(evt) {
    evt.preventDefault();
    let $cupcake = $(evt.target).closest("div");
    let cupcakeId = $cupcake.attr("data-cupcake-id");

    await axios.delete(`${BASE_URL}/cupcakes/${cupcakeId}`);
    $cupcake.remove();
  }
}

$(function() {
  new CupcakeManager();
});
