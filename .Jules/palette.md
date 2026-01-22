## 2025-02-14 - Keyboard Accessibility Foundations
**Learning:** Even visually polished marketing sites often miss basic keyboard accessibility. The absence of a skip link and focus indicators on key inputs like search creates a major barrier.
**Action:** Always check for `focus:outline-none` in Tailwind projects. If removed, ensure a replacement `focus:ring` or similar is added immediately. Always check for a skip link on pages with heavy navigation.

## 2025-02-14 - Interactive Diagrams Accessibility
**Learning:** Purely informational "delight" interactions (like the Smart Hub diagram) are often excluded from the keyboard tab order.
**Action:** For interactive-looking but purely informational elements, use `role="img"` with `tabindex="0"` and an `aria-label` instead of `role="button"` to avoid misleading screen reader users about interactivity.
