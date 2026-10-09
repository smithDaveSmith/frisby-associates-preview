# Frisby & Associates — website preview

Complete static concept for https://frisbyassoc.ie/. Preview hosting: GitHub Pages. No official-domain change, booking, payment or direct form submission is included.

## Edit and build

Requires Python 3.10+; no dependency installation.

- `content.json`: business details, service names/descriptions/questions, PDF labels and podcast links.
- `build.py`: shared header/footer, page layouts, homepage, about, resources, contact and preview privacy text.
- `assets/styles.css`: shared design tokens, layouts, responsive rules and reduced motion.
- `assets/site.js`: mobile navigation, email drafts and optional media players.
- `assets/`: retained branding, compressed illustration and nine original historical PDFs.
- `.github/workflows/pages.yml`: automatic `main` deployment and manual `workflow_dispatch`.
- `check.py`: export verification used by the deployment workflow.
- `ASSETS.md`: business sources, reference adaptations and asset rights.

From this project folder:

```bash
python3 build.py
python3 check.py
python3 -m http.server 8000 --directory dist
```

Open http://localhost:8000/. This root build is for local review. `dist` is generated, ignored by Git and not included in the project ZIP.

The workflow sets `BASE_PATH` to the repository name and `SITE_ORIGIN` to the owner's GitHub Pages origin. That builds working subdirectory paths for links, styles, scripts, images, PDFs, metadata and the missing-page actions. No SPA fallback or Jekyll configuration is needed.

If you rename the repository, the next workflow run uses the new name automatically. This workflow targets a project repository, not the special `username.github.io` root repository or a custom-domain site.

## GitHub deployment

1. Create the public repository `frisby-associates-preview` under your account. Add a README when creating it to initialise `main`.
2. Extract the project ZIP. Upload the **contents inside** `frisby-associates-preview/` to the repository root. Do not upload the ZIP itself or the containing project folder.
3. Include `.github/workflows/pages.yml` and `.gitignore`. In macOS Finder, press **Command + Shift + .** to show them. If `.github` is absent after browser upload, use **Add file → Create new file**, name it exactly `.github/workflows/pages.yml`, and paste the YAML from the extracted file. Commit it to `main`.
4. Open **Settings → Pages → Build and deployment → Source → GitHub Actions**. You do not need to create another workflow or choose Jekyll/static HTML templates.
5. Open **Actions → Deploy GitHub Pages preview → Run workflow → main → Run workflow**. The button becomes available after this workflow file has been committed to the default branch. Later pushes to `main` trigger deployment automatically.
6. Wait for both `build` and `deploy` jobs to pass. Use the published URL in the successful deployment/environment. If a job fails, inspect its actual log before changing files.

Repository: https://github.com/smithDaveSmith/frisby-associates-preview. Preview address: https://smithDaveSmith.github.io/frisby-associates-preview/. Check the latest successful Actions run and published environment when deploying changes.

### Browser upload size

Official limits checked 8 October 2026: 25 MiB per file and up to 100 files per upload. This package has fewer than 25 files, with its largest file below 1 MiB, so one upload fits. If hidden folders cannot be dragged, upload visible contents first and create the workflow by its exact path as described above.

https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository
https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages

## Working preview features

- Home, about, service directory, nine service pages, resources, podcasts, presentation, contact, privacy, a legacy news destination and a useful 404 screen.
- Service-specific enquiry topic preselection, required-field/email validation and meaningful-message validation.
- Email draft and copy-message fallback. The visitor must review and send the draft. No delivery confirmation is simulated.
- Telephone, email, directions and source-linked social profiles.
- Nine locally hosted historical PDFs. All are marked as 2020 material.
- Third-party video/audio players load only after the visitor chooses to load them; direct-platform links remain available.
- Responsive menu with Escape support, skip link, focus states and reduced-motion support.
- Page metadata, verified-business structured data and `noindex, nofollow, noarchive` on every HTML page. Robots permit crawling so search engines can read noindex. This is not access control: the public preview is shareable.

## Verification

8 October 2026, local headless Chromium 133.0.6943.0:

- 19 HTML pages at 375, 768 and 1440px: 57 rendered layouts checked; no page overflow, missing images or script errors.
- Manually inspected representative home, service, contact and resources screenshots.
- Service-to-enquiry preselection, blank form, invalid email, whitespace message, valid draft content, mobile menu/Escape, keyboard skip link, reduced motion and 200% text reflow verified.
- Axe-core WCAG A/AA/2.1 AA automated checks on all 19 pages: zero reported violations. This is not a full accessibility certification.
- Root and repository-subdirectory exports checked for local links, anchors, assets, form labels, image dimensions, PDF signatures and noindex.
- Third-party iframe wiring tested using mocked provider responses. Actual video/audio playback and provider cookie behaviour require live review; direct provider links are preserved.
- No enquiry sent, booking created or payment made. No Lighthouse or performance score measured.
- The ZIP is closed, CRC-tested, extracted and rebuilt before delivery. GitHub deployment is configured by the included workflow.

## URL continuity

Keep `/`, `/about-us/`, `/services/`, `/resources/`, `/podcasts/`, `/auto-enrolment-presentation/`, `/contact/` and `/privacy-policy/` unchanged on the final domain. Service detail routes are new additions.

| Existing destination | Final-platform recommendation |
|---|---|
| `/news/` | 301 to `/resources/`; preview includes a useful local `/news/` page. |
| `/tag/news/`, `/tag/coronavirus/` | 301 to `/resources/#archive` if those legacy archives are retained as inbound destinations. |
| `/wp-content/uploads/2020/03/{PDF}`, `/2020/04/{PDF}`, `/2020/05/{PDF}` | Keep original paths or 301 to `/assets/archive/{same-filename}`; see content.json for all nine names. |

GitHub Pages does not provide configurable HTTP 301 rules. Apply this mapping only on the selected final platform/server. Do not redirect business visitors to the old site for core content.

## Essential launch decisions

- Owner review of editorial service descriptions/questions and the exact scope. No credentials, reviews, prices or guarantees were fabricated.
- Confirm contact details, opening hours, social ownership and the right to reuse the existing photograph and PDFs.
- Supply genuine staff/office photography, approved team information and credentials if wanted. These are absent rather than invented.
- Approve a full production privacy notice. The existing published notice includes inconsistent data-sharing language and historical analytics descriptions; it was not copied as a production policy.
- Connect and test the final enquiry handler, notifications, spam controls and honest error/success states. The original WordPress Fluent Forms endpoint/credentials were not available or reused.
- Confirm third-party media accessibility, captions and current playback. Do not silently load players or carry the old analytics ID into this public concept.
- On authorised production launch only: replace preview notices/metadata, remove noindex, set final canonical URLs, update sitemap, configure any analytics/consent and implement redirects. Preserve business email DNS when changing hosting.

No WordPress, Webflow or other platform package is included. Migration happens only after a platform is selected.
