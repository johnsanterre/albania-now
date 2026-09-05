# Albania Now — platform requirements

**Living document.** Started 2026-09-05 from John's directive: turn the static
site into a functional web app with logins and automatic progress — no
volunteer teachers grading anyone. We expand this until it feels well built;
then the pitch deck gets rebuilt on top of it.

Status of each requirement: **M** must have for the app pilot · **S** should
have soon after · **L** later.

---

## 1. What similar platforms actually do (carrots and sticks)

| Platform | Carrots | Sticks | Verdict for us |
|---|---|---|---|
| **Duolingo** | Streaks, XP, leagues, badges, mascot | Streak LOSS (loss aversion), league demotion, guilt notifications | Streak psychology works but the sticks are dark patterns aimed at engagement, not learning. **Refuse the sticks; borrow the visible-progress instinct.** |
| **freeCodeCamp** | Linear curriculum map, auto-graded projects, **certificates**, public profile with contribution heatmap | None — entirely carrot | Closest to our shape. Auto-graded projects = our CHECK cells. **Borrow: certificates with verification URLs, the progress map, test-gated completion.** |
| **Khan Academy** | Mastery levels per skill, energy points, teacher dashboards | None | Mastery-progress UI is the gold standard for "where am I." **Borrow the per-lesson progress model (we have 8 segments — already granular).** |
| **CS50 (Harvard)** | The **famous lecture** as the spine, real certificates, auto-graded problem sets (check50) | Hard deadlines per cohort | The nearest cousin to our lecture-as-reward model — prestige and access as the carrot. **Borrow: cohort deadlines as the one healthy stick; the lecture as identity.** |
| **Scratch** | Community showcase, remixing, social identity | None | The community IS the product. **Borrow later: a place to show builds.** |
| **Zooniverse** | Contribution to real science; "you matter" | None | Meaning as a carrot. Our planetary sprint can end in real citizen-science contribution (Planet Hunters) — already linked in go-deeper. |
| **Kaggle / LeetCode** | Rankings, medals, competition | Public ranking pressure | **Refuse** — ranking teenagers against each other in an optional program kills the weakest students' participation first. |

**The carrot stack we choose (in order of power):**
1. **The lecture** — access to a real scientist, earned. Nobody else has this.
2. **The certificate** — verifiable URL, signed by Free Focus, listable on a
   CV/university application. (Albania context: university admissions and
   first-job CVs are where students need artifacts.)
3. **The sticker** — physical, mailed, collectible. Digital platforms cannot
   mail you anything; we can.
4. **Visible progress** — per-segment, per-week, per-sprint; the map fills in.
5. **The community** — Discord access, and later a build showcase.

**The one stick we allow:** the cohort clock. A cohort's lecture happens on a
date; complete the four weeks by then or join the next cohort. Deadlines
create completion; losing a streak creates guilt. We take the first, refuse
the second. **No leagues, no hearts, no daily-guilt notifications, no public
rankings. Ever.** (Human-factors section, below, makes this a requirement,
not a taste.)

---

## 2. Product principles

- **P1 — No volunteer graders.** Completion is verified by the platform
  (automatic) plus Free Focus's own people for capstones. Schools distribute
  and encourage; they do not administer. (John, 2026-09-05.)
- **P2 — The connection is the product.** Every feature serves the path from
  a student's effort to a real scientist's attention. Features that serve
  engagement-for-its-own-sake get cut.
- **P3 — Free for students, forever.** No paywalls, no premium tier.
- **P4 — Minors-safe by design.** Minimal data, parental consent, moderated
  spaces, no public student-to-student comparison.
- **P5 — Honest mechanics.** Nothing the pacing map, the checker, or a parent
  reading over a shoulder would embarrass us about.
- **P6 — Content stays static.** Lessons remain generated HTML (the
  build_lessons machinery). The app is a thin shell around them — auth,
  progress, cohorts — so content velocity never waits on app engineering.

## 3. Functional requirements

### 3.1 Accounts & identity
- **M** Sign in with Google (students already need Google accounts for
  Colab — one identity, no new passwords). Email+password fallback.
- **M** Minimal profile: display name, school (from a list), year. No
  addresses, no phone numbers. Stickers ship to schools, not homes.
- **M** Parental consent flow for students under the digital-consent age —
  consent link sent to a parent email, recorded with timestamp. (Exact age
  threshold: confirm against Albanian data-protection law — open question Q1.)
- **M** Roles: student · mentor (Free Focus) · speaker · admin.
- **S** School accounts: a teacher/director view of *their* students'
  aggregate progress (opt-in roster, no grades — counts only).

### 3.2 Progress & verification (replaces teacher grading)
- **M** Per-segment completion tracked server-side: quiz answers and figure
  interactions submit to the API (the current localStorage marks become
  authenticated events). Watch/listen/read marks stay self-attested — they
  are not the gate.
- **M** The gate per week = **check passed + build submitted**. Check
  questions grade automatically (they already have correct answers). Builds
  upload into the app (screenshot/notebook/text per lesson spec).
- **M** **Notebook completion codes**: the CHECK cells in each notebook are
  extended to print a short code derived from the student's app ID (entered
  once at the top of the notebook) + the notebook ID. Student pastes the code
  into the app; the API verifies. Offline-friendly, no notebook execution
  server needed, and gaming it requires more Python skill than the lesson
  teaches. (v2, **L**: server-side notebook execution for real autograding.)
- **M** Capstone builds (week 4 of each sprint) reviewed by a **Free Focus
  mentor** in an app queue — human eyes on the thing that earns the lecture,
  platform eyes on everything else. Review SLA target: 72h.
- **S** Anti-gaming posture, stated honestly: v1 optimizes for honest
  students (they are joining voluntarily for a lecture); audits sample
  submissions; getting caught forfeits the cohort. Not adversarial-proof and
  doesn't need to be yet.

### 3.3 Cohorts & lectures
- **M** Cohorts: named start dates per sprint ("Data Science — October
  cohort"), enrollment window, lecture date visible from day one (the healthy
  stick).
- **M** Lecture pipeline: completion list auto-generated → RSVP → join link
  issued only to completers → recording posted to all enrolled after.
- **M** Q&A submission before the lecture (moderated queue) + live questions.
- **S** Speaker view: who completed, their capstone highlights, submitted
  questions — so the speaker walks in knowing the room.
- **S** Missed-the-cutoff path: progress carries into the next cohort
  automatically. A missed week never zeroes anyone.

### 3.4 Rewards
- **M** Certificates: per-sprint, generated PDF + permanent verification URL
  (`/verify/<id>`), named signer. (Open question Q3: who signs.)
- **M** Sticker fulfillment workflow: batch per cohort, shipped to the
  school contact, handed out in person (a small ceremony beats an envelope).
- **S** Profile progress map: sprints as a fillable map — private by default,
  shareable by choice.
- **L** Build showcase: opt-in public gallery of capstones (Scratch lesson).

### 3.5 Community
- **M** Discord stays the community layer; the app gates invites (enrolled
  students only get the invite link) and displays the rules.
- **S** Per-cohort channels created/archived automatically.
- **L** In-app comments per lesson (only if Discord proves insufficient).

### 3.6 Admin & ops
- **M** Funnel dashboard: visits → signups → enrollments → week completions →
  capstones → lecture attendance, per cohort. (GoatCounter keeps counting
  pageviews; the app owns the authenticated funnel.)
- **M** Mentor queue (capstone review), moderation queue (Q&A, reports).
- **S** Content health: which check questions get failed most (bad question
  or bad teaching — either way, a signal the pacing map can't see).

## 4. Human-factors requirements

- **HF1 (M)** Motivation architecture is exactly the carrot stack in §1 —
  lecture, certificate, sticker, progress, community. The weekly rhythm is
  encouraged by the cohort calendar and a single optional weekly email.
  **Prohibited: daily streaks, guilt notifications, leagues, hearts, public
  rankings, decaying scores.**
- **HF2 (M)** Failure tolerance: every flow assumes a student who disappeared
  for two weeks and came back. Nothing shames; everything says "pick up
  where you left off"; progress carries across cohorts.
- **HF3 (M)** Safeguarding: named adult moderators; DMs from adults to
  students discouraged by policy and channel design; report button in app
  and Discord; recording policy (students on mic/camera only with consent —
  default is chat questions read by the moderator).
- **HF4 (M)** Data minimization: we can run the entire program knowing only
  name, school, year, email, progress. Collect nothing else. Deletion on
  request, actually implemented.
- **HF5 (M)** Language: UI chrome in English (matches the material), but the
  **join flow, parent consent, and rules pages exist in Albanian** — parents
  are the decision-makers and the trust surface.
- **HF6 (M)** Device floor: every app surface works on a phone; notebooks
  declare "needs a computer — school lab counts" honestly per lesson; the
  no-code sprints (5, 7) are first-class phone citizens and get recommended
  to phone-only students at signup.
- **HF7 (S)** Accessibility: the existing checker habits (contrast, keyboard,
  reduced motion) become requirements on app surfaces; reading-level pass on
  all UI copy.
- **HF8 (S)** Trust surface: About page with Free Focus registration
  details, the people (photos, real bios), partners, and the privacy policy
  in plain language, both languages.

## 5. Technical architecture (proposed, not locked)

- **Content plane (exists):** static generated lessons, GitHub Pages,
  unchanged. The app never blocks content.
- **App plane (new):** Firebase — Auth (Google + email), Firestore
  (users/enrollments/events/submissions/cohorts), Cloud Functions (API:
  completion codes, certificate generation, invite gating), Hosting for the
  app shell. Rationale: zero-ops, free tier covers pilot scale (hundreds of
  students), GCP-adjacent to PhotoApp experience. Alternative if we want to
  own more: Cloud Run + Cloud SQL, PhotoApp-style. Decision = open question
  Q4.
- **Auth bridge on lesson pages:** lessons stay static; a small JS include
  reads the session and POSTs segment events to the API when signed in;
  localStorage remains the fallback for anonymous visitors (try-before-join
  stays frictionless).
- **Completion codes:** HMAC(user_salt + notebook_id) truncated to 8 chars;
  the notebook's final CHECK cell prints it after all asserts pass; the API
  recomputes and verifies. No student data enters the notebook beyond the
  opaque salt they paste.
- **Data model sketch:** `users`, `consents`, `schools`, `cohorts`,
  `enrollments`, `progress_events`, `submissions` (build uploads + review
  state), `certificates`, `invites`.
- **Cost envelope:** pilot ≈ $0/mo (free tiers); 10k students ≈ low tens of
  $/mo. The expensive resource stays speaker time, not compute.

## 6. Phases

- **P0 — now (static):** Join page + call to action (email-based, ships
  today) · completion events wired to GoatCounter for a pre-app funnel ·
  About/trust page · Albanian parent letter. Unblocks: gaps 1 (partially),
  5, and measurement.
- **P1 — app MVP:** Auth, profiles, consent flow, enrollments, server-side
  segment tracking, build uploads, one cohort run end-to-end with mentor
  review. Exit criterion: one real cohort completes and gets its lecture
  with zero volunteer grading.
- **P2 — the engine:** completion codes in notebooks, certificates +
  verification URLs, sticker workflow, speaker view, funnel dashboard,
  Q&A pipeline.
- **P3 — scale:** school accounts, showcase, per-cohort Discord automation,
  server-side autograding, more cohorts in parallel.

## 7. Open questions (John)

- **Q1** Parental-consent age threshold under Albanian law — needs a real
  answer before P1 ships (counsel, or the local partner will know).
- **Q2** Discord vs in-app community for minors — Discord is where students
  are, but its minimum age is 13 and moderation is on us either way.
- **Q3** Who signs the certificates (Free Focus + the sprint's speaker?).
- **Q4** Firebase vs PhotoApp-style Cloud Run/SQL — comfort vs ops weight.
- **Q5** Pilot cohort: which sprint first, and target start date?
- **Q6** Does "no teacher grading" also mean no school involvement at all,
  or do schools stay as distribution + sticker-ceremony partners? (This doc
  assumes the latter.)
