import streamlit as st
import os, base64

st.set_page_config(
    page_title="Shinvi Nur Najmil Jannah — Portfolio",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ── helpers ─────────────────────────────────────────────
def to_b64(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return None

photo_b64 = to_b64("profile.jpg")
cv_b64    = to_b64("cv-shinvi.pdf")

photo_tag = (
    f'<img src="data:image/jpeg;base64,{photo_b64}" class="hero-photo" />'
    if photo_b64 else
    '<div class="hero-photo-avatar"><span style="font-size:4rem;">👩</span><p>Taruh profile.jpg</p></div>'
)

cv_btn = (
    f'<a href="data:application/pdf;base64,{cv_b64}" download="CV-Shinvi.pdf" class="btn-cv">⬇ Download CV</a>'
    if cv_b64 else ""
)

# ── CSS (mirrors the HTML version) ──────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,400&family=DM+Sans:wght@300;400;500&display=swap');

:root {
  --purple:#7C3AED; --purple-lt:#A78BFA; --purple-dim:#DDD6FE;
  --pink:#EC4899; --blue:#3B82F6; --teal:#14B8A6;
  --dark:#0D0B18; --text:#1E1B2E; --muted:#6B7280;
  --amber:#F59E0B;
}
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html, body, [class*="css"], [data-testid="stAppViewContainer"] {
  font-family: 'DM Sans', sans-serif !important;
}
#MainMenu, footer, header,
[data-testid="stToolbar"], [data-testid="stDecoration"],
[data-testid="stStatusWidget"], [data-testid="stSidebarNav"] { display:none !important; }
.block-container { padding: 0 !important; max-width: 100% !important; }
[data-testid="stAppViewContainer"] { background: var(--dark); }
section[data-testid="stMain"] { padding: 0 !important; }

/* ══ NAV ══ */
.navbar {
  position: sticky; top: 0; z-index: 999;
  background: rgba(255,255,255,0.92); backdrop-filter: blur(20px);
  border-bottom: 1px solid rgba(124,58,237,0.1);
  display: flex; justify-content: space-between; align-items: center;
  padding: 0 6%; height: 62px;
}
.nav-logo { font-family:'Cormorant Garamond',serif; font-size:1.1rem; font-weight:600; color:var(--purple); letter-spacing:0.05em; }
.nav-links a { font-size:0.68rem; letter-spacing:0.14em; text-transform:uppercase; color:var(--muted); text-decoration:none; margin-left:1.75rem; transition:color 0.2s; }
.nav-links a:hover { color:var(--purple); }

/* ══ HERO ══ */
.hero {
  background: var(--dark);
  background-image:
    radial-gradient(ellipse 80% 60% at 10% 20%, rgba(124,58,237,0.45) 0%, transparent 60%),
    radial-gradient(ellipse 60% 50% at 90% 80%, rgba(236,72,153,0.30) 0%, transparent 55%),
    radial-gradient(ellipse 50% 40% at 55% 50%, rgba(59,130,246,0.15) 0%, transparent 60%);
  min-height: 100vh;
  display: grid; grid-template-columns: 1fr 1fr;
  align-items: center; gap: 2rem;
  padding: 5.5rem 6% 3.5rem;
  position: relative; overflow: hidden;
}
.hero::before {
  content:''; position:absolute; width:480px; height:480px; border-radius:50%;
  background:radial-gradient(circle,rgba(124,58,237,0.30) 0%,transparent 70%);
  top:-100px; left:-80px; pointer-events:none;
}
.hero::after {
  content:''; position:absolute; width:360px; height:360px; border-radius:50%;
  background:radial-gradient(circle,rgba(236,72,153,0.22) 0%,transparent 70%);
  bottom:-60px; right:-60px; pointer-events:none;
}
.hero-left { position:relative; z-index:1; }
.hero-pill {
  display:inline-flex; align-items:center; gap:0.5rem;
  font-size:0.68rem; letter-spacing:0.15em; text-transform:uppercase;
  color:var(--purple-lt); border:1.5px solid rgba(167,139,250,0.35);
  padding:0.4rem 1rem; border-radius:20px; margin-bottom:1.5rem;
  background:rgba(255,255,255,0.06);
}
.hero-dot { display:inline-block; width:7px; height:7px; border-radius:50%; background:#6EE7B7; box-shadow:0 0 7px #6EE7B7; }
.hero-name {
  font-family:'Cormorant Garamond',serif;
  font-size: clamp(3rem, 5.5vw, 5rem); font-weight:700;
  line-height:1.05; color:#fff; margin-bottom:0.75rem;
}
.hero-name em {
  font-style:italic; font-weight:400;
  background:linear-gradient(135deg,#C084FC,#F472B6,#60A5FA);
  -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text;
}
.hero-tagline {
  font-size:0.77rem; letter-spacing:0.13em; text-transform:uppercase;
  color:rgba(255,255,255,0.42); margin-bottom:2rem; line-height:2;
}
.hero-btns { display:flex; gap:0.75rem; flex-wrap:wrap; margin-bottom:2rem; }
.btn-fill {
  display:inline-block; padding:0.78rem 1.8rem;
  background:linear-gradient(135deg,var(--purple),var(--pink));
  color:#fff !important; font-size:0.71rem; font-weight:500;
  letter-spacing:0.12em; text-transform:uppercase; border-radius:4px;
  text-decoration:none !important; box-shadow:0 4px 20px rgba(124,58,237,0.40);
}
.btn-ghost {
  display:inline-block; padding:0.78rem 1.8rem;
  border:1.5px solid rgba(255,255,255,0.22); color:rgba(255,255,255,0.82) !important;
  font-size:0.71rem; font-weight:500; letter-spacing:0.12em; text-transform:uppercase;
  border-radius:4px; text-decoration:none !important; background:rgba(255,255,255,0.06);
}
.btn-cv {
  display:inline-flex; align-items:center; gap:0.45rem; padding:0.78rem 1.5rem;
  border:1.5px solid rgba(255,255,255,0.20); color:rgba(255,255,255,0.78) !important;
  font-size:0.71rem; font-weight:500; letter-spacing:0.12em; text-transform:uppercase;
  border-radius:4px; text-decoration:none !important; background:rgba(255,255,255,0.07);
}

/* ══ HERO RIGHT — photo frame ══ */
.hero-right { display:flex; flex-direction:column; align-items:center; gap:1.75rem; position:relative; z-index:1; }
.hero-photo-wrap { position:relative; width:300px; height:380px; }
.hero-photo-bg {
  position:absolute; inset:0; border-radius:180px 180px 0 0;
  background:linear-gradient(160deg,rgba(124,58,237,0.55),rgba(236,72,153,0.40));
  box-shadow:0 0 70px rgba(124,58,237,0.50),0 0 130px rgba(236,72,153,0.25);
}
.hero-photo {
  position:absolute; bottom:0; left:50%; transform:translateX(-50%);
  width:278px; height:360px;
  object-fit:cover; object-position:top center;
  border-radius:160px 160px 0 0;
}
.hero-photo-avatar {
  position:absolute; bottom:0; left:50%; transform:translateX(-50%);
  width:278px; height:360px; border-radius:160px 160px 0 0;
  background:linear-gradient(160deg,rgba(124,58,237,0.35),rgba(59,130,246,0.25));
  display:flex; flex-direction:column; align-items:center; justify-content:center;
  color:rgba(255,255,255,0.5); font-size:0.7rem; text-align:center; gap:0.5rem;
}

/* Stats */
.hero-stats { display:flex; gap:1.1rem; }
.stat {
  text-align:center; background:rgba(255,255,255,0.07);
  border:1px solid rgba(255,255,255,0.12); border-radius:12px; padding:0.8rem 1.3rem;
  backdrop-filter:blur(8px);
}
.stat-num {
  font-family:'Cormorant Garamond',serif; font-size:1.55rem; font-weight:700;
  background:linear-gradient(135deg,#C084FC,#F472B6);
  -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text; line-height:1;
}
.stat-lbl { font-size:0.58rem; letter-spacing:0.13em; text-transform:uppercase; color:rgba(255,255,255,0.35); margin-top:0.2rem; }

/* ══ SECTION SHELLS ══ */
.section { padding: 6.5rem 6%; }
.sec-about {
  background:#fff8f9;
  background-image:radial-gradient(ellipse 70% 55% at 5% 10%,rgba(251,207,232,0.70) 0%,transparent 55%),
    radial-gradient(ellipse 60% 50% at 95% 90%,rgba(221,214,254,0.60) 0%,transparent 55%);
}
.sec-skills {
  background:#0f172a;
  background-image:radial-gradient(ellipse 75% 55% at 15% 25%,rgba(99,102,241,0.40) 0%,transparent 60%),
    radial-gradient(ellipse 60% 50% at 85% 75%,rgba(20,184,166,0.35) 0%,transparent 55%);
}
.sec-exp {
  background:#fffbf5;
  background-image:radial-gradient(ellipse 70% 55% at 90% 10%,rgba(253,186,116,0.50) 0%,transparent 55%),
    radial-gradient(ellipse 55% 45% at 5% 85%,rgba(251,207,232,0.55) 0%,transparent 55%);
}
.sec-projects {
  background:#0a1628;
  background-image:radial-gradient(ellipse 70% 55% at 80% 15%,rgba(20,184,166,0.35) 0%,transparent 58%),
    radial-gradient(ellipse 60% 45% at 10% 80%,rgba(59,130,246,0.30) 0%,transparent 55%);
}
.sec-education {
  background:#f5f3ff;
  background-image:radial-gradient(ellipse 65% 50% at 0% 0%,rgba(221,214,254,0.80) 0%,transparent 55%),
    radial-gradient(ellipse 60% 50% at 100% 100%,rgba(199,210,254,0.70) 0%,transparent 55%);
}
.sec-contact {
  background:#08051a;
  background-image:radial-gradient(ellipse 70% 55% at 20% 20%,rgba(124,58,237,0.45) 0%,transparent 60%),
    radial-gradient(ellipse 60% 50% at 85% 80%,rgba(236,72,153,0.30) 0%,transparent 55%);
}

/* eyebrow / title / divider */
.eyebrow { font-size:.62rem; letter-spacing:.25em; text-transform:uppercase; display:block; text-align:center; margin-bottom:.5rem; }
.ey-p { color:var(--purple); } .ey-l { color:#A5B4FC; } .ey-t { color:#5EEAD4; } .ey-a { color:#D97706; } .ey-pk { color:var(--purple-lt); }
.sec-title { font-family:'Cormorant Garamond',serif; font-size:clamp(2rem,4vw,3rem); font-weight:700; text-align:center; line-height:1.15; margin-bottom:.5rem; }
.t-d { color:var(--dark); } .t-l { color:#fff; }
.divider { display:flex; align-items:center; gap:1rem; max-width:280px; margin:0 auto 3rem; }
.dl { flex:1; height:1px; } .dl-d { background:rgba(124,58,237,.15); } .dl-l { background:rgba(255,255,255,.12); }
.dg { width:7px; height:7px; transform:rotate(45deg); } .dg-p { background:#DDD6FE; } .dg-l { background:rgba(165,180,252,.4); } .dg-t { background:rgba(94,234,212,.4); }

/* About */
.about-grid { display:grid; grid-template-columns:1fr 1fr; gap:3.5rem; align-items:start; }
.about-para { font-size:.88rem; line-height:1.95; color:var(--text); margin-bottom:1.2rem; }
.about-para strong { color:var(--purple); }
.facts-grid { display:grid; grid-template-columns:1fr 1fr; gap:1px; background:rgba(124,58,237,.12); border:1px solid rgba(124,58,237,.12); border-radius:14px; overflow:hidden; box-shadow:0 4px 16px rgba(124,58,237,.08); }
.fact { background:rgba(255,255,255,.9); padding:1rem 1.25rem; }
.fact-lbl { font-size:.6rem; letter-spacing:.18em; text-transform:uppercase; color:var(--purple-lt); margin-bottom:.3rem; }
.fact-val { font-size:.82rem; color:var(--text); }

/* Skills */
.skills-grid { display:grid; grid-template-columns:repeat(2,1fr); gap:1.5rem; }
.skill-card { background:rgba(255,255,255,.06); border:1px solid rgba(255,255,255,.10); border-radius:16px; padding:2rem; }
.skill-num { font-family:'Cormorant Garamond',serif; font-size:2.2rem; font-weight:700; background:linear-gradient(135deg,#A5B4FC,#34D399); -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text; margin-bottom:.75rem; line-height:1; }
.skill-name { font-size:.92rem; font-weight:500; color:#e2e8f0; margin-bottom:.75rem; }
.skill-tags { display:flex; flex-wrap:wrap; gap:.4rem; }
.stag { font-size:.63rem; padding:.25rem .7rem; letter-spacing:.08em; border:1px solid rgba(165,180,252,.30); color:#a5b4fc; border-radius:20px; background:rgba(99,102,241,.15); }

/* Experience */
.exp-card { display:flex; gap:1.5rem; align-items:flex-start; background:rgba(255,255,255,.85); border:1px solid rgba(245,158,11,.18); border-radius:16px; padding:1.75rem; margin-bottom:1.25rem; box-shadow:0 2px 12px rgba(245,158,11,.07); }
.exp-num { width:48px; height:48px; border-radius:12px; flex-shrink:0; background:linear-gradient(135deg,#F59E0B,#EC4899); display:flex; align-items:center; justify-content:center; font-family:'Cormorant Garamond',serif; font-size:1.1rem; font-weight:700; color:#fff; }
.exp-role { font-size:.95rem; font-weight:500; color:var(--dark); margin-bottom:.25rem; }
.exp-place { font-size:.7rem; letter-spacing:.1em; text-transform:uppercase; color:#D97706; margin-bottom:.5rem; }
.exp-desc { font-size:.82rem; color:var(--muted); line-height:1.85; }

/* Projects */
.proj-grid { display:grid; grid-template-columns:repeat(3,1fr); gap:1.5rem; }
.proj-card { background:rgba(255,255,255,.06); border:1px solid rgba(255,255,255,.10); border-radius:20px; overflow:hidden; }
.proj-thumb { height:130px; display:flex; align-items:center; justify-content:center; font-size:3rem; }
.pt1{background:linear-gradient(135deg,#7C3AED,#06B6D4)} .pt2{background:linear-gradient(135deg,#0EA5E9,#14B8A6)} .pt3{background:linear-gradient(135deg,#6366F1,#7C3AED)}
.proj-body { padding:1.25rem; }
.proj-tag { font-size:.6rem; letter-spacing:.15em; text-transform:uppercase; color:#5EEAD4; margin-bottom:.5rem; display:block; }
.proj-name { font-family:'Cormorant Garamond',serif; font-size:1.1rem; font-weight:600; color:#f0fdf4; margin-bottom:.4rem; }
.proj-desc { font-size:.78rem; color:rgba(255,255,255,.50); line-height:1.75; }

/* Education */
.edu-timeline { border-left:2px solid var(--purple-dim); margin-left:1.5rem; }
.edu-row { display:grid; grid-template-columns:130px 1fr; gap:1.5rem; padding:1.5rem 1.5rem 1.5rem 2rem; position:relative; border-bottom:1px solid rgba(124,58,237,.10); }
.edu-row:last-child { border-bottom:none; }
.edu-dot { position:absolute; left:-7px; top:1.75rem; width:12px; height:12px; border-radius:50%; background:#fff; border:2.5px solid var(--purple); box-shadow:0 0 0 3px rgba(124,58,237,.15); }
.edu-year { font-size:.7rem; letter-spacing:.1em; text-transform:uppercase; color:var(--purple-lt); padding-top:3px; }
.edu-school { font-size:.95rem; font-weight:500; color:var(--dark); margin-bottom:.25rem; }
.edu-deg { font-size:.82rem; color:var(--muted); margin-bottom:.5rem; }
.edu-badge { display:inline-block; font-size:.6rem; letter-spacing:.1em; text-transform:uppercase; color:var(--purple); border:1px solid var(--purple-dim); border-radius:20px; padding:.2rem .75rem; background:#EDE9FE; }

/* Contact */
.contact-grid { display:grid; grid-template-columns:repeat(2,1fr); gap:1.25rem; }
.contact-card { display:flex; align-items:flex-start; gap:1rem; background:rgba(255,255,255,.05); border:1px solid rgba(255,255,255,.10); border-radius:16px; padding:1.5rem 1.75rem; }
.contact-card a { color:#fff; text-decoration:none; }
.c-icon { font-size:1.6rem; flex-shrink:0; }
.c-lbl { font-size:.6rem; letter-spacing:.18em; text-transform:uppercase; color:var(--purple-lt); margin-bottom:.35rem; }
.c-val { font-size:.88rem; color:#fff; }

/* Footer */
.footer { background:#050311; text-align:center; padding:2rem; font-size:.65rem; letter-spacing:.15em; text-transform:uppercase; color:rgba(255,255,255,.22); border-top:1px solid rgba(255,255,255,.05); }

/* Responsive */
@media (max-width:900px) {
  .hero { grid-template-columns:1fr; padding-top:5.5rem; text-align:center; }
  .hero-right { order:-1; }
  .hero-btns { justify-content:center; }
  .hero-stats { justify-content:center; }
  .about-grid { grid-template-columns:1fr; }
  .skills-grid { grid-template-columns:1fr 1fr; }
  .proj-grid { grid-template-columns:1fr 1fr; }
  .contact-grid { grid-template-columns:1fr 1fr; }
}
@media (max-width:640px) {
  .section { padding:4.5rem 5%; }
  .hero { padding:5rem 5% 3rem; }
  .skills-grid,.proj-grid,.contact-grid { grid-template-columns:1fr; }
  .edu-row { grid-template-columns:1fr; gap:.4rem; }
  .edu-list { margin-left:1rem; }
  .hero-photo-wrap { width:230px; height:290px; }
  .hero-photo { width:212px; height:274px; }
  .navbar { padding:0 5%; }
  .nav-links a { margin-left:1rem; font-size:.6rem; }
}
</style>
""", unsafe_allow_html=True)

# ══ NAV ═════════════════════════════════════════════════
st.markdown("""
<div class="navbar">
  <span class="nav-logo">S · N · J</span>
  <div class="nav-links">
    <a href="#home">Home</a><a href="#about">About</a><a href="#skills">Skills</a>
    <a href="#experience">Experience</a><a href="#projects">Projects</a>
    <a href="#education">Education</a><a href="#contact">Contact</a>
  </div>
</div>
""", unsafe_allow_html=True)

# ══ 01 HERO ══════════════════════════════════════════════
st.markdown(f"""
<div class="hero" id="home">
  <div class="hero-left">
    <div class="hero-pill"><span class="hero-dot"></span>&nbsp; Available for work</div>
    <h1 class="hero-name">Shinvi<br><em>Nur Najmil</em><br>Jannah</h1>
    <p class="hero-tagline">Informatics Engineering · Web Developer<br>Data Analyst · UI Designer</p>
    <div class="hero-btns">
      <a href="#projects" class="btn-fill">View Projects</a>
      <a href="#contact" class="btn-ghost">Get in Touch</a>
      {cv_btn}
    </div>
    <div class="hero-stats">
      <div class="stat"><div class="stat-num">3+</div><div class="stat-lbl">Projects</div></div>
      <div class="stat"><div class="stat-num">2+</div><div class="stat-lbl">Years Exp</div></div>
      <div class="stat"><div class="stat-num">4</div><div class="stat-lbl">Skills</div></div>
    </div>
  </div>
  <div class="hero-right">
    <div class="hero-photo-wrap">
      <div class="hero-photo-bg"></div>
      {photo_tag}
    </div>
    <div class="hero-stats" style="margin-top:0">
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ══ 02 ABOUT ═════════════════════════════════════════════
st.markdown("""
<div class="section sec-about" id="about">
  <span class="eyebrow ey-p">02 · About</span>
  <h2 class="sec-title t-d">Who I Am</h2>
  <div class="divider"><div class="dl dl-d"></div><div class="dg dg-p"></div><div class="dl dl-d"></div></div>
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

# ══ 03 SKILLS ════════════════════════════════════════════
st.markdown("""
<div class="section sec-skills" id="skills">
  <span class="eyebrow ey-l">03 · Skills</span>
  <h2 class="sec-title t-l">Expertise</h2>
  <div class="divider"><div class="dl dl-l"></div><div class="dg dg-l"></div><div class="dl dl-l"></div></div>
  <div class="skills-grid">
    <div class="skill-card"><div class="skill-num">01</div><div class="skill-name">Web Development</div><div class="skill-tags"><span class="stag">HTML</span><span class="stag">CSS</span><span class="stag">JavaScript</span><span class="stag">Responsive</span></div></div>
    <div class="skill-card"><div class="skill-num">02</div><div class="skill-name">Data Analysis</div><div class="skill-tags"><span class="stag">Python</span><span class="stag">SQL</span><span class="stag">Excel</span><span class="stag">Visualization</span></div></div>
    <div class="skill-card"><div class="skill-num">03</div><div class="skill-name">Content &amp; Research</div><div class="skill-tags"><span class="stag">Writing</span><span class="stag">Research</span><span class="stag">Market Analysis</span></div></div>
    <div class="skill-card"><div class="skill-num">04</div><div class="skill-name">Design Tools</div><div class="skill-tags"><span class="stag">Canva</span><span class="stag">Figma</span><span class="stag">UI/UX</span></div></div>
  </div>
</div>
""", unsafe_allow_html=True)

# ══ 04 EXPERIENCE ════════════════════════════════════════
st.markdown("""
<div class="section sec-exp" id="experience">
  <span class="eyebrow ey-a">04 · Experience</span>
  <h2 class="sec-title t-d">Work History</h2>
  <div class="divider"><div class="dl dl-d"></div><div class="dg dg-p"></div><div class="dl dl-d"></div></div>
  <div class="exp-card"><div class="exp-num">01</div><div><div class="exp-role">Data Analyst Staff</div><div class="exp-place">SMA Ibnu Siena Tasikmalaya</div><div class="exp-desc">Responsible for collecting, processing, and analyzing school data to produce structured reports supporting informed decision-making.</div></div></div>
  <div class="exp-card"><div class="exp-num">02</div><div><div class="exp-role">Web Designer — Automotive Sales Website</div><div class="exp-place">Freelance / Personal Project</div><div class="exp-desc">Designed and developed a car sales website with a clean, user-friendly interface featuring product listings and fully responsive layout.</div></div></div>
  <div class="exp-card"><div class="exp-num">03</div><div><div class="exp-role">Web Developer — Room Monitoring System</div><div class="exp-place">Academic / Personal Project</div><div class="exp-desc">Built a web-based system to monitor room temperature, humidity, and energy data with real-time data visualization.</div></div></div>
</div>
""", unsafe_allow_html=True)

# ══ 05 PROJECTS ══════════════════════════════════════════
st.markdown("""
<div class="section sec-projects" id="projects">
  <span class="eyebrow ey-t">05 · Projects</span>
  <h2 class="sec-title t-l">Featured Work</h2>
  <div class="divider"><div class="dl dl-l"></div><div class="dg dg-t"></div><div class="dl dl-l"></div></div>
  <div class="proj-grid">
    <div class="proj-card"><div class="proj-thumb pt1">🚗</div><div class="proj-body"><span class="proj-tag">Web Development</span><div class="proj-name">Automotive Sales Website</div><div class="proj-desc">A responsive car sales platform with product listings and intuitive navigation.</div></div></div>
    <div class="proj-card"><div class="proj-thumb pt2">🌡️</div><div class="proj-body"><span class="proj-tag">Data Visualization</span><div class="proj-name">Room Monitoring System</div><div class="proj-desc">Real-time monitoring for room temperature, humidity, and energy with live visualization.</div></div></div>
    <div class="proj-card"><div class="proj-thumb pt3">📊</div><div class="proj-body"><span class="proj-tag">Data Analysis</span><div class="proj-name">School Data Analysis</div><div class="proj-desc">Comprehensive data analysis at SMA Ibnu Siena producing structured decision-making reports.</div></div></div>
  </div>
</div>
""", unsafe_allow_html=True)

# ══ 06 EDUCATION ═════════════════════════════════════════
st.markdown("""
<div class="section sec-education" id="education">
  <span class="eyebrow ey-p">06 · Education</span>
  <h2 class="sec-title t-d">Academic Background</h2>
  <div class="divider"><div class="dl dl-d"></div><div class="dg dg-p"></div><div class="dl dl-d"></div></div>
  <div class="edu-timeline">
    <div class="edu-row"><div class="edu-dot"></div><div class="edu-year">2023 — Present</div><div><div class="edu-school">Universitas Siliwangi, Tasikmalaya</div><div class="edu-deg">S1 Informatics Engineering</div><span class="edu-badge">Himpunan Informatika</span></div></div>
    <div class="edu-row"><div class="edu-dot"></div><div class="edu-year">2020 — 2023</div><div><div class="edu-school">SMAN 1 Ciamis</div><div class="edu-deg">Senior High School — Science (IPA)</div></div></div>
    <div class="edu-row"><div class="edu-dot"></div><div class="edu-year">2017 — 2020</div><div><div class="edu-school">SMPN 1 Cikoneng</div><div class="edu-deg">Junior High School</div><span class="edu-badge">Vice Chairman of OSIS</span></div></div>
    <div class="edu-row"><div class="edu-dot"></div><div class="edu-year">2011 — 2017</div><div><div class="edu-school">MI Cisaray</div><div class="edu-deg">Elementary School</div></div></div>
  </div>
</div>
""", unsafe_allow_html=True)

# ══ 07 CONTACT ═══════════════════════════════════════════
st.markdown("""
<div class="section sec-contact" id="contact">
  <span class="eyebrow ey-pk">07 · Contact</span>
  <h2 class="sec-title t-l">Let's Work Together</h2>
  <p style="text-align:center;color:rgba(255,255,255,.45);font-size:.88rem;margin-bottom:3rem;">Open to freelance projects, collaboration, and new opportunities.</p>
  <div class="divider"><div class="dl dl-l"></div><div class="dg" style="background:rgba(167,139,250,.4)"></div><div class="dl dl-l"></div></div>
  <div class="contact-grid">
    <div class="contact-card"><div class="c-icon">📱</div><div><div class="c-lbl">Phone / WhatsApp</div><div class="c-val"><a href="https://wa.me/6288102215118" target="_blank">+62 881-0221-51118</a></div></div></div>
    <div class="contact-card"><div class="c-icon">✉️</div><div><div class="c-lbl">Email</div><div class="c-val"><a href="mailto:shinviiiiii@gmail.com">shinviiiiii@gmail.com</a></div></div></div>
    <div class="contact-card"><div class="c-icon">📍</div><div><div class="c-lbl">Location</div><div class="c-val">Ciamis, West Java, Indonesia</div></div></div>
    <div class="contact-card"><div class="c-icon">💼</div><div><div class="c-lbl">Availability</div><div class="c-val">Available for hire</div></div></div>
  </div>
</div>
""", unsafe_allow_html=True)

# ══ FOOTER ═══════════════════════════════════════════════
st.markdown("""
<div class="footer">© 2026 · Shinvi Nur Najmil Jannah · Informatics Engineering · Universitas Siliwangi</div>
""", unsafe_allow_html=True)
