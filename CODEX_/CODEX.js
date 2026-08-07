//┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
//#region    [const Search* = document.getElementById('');]┃
const SearchBox      = document.getElementById('X0Y0');
const SearchToggle   = document.getElementById('X0Y0-X0');
const SearchPanel    = document.getElementById('X0Y0-X1');
const SearchInput    = document.getElementById('SearchInput');
const SearchResults  = document.getElementById('SearchResults');
const SearchStatus   = document.getElementById('SearchStatus');
const SearchClear    = document.getElementById('SearchClear');
//#endregion [const Search* = document.getElementById('');]┃
//┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
//#region    [BuildSearchIndex()]						   ┃
function BuildSearchIndex() {
    const nodes = document.querySelectorAll('main summary, main p');
    const index = [];
    nodes.forEach(el => {
        const text = el.textContent.trim();
        if (!text || text.length < 3) return;

        let label = 'Page';
        if (el.tagName === 'SUMMARY') {
            label = text;
        } else {
            const details = el.closest('details');
            if (details) {
                const summary = details.querySelector('summary');
                if (summary) label = summary.textContent.trim();
            }
        }
        index.push({ el, text, label });
    });
    return index;
}
//#endregion [BuildSearchIndex()]						   ┃
//┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
//#region    [const SearchIndex = BuildSearchIndex();]	   ┃
const SearchIndex = BuildSearchIndex();
//#endregion [const SearchIndex = BuildSearchIndex();]	   ┃
//┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
//#region    [EscapeHTML(str);]							   ┃
function EscapeHTML(str) {
    return str.replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
}
//#endregion [EscapeHTML(str);]							   ┃
//┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
//#region    [HighLightSnippet(Text, Query)]			   ┃
function highlightSnippet(text, query) {
    //┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    //#region    [const * = *.()]							   ┃
    const lower  = text.toLowerCase();
    const q      = query.toLowerCase();
    const idx    = lower.indexOf(q);
    //#endregion [const * = *.()]							   ┃
    //┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
    //#region    [if (idx === -1)]							   ┃
    if (idx === -1) return EscapeHTML(text.slice(0, 120));
    //#endregion [if (idx === -1)]							   ┃
    //┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
    const start  = Math.max(0, idx - 40);
    const end    = Math.min(text.length, idx + q.length + 60);
    let snippet = text.slice(start, end);
    if (start > 0) snippet = '…' + snippet;
    if (end < text.length) snippet += '…';
    const localIdx = snippet.toLowerCase().indexOf(q);
    const before = EscapeHTML(snippet.slice(0, localIdx));
    const match = EscapeHTML(snippet.slice(localIdx, localIdx + q.length));
    const after = EscapeHTML(snippet.slice(localIdx + q.length));
    return `${before}<mark>${match}</mark>${after}`;
}
//#endregion [HighLightSnippet(Text, Query)]			   ┃
//┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
//#region    [RunSearch(RawQuery)]						   ┃
function runSearch(rawQuery) {
    const q = rawQuery.trim();
    if (!q) {
        SearchResults.classList.remove('show');
        SearchResults.innerHTML = '';
        SearchResults._matches = [];
        SearchStatus.textContent = '';
        return;
    }
    const matches = SearchIndex
        .filter(item => item.text.toLowerCase().includes(q.toLowerCase()))
        .slice(0, 10);

    if (matches.length === 0) {
        SearchResults.innerHTML = `<div class="Search-empty">No results for “${EscapeHTML(q)}”</div>`;
        SearchStatus.textContent = `No results for ${q}`;
    } else {
        const count = matches.length;
        SearchResults.innerHTML = matches.map((m, i) => `
                <button type="button" class="Search-result" data-index="${i}" role="option">
                    <span class="r-label">${EscapeHTML(m.label)} <span class="r-count">${i + 1}/${count}</span></span>
                    <span class="r-snippet">${highlightSnippet(m.text, q)}</span>
                </button>
            `).join('');
        SearchStatus.textContent = `${count} result${count === 1 ? '' : 's'} found`;
    }
    SearchResults._matches = matches;
    SearchResults.classList.add('show');
}
//#endregion [RunSearch(RawQuery)]						   ┃
//┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
//#region    [JumpToResult(Match)]  					   ┃
function jumpToResult(match) {
    if (!match) return;

    let parent = match.el.closest('details');
    while (parent) {
        parent.open = true;
        parent = parent.parentElement.closest('details');
    }

    SearchResults.classList.remove('show');
    SearchPanel.classList.remove('open');
    SearchToggle.setAttribute('aria-expanded', 'false');
    SearchInput.blur();
    match.el.scrollIntoView({ behavior: 'smooth', block: 'start' });
    match.el.classList.add('Search-flash');
    setTimeout(() => match.el.classList.remove('Search-flash'), 1800);
}
//#endregion [JumpToResult(Match)]  					   ┃
//┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
//#region    [SearchInput.addEventListener()]			   ┃
SearchInput.addEventListener('input', (e) => {
    const val = e.target.value;
    runSearch(val);
    SearchClear.classList.toggle('show', val.length > 0);
});
//#endregion [SearchInput.addEventListener()]			   ┃
//┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
//#region    [SearchInput.addEventListener()]			   ┃
SearchInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') {
        e.preventDefault();
        const first = SearchResults._matches && SearchResults._matches[0];
        if (first) jumpToResult(first);
    }
});
//#endregion [SearchInput.addEventListener()]			   ┃
//┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
//#region    [SearchPanel.addEventListener()]			   ┃
SearchPanel.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        SearchInput.value = '';
        runSearch('');
        SearchClear.classList.remove('show');
        SearchPanel.classList.remove('open');
        SearchToggle.setAttribute('aria-expanded', 'false');
        SearchInput.blur();
        return;
    }

    const items = Array.from(SearchResults.querySelectorAll('.Search-result'));
    if (!items.length || (e.key !== 'ArrowDown' && e.key !== 'ArrowUp')) return;

    e.preventDefault();
    const current = document.activeElement;
    let idx = items.indexOf(current);

    if (e.key === 'ArrowDown') {
        idx = Math.min(idx + 1, items.length - 1);
        items[idx].focus();
    } else {
        if (idx <= 0) {
            SearchInput.focus();
        } else {
            items[idx - 1].focus();
        }
    }
});
//#endregion [SearchPanel.addEventListener()]			   ┃
//┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
//#region    [SearchResults.addEventListener()]			   ┃
SearchResults.addEventListener('click', (e) => {
    const btn = e.target.closest('.Search-result');
    if (!btn) return;
    const idx = Number(btn.dataset.index);
    const match = SearchResults._matches && SearchResults._matches[idx];
    if (match) jumpToResult(match);
});
//#endregion [SearchResults.addEventListener()]			   ┃
//┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
//#region    [SearchClear.addEventListener()]			   ┃
SearchClear.addEventListener('click', () => {
    SearchInput.value = '';
    runSearch('');
    SearchClear.classList.remove('show');
    SearchInput.focus();
});
//#endregion [SearchClear.addEventListener()]			   ┃
//┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
//#region    [SearchToggle.addEventListener()]			   ┃
SearchToggle.addEventListener('click', (e) => {
    e.stopPropagation();
    const isOpen = SearchPanel.classList.toggle('open');
    SearchToggle.setAttribute('aria-expanded', String(isOpen));
    if (isOpen) SearchInput.focus();
});
//#endregion [SearchToggle.addEventListener()]			   ┃
//┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
//#region    [document.addEventListener()]				   ┃
document.addEventListener('click', (e) => {
    if (!SearchBox.contains(e.target)) {
        SearchPanel.classList.remove('open');
        SearchToggle.setAttribute('aria-expanded', 'false');
        if (document.activeElement !== SearchInput) {
            SearchResults.classList.remove('show');
        }
    }
});
//#endregion [document.addEventListener()]				   ┃
//┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
//#region    [SearchInput.addEventListener()]			   ┃
SearchInput.addEventListener('blur', () => {
    setTimeout(() => {
        if (!SearchBox.contains(document.activeElement)) {
            SearchResults.classList.remove('show');
        }
    }, 150);
});
//#endregion [SearchInput.addEventListener()]			   ┃
//┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
