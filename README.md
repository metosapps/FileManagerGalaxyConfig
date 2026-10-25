# File Manager — Galaxy configuration repository

Package `com.filegx.appsmanager`; store `galaxy_store`. App source is maintained separately.
Public origin: https://metosapps.github.io/FileManagerGalaxyConfig/.
Pages deployment succeeded on 2026-10-25; this is configuration/legal hosting, not an app store release.

`site/payload.json` is human-editable data. `site/config.json` is the signed public envelope.
`config-public-key.b64` is public and pinned in this app's Galaxy build. The matching private
key is stored privately outside this repository.
Do not publish, paste or add that private key to Git. Retain an independent private backup.
This key signs configuration data; it is NOT the APK publisher certificate.

1. Increase `revision` whenever behavior changes.
2. Set `issued_at` and `expires_at` using current UTC epoch seconds; lifetime is at most seven days.
3. Keep the exact package/store scope and store URL. Production ads and IAP start off.
4. Sign: `python3 sign_config.py --key /absolute/private/path/to/key.pem`.
5. Commit and push the public `site/` changes. Wait for Pages deployment success.
   The app default is `https://metosapps.github.io/FileManagerGalaxyConfig/config.json`.
6. Verify the actual deployed response AND acceptance by the installed app. A local signature
   check or an uploaded hosting job does not prove the public endpoint works.

`rollback.local.json` is an undeployed example, not a revision to replay blindly. Choose a
revision greater than the then-current live revision and renew timestamps before signing.
Support: chennoufo11@gmail.com. Check hosting and app release evidence separately; public legal pages do not establish store availability.

Production advertising must stay off until this exact app is live and the user explicitly
authorizes activation. A remote flag cannot override consent, Pro, lifecycle, operation,
purchase, first-session, per-format and compiled safety gates.

Current deployed revision: 3; production ads and IAP OFF. Debug uses official Google demo inventory.
Renew before the signed seven-day expiry; no automatic renewal job is configured.
Never deploy private keys or signing credentials.
