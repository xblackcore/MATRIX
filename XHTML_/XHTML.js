//┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
//┃ []			        								   ┃
//┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
//┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
//┃ [class X extends HTMLElement {}]					   ┃
    //┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    //┃ [SearcherV0] "searcher-v0"  						   ┃
class SearcherV0 extends HTMLElement {
    connectedCallback() {
        this.innerHTML = `
            <div class="Search-V3">
                <input
                    class="Search-V3-input"
                    type="search"
                    placeholder="Search..."
                >

                <button
                    class="Search-V3-clear"
                    type="button">
                    ×
                </button>
            </div>
        `;

        const input = this.querySelector(".Search-V3-input");
        const clear = this.querySelector(".Search-V3-clear");

        input.addEventListener("input", () => {
            clear.hidden = !input.value;
        });

        clear.addEventListener("click", () => {
            input.value = "";
            input.focus();
            clear.hidden = true;
        });
    }
}
customElements.define("searcher-v0", SearcherV0);
    //┃ [SearcherV0] "searcher-v0"  						   ┃
    //┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
//┃ [class X extends HTMLElement {}]					   ┃
//┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛