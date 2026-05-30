import streamlit as st

# ── Page Config ─────────────────────────────────────────
st.set_page_config(
    page_title="Shinvi Nur Najmil Jannah — Portfolio",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ── Custom CSS ───────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,400&family=DM+Sans:wght@300;400;500&display=swap');

html, body, [class*="css"] {
  font-family: 'DM Sans', sans-serif;
}

/* Hide streamlit default elements */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }

/* ── HERO ── */
.hero {
  background: #0D0B18;
  background-image:
    radial-gradient(ellipse 80% 60% at 10% 20%, rgba(124,58,237,0.45) 0%, transparent 60%),
    radial-gradient(ellipse 60% 50% at 90% 80%, rgba(236,72,153,0.30) 0%, transparent 55%);
  padding: 5rem 8%;
  display: flex; align-items: center; justify-content: space-between;
  flex-wrap: wrap; gap: 2rem;
}
.hero-pill {
  display: inline-flex; align-items: center; gap: 0.5rem;
  font-size: 0.7rem; letter-spacing: 0.15em; text-transform: uppercase;
  color: #A78BFA; border: 1.5px solid rgba(167,139,250,0.35);
  padding: 0.4rem 1rem; border-radius: 20px; margin-bottom: 1.5rem;
  background: rgba(255,255,255,0.06);
}
.hero-dot { display:inline-block; width:8px; height:8px; border-radius:50%; background:#6EE7B7; margin-right:4px; }
.hero-name {
  font-family: 'Cormorant Garamond', serif;
  font-size: clamp(2.8rem, 5vw, 4.5rem); font-weight: 700;
  line-height: 1.05; color: #fff; margin: 0 0 0.75rem;
}
.hero-name em {
  font-style: italic; font-weight: 400;
  background: linear-gradient(135deg, #C084FC, #F472B6, #60A5FA);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
}
.hero-tagline {
  font-size: 0.78rem; letter-spacing: 0.12em; text-transform: uppercase;
  color: rgba(255,255,255,0.45); margin-bottom: 2rem; line-height: 1.85;
}
.hero-btn {
  display: inline-block; padding: 0.75rem 1.75rem; margin-right: 0.75rem; margin-bottom: 0.5rem;
  border-radius: 4px; font-size: 0.72rem; font-weight: 500;
  letter-spacing: 0.12em; text-transform: uppercase; text-decoration: none;
}
.btn-fill { background: linear-gradient(135deg,#7C3AED,#EC4899); color:#fff; }
.btn-ghost { border: 1.5px solid rgba(255,255,255,0.25); color:rgba(255,255,255,0.85); }
.hero-stat-box {
  display: flex; gap: 1rem; margin-top: 1rem; flex-wrap: wrap;
}
.stat {
  text-align: center;
  background: rgba(255,255,255,0.07);
  border: 1px solid rgba(255,255,255,0.12);
  border-radius: 12px; padding: 0.8rem 1.4rem;
}
.stat-num {
  font-family: 'Cormorant Garamond', serif; font-size: 1.6rem; font-weight: 700;
  background: linear-gradient(135deg,#C084FC,#F472B6);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
  line-height: 1;
}
.stat-lbl { font-size: 0.58rem; letter-spacing: 0.12em; text-transform: uppercase; color: rgba(255,255,255,0.4); }

/* ── SECTION BASE ── */
.section { padding: 5rem 8%; }
.section-light { background: #fff8f9; }
.section-dark  { background: #0f172a; }
.section-amber { background: #fffbf5; }
.section-teal  { background: #0a1628; }
.section-lav   { background: #f5f3ff; }
.section-midnight { background: #08051a; }

.eyebrow {
  font-size: 0.62rem; letter-spacing: 0.25em; text-transform: uppercase;
  color: #7C3AED; display: block; text-align: center; margin-bottom: 0.5rem;
}
.eyebrow-light { color: #A5B4FC; }
.eyebrow-teal  { color: #5EEAD4; }
.eyebrow-purple{ color: #A78BFA; }

.section-title {
  font-family: 'Cormorant Garamond', serif;
  font-size: clamp(2rem,4vw,3rem); font-weight: 700;
  text-align: center; line-height: 1.15; margin-bottom: 0.5rem;
}
.title-dark  { color: #0D0B18; }
.title-light { color: #fff; }

.divider {
  display: flex; align-items: center; gap: 1rem;
  max-width: 280px; margin: 0 auto 3rem;
}
.divider-line { flex:1; height:1px; background: rgba(124,58,237,0.15); }
.divider-gem  { width:7px; height:7px; background:#DDD6FE; transform:rotate(45deg); }

/* ── ABOUT ── */
.about-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 3rem; align-items: start; }
.about-para { font-size: 0.88rem; line-height: 1.95; color: #1E1B2E; margin-bottom: 1.2rem; }
.about-para strong { color: #7C3AED; }
.facts-grid {
  display: grid; grid-template-columns: 1fr 1fr; gap: 1px;
  background: rgba(124,58,237,0.12); border: 1px solid rgba(124,58,237,0.12);
  border-radius: 14px; overflow: hidden;
}
.fact { background: rgba(255,255,255,0.9); padding: 1rem 1.25rem; }
.fact-lbl { font-size: 0.6rem; letter-spacing: 0.18em; text-transform: uppercase; color: #A78BFA; margin-bottom: 0.3rem; }
.fact-val { font-size: 0.82rem; color: #1E1B2E; }

/* ── SKILLS ── */
.skills-grid { display: grid; grid-template-columns: repeat(2,1fr); gap: 1.5rem; }
.skill-card {
  background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.10);
  border-radius: 16px; padding: 2rem;
}
.skill-num {
  font-family: 'Cormorant Garamond', serif; font-size: 2.2rem; font-weight: 700;
  background: linear-gradient(135deg,#A5B4FC,#34D399);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
  margin-bottom: 0.75rem; line-height: 1;
}
.skill-name { font-size: 0.92rem; font-weight: 500; color: #e2e8f0; margin-bottom: 0.75rem; }
.skill-tags { display: flex; flex-wrap: wrap; gap: 0.4rem; }
.stag {
  font-size: 0.63rem; padding: 0.25rem 0.7rem; letter-spacing: 0.08em;
  border: 1px solid rgba(165,180,252,0.30); color: #a5b4fc;
  border-radius: 20px; background: rgba(99,102,241,0.15);
}

/* ── EXPERIENCE ── */
.exp-card {
  display: flex; gap: 1.5rem; align-items: flex-start;
  background: rgba(255,255,255,0.85); border: 1px solid rgba(245,158,11,0.18);
  border-radius: 16px; padding: 1.75rem; margin-bottom: 1.25rem;
}
.exp-num {
  width: 48px; height: 48px; border-radius: 12px; flex-shrink: 0;
  background: linear-gradient(135deg,#F59E0B,#EC4899);
  display: flex; align-items: center; justify-content: center;
  font-family: 'Cormorant Garamond', serif; font-size: 1.1rem; font-weight: 700; color: #fff;
}
.exp-role { font-size: 0.95rem; font-weight: 500; color: #0D0B18; margin-bottom: 0.25rem; }
.exp-place { font-size: 0.7rem; letter-spacing: 0.1em; text-transform: uppercase; color: #D97706; margin-bottom: 0.5rem; }
.exp-desc { font-size: 0.82rem; color: #6B7280; line-height: 1.85; }

/* ── PROJECTS ── */
.proj-grid { display: grid; grid-template-columns: repeat(3,1fr); gap: 1.5rem; }
.proj-card {
  background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.10);
  border-radius: 20px; overflow: hidden;
}
.proj-thumb {
  height: 130px; display: flex; align-items: center; justify-content: center;
  font-size: 3rem;
}
.pt1 { background: linear-gradient(135deg,#7C3AED,#06B6D4); }
.pt2 { background: linear-gradient(135deg,#0EA5E9,#14B8A6); }
.pt3 { background: linear-gradient(135deg,#6366F1,#7C3AED); }
.proj-body { padding: 1.25rem; }
.proj-tag { font-size: 0.6rem; letter-spacing: 0.15em; text-transform: uppercase; color: #5EEAD4; margin-bottom: 0.5rem; display: block; }
.proj-name { font-family: 'Cormorant Garamond', serif; font-size: 1.1rem; font-weight: 600; color: #f0fdf4; margin-bottom: 0.4rem; }
.proj-desc { font-size: 0.78rem; color: rgba(255,255,255,0.50); line-height: 1.75; }

/* ── EDUCATION ── */
.edu-timeline { border-left: 2px solid #DDD6FE; margin-left: 1.5rem; }
.edu-row {
  display: grid; grid-template-columns: 130px 1fr;
  gap: 1.5rem; padding: 1.5rem 1.5rem 1.5rem 2rem;
  position: relative; border-bottom: 1px solid rgba(124,58,237,0.10);
}
.edu-row:last-child { border-bottom: none; }
.edu-dot {
  position: absolute; left: -7px; top: 1.75rem;
  width: 12px; height: 12px; border-radius: 50%;
  background: #fff; border: 2.5px solid #7C3AED;
}
.edu-year { font-size: 0.7rem; letter-spacing: 0.1em; text-transform: uppercase; color: #A78BFA; padding-top: 3px; }
.edu-school { font-size: 0.95rem; font-weight: 500; color: #0D0B18; margin-bottom: 0.25rem; }
.edu-deg { font-size: 0.82rem; color: #6B7280; margin-bottom: 0.5rem; }
.edu-badge {
  display: inline-block; font-size: 0.6rem; letter-spacing: 0.1em; text-transform: uppercase;
  color: #7C3AED; border: 1px solid #DDD6FE; border-radius: 20px;
  padding: 0.2rem 0.75rem; background: #EDE9FE;
}

/* ── CONTACT ── */
.contact-grid { display: grid; grid-template-columns: repeat(2,1fr); gap: 1.25rem; }
.contact-card {
  display: flex; align-items: flex-start; gap: 1rem;
  background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.10);
  border-radius: 16px; padding: 1.5rem 1.75rem;
}
.contact-card a { color: #fff; text-decoration: none; }
.c-icon { font-size: 1.6rem; flex-shrink: 0; }
.c-lbl { font-size: 0.6rem; letter-spacing: 0.18em; text-transform: uppercase; color: #A78BFA; margin-bottom: 0.35rem; }
.c-val { font-size: 0.88rem; color: #fff; }

/* ── FOOTER ── */
.footer {
  background: #050311; text-align: center; padding: 2rem;
  font-size: 0.65rem; letter-spacing: 0.15em; text-transform: uppercase;
  color: rgba(255,255,255,0.22); border-top: 1px solid rgba(255,255,255,0.05);
}

/* Responsive */
@media (max-width: 768px) {
  .hero { padding: 4rem 5%; }
  .section { padding: 4rem 5%; }
  .about-grid, .skills-grid, .proj-grid, .contact-grid { grid-template-columns: 1fr; }
  .edu-row { grid-template-columns: 1fr; gap: 0.4rem; }
}
</style>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════
# NAVIGATION
# ══════════════════════════════════════════════════════
st.markdown("""
<style>
.nav {
  position: sticky; top: 0; z-index: 999;
  background: rgba(255,255,255,0.92); backdrop-filter: blur(20px);
  border-bottom: 1px solid rgba(124,58,237,0.1);
  display: flex; justify-content: space-between; align-items: center;
  padding: 0 8%; height: 60px;
}
.nav-logo { font-family:'Cormorant Garamond',serif; font-size:1.1rem; font-weight:600; color:#7C3AED; }
.nav-links a {
  font-size: 0.68rem; letter-spacing: 0.14em; text-transform: uppercase;
  color: #6B7280; text-decoration: none; margin-left: 1.75rem;
}
.nav-links a:hover { color: #7C3AED; }
</style>
<div class="nav">
  <span class="nav-logo">S · N · J</span>
  <div class="nav-links">
    <a href="#home">Home</a>
    <a href="#about">About</a>
    <a href="#skills">Skills</a>
    <a href="#experience">Experience</a>
    <a href="#projects">Projects</a>
    <a href="#education">Education</a>
    <a href="#contact">Contact</a>
  </div>
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════
# 01 HERO
# ══════════════════════════════════════════════════════
st.markdown('<div id="home"></div>', unsafe_allow_html=True)

col1, col2 = st.columns([1.2, 1])

with col1:
    st.markdown("""
    <div style="padding: 5rem 0 3rem 8%;">
      <div class="hero-pill"><span class="hero-dot"></span> Available for work</div>
      <h1 class="hero-name">Shinvi<br><em>Nur Najmil</em><br>Jannah</h1>
      <p class="hero-tagline">Informatics Engineering · Web Developer<br>Data Analyst · UI Designer</p>
      <a href="#projects" class="hero-btn btn-fill">View Projects</a>
      <a href="#contact" class="hero-btn btn-ghost">Get in Touch</a>
      <div class="hero-stat-box">
        <div class="stat"><div class="stat-num">3+</div><div class="stat-lbl">Projects</div></div>
        <div class="stat"><div class="stat-num">2+</div><div class="stat-lbl">Years Exp</div></div>
        <div class="stat"><div class="stat-num">4</div><div class="stat-lbl">Skills</div></div>
      </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="background:#0D0B18; min-height:500px; display:flex; align-items:center; justify-content:center;
      background-image: radial-gradient(ellipse 80% 60% at 10% 20%, rgba(124,58,237,0.45) 0%, transparent 60%),
      radial-gradient(ellipse 60% 50% at 90% 80%, rgba(236,72,153,0.30) 0%, transparent 55%);">
    """, unsafe_allow_html=True)

    try:
        st.image("profile.jpg", width=280)
    except:
        st.markdown("""
        <div style="text-align:center; padding:3rem;">
          <div style="width:200px; height:240px; margin:0 auto; border-radius:120px 120px 0 0;
            background: linear-gradient(160deg, rgba(124,58,237,0.5), rgba(236,72,153,0.35));
            display:flex; align-items:flex-end; justify-content:center; padding-bottom:1rem;">
            <span style="color:rgba(255,255,255,0.5); font-size:0.65rem; letter-spacing:2px;">ADD PHOTO</span>
          </div>
          <p style="color:rgba(255,255,255,0.3); font-size:0.7rem; margin-top:1rem;">
            Taruh file <code>profile.jpg</code> di folder yang sama dengan app.py
          </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# Download CV button
with open("cv-shinvi.pdf", "rb") if __import__('os').path.exists("cv-shinvi.pdf") else __import__('io').BytesIO(b"") as f:
    cv_data = f.read() if hasattr(f, 'read') else b""

import os
if os.path.exists("cv-shinvi.pdf"):
    with open("cv-shinvi.pdf", "rb") as f:
        st.download_button(
            label="⬇ Download CV",
            data=f,
            file_name="CV-Shinvi-Nur-Najmil-Jannah.pdf",
            mime="application/pdf"
        )


# ══════════════════════════════════════════════════════
# 02 ABOUT
# ══════════════════════════════════════════════════════
st.markdown('<div id="about"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section section-light">
  <span class="eyebrow">02 · About</span>
  <h2 class="section-title title-dark">Who I Am</h2>
  <div class="divider"><div class="divider-line"></div><div class="divider-gem"></div><div class="divider-line"></div></div>
  <div class="about-grid">
    <div>
      <p class="about-para">I am an <strong>Informatics Engineering</strong> student at Universitas Siliwangi with real hands-on experience in data analysis and web development.</p>
      <p class="about-para">I combine <strong>analytical thinking</strong> with technical skills to deliver structured and impactful digital solutions for every project I take on.</p>
      <p class="about-para">Active in organizational life — from <strong>Vice Chairman of Student Council</strong> to member of Himpunan Informatika — I bring leadership and collaboration to every team.</p>
      <p class="about-para">Early in my freelance journey, yet fully committed to quality, reliability, and continuous growth as a professional.</p>
    </div>
    <div class="facts-grid">
      <div class="fact"><div class="fact-lbl">Full Name</div><div class="fact-val">Shinvi Nur Najmil Jannah</div></div>
      <div class="fact"><div class="fact-lbl">Born</div><div class="fact-val">Ciamis, 08 Jan 2005</div></div>
      <div class="fact"><div class="fact-lbl">Location</div><div class="fact-val">Ciamis, West Java</div></div>
      <div class="fact"><div class="fact-lbl">Religion</div><div class="fact-val">Islam</div></div>
      <div class="fact"><div class="fact-lbl">University</div><div class="fact-val">Universitas Siliwangi</div></div>
      <div class="fact"><div class="fact-lbl">Status</div><div class="fact-val">Active Student '23</div></div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════
# 03 SKILLS
# ══════════════════════════════════════════════════════
st.markdown('<div id="skills"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section section-dark">
  <span class="eyebrow eyebrow-light">03 · Skills</span>
  <h2 class="section-title title-light">Expertise</h2>
  <div class="divider"><div class="divider-line" style="background:rgba(255,255,255,0.12)"></div><div class="divider-gem" style="background:rgba(165,180,252,0.4)"></div><div class="divider-line" style="background:rgba(255,255,255,0.12)"></div></div>
  <div class="skills-grid">
    <div class="skill-card">
      <div class="skill-num">01</div>
      <div class="skill-name">Web Development</div>
      <div class="skill-tags"><span class="stag">HTML</span><span class="stag">CSS</span><span class="stag">JavaScript</span><span class="stag">Responsive</span></div>
    </div>
    <div class="skill-card">
      <div class="skill-num">02</div>
      <div class="skill-name">Data Analysis</div>
      <div class="skill-tags"><span class="stag">Python</span><span class="stag">SQL</span><span class="stag">Excel</span><span class="stag">Visualization</span></div>
    </div>
    <div class="skill-card">
      <div class="skill-num">03</div>
      <div class="skill-name">Content & Research</div>
      <div class="skill-tags"><span class="stag">Writing</span><span class="stag">Research</span><span class="stag">Market Analysis</span></div>
    </div>
    <div class="skill-card">
      <div class="skill-num">04</div>
      <div class="skill-name">Design Tools</div>
      <div class="skill-tags"><span class="stag">Canva</span><span class="stag">Figma</span><span class="stag">UI/UX</span></div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════
# 04 EXPERIENCE
# ══════════════════════════════════════════════════════
st.markdown('<div id="experience"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section section-amber">
  <span class="eyebrow">04 · Experience</span>
  <h2 class="section-title title-dark">Work History</h2>
  <div class="divider"><div class="divider-line"></div><div class="divider-gem"></div><div class="divider-line"></div></div>
  <div class="exp-card">
    <div class="exp-num">01</div>
    <div>
      <div class="exp-role">Data Analyst Staff</div>
      <div class="exp-place">SMA Ibnu Siena Tasikmalaya</div>
      <div class="exp-desc">Responsible for collecting, processing, and analyzing school data to produce structured reports supporting informed decision-making.</div>
    </div>
  </div>
  <div class="exp-card">
    <div class="exp-num">02</div>
    <div>
      <div class="exp-role">Web Designer — Automotive Sales Website</div>
      <div class="exp-place">Freelance / Personal Project</div>
      <div class="exp-desc">Designed and developed a car sales website with a clean, user-friendly interface featuring product listings and a fully responsive layout.</div>
    </div>
  </div>
  <div class="exp-card">
    <div class="exp-num">03</div>
    <div>
      <div class="exp-role">Web Developer — Room Monitoring System</div>
      <div class="exp-place">Academic / Personal Project</div>
      <div class="exp-desc">Built a web-based system to monitor room temperature, humidity, and energy data with real-time data visualization.</div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════
# 05 PROJECTS
# ══════════════════════════════════════════════════════
st.markdown('<div id="projects"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section section-teal">
  <span class="eyebrow eyebrow-teal">05 · Projects</span>
  <h2 class="section-title title-light">Featured Work</h2>
  <div class="divider"><div class="divider-line" style="background:rgba(255,255,255,0.12)"></div><div class="divider-gem" style="background:rgba(94,234,212,0.4)"></div><div class="divider-line" style="background:rgba(255,255,255,0.12)"></div></div>
  <div class="proj-grid">
    <div class="proj-card">
      <div class="proj-thumb pt1">🚗</div>
      <div class="proj-body">
        <span class="proj-tag">Web Development</span>
        <div class="proj-name">Automotive Sales Website</div>
        <div class="proj-desc">A responsive car sales platform with product listings and intuitive navigation.</div>
      </div>
    </div>
    <div class="proj-card">
      <div class="proj-thumb pt2">🌡️</div>
      <div class="proj-body">
        <span class="proj-tag">Data Visualization</span>
        <div class="proj-name">Room Monitoring System</div>
        <div class="proj-desc">Real-time monitoring for room temperature, humidity, and energy with live visualization.</div>
      </div>
    </div>
    <div class="proj-card">
      <div class="proj-thumb pt3">📊</div>
      <div class="proj-body">
        <span class="proj-tag">Data Analysis</span>
        <div class="proj-name">School Data Analysis</div>
        <div class="proj-desc">Comprehensive data analysis at SMA Ibnu Siena producing structured decision-making reports.</div>
      </div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════
# 06 EDUCATION
# ══════════════════════════════════════════════════════
st.markdown('<div id="education"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section section-lav">
  <span class="eyebrow">06 · Education</span>
  <h2 class="section-title title-dark">Academic Background</h2>
  <div class="divider"><div class="divider-line"></div><div class="divider-gem"></div><div class="divider-line"></div></div>
  <div class="edu-timeline">
    <div class="edu-row">
      <div class="edu-dot"></div>
      <div class="edu-year">2023 — Present</div>
      <div><div class="edu-school">Universitas Siliwangi, Tasikmalaya</div><div class="edu-deg">S1 Informatics Engineering</div><span class="edu-badge">Himpunan Informatika</span></div>
    </div>
    <div class="edu-row">
      <div class="edu-dot"></div>
      <div class="edu-year">2020 — 2023</div>
      <div><div class="edu-school">SMAN 1 Ciamis</div><div class="edu-deg">Senior High School — Science (IPA)</div></div>
    </div>
    <div class="edu-row">
      <div class="edu-dot"></div>
      <div class="edu-year">2017 — 2020</div>
      <div><div class="edu-school">SMPN 1 Cikoneng</div><div class="edu-deg">Junior High School</div><span class="edu-badge">Vice Chairman of OSIS</span></div>
    </div>
    <div class="edu-row">
      <div class="edu-dot"></div>
      <div class="edu-year">2011 — 2017</div>
      <div><div class="edu-school">MI Cisaray</div><div class="edu-deg">Elementary School</div></div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════
# 07 CONTACT
# ══════════════════════════════════════════════════════
st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section section-midnight">
  <span class="eyebrow eyebrow-purple">07 · Contact</span>
  <h2 class="section-title title-light">Let's Work Together</h2>
  <p style="text-align:center; color:rgba(255,255,255,0.45); font-size:0.88rem; margin-bottom:3rem;">
    Open to freelance projects, collaboration, and new opportunities.
  </p>
  <div class="divider"><div class="divider-line" style="background:rgba(255,255,255,0.12)"></div><div class="divider-gem" style="background:rgba(167,139,250,0.4)"></div><div class="divider-line" style="background:rgba(255,255,255,0.12)"></div></div>
  <div class="contact-grid">
    <div class="contact-card">
      <div class="c-icon">📱</div>
      <div><div class="c-lbl">Phone / WhatsApp</div><div class="c-val"><a href="https://wa.me/6288102215118" target="_blank">+62 881-0221-51118</a></div></div>
    </div>
    <div class="contact-card">
      <div class="c-icon">✉️</div>
      <div><div class="c-lbl">Email</div><div class="c-val"><a href="mailto:shinviiiiii@gmail.com">shinviiiiii@gmail.com</a></div></div>
    </div>
    <div class="contact-card">
      <div class="c-icon">📍</div>
      <div><div class="c-lbl">Location</div><div class="c-val">Ciamis, West Java, Indonesia</div></div>
    </div>
    <div class="contact-card">
      <div class="c-icon">💼</div>
      <div><div class="c-lbl">Availability</div><div class="c-val">Available for hire</div></div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)


# ── FOOTER ──
st.markdown("""
<div class="footer">
  © 2026 · Shinvi Nur Najmil Jannah · Informatics Engineering · Universitas Siliwangi
</div>
""", unsafe_allow_html=True)
