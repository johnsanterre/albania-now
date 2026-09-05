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
| **Wordle** | One daily puzzle, same for everyone; the emoji-grid share card — low-effort, intriguing, shows off without explaining | None | The canonical viral loop: a **share artifact** with a **shared daily context** and a minutes-long cycle. **Borrow all three — this is the growth model (§4).** |
| **Chess.com / multiplayer games** | Playing requires a second person — growth is built into use | Rating anxiety | The multiplayer lesson without the ratings: **crews** (§4). A crew that needs a fourth member is a recruitment engine. |

**The carrot stack we choose (in order of power):**
0. *(acquisition layer)* **The challenge + share card** — five minutes of
   cleverness, displayable. Not a reason to stay; the reason a friend arrives.
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

**The organizing frame — one destination, many doors (John, 2026-09-05).**
The destination is always the same: a student's effort earning a real
scientist's attention. The doors are shaped differently because students
are:

| Door | Shape | Who walks through it |
|---|---|---|
| Sprints | class-shaped | students who want a path and a finish line |
| Challenges & playables | game-shaped | students who'd never enroll but will play |
| The lecture & ceremonies | event-shaped | students moved by occasions and access |
| Discord & crews | community-shaped | students who come because a friend is here |

Every door funnels toward the same destination; no door is a dead end.
Features get judged by which door they widen.

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

## 4. Growth-loop requirements

**The honest premise (2026-09-05 assessment):** as first designed, the program
was single-player with private rewards and a month-long cycle — K-factor zero
by construction. It would grow like Khan Academy: institutionally, over
years. These requirements add the game-shaped growth layer. The target is
not global virality: the addressable population is ~130–150k Albanian
high-schoolers, so "viral" means **K > 1 inside school social networks plus
one national media moment** — that is saturation.

**Guardrails first (these bind every G-requirement):** growth mechanics obey
HF1's prohibitions — no guilt streaks, no daily-nag notifications, no public
student rankings. Shares are always pull-based: the student chooses to
share; nothing auto-posts. Share artifacts contain **no PII by default** (no
names, no school unless the student adds them). We never request contact-list
access, ever.

- **G1 (M) The share card.** Every showable figure result — the transit
  detection, the crater count, a trace-puzzle score — generates a one-tap
  share image: result + visual + link (with attribution params). Built
  mobile-first for Instagram stories, WhatsApp class groups, and TikTok —
  where Albanian teens actually are. Web Share API + canvas render; server
  OG-image renderer later. Metric: cards created → link visits → joins.
- **G2 (M) The challenge — the five-minute front door.** A standing
  challenge, **same instance for everyone** (date-seeded — shared context is
  what makes the share intriguing): trace this code, spot the chart's lie,
  read this spectrum, find the dip. Drawn from the existing figure engine;
  complete-or-not today, **streak-free by design**. Completion offers the
  share card and the funnel line: "this is five minutes of week 1 —
  the sprint is the real thing." Cadence: weekly at launch, daily when the
  instance bank is deep enough.
- **G3 (M) Crews.** Students join as self-formed crews of 3–5. Crew
  completion = every member completes the sprint; crew rewards are
  crew-shaped: the crew sticker set, recognition at the lecture, the crew
  photo moment with the speaker. The mechanic's real job: a crew that needs
  a fourth member recruits one. Constraints: minimum size 3 (no 1-on-1
  pressure), leaving a crew is one click and costs no personal progress,
  crew-internal progress is visible to the crew only, and crews are never
  ranked against each other publicly.
- **G4 (S) Referral, both-sides, non-monetary.** Personal invite link; when
  the invitee completes week 1, both sides earn — a priority question slot
  at the lecture, a bonus sticker. Credit capped (~5 per student) so it
  stays a friend mechanic, not a spam mechanic.
- **G5 (M) The school-pride surface.** A public wall: **schools by completer
  count** — schools compete, students never (consistent with the
  no-student-ranking rule). Plus an opt-in completer wall per cohort (first
  names + school only). Inter-school pride is real fuel in Albania; this is
  the sanctioned outlet for competition.
- **G6 (S) Public recordings as the FOMO engine.** Lecture recordings fully
  public and promoted, with 60–90-second highlight clips cut for social.
  The live room stays earned — outsiders see exactly what they missed and
  exactly how to earn it.
- **G7 (S) The media moment.** "NASA's Titan scientist lectures Albanian
  teenagers who did the work" is a national news story in a 2.7M-person
  country. Product-side requirement: the site must absorb a spike (static —
  already true) and the join flow must capture it. Program-side: a launch
  kit (Albanian + English press release, speaker quotes, photos) timed to
  the first cohort's lecture — owner: Free Focus + the local partner.
- **G8 (M) Growth instrumentation.** The funnel dashboard (§3.6) extends to
  a K-factor proxy: share-card views → attributed visits → joins; referral
  conversion; challenge participation. If we can't measure the loop, we
  can't tune it.
- **G9 Playables — standalone programming games.** (Added 2026-09-05 from
  the CodeCombat-genre survey.) Lessons taken: CodeCombat's
  code-with-visible-consequence (not its asset-heavy fantasy), Human
  Resource Machine's instruction-set-as-movement, Zachtronics' honest
  compare (histogram of your solution vs the world, shown only AFTER
  solving — leaderboard energy without ranking children), SQL Murder
  Mystery's narrative wrapper (the cheapest proven viral format in the
  genre), Untrusted's read-code-to-escape. Two binding design rules:
  **solve first, optimize second** (struggle private, mastery shareable),
  and **every game ends in the funnel line** ("this was five minutes of
  sprint X, week N") — or it's decoration.
  - **Tier 1 (M — client-only, existing figure engine):** *Trace Race* —
    daily Wordle-of-code-reading, emoji-grid trace share (the G2 flagship);
    *Crater Hunter* — daily seeded terrain, 3 tries, found-minus-junk score;
    *Find the Lie* — swipe honest/lying charts, phone-native.
  - **Tier 2 (S):** *The Eagle's Flight* — Lightbot-shaped: Python-ish
    commands steer the eagle over a map of Albania; instruction-count
    compare as the share; the national symbol writing its own flight plan —
    highest kid-appeal ceiling; *Bigram Band* — the existing browser tiny-LM
    as a toy: train on your own words, share the funniest generated
    sentence.
  - **Tier 3 (L — Pyodide or backend):** *The Byrek Mystery* (SQL Murder
    Mystery, pandas edition, on our Tirana shop data); *Escape the
    Notebook* (rooms opened by fixing buggy code); *Crew Code Battles*
    (crews submit strategies, weekly simulated battles, shareable replays —
    the multiplayer growth engine).

## 5. Live operations — the playbook (added 2026-09-05)

Viral platforms win as much by *operations* as by features: synchronized
calendars, predictable rituals, event engineering, community ladders, and
weekly telemetry discipline. These are operating commitments, not code.

### 5.1 Seasons, not rolling cohorts *(source: games-as-service — Fortnite et al.)*
Cohorts across all sprints align to one named **season** ("Autumn 2026")
with a shared finale week — every sprint's lecture lands in the same few
days, so the whole community peaks together and the press moment has mass.
Season-unique sticker designs that never return (scarcity drives
cross-season collection); certificates numbered within season ("completer
#47, Founding Season" — founding status is a permanent good we can only
mint once). Lapsed students re-enter at any season boundary with progress
carried.

### 5.2 The weekly ritual *(source: patch-day culture, Wordle's daily sync)*
Predictability builds habit without streak-guilt: **Monday** the challenge
drops (same instance for everyone), **Wednesday** a community moment in
Discord (mentor office hour, mini-AMA), **Friday** the recap post (best
share cards, school wall movement, next week's tease). Students learn the
rhythm; nothing nags them.

### 5.3 Events as the growth engine *(source: live-event spikes)*
The lecture is operated as an event with a runway, not a calendar entry:
T-7 days question submissions open; T-1 reminder with the completer count;
schools encouraged to host **watch parties** (the projector in the lab —
a completer's plus-ones can watch, only completers ask questions); within
24h the highlight clips ship to social. Occasional limited-time specials
between seasons ("Planet Hunt Weekend") reuse existing material as events.

### 5.4 The people ladder *(source: Roblox/Reddit/fCC community ladders; the indie-dev-replies effect)*
Completers become the operation: **crew captain** (self-appointed at crew
formation) → **school ambassador** (named role, role sticker, early access
to new sprints) → **volunteer mentor** (post-completion, helps in Discord,
feeds the capstone-review queue under Free Focus supervision). Albanian-
speaking moderation from day one comes from this ladder, not from hiring.
And the highest-leverage 15 minutes in the whole operation: each sprint's
speaker drops one short async reply-round in Discord mid-sprint — "the
scientist answered me" is the single most shareable moment we can
manufacture, and it costs a coffee break.

### 5.5 Onboarding as an operational metric *(source: D1-retention discipline)*
Standing rule: every landing path reaches an interactive moment in **under
60 seconds** — the challenge lives on the homepage, not behind navigation.
Day-1 and week-1 return are measured and reviewed. And the **seeded-room
rule**: no public launch until 10–20 founding students are already active
in Discord — nobody joins an empty server. Pilot school = closed beta;
public launch timed to the first finale, not the first upload.

### 5.6 The telemetry ritual *(source: weekly live-ops reviews)*
A 30-minute weekly ops review, non-negotiable: K-proxy, funnel stages,
challenge participation, D1/W1, school wall movement. The report is
auto-generated (the funnel dashboard's job); the meeting decides one thing
per week — what to boost, what to kill. Each season ends with a retro that
feeds the next season's content priorities alongside the pacing map.

### 5.7 Re-engagement, respectfully *(source: what good win-back looks like)*
One email per season boundary to lapsed students: what's new, progress
carried, next season's date. No guilt mechanics, no "we miss you" drip —
the season calendar itself is the re-entry point.

## 6. Human-factors requirements

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

## 7. Technical architecture (proposed, not locked)

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
  state), `certificates`, `invites` — plus, for the growth layer: `crews`,
  `referrals`, `challenge_results`, `share_events`.
- **Compute budget (2026-09-05; assumes material creation is free — LLMs +
  volunteers + John).** Ranges, not promises; the LLM line dominates and is
  a policy choice:
  - Static hosting (GitHub Pages) + domain: **$0** (owned).
  - App plane (Firebase/equivalent): pilot ≤1k students **$0–10/mo**;
    ~10k active **$25–100/mo**; national saturation **$200–500/mo**.
  - LLM usage — the swing line. If LLM feedback is rationed to capstones
    only (recommended): pilot **$10–50/mo**, 10k active **$100–300/mo**.
    If every build gets LLM feedback: multiply by ~5–10. Class-key
    lessons (course-5 style) ride teacher/cohort keys and stay small.
  - Lecture streaming: **$0–15/mo** (YouTube Live / Zoom tier).
  - Email/notifications: **$0** early, **$10–30/mo** at scale.
  - **Bottom line: pilot ≈ $0–75/mo; 10k active ≈ $150–450/mo; national
    scale ≈ $500–2,000/mo worst case.** Stickers are physical, not compute
    (~$0.50–1 per sticker plus batch shipping to schools), budgeted
    separately. The scarce resources remain speaker hours and moderation —
    which is where volunteers and LLMs are aimed, not where money is.

## 8. Phases

- **P0 — now (static):** Join page + call to action (shipped 2026-09-05) ·
  completion events wired (shipped) · About/trust page · Albanian parent
  letter · **challenge v0** (date-seeded, client-only, from the figure
  engine) · **share-card v0** on the two most showable figures (transit
  finder, trace puzzle) with attribution params. Unblocks: gaps 1
  (partially), 5, measurement, and the first real test of the growth
  thesis — all before any backend exists.
- **P1 — app MVP:** Auth, profiles, consent flow, enrollments, server-side
  segment tracking, build uploads, one cohort run end-to-end with mentor
  review · **crews** (formation, crew view, crew rewards) · **referral
  links** · **school-pride wall** (opt-in). Exit criterion: one real cohort
  completes and gets its lecture with zero volunteer grading — and the
  measured share→join funnel is nonzero.
- **P2 — the engine:** completion codes in notebooks, certificates +
  verification URLs, sticker workflow, speaker view, Q&A pipeline · **growth
  dashboard with K-proxy** · server OG-image share renderer · highlight-clip
  pipeline for public recordings.
- **P3 — scale:** school accounts, showcase, per-cohort Discord automation,
  server-side autograding, more cohorts in parallel · daily challenge
  cadence once the instance bank supports it.

## 9. Open questions (John)

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
- **Q7** Crew rewards: what does a completing crew actually get, and what's
  the budget? (The crew photo with the speaker costs nothing and might be
  the strongest one.)
- **Q8** Public-wall consent granularity: first name + school, or school
  counts only? (This doc proposes both, opt-in per student.)
- **Q9** Who owns the media/launch kit, and with which local partner's name
  on it? (A Free Focus press release lands differently than one co-signed
  by an Albanian institution.)
- **Q10** Challenge cadence at launch: weekly (sustainable now) vs daily
  (stronger habit, needs a deep instance bank). This doc says weekly first.
