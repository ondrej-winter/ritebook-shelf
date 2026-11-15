# Design and accessibility

Use for iPhone interfaces and interactions. These are engineering applications of
Apple's HIG; the linked guidance supplies the full rationale and platform details.

## Navigation and input

Choose containers by the relationship between tasks and content:

| Need | Starting point |
| --- | --- |
| Stable top-level destinations | `TabView`; preserve each section's navigation state |
| Hierarchical drill-down | `NavigationStack` and value-based destinations |
| Sidebar, content, and detail | `NavigationSplitView`; check collapse into compact layouts |
| A scoped task in the current context | A sheet with clear completion and cancellation |

See [Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars),
[Sheets](https://developer.apple.com/design/human-interface-guidelines/sheets), and
[Migrating to new navigation types](https://developer.apple.com/documentation/swiftui/migrating-to-new-navigation-types).
The newer navigation containers require iOS 16 or later. Preserve older-OS
navigation where the deployment minimum requires it; migrate within the requested
scope. Model programmatic destinations so links can reach the intended content.

Keep expected back navigation and system gestures. Make frequent actions easy to
reach and discover, with visible alternatives to gesture-only functionality. Use
appropriate keyboard types, content types, focus, and submit actions for forms;
keep the active field and validation feedback visible when the keyboard appears.

## Adaptive layout and system appearance

Use flexible SwiftUI layouts or UIKit Auto Layout with safe areas, margins, and
the actual available space. Avoid fixed screen dimensions and device-name layout
branches. Check small and large supported layouts, rotation where supported,
Display Zoom, keyboard presentation, and large text. For existing iPad support,
also check resizable windows and compact/regular transitions; do not infer a
fixed layout from orientation. See the
[Layout HIG](https://developer.apple.com/design/human-interface-guidelines/layout).

Use semantic text styles, colors, SF Symbols, and asset variants that work in
Light and Dark appearances. Rebuild with the current SDK and inspect standard
components before adding appearance overrides. For Liquid Glass, keep the material
on controls and navigation, review custom bar backgrounds that obscure system
effects, and check reduced transparency, reduced motion, and contrast. Use
[Adopting Liquid Glass](https://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass)
for implementation choices and
[Apple Design Resources](https://developer.apple.com/design/resources/) for current
templates and assets; verify individual APIs against the deployment minimum.

## Accessibility and localization

- Let text grow and reflow through accessibility Dynamic Type sizes. Avoid fixed
  row heights that clip content. Use the HIG's control-size and spacing guidance
  rather than making only the visible icon tappable.
- Give custom controls meaningful accessibility labels, values, traits, and
  actions. Check VoiceOver reading order and focus after navigation or updates;
  distinguish decorative imagery from information.
- Convey state through more than color, sound, motion, or haptics. Support reduced
  motion, sufficient contrast, and alternative input such as Voice Control,
  Switch Control, and Full Keyboard Access where relevant.

Follow the [Accessibility HIG](https://developer.apple.com/design/human-interface-guidelines/accessibility).
Audit the actual task with assistive technologies; an automated audit alone does
not establish usability.

Use [string catalogs](https://developer.apple.com/documentation/xcode/localizing-and-varying-text-with-a-string-catalog)
for new localizable text when supported by the toolchain. Supply translator
context and plural variants; avoid assembling sentences from translated fragments.
Use Foundation's locale-aware formatting for dates, numbers, currencies, and
units. Check long translations, right-to-left order, and accessibility text in
the supported languages.

## Notifications

Send timely information with a useful destination or action, protect private
previews, and avoid repeated interruptions. Keep important content available in
the app if an alert is missed. Follow the
[Notifications HIG](https://developer.apple.com/design/human-interface-guidelines/notifications).
Request [notification authorization](https://developer.apple.com/documentation/usernotifications/asking-permission-to-use-notifications)
in a context that explains its value; recheck settings because people can change
them. Declining notifications should leave unrelated functionality usable.
