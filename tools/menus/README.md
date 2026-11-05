# Menu PDF builder

Builds `menus/iki-toro-drink-menu.pdf` and `menus/iki-toro-spirits-list.pdf` in the
same design as the food menu (page size, header mark, cherry blossom, koi, Noto Serif).

- Edit items and prices in `menu_data.py`
- `python3 build_template.py` rebuilds the background from `src/main.pdf` (only needed if the food-menu art changes)
- `python3 build_menus.py` writes both PDFs into `/menus`
- Then regenerate the page images in `/menus` (`*-1.webp`, `*-2.webp`, `*-thumb.webp`) used by the website viewer

Requires: reportlab, pypdf, pikepdf.
