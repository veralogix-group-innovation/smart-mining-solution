## 2025-02-14 - Keyboard Accessibility Foundations
**Learning:** Even visually polished marketing sites often miss basic keyboard accessibility. The absence of a skip link and focus indicators on key inputs like search creates a major barrier.
**Action:** Always check for `focus:outline-none` in Tailwind projects. If removed, ensure a replacement `focus:ring` or similar is added immediately. Always check for a skip link on pages with heavy navigation.

## 2025-02-14 - Custom Interactive Elements
**Learning:** Custom visual components like the "Smart Hub" diagram, which rely on hover effects for engagement, are often invisible to keyboard users.
**Action:** For interactive "img" or "div" elements, always add `tabindex="0"`, `role="img"` (or appropriate role), and `aria-label`. Ensure CSS `:hover` states are mirrored with `:focus` and `:focus-visible`.
