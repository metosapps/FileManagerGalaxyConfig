# File Manager — Galaxy configuration repository

Local preparation only. Package `com.filegx.appsmanager`; the public origin is configured during deployment. App source is maintained separately.

`site/payload.json` is human-editable data. `site/config.json` is the signed public envelope.
`config-public-key.b64` is public and pinned in this app's Galaxy build. The matching private
key is outside this repository at a private location outside this repository.
Do not publish, paste or add that private key to Git. Retain an independent private backup.
This key signs configuration data; it is NOT the APK publisher certificate.

1. Increase `revision` whenever behavior changes.
2. Set `issued_at` and `expires_at` using current UTC epoch seconds; lifetime is at most seven days.
3. Keep the exact package/store scope and store URL. Production ads and IAP start off.
4. Sign: `python3 sign_config.py --key /absolute/private/path/to/key.pem`.
5. After a public hosting destination is authorized, publish `site/` and build the app with
   `-PfilemanagerGalaxyConfigUrl=https://HOST/config.json`.
6. Verify the actual deployed response AND acceptance by the installed app. A local signature
   check or an uploaded hosting job does not prove the public endpoint works.

`rollback.local.json` is an undeployed example, not a revision to replay blindly. Choose a
revision greater than the then-current live revision and renew timestamps before signing.
Support: chennoufo11@gmail.com. Check hosting and app release evidence separately; public legal pages do not establish store availability.

Production advertising must stay off until this exact app is live and the user explicitly
authorizes activation. A remote flag cannot override consent, Pro, lifecycle, operation,
purchase, first-session, per-format and compiled safety gates.
