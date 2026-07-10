# Software Practices Design System

This document records the visual and interaction decisions behind the Software Practices site. It
is repository documentation, not site content. This document owns the design intent and component
contracts. The rendered site demonstrates those contracts, while CSS owns their current numerical
implementation.

The system developed through repeated review of the homepage, category roots, grouped indexes, and
leaf pages at wide, compact, and narrow widths. It should continue to be reviewed as a system rather
than as a collection of unrelated pages.

## Purpose

Software Practices is a technical reference for software work. It serves people reading at length,
people scanning for a named rule or pattern, and coding agents retrieving compact instructions. The
design needs to make several hundred related documents navigable without turning them into a generic
documentation portal or a dashboard.

The intended character is a well-designed older software reference manual:

- Editorial and technical rather than product-marketing oriented.
- Desaturated and warm rather than bright, glossy, or neon.
- Structured by alignment, type, rules, and spacing rather than rounded containers.
- Tactile enough to feel authored, but not skeuomorphic.
- Comfortable for sustained reading in both dark and light themes.
- Distinct from a terminal theme. Monospace type is metadata, not the default reading face.

## Authority and Decision Types

Use four kinds of design decision:

- **Principle:** durable intent that should survive a redesign.
- **Contract:** testable behavior or relationship shared by implementations.
- **Recipe:** the current implementation of a contract, including token values and breakpoints.
- **Exception:** a named, scoped departure with a rationale and a condition for review.

`DESIGN.md` owns principles and contracts. `src/styles/system.css` owns current recipes and token
values. `src/pages/about/design-system.astro` demonstrates the implemented system. Shared layouts
and components apply it to real page families.

When CSS conflicts with a contract, treat that as a defect or record a deliberate exception. Do
not let an accidental implementation detail silently redefine the system.

`src/styles/global.css` still contains an older structural layer that `system.css` overrides. This
is migration debt rather than a design principle. Consolidate ownership when touching an affected
component; do not create a third visual layer.

## System Principles

### Let the content family set the accent

Each major content family owns one hue. The hue flows through the page title, icons, major rules,
interactive borders, links, and tinted fields. This gives a reader orientation without requiring a
badge on every object.

The surrounding structure stays neutral. Body text, site chrome, peer separators, and most prose do
not inherit a strong category color.

### Use typography to identify the role of text

The shorthand is:

> Serif names things. Sans explains them. Mono carries metadata and compact controls.

Titles and navigation-card names use the serif face. Body copy and supporting explanations use the
sans face. IDs, tags, breadcrumbs, keyboard hints, and compact button labels use monospace.

### Prefer planned relationships over containers

Alignment should explain which elements belong together. A heading column and content column, a
shared baseline, a peer rule, or an accent rule should do more work than a rounded box.

Containers are justified when they create a real interaction surface, group code, or carry a
category field. Avoid adding a panel simply because a block of text needs visual interest.

### Give repeated elements one grammar

Cards, arrows, chips, buttons, rules, icons, and headings should behave consistently across page
types. A shared component may vary in density, but it should not change its meaning or affordance.

### Compose responsive states explicitly

Do not rely on content wrapping to discover the compact layout. Important changes such as hiding the
book cover, grouping leaf actions, switching navigation modes, or collapsing a card grid happen at
named breakpoints.

### Keep text comfortably readable

The base font size stays between 16px and 17px. Metadata is quieter, but it should not become
microtext. When space is tight, change layout before reducing important text.

## Color

### Tonal recipe

Every content hue has four family roles:

- `solid`: the strongest accent, used for rules, borders, and active indicators.
- `heading`: a brighter or darker same-hue value for titles and object identity.
- `field`: a dark or light same-hue surface for cards and primary controls.
- `on-field`: readable text for the field surface.

This same-hue pairing is intentional. A bright red heading on a dark red field feels richer and
more specific than placing every category on a neutral card. The recipe stays the same across hues,
which keeps the expanded palette coherent. The palette is optically balanced rather than merely
assigned equal numerical saturation. Yellow should not glare, indigo should not disappear, and red
may remain deliberately strongest without overwhelming neighboring families. Review lightness,
chroma, and occupied surface area together when adjusting a hue.

Interaction roles sit above the family palette:

- `link`: interactive text that retains the family hue and a persistent non-color cue.
- `focus-ring`: a high-contrast outline visible against neutral and family fields.
- `current`: the active location, paired with `aria-current` and a structural marker.
- Semantic status colors such as success, warning, critical, or informational are independent of
  content families and always include a label or icon.

### Content-family assignments

| Family              | Hue     | Intended weight and use                                      |
| ------------------- | ------- | ------------------------------------------------------------ |
| Site and About      | Brown   | Brand, site-level structure, homepage, and neutral framing   |
| Guides              | Red     | Strongest content family; broad guidance and work-area entry |
| Rules               | Orange  | Compact instructions and operational decisions               |
| Patterns            | Yellow  | Repeatable situations and review moves                       |
| Principles          | Olive   | Rationale, tradeoffs, and underlying beliefs                 |
| Mechanisms          | Teal    | Commands, checks, generators, and workflows                  |
| Agents              | Indigo  | Agent snippets, packs, and operational context               |
| Tags and References | Neutral | Weakest family; lookup, grouping, and source material        |

Tags and References intentionally share a hue. They are both indexing surfaces, and giving each a
strong independent color would overstate their hierarchy. Brown remains site-level rather than
being reused as another content category.

### Dark theme tokens

| Role              | Value     |
| ----------------- | --------- |
| Background        | `#171914` |
| Raised background | `#1e211b` |
| Strong background | `#272b22` |
| Primary text      | `#f1eee2` |
| Soft text         | `#d8d4c7` |
| Muted text        | `#aaa99a` |
| Neutral line      | `#3b3f34` |

| Family  | Solid     | Heading   | Field     | On field  |
| ------- | --------- | --------- | --------- | --------- |
| Brown   | `#b48755` | `#d0a874` | `#493421` | `#f6eadf` |
| Red     | `#de6661` | `#f08a83` | `#512725` | `#fbeae6` |
| Orange  | `#e2853f` | `#f0a05f` | `#55331d` | `#fff0df` |
| Yellow  | `#bda342` | `#dcc263` | `#473d1c` | `#faf2d4` |
| Olive   | `#8fa34b` | `#b0c36e` | `#34401f` | `#eef4da` |
| Teal    | `#4d9996` | `#72b8b5` | `#204442` | `#e5f6f6` |
| Indigo  | `#7f82b6` | `#a5a6d1` | `#30324f` | `#eeeefa` |
| Neutral | `#7f8994` | `#a2abb5` | `#333a42` | `#edf0f3` |

The dark background is green-black rather than neutral black. That slight cast lets the warm and
cool category hues coexist without turning the page blue-black or terminal-like.

### Light theme

Light mode is a first-class reading mode, not an inverted afterthought. It uses warm paper-like
neutrals:

- Background: `#f2eee3`.
- Raised background: `#faf7ee`.
- Strong background: `#e5dfd1`.
- Primary text: `#272920`.
- Soft text: `#44463b`.
- Muted text: `#696b5f`.
- Neutral line: `#c9c3b4`.

Each content hue also has a darker solid and heading plus a pale field. Do not generate light mode
by applying a filter to dark-mode colors.

| Family  | Solid     | Heading   | Field     | On field  |
| ------- | --------- | --------- | --------- | --------- |
| Brown   | `#8b5c2c` | `#69451f` | `#ead8c4` | `#432914` |
| Red     | `#a63f3b` | `#7d2f2c` | `#f0cecb` | `#572522` |
| Orange  | `#9a4e16` | `#71370f` | `#f0d5bf` | `#52270d` |
| Yellow  | `#796500` | `#5a4b00` | `#e7dfb7` | `#413600` |
| Olive   | `#596a20` | `#414f16` | `#dce3bf` | `#30400f` |
| Teal    | `#34706d` | `#245654` | `#c9e0de` | `#173f3d` |
| Indigo  | `#555989` | `#3e426d` | `#d5d6e8` | `#2d3159` |
| Neutral | `#5f6872` | `#484f58` | `#d9dde1` | `#353b42` |

### Color-use rules

- Use the current family heading color for page titles, section labels, and type icons.
- Use the family hue for links, but distinguish prose links from headings with a persistent
  underline. Whole-card links use their surface, focus treatment, and affordance instead.
- Use the family solid for the 3px family rule and active borders.
- Use the family field for deliberate interactive surfaces and emphasized instructions.
- Keep body text neutral even inside a colored page family.
- Do not use color alone for meaning. Icons, labels, border position, and hierarchy carry the same
  distinction.
- Do not introduce a new hue for a one-off component. First decide whether it belongs to an
  existing content or semantic role.
- Use one dominant family cue and at most one supporting family cue on a component. Interaction
  affordances do not need to repeat category identity.
- Verify contrast in both themes. The current card titles and reference links meet WCAG AA for
  normal text.

## Typography

### Families

- Display: Source Serif 4, weights 400 through 600.
- Reading and UI: IBM Plex Sans, weights 400 through 700.
- Metadata and code: IBM Plex Mono, weights 500 and 600.

Source Serif 4 replaced heavier serif directions that made the site feel stodgy. IBM Plex Sans is
kept out of primary titles; using sans everywhere made the homepage and guidance cards feel generic.

### Type tokens

| Token       | Current value                              | Use                         |
| ----------- | ------------------------------------------ | --------------------------- |
| `type-xs`   | `0.875rem`                                 | Metadata and compact labels |
| `type-sm`   | `0.92rem`                                  | Supporting card copy        |
| `type-body` | `1rem`                                     | Prose and ordinary UI       |
| `type-lead` | `clamp(1.12rem, 1rem + 0.45vw, 1.35rem)`   | Hero descriptions           |
| `type-h3`   | `clamp(1.25rem, 1.1rem + 0.55vw, 1.55rem)` | Local headings              |
| `type-h2`   | `clamp(2rem, 1.55rem + 1.8vw, 3.25rem)`    | Major section headings      |
| `type-h1`   | `clamp(3rem, 2.05rem + 4vw, 6rem)`         | Page titles                 |

The root font size uses `clamp(16px, 15.25px + 0.18vw, 17px)`. Leaf titles are capped at 64px in
the compact layout and 48px on narrow screens so long rule names do not consume the whole viewport.

Size tokens are only half the type system. Current line-height recipes are `1.62` for ordinary
reading, `1.7` for long prose, approximately `1.5` for supporting card copy, and `0.9` through `1.2`
for display text according to size. Display letter-spacing may tighten slightly; body copy remains
at normal tracking. Reading measure stays near 66 to 72 characters.

Metadata normally uses `type-xs` rather than a smaller private scale. The `SP.` monogram is an
optical brand exception, not a precedent for undersized controls or keyboard hints.

### Heading rules

- Page titles, major section titles, card titles, and leaf section labels use Source Serif 4.
- Prose headings are smaller than page-level headings and should not produce large empty blocks.
- Heading and body columns align at their top edge on leaf pages.
- A heading should remain visibly larger than nearby body text, including inline-feeling section
  labels.
- Avoid all-caps serif headings. Uppercase belongs to mono metadata and small labels.
- Use `text-wrap: pretty` on headings and paragraphs, but set layout widths so wrapping remains
  predictable.

## Spacing and Rhythm

### Scale

| Token     | Value     |
| --------- | --------- |
| `space-1` | `0.25rem` |
| `space-2` | `0.5rem`  |
| `space-3` | `0.75rem` |
| `space-4` | `1rem`    |
| `space-5` | `1.5rem`  |
| `space-6` | `2rem`    |
| `space-7` | `3rem`    |
| `space-8` | `4rem`    |
| `space-9` | `6rem`    |

Spacing expresses relationship:

- `space-1` and `space-2` keep metadata and title parts together.
- `space-3` and `space-4` separate controls, chips, and card content.
- `space-5` and `space-6` are normal card and section padding.
- `space-7` through `space-9` separate major editorial regions at wide widths.

Large values are reduced at compact and narrow widths. Mobile layouts should not preserve desktop
whitespace simply because the tokens exist.

### Rhythm rules

- Measure the space around an element against both neighbors, not against a component in isolation.
- Do not place two horizontal rules close enough that they read as an accidental double rule.
- Do not use a large vertical rule merely to fill a hero edge.
- Card padding should leave enough room for text and the title-row arrow without reserving a large
  empty strip on the right.
- Long catalogs use a denser profile than landing pages.
- Prefer changing columns or grouping before shrinking text.

## Lines, Fields, and Depth

The main structural vocabulary is deliberately small:

- A 1px neutral rule separates peers.
- A 3px family-colored rule marks a major boundary or category context.
- A 2px tinted left border identifies a navigational card surface.
- A same-hue field gives a card or action more weight.
- A subtle radial wash in the page background carries the current family color.

Most cards have square corners. Controls use a small `0.2rem` radius to keep focus, hover, and
clickable shapes comfortable without drifting into rounded-box UI.

Shadows are rare. The sticky header uses translucent background blur, the homepage book uses one
offset shadow, and menus or dialogs use elevation because they sit above the page. Ordinary content
cards should use fields, lines, and alignment instead of floating shadows.

## Icons

Font Awesome solid icons identify artifact type:

- Book: Guide.
- Ruler: Rule.
- Compass drafting: Pattern.
- Brain: Principle.
- Wrench: Mechanism.
- Robot: Agent.
- Tags: Tag.
- Globe: Reference.

Icons provide the exact object type; color provides the broader family context. They use
`currentColor` and inherit the family heading color.

Hero icons should be close enough to title size to read as part of the title lockup, but they should
not dominate it. Card icons match the first title line rather than the full height of a multiline
title. Do not use icons as generic decoration when the object type is already clear.

Every icon sits in a fixed square box. The glyph is optically sized inside that box: card glyphs are
approximately `0.9em` of the title, while hero glyphs are approximately `0.72em` to `0.85em` of the
title cap height. Font Awesome glyphs have unequal apparent mass, so centralized per-glyph scale or
vertical corrections are allowed. Judge the visible shape rather than the raw SVG bounds, and
never allow an icon box to overlap a structural rule.

## Arrows and Navigation Affordance

An arrow means the entire surrounding surface navigates to another page. A whole-surface
destination uses one persistent navigational affordance: either a title-row arrow or an explicit
destination action, never both.

- Compact rows and cards without another visible action use one right arrow.
- The arrow sits in a fixed `1em` box on the title row, aligned optically with the first title line.
- It uses the card or page accent color and the visual scale of the title.
- Its resting opacity is `0.8`.
- Hover and keyboard focus raise the opacity and move it `0.2rem` to the right.
- The arrow remains visible without hover. Hover is confirmation, not discovery.
- Current recipes use arrows for dense index entries, homepage cards, work-area cards, rule-domain
  cards, tag cards, related links, and use-case panels.

Chips, metadata labels, breadcrumb segments, and ordinary inline links do not receive card arrows.
A destination-oriented action button may contain an arrow in its label. Informational panels,
current-location panels, and cards with an explicit destination action omit the card arrow.

## Layout

### Shared frame

- Page and header maximum width: 1180px.
- Reading width: 72 characters.
- Label column: 11.5rem.
- Standard control height: 2.5rem.
- Minimum supported page width: 20rem.

The header, main content, and footer share the 1180px frame. Their outer edges should align at wide
widths. The brand sits at the left, primary navigation occupies the middle and aligns right, and
search plus theme controls sit at the right.

Tags and References are intentionally absent from the primary header. They are utility indexes and
live in the footer instead. This leaves enough room for the six primary content families.

### Page levels

The layout system recognizes four levels:

1. Site root: the homepage and its editorial overview.
1. Category root: Guides, Rules, Patterns, Principles, Mechanisms, Agents, Tags, and References.
1. Group: scoped indexes such as a rule domain or tag cluster.
1. Leaf: an individual guide, rule, pattern, principle, mechanism, agent pack, or reference.

Review every shared change across all four. A leaf-page improvement can make a category root feel
unrelated if the same alignments, colors, type roles, and spacing rules do not carry through.

### Homepage

The homepage is more editorial than interior pages. Its hero pairs a large serif statement with a
decorative reference-book cover.

- The title uses “How I [verb] software.” The verb changes slowly among real software-work verbs.
- The animation runs every 4.6 seconds and uses a short vertical fade.
- A visible pause control stops and resumes the changing word without changing layout.
- The accessible heading remains stable; visual changes are not repeatedly announced.
- `prefers-reduced-motion` freezes the default verb and stops the timer.
- The longest supported verb determines the reserved width so changes do not shift the layout.
- The book is a 4:5 cover, right-aligned, and sized by the height of the left hero content.
- The book is hidden at 73.5rem rather than wrapping beneath the hero.
- The book is decorative. Its labels stay short and do not repeat edition information.

The homepage then uses a label column plus content grid for Work areas, Guidance types, and use
cases. These sections should reveal useful site content promptly; avoid oversized gaps that push the
first cards far below the fold.

### Category roots

Category roots establish the family with an icon, colored title, short description, and an accent
rule. The Guides root includes a work-area panel before its full listing. Other roots choose density
according to their item count rather than copying that panel mechanically.

On narrow screens, category breadcrumbs are hidden because “Home / Category” repeats the visible
hero without adding useful orientation.

### Grouped indexes

Grouped indexes use a left label column for the group name and explanation, with navigational rows
in the content column. The group label may be sticky at wide widths and becomes ordinary flow below
52rem.

Large catalogs need group navigation and dense rows. Small indexes can use more generous cards.
Grouping follows reader work areas rather than filename order.

### Leaf pages

Leaf pages share:

1. Breadcrumbs.
1. Icon and page title.
1. Stable ID where relevant.
1. Short description or summary.
1. Topic chips and grouped actions.
1. Related guidance when present.
1. Two-column sections with a label and reading body.

At compact widths, chips occupy one row and copy/feedback actions stay together on a deliberate
second row. At narrow widths, the current-page breadcrumb is hidden so a long title is not repeated
immediately above itself.

Section headings and body text align at the top. The vertical gap between sections should be enough
to scan, but not so large that a short page becomes mostly empty space.

## Cards and Link Panels

### Work-area cards

Work-area cards use a light family wash as their dominant cue, with the family title as support.
Their number, serif title, title-row arrow, and concise sans description establish hierarchy
without another accent bar or colored edge. They use three columns on wide homepage layouts, two
columns at compact widths, and one column below 38rem.

### Guidance-type cards

Guidance-type cards use the full family field as their dominant cue. A same-color title and type
icon form one supporting lockup; the arrow communicates navigation rather than category. Avoid an
additional accent bar or colored edge. The grid uses four columns wide, two compact, and one narrow.

The field tint may fill the entire card because category identity is the content of this section.
Avoid using the same saturated treatment for every ordinary index entry.

### Dense index entries

Index entries use a light family wash rather than a full field. Tags appear above the title, while
one family edge provides the supporting cue. Tags appear above the title, while the type icon,
title, and arrow share one row. Stable IDs and descriptions follow beneath.

The title is the dominant line. Tags and IDs should not become larger or brighter than it.

### Related links

Related links use a compact tinted field with a left border. The stable ID and human title remain
distinct. Because the field is intentionally quiet, the edge remains its supporting family cue.
Their arrow follows the same scale and movement as other navigational cards.

### Chips and tags

Chips are small bordered metadata or navigation controls. They are not mystery containers for
ordinary prose.

- Metadata chips stay quiet and neutral.
- Navigational chips use the family heading color and a low-opacity tint.
- Filled fields are reserved for stronger actions.
- Tags should add a second axis of information rather than repeat the page, group, or title.
- Tags and chips do not use arrows.

## Controls

Primary controls, navigational chips, and stand-alone actions use a small radius, clear border,
and a minimum height of 40px. Compact labels use mono, but should normally remain at least 13px to
14px. Noninteractive metadata labels may be shorter because adjacent card or row spacing supplies
the reading separation without implying a touch target.

The hierarchy is:

1. Filled same-hue field for the primary action.
1. Transparent or lightly tinted field with a family border for secondary navigation.
1. Neutral border for tertiary controls such as theme and compact search buttons.

Search, theme, menu, copy, and feedback controls need visible focus outlines. Do not make a whole
text container look like a button unless the whole surface is interactive.

### Interaction states

Every interactive component defines the states that apply to it. State changes must not move
surrounding layout.

- **Rest:** The action or destination is recognizable without hover.
- **Hover:** Tone or border strengthens; the surface does not lift.
- **Focus visible:** A 3px high-contrast ring appears with enough offset.
- **Pressed:** Feedback remains within the existing footprint.
- **Current or open:** `aria-current`, `aria-expanded`, or checked semantics accompany styling.
- **Visited:** Prose and reference links may change tone without losing contrast.
- **Disabled:** Semantics and more than opacity communicate unavailability.
- **Loading:** The control retains its dimensions and accessible name.
- **Invalid:** A semantic status, text explanation, and programmatic state agree.

Not every component uses every state. A link is never disabled; a static specimen is never made to
look focusable. Menus return focus to their trigger when they close and support expected keyboard
navigation.

## Code, Tables, and Prose Structures

Code blocks use a dark raised surface, a neutral border, a 3px family top rule, and a visible copy
control. In light mode they use the raised light surface rather than a dark terminal inset.

Tables use neutral cell rules and a family field for the header row. Increase spacing before
reducing type below a comfortable reading size.

Agent instructions may use a family field and left accent rule because they are copyable artifacts.
Ordinary explanatory prose should remain on the page background.

Blockquotes and callouts use a left accent rule and neutral text. Avoid bright full-surface warning
colors unless the semantic state requires them.

## Responsive Behavior

### Navigation collapse

This transition occurs when the primary navigation, brand, search, and theme controls no longer fit
with balanced spacing. The current recipe maps it to `73.5rem`.

- Hide the full primary navigation and show the menu control.
- Change homepage guidance cards from four columns to two.
- Change the Guides work-area grid from three columns to two.
- Cap leaf titles at 64px.
- Put leaf metadata actions on a separate row from chips.

### Hero decoration hide

This transition occurs before the book forces hero text or actions to wrap. The current recipe maps
it to `73.5rem`, alongside the navigation collapse.

- Hide the homepage book before hero buttons or text begin to wrap around it.
- Keep the hero as one content column.

### Layout stack

This transition occurs when the label and reading columns can no longer preserve useful measure.
The current recipe maps it to `52rem`.

- Collapse label/content layouts to one column.
- Stop sticky group labels.
- Reduce major hero and section gaps.
- Use two columns for ordinary task grids where space permits.

### Single column

This transition occurs when cards can no longer preserve title and body measure side by side. The
current recipe maps it to `38rem`.

- Hide the text site name and show the `SP.` mark.
- Reduce search to its icon control.
- Collapse task, card, and related-link grids to one column.
- Stack hero icons above titles.
- Hide redundant category and current-page breadcrumbs.
- Group footer source links deliberately rather than letting one link orphan by accident.

These are content decisions, not device classes. The numerical mappings are recipes and may differ
by component when their fit conditions diverge. Change a mapping when its named relationship stops
fitting, not to match a generic device list.

## Motion

Motion is brief and functional:

- Card arrows move slightly to confirm navigation.
- Hover fields change tone without lifting or floating the card.
- The homepage verb changes slowly and is the only editorial animation.
- Menus and dialogs may use ordinary control transitions.

Ordinary feedback transitions collapse to near-zero duration under `prefers-reduced-motion`.
Editorial animation is disabled completely rather than continuing to swap content at near-zero
duration. Avoid parallax, shimmer, texture animation, card lift, and attention-seeking page
entrances.

## Content and Interface Voice

UI copy follows the repository's technical-writing rules.

- Name the destination, decision, artifact, or work area directly.
- Do not narrate the interface with phrases such as “cards map,” “pages carry,” or “the full map.”
- Avoid slogans, coaching language, generic praise, and repeated summaries.
- Use prose for relationships and lists for real enumerations.
- Keep descriptions concrete enough to distinguish neighboring destinations.
- Do not mention internal catalog mechanics unless they are part of the reader's task.
- Stable IDs are useful metadata, but human titles remain the primary reading line.

Review new copy against `DOCS-AVOID-GENERATED-PROSE-TELLS`,
`DOCS-WRITE-TECHNICAL-PROSE`, and `DOCS-OWN-AI-ASSISTED-PROSE`.

## Accessibility

- Meet WCAG AA contrast for normal text in both themes.
- Pair category color with labels, icons, or position.
- Keep focus outlines at 3px with enough offset to remain visible against tinted fields.
- Preserve a 40px target for primary controls, navigational chips, and stand-alone actions.
  Compact inline metadata is not a control.
- Use semantic links for navigational cards and buttons for actions.
- Keep decorative icons hidden from assistive technology; label meaningful icons.
- Do not depend on hover to reveal that a card is clickable.
- Respect `prefers-reduced-motion`.
- Preserve structure, current state, and focus visibility in forced-colors mode.
- Reflow without horizontal scrolling at 320 CSS pixels except for intrinsically two-dimensional
  content such as large tables.
- Give auto-updating content a pause mechanism and prevent repeated assistive-technology
  announcements when the update is decorative.
- Check keyboard navigation through the header, search dialog, cards, leaf actions, and footer.

## Named Exceptions

Exceptions stay local and include a review trigger. They do not establish a new default.

- **Homepage hero:** Uses more editorial scale and decorative art to establish identity. Review
  when the hero delays access to useful content.
- **Homepage book:** Uses one shadow and a simulated printed object as a memorable, nonessential
  brand element. Review when it wraps, distorts, or dominates.
- **`SP.` monogram:** Uses a slightly smaller optical mono label because it reads as a symbol, not
  body text. Review when it becomes difficult to distinguish.
- **Large catalogs:** Use denser cards and metadata to support scanning. Review when important
  labels become microtext.
- **Catalog metadata:** Noninteractive tags may use a 28px label height inside already-spaced rows.
  Review if the label becomes interactive or is mistaken for a control.
- **Agent instruction and code:** Use a stronger contained field because the entire block is a
  copyable artifact. Review when ordinary explanatory prose adopts the treatment.

## Directions Intentionally Rejected

The following choices were explored or appeared during iteration and should not return without a
new design decision:

- A terminal, cyberpunk, or developer-console theme.
- Monospace body copy.
- IBM Plex Serif or another heavy serif as the main display face.
- Pure white titles disconnected from the current family color.
- Large rounded boxes around unrelated prose.
- Shadows and gradients without a structural meaning.
- Large vertical hero rules or closely repeated horizontal rules.
- Similar-strength colors for Tags, References, and primary content families.
- A full left documentation sidebar; the site uses global navigation plus page-local grouping.
- A decorative book that changes aspect ratio, wraps below the hero, or remains on narrow screens.
- Small text as the default solution to crowded layouts.
- Tiny absolute arrows floating at the far edge of a card.

## Useful Structure Borrowed from the Stitch Design Record

The earlier Stitch `DESIGN.md` described a different analog documentation project. Its visual
tokens and brand rules do not apply here, but its documentation structure exposed useful gaps in
our first design-system specimen:

- State the mood and the boundaries of the reference-manual influence.
- Record token values as well as their semantic roles.
- Describe component contracts, not only isolated examples.
- Give page-type guidance.
- Keep explicit accessibility and implementation sections.
- Record do/don't decisions so later work does not repeat rejected experiments.

This document adopts that structure while retaining Software Practices' current palette,
typography, navigation model, and low-container layout.

## Review and Maintenance

### Representative page set

Broad design changes should be checked against a representative set of at least 19 routes covering:

- Homepage.
- All category roots.
- A rule-domain group.
- A tag-results group.
- A long guide leaf.
- A long rule leaf.
- Pattern, principle, mechanism, agent, and reference leaves.
- The rendered design-system specimen.

Check each at approximately 1440px, 1024px, and 390px. The exact viewport may move when a real
breakpoint needs investigation, but the audit must include wide, compact, and narrow compositions.

Keep a small evidence set for major revisions, but store routine review captures outside the source
tree and surface them in the review session. Do not commit screenshots unless they are an explicit
project artifact.

### What to inspect

- Horizontal overflow and unexpectedly clipped content.
- Header balance, baseline alignment, and transition to compact navigation.
- Title wrapping and title/icon alignment.
- Spacing between heroes, rules, sections, cards, and footer.
- Card padding, arrow presence, arrow scale, and title-row alignment.
- Category color, body contrast, link contrast, and focus contrast.
- Leaf chip/action grouping.
- Group-label and content-column alignment.
- Repeated or orphaned footer controls.
- Dark and light themes.

### Change checklist

Before merging a design-system change:

1. Decide whether it changes a token, component contract, page family, or one local exception.
1. Update the shared rule rather than patching several pages independently.
1. Check the rendered design-system specimen when the change affects a documented primitive.
1. Run the representative-page audit across all three width classes.
1. Test keyboard focus and reduced motion when interaction changes.
1. Run `markdownlint-cli2 "**/*.md"` and `pnpm build`.
1. Update this document when the rationale or component contract changed.

## Short Do/Don't Reference

### Do

- Use family color for orientation and neutral text for reading.
- Use serif for titles, sans for explanation, and mono for metadata.
- Build hierarchy with alignment, spacing, and meaningful lines.
- Make whole-card navigation obvious before hover.
- Choose density according to item count and reader task.
- Hide decorative elements before they force awkward wrapping.
- Test root, group, and leaf pages together.

### Don't

- Add a rounded container because a section feels empty.
- Introduce a hue or font for one page.
- Use two adjacent rules without distinct structural meanings.
- Float arrows at arbitrary positions or pair an arrow with a competing destination action.
- Shrink body or control text to rescue a layout.
- Turn the reference-manual influence into terminal or hardware skeuomorphism.
- Treat the desktop layout as the mobile layout with narrower columns.
