# Design and accessibility

Use this reference for watch interfaces and interactions. These are concise
engineering applications of Apple's guidance; follow the linked sources for
full platform rules and API details.

## Navigation and input

Choose a container that matches the task:

| Need                                         | Preferred starting point                                   |
| -------------------------------------------- | ---------------------------------------------------------- |
| A short hierarchy with drill-down            | `NavigationStack`                                          |
| A source list and its selected detail        | `NavigationSplitView`; watch displays one column at a time |
| Distinct peer screens reached with the Crown | `TabView` with `.verticalPage` where supported             |
| A value selection                            | A system `Picker` before custom Crown handling             |

Keep primary content prominent and use system toolbars for consistent button
placement. Avoid custom navigation chrome that competes with the system.
[Creating an intuitive and effective UI](https://developer.apple.com/documentation/watchos-apps/creating-an-intuitive-and-effective-ui-in-watchos-10)
explains these watch-specific container behaviors.

Preserve Crown scrolling and touch equivalents. Custom Crown input should produce
immediate visual feedback and allow precise selection; do not intercept expected
navigation without a clear reason. Crown presses belong to the system.
See the [Digital Crown HIG](https://developer.apple.com/design/human-interface-guidelines/digital-crown).

Where supported, assign `.handGestureShortcut(.primaryAction)` to one obvious
buttonlike control per scene. Keep a visible touch action available. Check actual
hardware support, and remember that an offscreen primary action causes scrolling
toward the control before invocation.
[Double-tap guidance](https://developer.apple.com/documentation/watchos-apps/enabling-double-tap)
describes the default behaviors and precedence.

## Layout, appearance, and accessibility

- Use flexible layouts, semantic text styles, and system controls. Respect safe
  areas for interaction and use `scenePadding` to align content with system text
  margins. Extend decorative backgrounds to the edges only where appropriate.
- Inspect small and large supported displays and different aspect ratios. Use
  extra space for legibility and larger controls before adding density. Avoid
  branching on a hardcoded list of watch models.
  [Supporting multiple watch sizes](https://developer.apple.com/documentation/watchos-apps/supporting-multiple-watch-sizes)
  explains sizing and margins.
- Test Dynamic Type, VoiceOver labels and traversal, contrast, reduced motion,
  and reduced transparency. Give custom controls meaningful labels, values, and
  actions; never convey status only through color, motion, sound, or haptics.
  Validate long localized text, right-to-left layouts, and localized dates,
  numbers, and units. See the
  [Accessibility HIG](https://developer.apple.com/design/human-interface-guidelines/accessibility).
- Rebuild and inspect system components with the current SDK before adding custom
  appearance code. Standard controls adopt the current visual language. Keep
  Liquid Glass focused on controls/navigation and audit custom backgrounds for
  interference and poor contrast. Verify each custom API's watchOS availability;
  shared Apple-platform articles also contain APIs for other platforms.
  [Adopting Liquid Glass](https://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass)
  and [Apple Design Resources](https://developer.apple.com/design/resources/)
  provide the implementation and design starting points.

## Always On and feedback

Handle active, inactive, and background phases explicitly. On supported watches,
an inactive app can remain visible at reduced luminance and update frequency.
Stop unnecessary animation and subsecond work. Use system date rendering or
`TimelineView` where appropriate and adapt to the actual cadence rather than
driving a timer to force continuous updates.

Mark sensitive views with `privacySensitive()` and honor privacy redaction;
inspect both redacted and unredacted states. Keep important information legible
at reduced luminance. Test wrist lowering, reactivation, and Always On disabled.
See [Designing for Always On](https://developer.apple.com/documentation/watchos-apps/designing-your-app-for-the-always-on-state).

Use system haptic meanings consistently and sparingly, with visual equivalents.
Do not assume a cross-platform custom haptics API works on watchOS.
See [Playing haptics](https://developer.apple.com/design/human-interface-guidelines/playing-haptics).

## Notifications

Send concise, timely, high-value information and offer useful actions that avoid
opening the app. Do not repeat the same notification because it went unanswered.
Keep short-look content discreet and provide a coherent long-look experience.
Protect private data in titles and hidden previews; prefer nondestructive actions.
See the [Notifications HIG](https://developer.apple.com/design/human-interface-guidelines/notifications).

For implementation, use
[watchOS notifications](https://developer.apple.com/documentation/watchos-apps/notifications)
and UserNotifications. Distinguish direct watch delivery from iPhone forwarding;
test the selected route rather than assuming both devices display every alert.
Handle authorization refusal and changed settings without blocking unrelated app
features. Keep information available in the app if a notification is missed.
