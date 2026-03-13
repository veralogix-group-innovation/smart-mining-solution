## 2025-02-14 - Keyboard Accessibility Foundations
**Learning:** Even visually polished marketing sites often miss basic keyboard accessibility. The absence of a skip link and focus indicators on key inputs like search creates a major barrier.
**Action:** Always check for `focus:outline-none` in Tailwind projects. If removed, ensure a replacement `focus:ring` or similar is added immediately. Always check for a skip link on pages with heavy navigation.

## 2025-02-14 - Accessible Interactive Diagrams
**Learning:** Custom interactive diagrams built with `div`s and absolute positioning often bypass standard accessibility audits. They are invisible to keyboard users without explicit `tabindex`.
**Action:** For any custom JS-generated interactive component, manually verify: 1) Can I tab to it? 2) Does it have a role/label? 3) Does focus override inline styles (often needing `!important` in CSS)?
