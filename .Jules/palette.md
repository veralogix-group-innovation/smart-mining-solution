## 2025-02-14 - Keyboard Accessibility Foundations
**Learning:** Even visually polished marketing sites often miss basic keyboard accessibility. The absence of a skip link and focus indicators on key inputs like search creates a major barrier.
**Action:** Always check for `focus:outline-none` in Tailwind projects. If removed, ensure a replacement `focus:ring` or similar is added immediately. Always check for a skip link on pages with heavy navigation.

## 2025-02-14 - Inline Styles vs CSS Focus
**Learning:** When elements have inline styles for positioning (like `transform`), CSS `:hover` or `:focus` states modifying that property will fail unless `!important` is used. Also, focus rings follow the element's box model; for circular interactive elements, ensure the wrapper element has `rounded-full` so the focus ring matches the shape.
**Action:** Always check for inline styles when debugging broken hover/focus states. Use `border-radius` on the focusable container, not just inner content, for proper focus ring shaping.
