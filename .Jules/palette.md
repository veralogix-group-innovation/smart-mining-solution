## 2025-02-14 - Keyboard Accessibility Foundations
**Learning:** Even visually polished marketing sites often miss basic keyboard accessibility. The absence of a skip link and focus indicators on key inputs like search creates a major barrier.
**Action:** Always check for `focus:outline-none` in Tailwind projects. If removed, ensure a replacement `focus:ring` or similar is added immediately. Always check for a skip link on pages with heavy navigation.

## 2025-02-14 - Interactive Graphics Accessibility
**Learning:** Purely visual interactive elements (like the Smart Hub diagram) generated via JS often get missed in accessibility sweeps. Adding `role="img"`, `tabindex="0"`, and `aria-label` makes them accessible to keyboard and screen reader users. Crucially, focus states must mirror hover states (transforms, shadows) to provide equivalent feedback.
**Action:** When auditing canvas/JS-heavy UIs, explicitly check for keyboard reachability of "clickable" or "hoverable" graphics. Ensure CSS `:focus-visible` shares styles with `:hover`.
