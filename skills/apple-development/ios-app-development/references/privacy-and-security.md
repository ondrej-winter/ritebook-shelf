# Privacy and security

Use before changing protected-resource access, accounts, data storage, analytics,
or third-party SDKs. Review actual data flows and the app's distribution context.

## Minimize access and provide recovery

Collect only what the feature requires. Prefer a system-mediated selection when
it supplies the needed item without broad library or resource access. Request
permission when the person invokes the relevant feature, with a specific,
localized purpose string in the correct target. Handle denied, restricted,
limited, and later-revoked access according to the framework's actual states.
Keep unrelated tasks usable and provide a useful fallback. See
[Protecting the user's privacy](https://developer.apple.com/documentation/uikit/protecting-the-user-s-privacy).

Inspect current API-specific authorization documentation rather than copying an
older general sample. For tracking and advertising identifiers, follow current
[User privacy and data use](https://developer.apple.com/app-store/user-privacy-and-data-use/)
and App Tracking Transparency requirements; another identifier or a custom consent
screen does not bypass a refusal.

## Protect stored and transmitted data

Store credentials, tokens, and small secrets with
[Keychain services](https://developer.apple.com/documentation/security/keychain-services),
not preferences or bundled configuration. Choose accessibility and sharing rules
for the actual locked-device and extension needs. Apply appropriate file data
protection to sensitive files and keep secrets and personal content out of logs,
analytics, notifications, and test fixtures.

For account authentication, consider
[passkeys](https://developer.apple.com/documentation/authenticationservices/supporting-passkeys)
when supported by the service; configure associated domains and server challenge
verification. Check cancellation, credential unavailability, sign-out, and account
recovery. A local biometric check is not a substitute for server authentication.

## Keep declarations aligned with behavior

Audit the app and embedded SDKs for collection, tracking, and required-reason API
use. Bundle accurate
[privacy manifests](https://developer.apple.com/documentation/bundleresources/privacy-manifest-files)
as target resources, with reasons that match actual use. Inspect Xcode's combined
privacy report and current third-party SDK requirements. A manifest does not
replace permission prompts, a privacy policy, or App Store privacy disclosures.

Review the applicable
[App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/)
early for accounts, sensitive data, purchases, and content. For example, account
creation requires an in-app account-deletion path. Recheck feature-specific and
regional requirements at release time rather than treating this summary as a
complete compliance checklist.
