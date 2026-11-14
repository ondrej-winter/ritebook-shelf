# Runtime and integrations

Read the sections relevant to the requested feature. Verify watchOS symbol
availability and target capabilities before copying an API from a shared-platform
article. The recovery checks below are engineering applications of the documented
execution constraints, rather than promises of delivery from the OS.

## Data, networking, and independent operation

Keep a useful local state and distinguish pending work, confirmed success, stale
data, and failure. For user-initiated writes, make retries safe and reconcile
uncertain outcomes before repeating a side effect. Define conflict handling if
the watch and phone can both change the same data.

Use `URLSession` for direct requests and let the system choose the transport.
Default or ephemeral sessions suit small foreground requests. For suitable
transfers that must outlive foreground execution, use a background session,
its delegate callbacks, and the watch background-task lifecycle. Keep transfers
small; persist enough identity to reconnect delivery with stored work.
Background execution and delivery can be deferred.
[Keeping watch content up to date](https://developer.apple.com/documentation/watchos-apps/keeping-your-watchos-app-s-content-up-to-date)
and [Making background requests](https://developer.apple.com/documentation/watchos-apps/making-background-requests)
cover these choices. Older extension-delegate examples need adaptation to the
current single-target app lifecycle.

An independent app must support its own account setup and sign-in when accounts
are required. Avoid requiring an account without a product need; consider
CloudKit or AuthenticationServices when appropriate. For custom credential
fields, use `TextField`/`SecureField`, correct content types, and associated
domains for autofill. See
[Authenticating on Apple Watch](https://developer.apple.com/documentation/watchos-apps/authenticating-users-on-apple-watch).

## Optional iPhone communication

Configure and asynchronously activate `WCSession` on each app before transferring
data. Inspect activation and platform-appropriate installation state; implement
iPhone deactivation/reactivation for watch switching. Reachability is a live
messaging condition, not general internet connectivity or a requirement for all
queued transfers.

| Data need                                    | WatchConnectivity mechanism                                             |
| -------------------------------------------- | ----------------------------------------------------------------------- |
| Latest replaceable snapshot                  | `updateApplicationContext`; replaces previous context                   |
| Immediate request to a reachable counterpart | `sendMessage`/`sendMessageData`; handle reachability changes and errors |
| Queued dictionaries                          | `transferUserInfo`; deferred background delivery                        |
| Larger file payload                          | `transferFile`; deferred background delivery                            |

Delegate callbacks arrive on a background thread; cross into the appropriate
isolation before changing UI state. Send changes rather than repeatedly sending
all data. See [WCSession](https://developer.apple.com/documentation/watchconnectivity/wcsession).
Keep useful operation when the phone is unreachable or the companion is absent;
WatchConnectivity cannot be an independent app's primary data source.

## Background execution and energy

Choose the mechanism from the actual task:

- Brief refresh: handle the supported task using SwiftUI `backgroundTask` or
  `WKApplicationDelegate`. Finish promptly; explicitly complete delegate-managed
  tasks, including failure paths. Handle cancellation and expiration.
- Transfer: use a background `URLSession` and its task delivery mechanism.
- Genuine workout, audio, or location session: use that framework's session and
  required capability. Start and end it according to its documented lifecycle.
- Eligible self care, mindfulness, physical therapy, or smart alarm:
  consider `WKExtendedRuntimeSession`, with expiration and invalidation handling.

Do not claim periodic refresh runs at an exact time, keep the process alive with
a timer, or select a workout/extended session solely to obtain runtime. Profile
CPU and stop unnecessary sensors, networking, animation, and disk work when the
user's activity ends. See
[Background execution](https://developer.apple.com/documentation/watchkit/background-execution)
and [Extended runtime sessions](https://developer.apple.com/documentation/watchkit/using-extended-runtime-sessions).

## Complications, Smart Stack, and system actions

Build watch complications in a watchOS WidgetKit extension. Choose the accessory
families that suit the data and test their rendering, privacy, placeholders,
configuration, and launch routes. For ClockKit migration, map existing
configurations and verify installed complications survive: once WidgetKit
complications are provided, the system stops requesting ClockKit timelines.
See [Accessory widgets and complications](https://developer.apple.com/documentation/widgetkit/creating-accessory-widgets-and-watch-complications)
and [Migrating ClockKit](https://developer.apple.com/documentation/widgetkit/converting-a-clockkit-app).

Generate timelines for predictable changes; request reloads when underlying data
changes. WidgetKit renders in a separate process; give the provider access to a
persisted snapshot or other appropriate data source rather than relying on the
app's in-memory model. Use system-rendered dynamic dates for time displays. Reload
budgets are dynamic; a reload request or timeline date does not guarantee immediate fresh
data. Provide a meaningful stale/empty state. Follow
[Keeping a widget up to date](https://developer.apple.com/documentation/widgetkit/keeping-a-widget-up-to-date).

For contextual Smart Stack suggestions, use watchOS relevance mechanisms rather
than assuming iOS timeline relevance scores behave identically. Consider a
timeline provider's relevance callback or `RelevanceConfiguration` with
`RelevanceEntriesProvider`, according to availability and the widget's purpose.
Request permissions needed for context clues. See
[Smart Stack visibility](https://developer.apple.com/documentation/widgetkit/widget-suggestions-in-smart-stacks)
and the [RelevanceConfiguration reference](https://developer.apple.com/documentation/widgetkit/relevanceconfiguration).
The symbol reference lists watchOS 26 availability; older snippets may use
different version annotations. Check the installed SDK before implementation.

Expose appropriate actions using
[App Intents](https://developer.apple.com/documentation/appintents)
for Siri, Shortcuts, and supported system surfaces. Reuse the app's validated
operations instead of building a second write path. For
[WidgetKit controls](https://developer.apple.com/documentation/widgetkit/creating-controls-to-perform-actions-across-the-system),
choose buttons versus toggles by semantics, provide accurate current values, and
finish and persist state before `perform()` returns. Check watch support and
privacy/authentication requirements for each surface. Apple's
[watchOS 26 session](https://developer.apple.com/videos/play/wwdc2025/334/)
explains watch controls and the newer widget patterns.

When extending an iPhone Live Activity, distinguish its remote Apple Watch
presentation from an independently executing watch app. Provide a layout for
the small activity family and test update delays and interaction destinations.
See [Bring your Live Activity to Apple Watch](https://developer.apple.com/videos/play/wwdc2024/10068/).

## Health and fitness, when relevant

Check HealthKit availability, configure the owning target's capability and usage
descriptions, and request only the read/write types needed at the point of use.
Authorization request completion is not proof of read access. HealthKit protects
read-denial status, so an empty query is not evidence that no health data exists.
Respect limited history access where supported. See
[Authorizing health data](https://developer.apple.com/documentation/healthkit/authorizing-access-to-health-data).

For actual workouts, use `HKWorkoutSession` and the appropriate builder, configure
the activity accurately, and expose clear start, pause/resume, end, and save or
discard behavior. Handle session errors, interruption, and recovery using the
current APIs; stop resources when finished. Follow
[Running workout sessions](https://developer.apple.com/documentation/healthkit/running-workout-sessions).
Apple's [workout sample](https://developer.apple.com/documentation/healthkit/build-a-workout-app-for-apple-watch)
is useful for the flow, but its older extension-target setup is not the default
for a new single-target app.
