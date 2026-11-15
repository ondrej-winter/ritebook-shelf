# Development and integrations

Use the sections relevant to the changed behavior. Check symbol availability
individually; a framework's minimum version does not cover every API it contains.

## State and concurrency

Give each piece of model state a clear owner. Derive presentation from that state
and pass bindings for edits instead of maintaining competing copies. On iOS 17
or later, prefer Observation's `@Observable` for new observable models, `@State`
for view-owned instances, and `@Bindable` where bindings are needed. Existing
`ObservableObject` code can migrate incrementally; it remains useful for older
deployment targets. Follow Apple's
[Observation migration](https://developer.apple.com/documentation/swiftui/migrating-from-the-observable-object-protocol-to-the-observable-macro).
Observation tracks changes; it does not provide persistence or actor isolation.

Use [Swift concurrency](https://developer.apple.com/documentation/swift/concurrency)
for asynchronous work. Isolate UI-facing mutable state appropriately with
[`MainActor`](https://developer.apple.com/documentation/swift/mainactor), and
respect actor and `Sendable` boundaries. Inspect the language mode, default actor
isolation, and concurrency settings before changing them. Resolve diagnostics
through ownership and isolation, rather than broadly adding unchecked annotations.

Tie view-scoped loading to SwiftUI's
[`task(id:...)`](https://developer.apple.com/documentation/swiftui/view/task%28id%3Aname%3Apriority%3Afile%3Aline%3A_%3A%29)
when appropriate; it restarts when the identity changes. Keep longer-lived work
under an explicit owner. [Task cancellation](https://developer.apple.com/documentation/swift/task)
is cooperative: propagate it, check it during lengthy work, and prevent superseded
results from replacing newer state. Creating a `Task` or adding `async` does not
automatically move expensive synchronous work off the main actor. Follow
[Improving app responsiveness](https://developer.apple.com/documentation/xcode/improving-app-responsiveness)
and verify execution with the project's concurrency settings.

## Lifecycle and data

Use the SwiftUI `App`/scene lifecycle for new SwiftUI apps. Observe
[`scenePhase`](https://developer.apple.com/documentation/swiftui/scenephase) at the
appropriate scope; the app-level value aggregates all scenes. In scene-based
UIKit apps, use [scene lifecycle callbacks](https://developer.apple.com/documentation/uikit/managing-your-app-s-life-cycle).
Persist meaningful edits promptly, preserve useful navigation state, and reconcile
external changes on resume. Do not depend on a termination callback to save data.

On deactivation/backgrounding, pause unnecessary work and release resources as
the framework requires. Hide sensitive content before the app-switcher snapshot.
See [Preparing your UI for the background](https://developer.apple.com/documentation/uikit/preparing-your-ui-to-run-in-the-background).

Choose storage by data lifetime and compatibility. Use preferences for settings,
files for documents, and managed persistence for an appropriate object graph.
[SwiftData](https://developer.apple.com/documentation/swiftdata) is an option for
new managed persistence on iOS 17 or later; preserve suitable existing Core Data
or other storage. Plan schema evolution with
[`SchemaMigrationPlan`](https://developer.apple.com/documentation/swiftdata/schemamigrationplan)
when using SwiftData. Test upgrades from real earlier schemas and handle save or
migration failures without silently discarding the user's store. Treat cached
content as replaceable and distinguish it from authoritative user data.

## Networking and background execution

Use [`URLSession`](https://developer.apple.com/documentation/foundation/urlsession)
and async APIs where appropriate. Keep App Transport Security protections; review
exceptions narrowly. Handle HTTP failures, decoding errors, cancellation, offline
operation, and cached/stale content explicitly. Define safe retry behavior for
writes, including uncertain outcomes, rather than duplicating side effects.

Select background execution by the actual job:

| Job | Apple facility |
| --- | --- |
| Finish brief critical foreground work | Limited UIKit background task; end it and handle expiration |
| Transfer files while suspended | Background `URLSession` uploads/downloads |
| Refresh content opportunistically | `BGAppRefreshTask` |
| Deferred intensive maintenance | `BGProcessingTask` |
| Continue a user-started long-running job | `BGContinuedProcessingTask` where supported |

Use [Choosing background strategies](https://developer.apple.com/documentation/backgroundtasks/choosing-background-strategies-for-your-app)
and [Performing long-running tasks](https://developer.apple.com/documentation/backgroundtasks/performing-long-running-tasks-on-ios-and-ipados).
Configure the required capabilities and task identifiers, register handlers as
documented, and implement completion, expiration, and cancellation. Continued
processing starts from a person's foreground action and reports progress; it is
not a general scheduler. Refresh, processing, and silent pushes do not guarantee
execution at a requested time. Keep the foreground path useful after missed work.

## Optional system surfaces

Add integrations only when the product needs them:

- [WidgetKit](https://developer.apple.com/documentation/widgetkit): provide a small,
  useful presentation, appropriate timeline content, and a route to matching app
  content. Design for stale or unavailable data rather than continuous execution.
- [ActivityKit](https://developer.apple.com/documentation/activitykit): use Live
  Activities for a bounded ongoing event. Manage start, updates, and end; these
  updates differ from widget timelines.
- [App Intents](https://developer.apple.com/documentation/appintents): expose useful
  actions/entities for system experiences, reuse the app's behavior, and preserve
  authorization and validation outside the foreground UI. Check availability and
  preview status of each Siri or intelligence integration.
- [StoreKit purchases](https://developer.apple.com/documentation/storekit/in-app-purchase): for purchases,
  use current Swift APIs and verify transaction/entitlement handling, pending and
  canceled flows, restoration, and revocation with the documented testing tools.

For other capabilities such as location, camera, or HealthKit, open the specific
Apple framework's authorization, lifecycle, background, and hardware guidance
before implementation. Shared platform documentation is not evidence that every
device supports a capability.
