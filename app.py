
import streamlit as st
import textwrap
import io
from datetime import datetime

st.set_page_config(page_title="Virtual CyberLab", page_icon="🛡️", layout="wide")

# ---------- STYLE ----------
st.html(textwrap.dedent("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
html,body,[class*="css"]{font-family:Inter,sans-serif}
.stApp{background:radial-gradient(circle at 86% 10%,rgba(22,129,215,.18),transparent 28%),radial-gradient(circle at 10% 45%,rgba(124,51,190,.10),transparent 30%),linear-gradient(145deg,#020914,#061a2d 52%,#020a14);color:#f7fbff}
.block-container{max-width:1320px;width:100%;padding:clamp(.45rem,.8vw,.8rem) clamp(.6rem,1.7vw,1.6rem) 1.1rem;margin:auto;box-sizing:border-box}
.topbar{position:relative;display:flex;align-items:center;justify-content:space-between;gap:clamp(10px,1.5vw,22px);padding:5px 0 12px;border-bottom:1px solid rgba(60,150,200,.27)}
.logo-wrap{display:flex;align-items:center;gap:11px;min-width:260px}.logo{font-size:38px;filter:drop-shadow(0 0 13px rgba(32,220,239,.45))}
.logo-title{font-size:19px;font-weight:800;white-space:nowrap}.logo-title .cyan{color:#20d9ea}.logo-title .purple{color:#9c6ff1}.logo-sub{font-size:8px;color:#7e99ad;letter-spacing:1px}
.nav{display:flex;gap:8px;align-items:center;color:#d9e8f2;font-size:12px}.nav span{padding:7px 11px}.nav .active{border:1px solid #20c9df;border-radius:18px;background:rgba(25,207,226,.10)}
.st-key-main_nav{position:relative!important;z-index:100!important;width:100%!important;isolation:isolate!important}.st-key-main_nav > div{position:relative!important;z-index:100!important}.st-key-main_nav [data-testid="column"]{position:relative!important;z-index:100!important}.st-key-main_nav .stButton{position:relative!important;z-index:101!important}.st-key-main_nav .stButton>button{position:relative!important;z-index:102!important;pointer-events:auto!important}.topbar{z-index:1!important}.hero{position:relative;z-index:0!important}
.main-nav{display:flex;gap:6px;align-items:center;justify-content:center;padding:5px 0 8px;border-bottom:1px solid rgba(60,150,200,.16);margin-bottom:5px}.main-nav .stButton{margin:0}.main-nav .stButton>button{min-height:33px!important;padding:3px 8px!important;background:rgba(10,48,77,.92)!important;border:1px solid #255f7e!important;font-size:11px!important;white-space:nowrap!important;color:#f7fbff!important;opacity:1!important;visibility:visible!important}.main-nav .stButton>button p,.main-nav .stButton>button span,.main-nav .stButton>button div{color:#f7fbff!important;opacity:1!important;visibility:visible!important}.main-nav .stButton>button:hover{border-color:#20d9ea!important;background:rgba(25,207,226,.16)!important;color:#ffffff!important}.main-nav .stButton>button:focus,.main-nav .stButton>button:active{color:#ffffff!important}.main-nav .active-nav>button{border-color:#20d9ea!important;background:rgba(25,207,226,.14)!important}
/* Streamlit renders the navigation columns outside the markdown wrapper, so style the keyed buttons directly. */
[class*="st-key-nav_home"] button,[class*="st-key-nav_about"] button,[class*="st-key-nav_resources"] button,[class*="st-key-nav_contact"] button{min-height:33px!important;padding:3px 8px!important;background:rgba(10,48,77,.92)!important;border:1px solid #255f7e!important;border-radius:14px!important;font-size:11px!important;white-space:nowrap!important;color:#f7fbff!important;opacity:1!important;visibility:visible!important;position:relative!important;z-index:20!important;box-shadow:none!important}
[class*="st-key-nav_home"] button p,[class*="st-key-nav_home"] button span,[class*="st-key-nav_home"] button div,[class*="st-key-nav_about"] button p,[class*="st-key-nav_about"] button span,[class*="st-key-nav_about"] button div,[class*="st-key-nav_resources"] button p,[class*="st-key-nav_resources"] button span,[class*="st-key-nav_resources"] button div,[class*="st-key-nav_contact"] button p,[class*="st-key-nav_contact"] button span,[class*="st-key-nav_contact"] button div{color:#f7fbff!important;opacity:1!important;visibility:visible!important}
[class*="st-key-nav_home"] button:hover,[class*="st-key-nav_about"] button:hover,[class*="st-key-nav_resources"] button:hover,[class*="st-key-nav_contact"] button:hover{border-color:#20d9ea!important;background:rgba(25,207,226,.16)!important;color:#fff!important}
[class*="st-key-nav_home"],[class*="st-key-nav_about"],[class*="st-key-nav_resources"],[class*="st-key-nav_contact"]{position:relative!important;z-index:20!important} 

.safe{text-align:center;font-size:11px;color:#86dce6;min-width:0;position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);white-space:nowrap;z-index:3}.safe b{color:#fff}
.hero{text-align:center;padding:12px 0 11px}.hero-kicker{font-size:16px}.hero-title{font-size:clamp(38px,4.4vw,52px);line-height:1.02;font-weight:800;letter-spacing:-3px;margin:5px 0 9px}.hero-title .cyan{color:#20d9ea}.hero-title .purple{color:#9b6cf1}.hero-desc{font-size:13px;color:#b7c9d6}.hero-tag{color:#23d9e8;font-weight:700;font-size:12px;margin:8px auto 0;text-align:center;width:100%;display:block}
.stat{background:linear-gradient(145deg,rgba(10,48,77,.88),rgba(4,23,41,.92));border:1px solid #1a587a;border-radius:16px;padding:9px 8px;text-align:center;min-height:70px;height:auto;box-sizing:border-box}.stat-label{font-size:9px;color:#aec1cd;letter-spacing:.7px}.stat-value{font-size:21px;font-weight:800;color:#24d9e9;margin-top:5px}.gold{color:#ffc12b}
.section-title{font-size:16px;font-weight:800;margin:15px 0 9px}
.lab{min-height:220px;height:auto;padding:13px 12px 10px;border-radius:22px;background:linear-gradient(150deg,rgba(8,41,68,.96),rgba(3,18,32,.98));border:1px solid #1b5575;box-shadow:0 12px 28px rgba(0,0,0,.25)}
.lab.phish{border-color:#b94dd0}.lab.pass{border-color:#16d8cc}.lab.inc{border-color:#2b8ff0}.lab.final{border-color:#e7ae27}
.lab-icon{width:58px;height:58px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:30px;margin:0 auto 10px;background:radial-gradient(circle,rgba(65,125,180,.34),rgba(10,38,65,.30));box-shadow:inset 0 0 20px rgba(60,210,235,.12)}
.lab h3{font-size:16px;margin:0 0 4px;text-align:center}.lab .ar{color:#2be0ec;font-weight:700;font-size:12px;text-align:center}.lab p{font-size:11px;color:#b8cad7;line-height:1.5;min-height:48px;height:auto;margin-top:6px;text-align:center}
.stButton>button,.stButton>button:hover,.stButton>button:focus,.stButton>button:active{color:#fff!important;opacity:1!important;font-weight:800!important;font-size:13px!important;border-radius:13px!important;min-height:45px!important;border:1px solid #43e8f5!important;background:linear-gradient(90deg,#12c6dd,#1786ed)!important;box-shadow:0 0 18px rgba(25,207,229,.15)!important}.stButton>button p,.stButton>button span,.stButton>button div{color:#fff!important;opacity:1!important}
.st-key-go_phishing button{background:linear-gradient(90deg,#b63bd3,#e34dd7)!important;border-color:#ed79ef!important}.st-key-go_identity button{background:linear-gradient(90deg,#08bcb5,#19d8ce)!important;border-color:#61fff4!important}.st-key-go_incident button{background:linear-gradient(90deg,#087fe7,#168cf4)!important;border-color:#59b8ff!important}.st-key-go_final button{background:linear-gradient(90deg,#e2a41b,#f1bc35)!important;border-color:#ffd968!important}
.feature{border:1px solid #155373;background:rgba(7,31,51,.74);border-radius:15px;padding:11px;min-height:80px}.feature-icon{font-size:25px}.feature b{font-size:13px}.feature span{color:#98adbd;font-size:11px}.footer{border-top:1px solid rgba(61,151,198,.25);margin-top:18px;padding-top:11px;color:#829bab;font-size:11px;display:flex;justify-content:space-between}
.partner-logos{display:flex;align-items:center;gap:7px;margin-left:auto;flex:0 0 auto}.partner-logo{height:40px;width:auto;max-width:150px;object-fit:contain;background:rgba(255,255,255,.96);padding:6px 10px;border-radius:10px;border:1px solid rgba(120,180,205,.35)}.partner-logo.tuwaiq{background:#fff;padding:7px 12px}.institution-row{display:flex;justify-content:center;align-items:center;gap:18px;margin:8px 0 2px}.institution-label{font-size:9px;color:#7e99ad;letter-spacing:.8px;text-transform:uppercase}

/* Mission readability */
.mission{background:linear-gradient(145deg,rgba(8,43,70,.96),rgba(3,20,36,.98));border:1px solid #2a6b91;border-radius:16px;padding:16px 18px;margin:8px 0 12px;color:#f5fbff!important;box-shadow:0 8px 24px rgba(0,0,0,.18)}
.mission h2,.mission h3{color:#ffffff!important;margin-top:0}.mission p{color:#d9eaf3!important;line-height:1.65;font-size:14px}
.evidence{background:rgba(8,39,63,.96);border:1px solid #287da5;border-radius:14px;padding:14px 16px;margin:8px 0 12px;color:#eaf7ff!important;font-size:13px;line-height:1.75}
.evidence b{color:#5cecf5!important}.stCaption,.stCaption p,[data-testid="stCaptionContainer"]{color:#bfe2ee!important}
[data-testid="stWidgetLabel"] p,[data-testid="stWidgetLabel"] label,[data-testid="stWidgetLabel"] span,.stRadio label,.stRadio label p,.stRadio label span,.stRadio div[role="radiogroup"] label,.stRadio div[role="radiogroup"] label p,.stMultiSelect label,.stMultiSelect label p,.stMultiSelect label span{color:#f7fbff!important;opacity:1!important;text-shadow:0 0 8px rgba(32,217,234,.10)}
[data-testid="stWidgetLabel"] span{color:#f7fbff!important;opacity:1!important}.mission-question,.mission-question *{color:#f7fbff!important}
.stAlert p{color:#f7fbff!important}
.stDownloadButton button,[data-testid="stDownloadButton"] button{background:linear-gradient(90deg,#7b4fe8,#b64ee8)!important;border:1px solid #d58cff!important;color:#ffffff!important;box-shadow:0 0 18px rgba(163,91,235,.25)!important}
.stDownloadButton button p,.stDownloadButton button span,[data-testid="stDownloadButton"] button p,[data-testid="stDownloadButton"] button span{color:#ffffff!important}
.footer-final{border-top:1px solid rgba(61,151,198,.3);margin-top:24px;padding:16px 0 6px;display:flex;align-items:center;justify-content:space-between;gap:18px;color:#d7e8f1}
.footer-final .rights{font-size:12px;line-height:1.75;color:#c8dbe5}
.footer-final .rights b{color:#27d9ea}.footer-final .partner-logos{margin:0}
.footer-final .partner-logo{height:38px}

@media (max-width: 1100px){
  .topbar{gap:10px}.logo-title{font-size:17px}.logo{font-size:29px}.logo-sub{font-size:8px}.safe{font-size:10px}.partner-logo{height:34px;max-width:110px}.hero-title{font-size:42px}.hero-desc{font-size:13px}.lab{min-height:205px;padding:11px 9px 9px}.lab-icon{width:58px;height:58px;font-size:30px}.lab h3{font-size:16px}.lab p{font-size:11px}.stButton>button{font-size:12px!important;min-height:40px!important}}
@media (max-width: 900px){
  .block-container{padding-left:.75rem;padding-right:.75rem}
  .topbar{flex-wrap:wrap;justify-content:center}.logo-wrap{width:100%;justify-content:center}.safe{display:block;position:static;transform:none;order:2;width:100%;text-align:center;font-size:9px;line-height:1.35;white-space:normal}.partner-logos{margin:0 auto;order:3}.logo-wrap{order:1}
  .hero{padding:9px 0 10px}.hero-title{font-size:clamp(34px,8vw,42px);letter-spacing:-1.5px}.hero-desc{font-size:12px}.hero-tag{font-size:12px}
  .main-nav{gap:4px;padding:4px 0 8px}.main-nav .stButton>button{padding:3px 4px!important;font-size:10px!important;min-height:34px!important;border-radius:11px!important}
  .stat{min-height:68px;padding:9px 7px;border-radius:15px}.stat-value{font-size:20px}.section-title{font-size:15px;margin:12px 0 7px}
  .lab{min-height:205px;padding:12px 9px 10px;border-radius:18px}.lab-icon{width:54px;height:54px;font-size:28px;margin-bottom:8px}.lab h3{font-size:15px}.lab .ar{font-size:10px}.lab p{font-size:10px;line-height:1.35;min-height:42px}
  .feature{min-height:70px;padding:9px;border-radius:14px}.feature-icon{font-size:24px}
}
@media (max-width: 600px){
  .block-container{padding-left:.5rem;padding-right:.5rem}
  .topbar{padding-bottom:8px}.logo-title{font-size:17px}.logo{font-size:28px}.logo-sub{font-size:7px;letter-spacing:.7px}.partner-logos{gap:5px}.partner-logo{height:30px;max-width:95px;padding:4px 7px}.partner-logo.tuwaiq{padding:5px 8px}
  .main-nav{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:4px;width:100%}.main-nav .stButton{width:100%}.main-nav .stButton>button{width:100%!important;padding:2px 2px!important;font-size:9px!important;min-height:32px!important}
  .hero{padding:7px 0 8px}.hero-kicker{font-size:13px}.hero-title{font-size:clamp(30px,9vw,38px);margin:4px 0 7px}.hero-desc{font-size:10px;line-height:1.35}.hero-tag{font-size:10px;margin-top:5px}
  .stat{min-height:62px;padding:8px 5px}.stat-label{font-size:7px}.stat-value{font-size:18px;margin-top:3px}
  .lab{min-height:190px;padding:11px 8px 9px}.lab-icon{width:50px;height:50px;font-size:26px}.lab h3{font-size:14px}.lab p{font-size:10px;min-height:38px;margin-top:5px}.stButton>button{font-size:11px!important;min-height:38px!important}
  .feature{min-height:62px;padding:8px}.feature-icon{font-size:22px}.feature b{font-size:11px}.feature span{font-size:9px}
  .footer{font-size:9px;gap:8px;flex-direction:column;text-align:center}
}
@media (max-width: 420px){
  .logo-wrap{gap:7px}.logo-title{font-size:15px}.logo{font-size:25px}.partner-logo{height:27px;max-width:82px}.main-nav .stButton>button{font-size:8px!important;min-height:30px!important}
  .hero-title{font-size:29px}.hero-desc{font-size:9px}.hero-tag{font-size:9px}.stat-label{font-size:6.5px}.stat-value{font-size:17px}
}
@media (max-width:600px){.footer-final{flex-direction:column;text-align:center;gap:10px}.footer-final .partner-logos{justify-content:center}.footer-final .rights{font-size:10px}.footer-final .partner-logo{height:32px}}
.nav-html{display:flex;align-items:center;justify-content:center;gap:6px;width:100%;padding:4px 0 8px;border-bottom:1px solid rgba(60,150,200,.16);margin-bottom:12px;position:relative;z-index:9999}
.nav-html a{display:inline-flex;align-items:center;justify-content:center;min-height:33px;padding:3px 10px;border:1px solid #255f7e;border-radius:14px;background:rgba(10,48,77,.92);color:#f7fbff!important;text-decoration:none!important;font-size:11px;font-weight:800;white-space:nowrap;box-sizing:border-box;position:relative;z-index:10000}
.nav-html a:hover{border-color:#20d9ea;background:rgba(25,207,226,.16)}
@media(max-width:600px){.nav-html{gap:4px}.nav-html a{flex:1;min-width:0;padding:2px 3px;font-size:9px;min-height:30px}}
</style>
"""))


# ---------- STATE ----------
if "page" not in st.session_state: st.session_state.page = "home"
if "score" not in st.session_state: st.session_state.score = 0
if "completed" not in st.session_state: st.session_state.completed = set()

def go(page):
    # Navigate immediately after a button click and clear any stale URL route.
    st.session_state.page = page
    try:
        st.query_params.clear()
    except Exception:
        pass
    st.rerun()

def complete(mission, points):
    if mission not in st.session_state.completed:
        st.session_state.completed.add(mission)
        st.session_state.score += points

def record_attempt(mission):
    key = f"attempts_{mission}"
    st.session_state[key] = st.session_state.get(key, 0) + 1

def mission_feedback(mission):
    attempts = st.session_state.get(f"attempts_{mission}", 0)
    if attempts:
        st.caption(f"Attempts: {attempts}")

def reset_progress():
    st.session_state.score = 0
    st.session_state.completed = set()
    for key in list(st.session_state.keys()):
        if key.startswith("attempts_") or key.endswith("_awarded"):
            del st.session_state[key]


def build_progress_pdf():
    try:
        from reportlab.lib.pagesizes import A4
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.enums import TA_CENTER
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
        from reportlab.lib import colors
    except ModuleNotFoundError:
        st.error("PDF export needs ReportLab. Run START_Virtual_CyberLab.bat or: py -m pip install -r requirements.txt")
        return None
    buf = io.BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=A4, rightMargin=42, leftMargin=42, topMargin=42, bottomMargin=42)
    styles = getSampleStyleSheet()
    title = ParagraphStyle("title", parent=styles["Title"], alignment=TA_CENTER, fontSize=20, leading=24)
    center = ParagraphStyle("center", parent=styles["Normal"], alignment=TA_CENTER, fontSize=10, leading=14)
    story=[Paragraph("Virtual CyberLab", title), Paragraph("Virtual Cybersecurity Laboratory", center), Spacer(1,14)]
    story.append(Paragraph(f"Learner: {st.session_state.get('learner_name','Learner')}", styles["Normal"]))
    story.append(Paragraph(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}", styles["Normal"]))
    story.append(Spacer(1,10))
    data=[["Metric","Result"],["Security Score",f"{st.session_state.score}/1200"],["Missions Completed",f"{len(st.session_state.completed)}/12"],["Badge",badge_name(st.session_state.score)]]
    t=Table(data,colWidths=[220,220]); t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#123d59')),('TEXTCOLOR',(0,0),(-1,0),colors.white),('GRID',(0,0),(-1,-1),0.5,colors.HexColor('#9ab7c8')),('PADDING',(0,0),(-1,-1),7)])); story += [t,Spacer(1,14)]
    story.append(Paragraph("Completed Missions", styles["Heading2"]))
    if st.session_state.completed:
        for mid in sorted(st.session_state.completed): story.append(Paragraph(f"• {MISSIONS[mid]}", styles["Normal"]))
    else: story.append(Paragraph("No missions completed yet.", styles["Normal"]))
    story += [Spacer(1,18), Paragraph("Developed & Designed by Aishah Ali Khawaji", center), Paragraph("Gifted Secondary School for Girls - Gizan • School Principal: Samia Hammadi", center)]
    doc.build(story); buf.seek(0); return buf.getvalue()

def badge_name(score):
    if score >= 1200: return "CYBER DEFENDER"
    if score >= 900: return "CYBER SPECIALIST"
    if score >= 600: return "CYBER GUARDIAN"
    if score >= 300: return "CYBER EXPLORER"
    return "IN PROGRESS"

MISSIONS = {
    "m1": "The Suspicious Invoice", "m2": "Fake Microsoft 365 Login",
    "m3": "QR Code Phishing", "m4": "Social Engineering Message",
    "m5": "The Reused Password", "m6": "MFA Alert",
    "m7": "Account Takeover", "m8": "Suspicious Login",
    "m9": "Malware Alert", "m10": "Lost Device",
    "m11": "Data Leakage Investigation", "m12": "Cyber Defender Mission"
}

# ---------- GLOBAL NAVIGATION ----------
page_from_url = st.query_params.get("page")
if page_from_url in {"home","about","resources","contact","phishing","identity","incident","final","m1","m2","m3","m4","m5","m6","m7","m8","m9","m10","m11","m12"}:
    st.session_state.page = page_from_url

nav_links = [("🏠 HOME","home"),("ℹ️ ABOUT","about"),("📚 RESOURCES","resources"),("✉️ CONTACT","contact")]
nav_html = '<div class="nav-html">' + ''.join(
    f'<a href="?page={page_name}" aria-label="{label}">{label}</a>' for label,page_name in nav_links
) + '</div>'
# ---------- HOME ----------
if st.session_state.page == "home":
    st.html(textwrap.dedent("""
    <div class="hero">
      <div class="hero-kicker">Welcome to</div>
      <div class="hero-title">🛡️ <span class="cyan">Virtual</span> <span class="cyan">Cyber</span><span class="purple">Lab</span></div>
      <div class="hero-desc">VIRTUAL CYBERSECURITY LABORATORY</div>
      <div class="hero-tag">Learn • Investigate • Protect</div>
      <div class="hero-desc" style="margin-top:5px;">A safer digital tomorrow starts with you</div>
    </div>
    """))
    st.html(nav_html)

    learner = st.text_input("Learner name (optional)", value=st.session_state.get("learner_name", ""), placeholder="Enter learner name for the progress report", label_visibility="collapsed")
    st.session_state.learner_name = learner.strip() or "Learner"

    a,b,c,d=st.columns(4)
    vals=[(a,"SECURITY SCORE",st.session_state.score,""),(b,"MISSIONS",len(st.session_state.completed),""),(c,"TOTAL MISSIONS",12,""),(d,"BADGE",badge_name(st.session_state.score),"gold")]
    for col,label,val,cl in vals:
        with col: st.html(f'<div class="stat"><div class="stat-label">{label}</div><div class="stat-value {cl}">{val}</div></div>')

    st.html('<div style="text-align:center;color:#829bab;font-size:10px;margin:6px 0 2px;">Badge levels: 300 Explorer • 600 Guardian • 900 Specialist • 1200 Defender</div>')
    progress = len(st.session_state.completed) / len(MISSIONS)
    st.progress(progress, text=f"Mission Progress • {len(st.session_state.completed)}/{len(MISSIONS)} completed")
    if st.session_state.completed:
        pdf_bytes = build_progress_pdf()
        if pdf_bytes:
            st.download_button("📄 DOWNLOAD PROGRESS REPORT", pdf_bytes, file_name="Virtual_CyberLab_Progress_Report.pdf", mime="application/pdf", use_container_width=True)
    if st.button("↻ RESET PROGRESS", use_container_width=True):
        reset_progress()
        st.rerun()

    st.html('<div class="section-title">Cybersecurity Labs</div>')
    cols=st.columns(4)
    cards=[
      (cols[0],"🎣","Phishing Lab","Analyze suspicious emails, links, QR codes and social-engineering attempts.","phish","phishing"),
      (cols[1],"🔐","Password & Identity","Investigate weak credentials, MFA alerts and account compromise.","pass","identity"),
      (cols[2],"🚨","Incident Response","Respond to security alerts and make evidence-based decisions.","inc","incident"),
      (cols[3],"🏆","Cyber Challenge","Combine your skills in multi-step cybersecurity investigations.","final","final")]
    for col,icon,title,desc,cl,page in cards:
        with col:
            st.html(f'<div class="lab {cl}"><div class="lab-icon">{icon}</div><h3>{title}</h3><p>{desc}</p></div>')
            if st.button("ENTER LAB  →",key="go_"+page,use_container_width=True): go(page)

    st.html('<div class="section-title">Why Virtual CyberLab?</div>')
    fs=[("💡","Interactive Experience","Learn through realistic scenarios."),("📊","Learn by Doing","Practice decisions, not memorization."),("🏅","Achievements","Earn badges as your skills grow."),("📚","Trusted Content","Built around cybersecurity awareness.")]
    cc=st.columns(4)
    for col,(ic,h,p) in zip(cc,fs):
        with col: st.html(f'<div class="feature"><div class="feature-icon">{ic}</div><b>{h}</b><br><span>{p}</span></div>')
    st.html(textwrap.dedent("""
    <div class="footer-final">
      <div class="rights">
        <div>© 2026 Virtual CyberLab</div>
        <div>Developed & Designed by <b>Aishah Ali Khawaji</b></div>
        <div>Gifted Secondary School for Girls - Gizan &nbsp;•&nbsp; School Principal: Samia Hammadi</div>
        <div>Educational Knowledge Product • All Rights Reserved</div>
      </div>
      <div class="partner-logos">
        <img class="partner-logo" src="https://www.moe.gov.sa/ar/mediacenter/MOEnews/NewsImages/moelogo1442.jpg" alt="Ministry of Education">
        <img class="partner-logo tuwaiq" src="https://events.kku.edu.sa/storage/uploads/sponser/IKNDr1gxKZbiFH9nP7HWY5D7UqeC4OTdpGCfWVt2.png" alt="Tuwaiq Academy">
      </div>
    </div>
    """))

# ---------- ABOUT ----------
elif st.session_state.page == "about":
    st.markdown("# ℹ️ About Virtual CyberLab")
    st.html(textwrap.dedent("""
    <div class="mission">
      <h2>Virtual CyberLab</h2>
      <p>A hands-on virtual cybersecurity laboratory designed to build awareness through investigation, decision-making and realistic digital scenarios.</p>
      <p><b>Educational Product Owner & Designer:</b> Aishah Ali Khawaji</p>
      <p><b>School:</b> Gifted Secondary School for Girls - Gizan</p>
      <p><b>School Principal:</b> Samia Hammadi</p>
      <p><b>Official School Email:</b> t281206@jzg.moe.gov.sa</p>
    </div>
    """))
    st.markdown("### 🎯 Learning Goals")
    st.write("- Recognize common cybersecurity risks.")
    st.write("- Analyze digital evidence before making decisions.")
    st.write("- Practice safe responses to security incidents.")
    st.write("- Build practical cybersecurity awareness.")
    if st.button("← BACK TO CYBERLAB"): go("home")

# ---------- RESOURCES ----------
elif st.session_state.page == "resources":
    st.markdown("# 📚 Resources")
    st.html(textwrap.dedent("""
    <div class="mission">
      <h3>Virtual CyberLab Resource Library</h3>
      <p>Use this area for cybersecurity awareness references, quick guides, checklists and classroom activities.</p>
    </div>
    """))
    rcols=st.columns(3)
    resources=[("🎣","Phishing Awareness","How to inspect senders, links, attachments and urgent requests."),("🔐","Password Security","Unique passwords, MFA and account-protection habits."),("🚨","Incident Response","Contain, preserve evidence, verify and escalate safely.")]
    for col,(ic,h,p) in zip(rcols,resources):
        with col: st.html(f'<div class="feature"><div class="feature-icon">{ic}</div><b>{h}</b><br><span>{p}</span></div>')
    st.markdown("### 🧭 Quick Safety Checklist")
    checklist=["Verify links independently before entering credentials.","Use unique passwords and enable MFA.","Deny unexpected MFA prompts.","Report suspicious activity through the approved school channel.","Preserve relevant evidence before deleting messages or logs."]
    for item in checklist: st.markdown(f"- {item}")
    if st.button("← BACK TO CYBERLAB"): go("home")

# ---------- CONTACT ----------
elif st.session_state.page == "contact":
    st.markdown("# ✉️ Contact")
    st.html(textwrap.dedent("""
    <div class="mission">
      <h3>Virtual CyberLab</h3>
      <p><b>Educational Product Owner:</b> Aishah Ali Khawaji</p>
      <p><b>School:</b> Gifted Secondary School for Girls - Gizan</p>
      <p><b>Principal:</b> Samia Hammadi</p>
      <p><b>Official School Email:</b> <a href="mailto:t281206@jzg.moe.gov.sa" style="color:#25d9ea;text-decoration:none;">t281206@jzg.moe.gov.sa</a></p>
    </div>
    """))
    st.caption("For official inquiries, please use the school email above.")
    if st.button("← BACK TO CYBERLAB"): go("home")

# ---------- PHISHING LAB HUB ----------
elif st.session_state.page == "phishing":
    st.markdown("# 🎣 Phishing Investigation")
    st.caption("LAB 01 • Four missions • Investigate evidence before making a decision.")
    ph=[("m1","01","The Suspicious Invoice","Analyze an urgent invoice email and identify multiple warning signs."),("m2","02","Fake Microsoft 365 Login","Inspect a sign-in message and determine whether the login request is trustworthy."),("m3","03","QR Code Phishing","Investigate a QR-code message designed to redirect a user to a fake page."),("m4","04","Social Engineering Message","Handle a convincing message that pressures you to bypass normal verification.")]
    cols=st.columns(2)
    for i,(mid,num,title,desc) in enumerate(ph):
        with cols[i%2]:
            done="✓ COMPLETED" if mid in st.session_state.completed else "MISSION READY"
            st.html(f'<div class="mission"><div style="color:#e16af0;font-size:11px;font-weight:800;">MISSION {num}</div><h3>{title}</h3><p>{desc}</p><div style="color:#2be0ec;font-size:11px;font-weight:700;">{done}</div></div>')
            if st.button("START MISSION  →",key=f"start_{mid}",use_container_width=True): go(mid)
    if st.button("← BACK TO CYBERLAB"): go("home")

# ---------- M1 ----------
elif st.session_state.page == "m1":
    st.markdown("# 🎣 Mission 01")
    st.caption("PHISHING LAB • Evidence-based investigation")
    st.html('<div class="mission"><h2>MISSION 01 — The Suspicious Invoice</h2><p>You are a junior security analyst supporting a school. A teacher reports an urgent invoice email.</p></div>')
    st.markdown("### 📩 Email Evidence")
    st.html(textwrap.dedent("""<div class="evidence"><b>From:</b> finance@school-payments.co<br><b>Subject:</b> ACTION REQUIRED — Outstanding Invoice<br><b>Message:</b> Your payment is overdue. Review the attached invoice immediately to avoid account suspension.<br><b>Attachment:</b> Invoice_September.html</div>"""))
    clues=st.multiselect("Which details are red flags? Select all that apply.",["Urgent language","Unfamiliar sender domain","HTML attachment","Request to act immediately","Normal school communication"],key="m1_clues")
    decision=st.radio("What should you do first?",["Open the attachment to verify it.","Forward it to colleagues.","Report the message and verify the request through a trusted channel.","Reply asking for the sender's password."],key="m1_decision")
    if st.button("SUBMIT INVESTIGATION",type="primary"):
        record_attempt("m1")
        points=(50 if set(clues)=={"Urgent language","Unfamiliar sender domain","HTML attachment","Request to act immediately"} else 0)+(50 if decision.startswith("Report") else 0)
        if points==100: complete("m1",100); st.success("MISSION COMPLETE — 100/100 🛡️"); st.info("Why: urgency, an unfamiliar domain and an HTML attachment are meaningful warning signs. Verify through a trusted channel.")
        else: st.warning(f"Investigation score: {points}/100. Review the evidence and try again.")
    mission_feedback("m1")
    if st.button("← BACK TO PHISHING LAB"): go("phishing")

# ---------- M2 ----------
elif st.session_state.page == "m2":
    st.markdown("# 🎣 Mission 02 — Fake Microsoft 365 Login")
    st.caption("PHISHING LAB • Inspect the destination before entering credentials.")
    st.html('<div class="mission"><h2>SCENARIO</h2><p>A student receives an email saying her Microsoft 365 session will expire in 10 minutes. The button says “Keep My Account Active.”</p></div>')
    st.html(textwrap.dedent("""<div class="evidence"><b>Sender:</b> microsoft-security@micr0soft-support.com<br><b>Button URL preview:</b> https://microsoft-account.verify-login.example<br><b>Message:</b> Immediate action required. Sign in now to avoid losing access.</div>"""))
    findings=st.multiselect("Select the strongest indicators of phishing.",["Look-alike sender domain","Urgent deadline","Unexpected sign-in request","URL does not use the organization's trusted domain","The message contains a greeting"],key="m2_findings")
    action=st.radio("What is the safest next step?",["Click the button and inspect the page.","Enter credentials but do not save them.","Use the official Microsoft 365 portal/bookmark instead of the email link and report the message.","Forward the email to a friend."],key="m2_action")
    if st.button("SUBMIT MISSION",type="primary"):
        record_attempt("m2")
        correct={"Look-alike sender domain","Urgent deadline","Unexpected sign-in request","URL does not use the organization's trusted domain"}
        findings_ok = set(findings)==correct
        action_ok = action.startswith("Use the official")
        awarded = 0
        if findings_ok and not st.session_state.get("m2_findings_awarded", False):
            st.session_state.m2_findings_awarded = True
            awarded += 50
        if action_ok and not st.session_state.get("m2_action_awarded", False):
            st.session_state.m2_action_awarded = True
            awarded += 50
        if awarded:
            st.session_state.score += awarded
            current = (50 if st.session_state.get("m2_findings_awarded", False) else 0) + (50 if st.session_state.get("m2_action_awarded", False) else 0)
            if current == 100 and "m2" not in st.session_state.completed:
                st.session_state.completed.add("m2")
                st.success("MISSION COMPLETE — 100/100 🛡️")
            else:
                st.info(f"Partial score recorded: +{awarded} points. Current mission score: {current}/100.")
            st.info("A familiar brand name does not make a link trustworthy. Verify the destination independently.")
        else:
            current = (50 if st.session_state.get("m2_findings_awarded", False) else 0) + (50 if st.session_state.get("m2_action_awarded", False) else 0)
            st.warning(f"No new points on this attempt. Current mission score: {current}/100.")
    mission_feedback("m2")
    if st.button("← BACK TO PHISHING LAB"): go("phishing")

# ---------- M3 ----------
elif st.session_state.page == "m3":
    st.markdown("# 🎣 Mission 03 — QR Code Phishing")
    st.caption("PHISHING LAB • QR codes can hide the real destination.")
    st.html('<div class="mission"><h2>SCENARIO</h2><p>A poster in a hallway says: “Scan to confirm your student account before Friday.” A QR code leads to a page requesting a school username, password and verification code.</p></div>')
    clues=st.multiselect("Which observations should make you pause?",["The QR code hides the destination until scanned","The request is unexpected","The page asks for a password","The page asks for an MFA verification code","The poster uses the school logo","The request creates pressure with a deadline"],key="m3_clues")
    action=st.radio("What should you do?",["Enter the requested information quickly.","Use the official school portal directly and report the suspicious poster/link.","Share the QR code with classmates.","Disable MFA so the page can work."],key="m3_action")
    if st.button("SUBMIT MISSION",type="primary"):
        record_attempt("m3")
        correct={"The QR code hides the destination until scanned","The request is unexpected","The page asks for a password","The page asks for an MFA verification code","The request creates pressure with a deadline"}
        pts=(50 if set(clues)==correct else 0)+(50 if action.startswith("Use the official") else 0)
        if pts==100: complete("m3",100); st.success("MISSION COMPLETE — 100/100 🛡️"); st.info("QR codes are simply another way to deliver a link. Treat the destination and credential request as you would any other link.")
        else: st.warning(f"Score: {pts}/100. Look at the hidden destination, unexpected request and credential collection.")
    mission_feedback("m3")
    if st.button("← BACK TO PHISHING LAB"): go("phishing")

# ---------- M4 ----------
elif st.session_state.page == "m4":
    st.markdown("# 🎣 Mission 04 — Social Engineering Message")
    st.caption("PHISHING LAB • Pressure is a signal to slow down, not a reason to bypass controls.")
    st.html('<div class="mission"><h2>SCENARIO</h2><p>A message appears to come from a senior staff member: “I am in a meeting. Buy three gift cards immediately and send me the codes. Do not call—I cannot talk.”</p></div>')
    redflags=st.multiselect("Identify the social-engineering indicators.",["Authority pressure","Urgency","Request to bypass normal communication","Request for gift-card codes","Instruction not to verify","A normal routine request"],key="m4_flags")
    response=st.radio("Choose your response.",["Complete the request immediately.","Verify the request through a known phone number or official channel before taking action.","Ask the sender for a different gift card brand.","Post the request in a public group."],key="m4_response")
    if st.button("SUBMIT MISSION",type="primary"):
        record_attempt("m4")
        correct={"Authority pressure","Urgency","Request to bypass normal communication","Request for gift-card codes","Instruction not to verify"}
        redflags_ok = set(redflags)==correct
        response_ok = response.startswith("Verify")
        awarded = 0
        if redflags_ok and not st.session_state.get("m4_redflags_awarded", False):
            st.session_state.m4_redflags_awarded = True
            awarded += 50
        if response_ok and not st.session_state.get("m4_response_awarded", False):
            st.session_state.m4_response_awarded = True
            awarded += 50
        if awarded:
            st.session_state.score += awarded
            current = (50 if st.session_state.get("m4_redflags_awarded", False) else 0) + (50 if st.session_state.get("m4_response_awarded", False) else 0)
            if current == 100 and "m4" not in st.session_state.completed:
                st.session_state.completed.add("m4")
                st.success("MISSION COMPLETE — 100/100 🛡️")
            else:
                st.info(f"Partial score recorded: +{awarded} points. Current mission score: {current}/100.")
            st.info("Social engineering often combines urgency, authority and isolation. Independent verification breaks the attacker's advantage.")
        else:
            current = (50 if st.session_state.get("m4_redflags_awarded", False) else 0) + (50 if st.session_state.get("m4_response_awarded", False) else 0)
            st.warning(f"No new points on this attempt. Current mission score: {current}/100.")
    mission_feedback("m4")
    if st.button("← BACK TO PHISHING LAB"): go("phishing")

# ---------- IDENTITY HUB ----------
elif st.session_state.page == "identity":
    st.markdown("# 🔐 Password & Identity Lab")
    st.caption("LAB 02 • Three missions • Protect credentials and account access.")
    ids=[("m5","05","The Reused Password","Investigate password reuse after an external breach."),("m6","06","MFA Alert","Respond to an unexpected multi-factor authentication prompt."),("m7","07","Account Takeover","Contain a compromised account and preserve evidence.")]
    cols=st.columns(3)
    for i,(mid,num,title,desc) in enumerate(ids):
        with cols[i]:
            done="✓ COMPLETED" if mid in st.session_state.completed else "MISSION READY"
            st.html(f'<div class="mission"><div style="color:#2be0ec;font-size:11px;font-weight:800;">MISSION {num}</div><h3>{title}</h3><p>{desc}</p><div style="color:#2be0ec;font-size:11px;font-weight:700;">{done}</div></div>')
            if st.button("START MISSION  →",key=f"start_{mid}",use_container_width=True): go(mid)
    if st.button("← BACK TO CYBERLAB"): go("home")

# ---------- M5 ----------
elif st.session_state.page == "m5":
    st.markdown("# 🔐 Mission 05 — The Reused Password")
    st.caption("PASSWORD & IDENTITY • Credential hygiene")
    st.html('<div class="mission"><h2>SCENARIO</h2><p>A student learns that an unrelated website she used was breached. She realizes the same password was used on the school portal for two years.</p></div>')
    st.html('<div class="evidence"><b>School Portal:</b> same password used for 2 years<br><b>External Website:</b> breach notification received<br><b>MFA:</b> enabled on school portal</div>')
    actions=st.multiselect("Choose all appropriate actions.",["Change the reused password","Use a unique password","Review recent account sessions","Keep the old password as a backup","Ignore the breach because MFA exists"],key="m5_actions")
    if st.button("SUBMIT RESPONSE",type="primary"):
        record_attempt("m5")
        correct={"Change the reused password","Use a unique password","Review recent account sessions"}
        if set(actions)==correct: complete("m5",100); st.success("MISSION COMPLETE — 100/100 🛡️"); st.info("MFA adds protection, but reused credentials still create risk and should be replaced.")
        else: st.warning("Review credential reuse and what MFA does—and does not—protect against.")
    mission_feedback("m5")
    if st.button("← BACK TO IDENTITY LAB"): go("identity")

# ---------- M6 ----------
elif st.session_state.page == "m6":
    st.markdown("# 🔐 Mission 06 — MFA Alert")
    st.caption("PASSWORD & IDENTITY • Unexpected authentication events")
    st.html('<div class="mission"><h2>SCENARIO</h2><p>While doing homework, a student receives three MFA approval prompts even though she did not attempt to sign in.</p></div>')
    choices=st.multiselect("Which conclusions/actions are appropriate?",["The prompts may indicate someone knows the password","Deny unexpected prompts","Change the password through the official portal","Report the event to the responsible school/team","Approve one prompt to make the notifications stop","Share the verification code with a friend"],key="m6_choices")
    if st.button("SUBMIT RESPONSE",type="primary"):
        record_attempt("m6")
        correct={"The prompts may indicate someone knows the password","Deny unexpected prompts","Change the password through the official portal","Report the event to the responsible school/team"}
        if set(choices)==correct: complete("m6",100); st.success("MISSION COMPLETE — 100/100 🛡️"); st.info("Unexpected MFA prompts can be a sign of an attempted account compromise. Never approve a request you did not initiate.")
        else: st.warning("Think about password compromise, denying unexpected prompts and reporting the event.")
    mission_feedback("m6")
    if st.button("← BACK TO IDENTITY LAB"): go("identity")

# ---------- M7 ----------
elif st.session_state.page == "m7":
    st.markdown("# 🔐 Mission 07 — Account Takeover")
    st.caption("PASSWORD & IDENTITY • Containment and recovery")
    st.html('<div class="mission"><h2>SCENARIO</h2><p>A student reports that her profile photo and recovery email changed without permission, and messages were sent from her account.</p></div>')
    order=st.multiselect("Select the appropriate response actions (order is not required).",["Use the official account-recovery process","Preserve relevant alerts/messages as evidence","Notify the responsible school/team","Tell classmates to use the same recovery link","Change credentials after securing recovery access"],key="m7_order")
    if st.button("SUBMIT RESPONSE",type="primary"):
        record_attempt("m7")
        correct={"Use the official account-recovery process","Preserve relevant alerts/messages as evidence","Notify the responsible school/team","Change credentials after securing recovery access"}
        if set(order)==correct: complete("m7",100); st.success("MISSION COMPLETE — 100/100 🛡️"); st.info("Recovery should use official channels while relevant evidence is preserved and the incident is escalated appropriately.")
        else: st.warning("Avoid untrusted recovery links and remember to preserve evidence while containing the account compromise.")
    mission_feedback("m7")
    if st.button("← BACK TO IDENTITY LAB"): go("identity")

# ---------- INCIDENT HUB ----------
elif st.session_state.page == "incident":
    st.markdown("# 🚨 Incident Response Lab")
    st.caption("LAB 03 • Three missions • Contain, investigate and respond.")
    incs=[("m8","08","Suspicious Login","Assess an unfamiliar login and decide how to contain it."),("m9","09","Malware Alert","Respond to a malware detection without destroying evidence."),("m10","10","Lost Device","Protect accounts and data after a school device is lost.")]
    cols=st.columns(3)
    for i,(mid,num,title,desc) in enumerate(incs):
        with cols[i]:
            done="✓ COMPLETED" if mid in st.session_state.completed else "MISSION READY"
            st.html(f'<div class="mission"><div style="color:#4aa9ff;font-size:11px;font-weight:800;">MISSION {num}</div><h3>{title}</h3><p>{desc}</p><div style="color:#2be0ec;font-size:11px;font-weight:700;">{done}</div></div>')
            if st.button("START MISSION  →",key=f"start_{mid}",use_container_width=True): go(mid)
    if st.button("← BACK TO CYBERLAB"): go("home")

# ---------- M8 ----------
elif st.session_state.page == "m8":
    st.markdown("# 🚨 Mission 08 — Suspicious Login")
    st.caption("INCIDENT RESPONSE • Contain while preserving evidence")
    st.html('<div class="mission"><h2>SCENARIO</h2><p>A security dashboard reports a login to a student account from an unfamiliar location at 02:14 AM using a device that has never been registered.</p></div>')
    st.html('<div class="evidence"><b>Time:</b> 02:14 AM<br><b>Location:</b> unfamiliar<br><b>Device:</b> not previously registered<br><b>MFA:</b> authentication approved</div>')
    steps=st.multiselect("Select appropriate response steps.",["Contact the account owner through a trusted channel","Review recent account activity","Secure the account according to school procedure","Post the alert publicly","Delete all logs"],key="m8_steps")
    if st.button("SUBMIT INCIDENT RESPONSE",type="primary"):
        record_attempt("m8")
        correct={"Contact the account owner through a trusted channel","Review recent account activity","Secure the account according to school procedure"}
        if set(steps)==correct: complete("m8",100); st.success("MISSION COMPLETE — 100/100 🛡️"); st.info("Contain the risk, verify the event and preserve logs for investigation.")
        else: st.warning("Review the principle of preserving evidence while containing the incident.")
    mission_feedback("m8")
    if st.button("← BACK TO INCIDENT LAB"): go("incident")

# ---------- M9 ----------
elif st.session_state.page == "m9":
    st.markdown("# 🚨 Mission 09 — Malware Alert")
    st.caption("INCIDENT RESPONSE • Safe containment")
    st.html('<div class="mission"><h2>SCENARIO</h2><p>An endpoint protection alert reports that a downloaded file attempted to launch a suspicious process on a school computer.</p></div>')
    actions=st.multiselect("What should the first response include?",["Follow the school's isolation/containment procedure","Preserve the alert and relevant logs","Open the suspicious file again to reproduce the issue","Notify the responsible technical/security team","Delete all evidence immediately"],key="m9_actions")
    if st.button("SUBMIT RESPONSE",type="primary"):
        record_attempt("m9")
        correct={"Follow the school's isolation/containment procedure","Preserve the alert and relevant logs","Notify the responsible technical/security team"}
        if set(actions)==correct: complete("m9",100); st.success("MISSION COMPLETE — 100/100 🛡️"); st.info("Containment reduces further exposure while evidence supports analysis and response.")
        else: st.warning("Do not execute suspicious files again. Think containment, evidence and escalation.")
    mission_feedback("m9")
    if st.button("← BACK TO INCIDENT LAB"): go("incident")

# ---------- M10 ----------
elif st.session_state.page == "m10":
    st.markdown("# 🚨 Mission 10 — Lost Device")
    st.caption("INCIDENT RESPONSE • Protect accounts and information")
    st.html('<div class="mission"><h2>SCENARIO</h2><p>A school laptop is reported missing after a classroom activity. The device may contain locally stored school files and an active browser session.</p></div>')
    actions=st.multiselect("Select the appropriate actions.",["Report the loss promptly through school procedure","Request remote lock/wipe if supported and authorized","Review and secure affected accounts","Wait a week in case the device is returned","Post the device details publicly"],key="m10_actions")
    if st.button("SUBMIT RESPONSE",type="primary"):
        record_attempt("m10")
        correct={"Report the loss promptly through school procedure","Request remote lock/wipe if supported and authorized","Review and secure affected accounts"}
        if set(actions)==correct: complete("m10",100); st.success("MISSION COMPLETE — 100/100 🛡️"); st.info("Fast reporting enables protective controls and account review before unauthorized access can occur.")
        else: st.warning("A lost device is an information-security incident. Report it quickly and use authorized protective controls.")
    mission_feedback("m10")
    if st.button("← BACK TO INCIDENT LAB"): go("incident")

# ---------- FINAL HUB ----------
elif st.session_state.page == "final":
    st.markdown("# 🏆 Final Cyber Challenge")
    st.caption("FINAL LAB • Two multi-step missions combining your investigation skills.")
    finals=[("m11","11","Data Leakage Investigation","Investigate an accidentally shared school folder and choose a safe response."),("m12","12","Cyber Defender Mission","Combine phishing, identity and incident-response evidence in one case.")]
    cols=st.columns(2)
    for i,(mid,num,title,desc) in enumerate(finals):
        with cols[i]:
            done="✓ COMPLETED" if mid in st.session_state.completed else "MISSION READY"
            st.html(f'<div class="mission"><div style="color:#ffc12b;font-size:11px;font-weight:800;">MISSION {num}</div><h3>{title}</h3><p>{desc}</p><div style="color:#2be0ec;font-size:11px;font-weight:700;">{done}</div></div>')
            if st.button("START MISSION  →",key=f"start_{mid}",use_container_width=True): go(mid)
    if st.button("← BACK TO CYBERLAB"): go("home")

# ---------- M11 ----------
elif st.session_state.page == "m11":
    st.markdown("# 🏆 Mission 11 — Data Leakage Investigation")
    st.caption("FINAL CHALLENGE • Access control and evidence")
    st.html('<div class="mission"><h2>SCENARIO</h2><p>A shared school folder containing student project files is discovered to be accessible to people outside the organization. A public link may have been active for several hours.</p></div>')
    st.html('<div class="evidence"><b>Access:</b> “Anyone with the link”<br><b>Content:</b> student project files<br><b>Discovery:</b> reported by a teacher<br><b>Unknown:</b> who accessed the files and whether copies were made</div>')
    response=st.radio("What should happen first?",["Ignore it until someone reports a problem.","Preserve relevant information, restrict inappropriate access, and notify the responsible team.","Delete the entire folder immediately.","Share the link with more users to test it."],key="m11_q")
    follow=st.multiselect("Which follow-up actions are appropriate?",["Review sharing/access logs if available","Document what was discovered and when","Restore the intended access settings","Publicly name suspected users","Assess whether affected users need notification"],key="m11_follow")
    if st.button("SUBMIT FINAL DECISION",type="primary"):
        record_attempt("m11")
        correct_follow={"Review sharing/access logs if available","Document what was discovered and when","Restore the intended access settings","Assess whether affected users need notification"}
        pts=(60 if response.startswith("Preserve") else 0)+(40 if set(follow)==correct_follow else 0)
        if pts==100: complete("m11",100); st.success("MISSION COMPLETE — 100/100 🛡️"); st.info("Contain the exposure, preserve evidence and assess impact through the appropriate process.")
        else: st.warning(f"Score: {pts}/100. Think containment, evidence, access control and impact assessment.")
    mission_feedback("m11")
    if st.button("← BACK TO FINAL CHALLENGE"): go("final")

# ---------- M12 ----------
elif st.session_state.page == "m12":
    st.markdown("# 🏆 Mission 12 — Cyber Defender Mission")
    st.caption("FINAL CHALLENGE • Multi-step investigation")
    st.html('<div class="mission"><h2>CASE FILE</h2><p>At 08:10 AM, a teacher reports an unexpected MFA prompt. At 08:16 AM, an email from the same account sends a link to a “shared document.” At 08:20 AM, the security dashboard records a new device login.</p></div>')
    st.html('<div class="evidence"><b>Evidence A:</b> unexpected MFA prompt<br><b>Evidence B:</b> suspicious link sent from the account<br><b>Evidence C:</b> unfamiliar device login<br><b>Evidence D:</b> user denies initiating any of these actions</div>')
    first=st.radio("What should be your first priority?",["Ask the user to approve the next MFA prompt.","Contain and secure the account through the approved process while preserving evidence.","Delete the suspicious email and close the case.","Send the suspicious link to other users for testing."],key="m12_first")
    indicators=st.multiselect("Which evidence points to possible account compromise?",["Unexpected MFA prompt","Suspicious link sent from the account","Unfamiliar device login","User denies initiating the activity","The event happened during school hours"],key="m12_indicators")
    final_action=st.radio("After containment, what should happen next?",["Document evidence, review account activity and escalate through the appropriate process.","Publish the incident details publicly.","Ignore the event because MFA was enabled.","Delete all logs to protect privacy."],key="m12_final")
    if st.button("SUBMIT CYBER DEFENDER MISSION",type="primary"):
        record_attempt("m12")
        pts=(40 if first.startswith("Contain") else 0)+(30 if set(indicators)=={"Unexpected MFA prompt","Suspicious link sent from the account","Unfamiliar device login","User denies initiating the activity"} else 0)+(30 if final_action.startswith("Document") else 0)
        if pts==100: complete("m12",100); st.success("CYBER DEFENDER MISSION COMPLETE — 100/100 🛡️"); st.balloons(); st.info("You connected identity signals, phishing evidence and an endpoint event into one incident-response decision.")
        else: st.warning(f"Case score: {pts}/100. Re-check the evidence chain and prioritize containment, preservation and escalation.")
    mission_feedback("m12")
    if st.button("← BACK TO FINAL CHALLENGE"): go("final")
