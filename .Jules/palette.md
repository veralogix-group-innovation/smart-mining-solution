## 2025-02-14 - Keyboard Accessibility Foundations
**Learning:** Even visually polished marketing sites often miss basic keyboard accessibility. The absence of a skip link and focus indicators on key inputs like search creates a major barrier.
**Action:** Always check for `focus:outline-none` in Tailwind projects. If removed, ensure a replacement `focus:ring` or similar is added immediately. Always check for a skip link on pages with heavy navigation.

## 2025-02-14 - Interactive Delight for Keyboard Users
**Learning:** Purely decorative or informational diagrams (like "Hub" nodes) often have hover effects that are lost to keyboard users. Making them focusable (`tabindex="0"`) and mirroring hover styles to `:focus-visible` extends the "delight" of the UI to everyone.
**Action:** When an element has a cool hover animation, ask: "Can a keyboard user see this?" If it adds value or joy, make it focusable (even with `role="img"` if it's not a button).
