//┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
//#region    [Debug(True)]								   ┃
/**
 * Enables or disables visual debugging for DOM elements.
 *
 * When enabled, hovering an element:
 *  - Highlights it with a cyan outline.
 *  - Displays its `id` as a tooltip.
 *
 * Intended for inspecting the interface hierarchy during development.
 */
function Debug(Enable = true) {
    let Overlay = document.getElementById("DebugOverlay");
    if (!Overlay) {
        Overlay    = document.createElement("div");
        Overlay.id = "DebugOverlay"               ;

        Overlay.style.position      = "fixed"         ;
        Overlay.style.pointerEvents = "none"          ;
        Overlay.style.border        = "1px solid cyan";
        Overlay.style.zIndex        = "2147483647"    ;
        Overlay.style.display       = "none"          ;
        Overlay.style.boxSizing     = "border-box"    ;

        document.body.appendChild(Overlay);
    }
    document.querySelectorAll("*").forEach(Element => {

        if (!Enable) {
            Element.onmouseenter  = null  ;
            Element.onmouseleave  = null  ;
            Overlay.style.display = "none";
            return;
        }

        Element.onmouseenter = () => {

            const R = Element.getBoundingClientRect();

            Overlay.style.display  = "block";
            Overlay.style.left     = R.left + "px";
            Overlay.style.top      = R.top + "px";
            Overlay.style.width    = R.width + "px";
            Overlay.style.height   = R.height + "px";

            document.title = `${Element.id} : ${Element.className}`;
        };

        Element.onmouseleave = () => {
            Overlay.style.display = "none";
        };

    });
}
Debug(false);
//#endregion [Debug(True)]								   ┃
//┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛