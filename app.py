
import streamlit as st
import streamlit.components.v1 as components
import textwrap
import io
import json
import random
import string
import urllib.request
import urllib.error
import threading
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
.stat{background:linear-gradient(145deg,rgba(10,48,77,.88),rgba(4,23,41,.92));border:1px solid #1a587a;border-radius:16px;padding:9px 8px;text-align:center;min-height:70px;height:auto;box-sizing:border-box}.stat-label{font-size:9px;color:#aec1cd;letter-spacing:.7px}.stat-value{font-size:21px;font-weight:800;color:#5ff6ff!important;margin-top:5px;text-shadow:0 0 8px rgba(32,217,234,.25)}.gold{color:#ffc12b!important}
.stMetric [data-testid="stMetricValue"]{color:#5ff6ff!important;font-weight:800!important;text-shadow:0 0 8px rgba(32,217,234,.25)}.stMetric label,.stMetric [data-testid="stMetricLabel"]{color:#d7e8f1!important}.section-title{font-size:16px;font-weight:800;margin:15px 0 9px}
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

/* Teacher dashboard: keep the original table on desktop and use a compact table-like layout on phones. */
.st-key-teacher_desktop_table [data-testid="stDownloadButton"],.st-key-teacher_desktop_table .stButton{width:100%!important;min-width:0!important}.st-key-teacher_desktop_table [data-testid="stDownloadButton"] button,.st-key-teacher_desktop_table .stButton>button{width:100%!important;box-sizing:border-box!important}
.st-key-teacher_mobile_table{display:none!important}
.st-key-teacher_desktop_table{display:block!important}
.st-key-teacher_mobile_table [data-testid="stVerticalBlock"]{gap:.25rem!important}.st-key-teacher_mobile_table [class*="st-key-mobile_"]{padding-bottom:12px!important;margin-bottom:10px!important;border-bottom:1px solid rgba(60,150,200,.22)!important}.st-key-teacher_mobile_table [class*="st-key-mobile_"] .stHorizontalBlock{margin-bottom:0!important}
@media (max-width:600px){
  .st-key-teacher_desktop_table{display:none!important}
  .st-key-teacher_mobile_table{display:block!important}
  .st-key-teacher_mobile_table [data-testid="stHorizontalBlock"]{align-items:center!important;gap:.5rem!important}.st-key-teacher_mobile_table .stButton,.st-key-teacher_mobile_table [data-testid="stDownloadButton"]{min-width:0!important;width:100%!important}
  .st-key-teacher_mobile_table .stButton>button,.st-key-teacher_mobile_table [data-testid="stDownloadButton"] button{font-size:9px!important;min-height:32px!important;padding:2px 4px!important;width:100%!important;box-sizing:border-box!important}
  .st-key-teacher_mobile_table .stCaption,.st-key-teacher_mobile_table [data-testid="stCaptionContainer"]{font-size:9px!important}
}

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
if "learner_id" not in st.session_state: st.session_state.learner_id = ""
if "learner_name" not in st.session_state: st.session_state.learner_name = ""
if "db_ready" not in st.session_state: st.session_state.db_ready = False
if "show_new_id_card" not in st.session_state: st.session_state.show_new_id_card = False
if "student_login_error" not in st.session_state: st.session_state.student_login_error = ""
if "current_mission" not in st.session_state: st.session_state.current_mission = ""

# ---------- SUPABASE PERSISTENCE ----------
# Uses the server-side Supabase key from Streamlit Secrets. The key is never shown to learners.
# If the app is opened locally before Secrets are configured, start normally and
# show the setup warning in the UI instead of crashing.
try:
    _secrets = st.secrets
    SUPABASE_URL = str(_secrets.get("SUPABASE_URL", "")).rstrip("/")
    SUPABASE_KEY = str(_secrets.get("SUPABASE_KEY", ""))
    TEACHER_PASSWORD = str(_secrets.get("TEACHER_PASSWORD", ""))
except Exception:
    SUPABASE_URL = ""
    SUPABASE_KEY = ""
    TEACHER_PASSWORD = ""


def _supabase_request(method, table, params="", payload=None):
    if not SUPABASE_URL or not SUPABASE_KEY:
        return None, "Supabase secrets are not configured."
    url = f"{SUPABASE_URL}/rest/v1/{table}"
    if params:
        url += "?" + params
    headers = {
        "apikey": SUPABASE_KEY,
        "Content-Type": "application/json",
        "Prefer": "return=representation",
    }
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=12) as resp:
            raw = resp.read().decode("utf-8")
            return (json.loads(raw) if raw else []), None
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        return None, f"Supabase error {e.code}: {body[:300]}"
    except Exception as e:
        return None, str(e)


def _new_student_id():
    # Generate the ID locally. The previous version made a Supabase GET request
    # just to check whether the random ID was free, which delayed new-learner login.
    # The 8-character random suffix makes collisions extremely unlikely.
    alphabet = string.ascii_uppercase + string.digits
    return "VCL-" + "".join(random.choice(alphabet) for _ in range(8))


def _collect_state():
    awarded = {k: bool(v) for k, v in st.session_state.items() if k.endswith("_awarded") and isinstance(v, bool)}
    attempts = {k.replace("attempts_", ""): int(v) for k, v in st.session_state.items() if k.startswith("attempts_")}
    return {
        "student_id": st.session_state.learner_id,
        "learner_name": st.session_state.get("learner_name", "Learner"),
        "score": int(st.session_state.score),
        "completed": sorted(list(st.session_state.completed)),
        "attempts": attempts,
        "awarded": awarded,
        "updated_at": datetime.utcnow().isoformat() + "Z",
    }


def save_progress():
    sid = st.session_state.get("learner_id", "")
    if not sid or not SUPABASE_URL or not SUPABASE_KEY:
        return False
    data = _collect_state()
    # Update an existing learner record. If no row exists yet, create it.
    rows, err = _supabase_request("PATCH", "vcl_learners", f"student_id=eq.{sid}", payload=data)
    if err is not None:
        return False
    if rows == []:
        _, insert_err = _supabase_request("POST", "vcl_learners", payload=data)
        return insert_err is None
    return True


def load_progress(student_id):
    rows, err = _supabase_request("GET", "vcl_learners", f"select=*&student_id=eq.{student_id}&limit=1")
    if err or not rows:
        return None, err or "Student ID not found."
    row = rows[0]
    st.session_state.learner_id = row.get("student_id", "")
    st.session_state.learner_name = row.get("learner_name", "Learner")
    st.session_state.score = int(row.get("score", 0) or 0)
    st.session_state.completed = set(row.get("completed") or [])
    st.session_state.current_mission = str(row.get("current_mission") or "")
    for key in list(st.session_state.keys()):
        if key.startswith("attempts_") or key.endswith("_awarded"):
            del st.session_state[key]
    for mission, count in (row.get("attempts") or {}).items():
        st.session_state[f"attempts_{mission}"] = int(count)
    for key, value in (row.get("awarded") or {}).items():
        st.session_state[key] = bool(value)

    # Rebuild the score from the awarded step flags so legacy records created
    # by the previous step-scoring bug are corrected automatically.
    score_weights = {
        "m1_sender_awarded":20, "m1_clues_awarded":40, "m1_decision_awarded":25, "m1_consequence_awarded":15,
        "m2_findings_awarded":40, "m2_credential_awarded":30, "m2_action_awarded":30,
        "m3_findings_awarded":40, "m3_assessment_awarded":20, "m3_action_awarded":30, "m3_consequence_awarded":10,
        "m4_flags_awarded":40, "m4_reason_awarded":20, "m4_verify_awarded":30, "m4_consequence_awarded":10,
        "m5_findings_awarded":30, "m5_priority_awarded":25, "m5_actions_awarded":30, "m5_consequence_awarded":15,
        "m6_obs_awarded":25, "m6_immediate_awarded":30, "m6_next_awarded":30, "m6_lesson_awarded":15,
        "m7_ind_awarded":25, "m7_contain_awarded":30, "m7_recovery_awarded":25, "m7_evidence_awarded":20,
        "m8_assess_awarded":25, "m8_contain_awarded":25, "m8_verify_awarded":25, "m8_recover_awarded":25,
        "m9_assess_awarded":25, "m9_contain_awarded":25, "m9_investigate_awarded":25, "m9_communicate_awarded":25,
        "m10_triage_awarded":25, "m10_contain_awarded":25, "m10_evidence_awarded":25, "m10_escalate_awarded":25,
        "m11_report_awarded":25, "m11_protect_awarded":25, "m11_assess_awarded":25, "m11_communicate_awarded":25,
        "m12_detect_awarded":25, "m12_contain_awarded":25, "m12_evidence_awarded":25, "m12_escalate_awarded":25,
        "m13_scope_awarded":25, "m13_contain_awarded":30, "m13_follow_awarded":30, "m13_consequence_awarded":15,
        "m14_chain_awarded":25, "m14_priority_awarded":25, "m14_actions_awarded":20, "m14_reason_awarded":15, "m14_communication_awarded":15,
        "m15_timeline_awarded":25, "m15_integrity_awarded":25, "m15_analysis_awarded":25, "m15_communication_awarded":25,
        "m16_detect_awarded":25, "m16_contain_awarded":25, "m16_investigate_awarded":25, "m16_impact_awarded":25,
    }
    step_score = sum(points for flag, points in score_weights.items() if st.session_state.get(flag, False))
    # A completed mission is always worth 100 points. This also repairs older
    # records where the mission was marked complete but some step-award flags
    # were not saved correctly.
    completed_score = len(st.session_state.completed) * 100
    recalculated_score = min(1600, max(step_score, completed_score))
    if recalculated_score != st.session_state.score:
        st.session_state.score = recalculated_score
        st.session_state.progress_dirty = True

    st.session_state.db_ready = True
    # Keep progress_dirty=True when the score was repaired so the corrected
    # score is written back to Supabase on the normal save cycle.
    st.session_state.show_new_id_card = False
    return row, None


def _save_new_learner_background(data):
    # Save the initial account without blocking the learner's transition to Home.
    # The UI can render immediately while this single Supabase request completes.
    try:
        _supabase_request("POST", "vcl_learners", payload=data)
    except Exception:
        pass


def start_new_learner(name):
    if not SUPABASE_URL or not SUPABASE_KEY:
        return None, "Supabase is not configured yet."
    learner_name = name.strip()
    if not learner_name:
        return None, "Please enter your name before creating your Student ID."
    sid = _new_student_id()
    st.session_state.learner_id = sid
    st.session_state.learner_name = learner_name
    st.session_state.score = 0
    st.session_state.completed = set()
    st.session_state.current_mission = ""
    for key in list(st.session_state.keys()):
        if key.startswith("attempts_") or key.endswith("_awarded"):
            del st.session_state[key]
    st.session_state.db_ready = True
    st.session_state.progress_dirty = False
    st.session_state.show_new_id_card = True

    # Do not wait for Supabase before showing the learner's Home page.
    # The initial record is inserted in the background; later progress saves
    # continue to use the normal save_progress() flow.
    data = {
        "student_id": sid,
        "learner_name": learner_name,
        "score": 0,
        "completed": [],
        "attempts": {},
        "awarded": {},
        "updated_at": datetime.utcnow().isoformat() + "Z",
    }
    threading.Thread(target=_save_new_learner_background, args=(data,), daemon=True).start()
    return sid, None



def _continue_student_callback():
    continue_id = str(st.session_state.get("continue_student_id", "")).strip().upper()
    st.session_state.student_login_error = ""
    if not continue_id:
        st.session_state.student_login_error = "Please enter your Student ID."
        return
    row, err = load_progress(continue_id)
    if err:
        st.session_state.student_login_error = err
        return
    st.session_state.show_new_id_card = False
    st.session_state.page = "home"
    try:
        st.query_params.clear()
    except Exception:
        pass


def _create_student_callback():
    name = str(st.session_state.get("new_learner_name", "")).strip()
    st.session_state.student_login_error = ""
    if not name:
        st.session_state.student_login_error = "Please enter your name before creating your Student ID."
        return
    sid, err = start_new_learner(name)
    if err:
        st.session_state.student_login_error = err
        return
    st.session_state.show_new_id_card = True
    st.session_state.page = "home"
    try:
        st.query_params.clear()
    except Exception:
        pass

def go(page):
    if page in {f"m{i}" for i in range(1, 17)}:
        st.session_state.current_mission = page
    st.session_state.page = page
    try:
        st.query_params.clear()
    except Exception:
        pass
    st.rerun()


def logout_learner():
    # Save the latest progress before ending the learner session.
    try:
        save_progress()
    except Exception:
        pass
    # Clear the current learner session so the next person must sign in.
    st.session_state.clear()
    st.session_state.page = "home"
    st.session_state.show_new_id_card = False


def complete(mission, points):
    # Award points for an individual mission step.
    # Mission completion is recorded only after all steps reach 100%.
    st.session_state.score += points
    st.session_state.progress_dirty = True


def record_attempt(mission):
    key = f"attempts_{mission}"
    st.session_state[key] = st.session_state.get(key, 0) + 1
    st.session_state.progress_dirty = True


def mission_feedback(mission):
    attempts = st.session_state.get(f"attempts_{mission}", 0)
    if attempts:
        st.caption(f"Attempts: {attempts}")


def reset_progress():
    st.session_state.score = 0
    st.session_state.completed = set()
    st.session_state.current_mission = ""
    for key in list(st.session_state.keys()):
        if key.startswith("attempts_") or key.endswith("_awarded"):
            del st.session_state[key]
    save_progress()


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
    data=[["Metric","Result"],["Security Score",f"{st.session_state.score}/1600"],["Missions Completed",f"{len(st.session_state.completed)}/16"],["Badge",badge_name(st.session_state.score)]]
    t=Table(data,colWidths=[220,220]); t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#123d59')),('TEXTCOLOR',(0,0),(-1,0),colors.white),('GRID',(0,0),(-1,-1),0.5,colors.HexColor('#9ab7c8')),('PADDING',(0,0),(-1,-1),7)])); story += [t,Spacer(1,14)]
    story.append(Paragraph("Completed Missions", styles["Heading2"]))
    if st.session_state.completed:
        for mid in sorted(st.session_state.completed): story.append(Paragraph(f"• {MISSIONS[mid]}", styles["Normal"]))
    else: story.append(Paragraph("No missions completed yet.", styles["Normal"]))
    story += [Spacer(1,18), Paragraph("Developed & Designed by Aishah Ali Khawaji", center), Paragraph("Gifted Secondary School for Girls - Gizan • School Principal: Samia Hammadi", center)]
    doc.build(story); buf.seek(0); return buf.getvalue()


def build_progress_pdf_for_row(row):
    try:
        from reportlab.lib.pagesizes import A4
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.enums import TA_CENTER
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
        from reportlab.lib import colors
    except ModuleNotFoundError:
        return None
    buf = io.BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=A4, rightMargin=42, leftMargin=42, topMargin=42, bottomMargin=42)
    styles = getSampleStyleSheet()
    title = ParagraphStyle("title", parent=styles["Title"], alignment=TA_CENTER, fontSize=20, leading=24)
    center = ParagraphStyle("center", parent=styles["Normal"], alignment=TA_CENTER, fontSize=10, leading=14)
    name = str(row.get("learner_name") or "Learner")
    sid = str(row.get("student_id") or "")
    score = int(row.get("score", 0) or 0)
    completed = row.get("completed") or []
    story=[Paragraph("Virtual CyberLab", title), Paragraph("Virtual Cybersecurity Laboratory", center), Spacer(1,14)]
    story.append(Paragraph(f"Learner: {name}", styles["Normal"]))
    story.append(Paragraph(f"Student ID: {sid}", styles["Normal"]))
    story.append(Paragraph(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}", styles["Normal"]))
    story.append(Spacer(1,10))
    data=[["Metric","Result"],["Security Score",f"{score}/1600"],["Missions Completed",f"{len(completed)}/16"],["Badge",badge_name(score)]]
    t=Table(data,colWidths=[220,220]); t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#123d59')),('TEXTCOLOR',(0,0),(-1,0),colors.white),('GRID',(0,0),(-1,-1),0.5,colors.HexColor('#9ab7c8')),('PADDING',(0,0),(-1,-1),7)])); story += [t,Spacer(1,14)]
    story.append(Paragraph("Completed Missions", styles["Heading2"]))
    if completed:
        for mid in sorted(completed): story.append(Paragraph(f"• {MISSIONS.get(mid, mid)}", styles["Normal"]))
    else: story.append(Paragraph("No missions completed yet.", styles["Normal"]))
    story += [Spacer(1,18), Paragraph("Developed & Designed by Aishah Ali Khawaji", center), Paragraph("Gifted Secondary School for Girls - Gizan • School Principal: Samia Hammadi", center)]
    doc.build(story); buf.seek(0); return buf.getvalue()

def badge_name(score):
    if score >= 1600: return "CYBER DEFENDER"
    if score >= 1200: return "CYBER SPECIALIST"
    if score >= 800: return "CYBER GUARDIAN"
    if score >= 400: return "CYBER EXPLORER"
    return "IN PROGRESS"

MISSIONS = {
    "m1": "The Suspicious Invoice", "m2": "Fake Microsoft 365 Login",
    "m3": "QR Code Phishing", "m4": "Social Engineering Message",
    "m5": "The Reused Password", "m6": "MFA Alert",
    "m7": "Account Takeover", "m8": "Credential Security Investigation",
    "m9": "Suspicious Login", "m10": "Malware Alert",
    "m11": "Lost Device", "m12": "Ransomware Incident",
    "m13": "Data Leakage Investigation", "m14": "Account Compromise Investigation",
    "m15": "Digital Evidence Case", "m16": "Cyber Defender: Final Mission"
}

# ---------- GLOBAL NAVIGATION ----------

# ---------- LEARNER ACCESS / TEACHER ACCESS ----------
page_from_url = st.query_params.get("page")

allowed_pages = {"home","about","resources","contact","student_access","phishing","identity","incident","final","m1","m2","m3","m4","m5","m6","m7","m8","m9","m10","m11","m12","m13","m14","m15","m16","teacher"}
lab_pages = {"phishing","identity","incident","final","m1","m2","m3","m4","m5","m6","m7","m8","m9","m10","m11","m12","m13","m14","m15","m16"}

# URL navigation is applied only when a page parameter is actually present.
# This prevents a button click (which uses session state) from being reset to HOME.
if page_from_url in allowed_pages:
    st.session_state.page = page_from_url

# Keep the labs protected until a learner has successfully entered.
if st.session_state.page in lab_pages and not st.session_state.get("learner_id"):
    st.session_state.page = "home"

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

    if not st.session_state.get("learner_id"):
        st.html('<div class="section-title">ACCESS THE CYBERLAB</div>')
        st.markdown('<div style="text-align:center;color:#9fb4c2;margin-bottom:14px;">Choose your access type to continue.</div>', unsafe_allow_html=True)
        access_a, access_b = st.columns(2)
        with access_a:
            if st.button("👩🏻‍🎓  STUDENT ACCESS", key="student_access_btn", use_container_width=True):
                go("student_access")
        with access_b:
            if st.button("👩🏻‍💻  TEACHER ACCESS", key="teacher_access_btn", use_container_width=True):
                go("teacher")
        st.html('<div style="text-align:center;color:#6f8796;font-size:11px;margin-top:12px;">Student access is required before entering the cybersecurity labs.</div>')
    else:
        # Display the learner name as a styled welcome label (not an editable white input).
        learner_display = st.session_state.get("learner_name", "Learner") or "Learner"
        st.html(f"""
        <div style="margin:10px auto 8px;max-width:760px;text-align:center;">
          <div style="font-size:11px;letter-spacing:1.8px;color:#7fdbe8;font-weight:700;text-transform:uppercase;">Welcome back</div>
          <div style="margin-top:4px;font-size:25px;font-weight:800;letter-spacing:.4px;color:#ffffff;text-shadow:0 0 14px rgba(32,217,234,.22);">{learner_display}</div>
          <div style="margin-top:3px;font-size:11px;color:#819aa9;letter-spacing:1px;">CYBERLAB LEARNER</div>
        </div>
        """)

        # Show the Student ID card + COPY only immediately after creating a new learner.
        # Returning learners see only their welcome/name area.
        if st.session_state.get("show_new_id_card", False):
            student_id = st.session_state.get("learner_id", "")
            copy_html = f"""
            <div style="margin:12px auto 16px;max-width:760px;padding:18px 22px;border:1px solid #20d9ea;border-radius:18px;background:linear-gradient(145deg,rgba(8,52,78,.96),rgba(4,24,42,.98));box-shadow:0 0 24px rgba(32,217,234,.12);">
              <div style="text-align:center;font-size:11px;letter-spacing:1.4px;color:#8fdbe5;font-weight:700;">YOUR STUDENT ID</div>
              <div style="display:flex;align-items:center;justify-content:center;gap:16px;margin-top:8px;">
                <div style="font-size:32px;line-height:1.2;font-weight:800;letter-spacing:2.5px;color:#ffffff;word-break:break-all;">{student_id}</div>
                <button id="copyBtn" onclick="copyStudentId()" style="flex:0 0 auto;border:1px solid #20d9ea;border-radius:10px;background:rgba(10,92,120,.65);color:#ffffff;padding:10px 14px;font-weight:800;cursor:pointer;">📋 COPY</button>
              </div>
              <div style="text-align:center;font-size:11px;color:#a9c5d2;margin-top:8px;">Save this ID to continue your progress from another session or device.</div>
            </div>
            <script>
            function copyStudentId() {{
              const id = {student_id!r};
              const btn = document.getElementById('copyBtn');
              navigator.clipboard.writeText(id).then(() => {{
                btn.textContent = '✓ COPIED';
                setTimeout(() => btn.textContent = '📋 COPY', 1500);
              }}).catch(() => {{
                const ta = document.createElement('textarea');
                ta.value = id; document.body.appendChild(ta); ta.select();
                document.execCommand('copy'); ta.remove();
                btn.textContent = '✓ COPIED';
                setTimeout(() => btn.textContent = '📋 COPY', 1500);
              }});
            }}
            </script>
            """
            components.html(copy_html, height=142, scrolling=False)

        a,b,c,d=st.columns(4)
        vals=[(a,"SECURITY SCORE",st.session_state.score,""),(b,"MISSIONS",len(st.session_state.completed),""),(c,"TOTAL MISSIONS",16,""),(d,"BADGE",badge_name(st.session_state.score),"gold")]
        for col,label,val,cl in vals:
            with col: st.html(f'<div class="stat"><div class="stat-label">{label}</div><div class="stat-value {cl}">{val}</div></div>')

        st.html('<div style="text-align:center;color:#829bab;font-size:10px;margin:6px 0 2px;">Badge levels: 400 Explorer • 800 Guardian • 1200 Specialist • 1600 Defender</div>')
        progress = len(st.session_state.completed) / len(MISSIONS)
        st.progress(progress, text=f"Mission Progress • {len(st.session_state.completed)}/{len(MISSIONS)} completed")
        if st.session_state.completed:
            pdf_bytes = build_progress_pdf()
            if pdf_bytes:
                st.download_button("📄 DOWNLOAD PROGRESS REPORT", pdf_bytes, file_name="Virtual_CyberLab_Progress_Report.pdf", mime="application/pdf", use_container_width=True)
        action_a, action_b = st.columns(2)
        with action_a:
            if st.button("↻ RESET PROGRESS", use_container_width=True):
                reset_progress()
                st.rerun()
        with action_b:
            if st.button("🚪 LOG OUT", use_container_width=True, key="learner_logout"):
                logout_learner()
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

# ---------- STUDENT ACCESS ----------

elif st.session_state.page == "student_access":
    st.html(textwrap.dedent("""
    <div class="hero">
      <div class="hero-kicker">Student Entry</div>
      <div class="hero-title">🛡️ <span class="cyan">Virtual</span> <span class="cyan">Cyber</span><span class="purple">Lab</span></div>
      <div class="hero-desc">VIRTUAL CYBERSECURITY LABORATORY</div>
    </div>
    """))
    st.html(nav_html)
    st.html('<div class="section-title">STUDENT ACCESS</div>')
    if not SUPABASE_URL or not SUPABASE_KEY:
        st.warning("Student progress saving is not configured yet. Add SUPABASE_URL and SUPABASE_KEY in Streamlit Secrets before using learner accounts.")
    # Do not render the login widgets after a successful login.
    # This prevents the old input boxes from flashing during Streamlit reruns.
    if not st.session_state.get("learner_id"):
        a, b = st.columns(2)
        with a:
            st.markdown("### 🆕 New Learner")
            st.text_input("Learner name (required)", key="new_learner_name", placeholder="Enter your name")
            if st.session_state.get("student_login_error"):
                st.error(st.session_state.student_login_error)
            st.button("CREATE STUDENT ID", key="create_student_id", use_container_width=True, disabled=not bool(SUPABASE_URL and SUPABASE_KEY), on_click=_create_student_callback)
        with b:
            st.markdown("### 🔄 Continue")
            st.text_input("Student ID (Use your own code)", key="continue_student_id", placeholder="Example: VCL-A1B2C3D4")
            st.button("CONTINUE", key="continue_student", use_container_width=True, disabled=not bool(SUPABASE_URL and SUPABASE_KEY), on_click=_continue_student_callback)
        if st.session_state.get("student_login_error"):
            st.error(st.session_state.student_login_error)
        if st.button("← BACK TO HOME", key="student_access_back", use_container_width=True):
            st.session_state.page = "home"
            st.rerun()
    else:
        # Safety redirect if the page state lags behind the authenticated session.
        # Clear the URL page parameter first so it cannot immediately switch
        # the app back to Student Access on the next rerun.
        st.session_state.page = "home"
        try:
            st.query_params.clear()
        except Exception:
            pass
        st.rerun()


# ---------- ABOUT ----------

elif st.session_state.page == "teacher":
    st.markdown("# 👩🏻‍💻 Teacher Dashboard")
    st.caption("Virtual CyberLab • Learner progress overview")
    if not TEACHER_PASSWORD:
        st.error("Teacher dashboard is not configured. Add TEACHER_PASSWORD to Streamlit Secrets.")
    else:
        if not st.session_state.get("teacher_authenticated", False):
            password = st.text_input("Teacher password", type="password", key="teacher_password")
            if st.button("SIGN IN", key="teacher_signin", use_container_width=True):
                st.session_state.teacher_authenticated = password == TEACHER_PASSWORD
                if not st.session_state.teacher_authenticated:
                    st.error("Incorrect teacher password.")
                    st.rerun()
                st.rerun()
        if st.session_state.get("teacher_authenticated", False):
            rows, err = _supabase_request("GET", "vcl_learners", "select=student_id,learner_name,score,completed,attempts,updated_at&order=updated_at.desc")
            if err:
                st.error(err)
            else:
                rows = rows or []
                total = len(rows)
                completed_count = sum(1 for r in rows if len(r.get("completed") or []) == 16)
                scored_rows = [r for r in rows if int(r.get("score", 0) or 0) > 0]
                avg_score = round(sum(int(r.get("score",0) or 0) for r in scored_rows) / len(scored_rows), 1) if scored_rows else 0
                avg_progress = round(sum(len(r.get("completed") or []) for r in rows) / (total*16) * 100, 1) if total else 0
                c1,c2,c3,c4 = st.columns(4)
                c1.metric("LEARNERS", total)
                c2.metric("COMPLETED", completed_count)
                c3.metric("AVERAGE SCORE", f"{avg_score}/1600")
                c4.metric("AVERAGE PROGRESS", f"{avg_progress}%")
                st.markdown("### Learner Progress")
                search = st.text_input("Search by name or Student ID", key="teacher_search")
                q = search.strip().lower()
                filtered_rows = []
                for r in rows:
                    sid = str(r.get("student_id", ""))
                    name = str(r.get("learner_name", ""))
                    if q and q not in sid.lower() and q not in name.lower():
                        continue
                    filtered_rows.append(r)

                if filtered_rows:
                    pending = st.session_state.get("teacher_delete_pending", "")

                    # Desktop/table view — kept close to the original dashboard.
                    with st.container(key="teacher_desktop_table"):
                        header = st.columns([1.45, 1.35, 0.9, 0.95, 1.55, 2.05])
                        for col, label in zip(header, ["Student ID", "Name", "Score", "Progress", "Last Update", "Actions"]):
                            col.markdown(f"**{label}**")
                        for r in filtered_rows:
                            sid = str(r.get("student_id", ""))
                            name = str(r.get("learner_name", ""))
                            score = int(r.get("score", 0) or 0)
                            completed = len(r.get("completed") or [])
                            updated = str(r.get("updated_at", ""))[:19].replace("T", " ")
                            cols = st.columns([1.45, 1.35, 0.9, 0.95, 1.55, 2.05])
                            cols[0].write(sid)
                            cols[1].write(name)
                            cols[2].write(f"{score}/1600")
                            cols[3].write(f"{completed}/16")
                            cols[4].write(updated)
                            with cols[5]:
                                ra, da = st.columns(2)
                                pdf = build_progress_pdf_for_row(r)
                                ra.download_button("📄 REPORT", data=pdf or b"", file_name=f"Virtual_CyberLab_{sid}_Report.pdf", mime="application/pdf", key=f"teacher_report_d_{sid}", disabled=pdf is None, use_container_width=True)
                                if pending == sid:
                                    if da.button("✓ CONFIRM", key=f"confirm_delete_d_{sid}", use_container_width=True):
                                        _, delete_err = _supabase_request("DELETE", "vcl_learners", f"student_id=eq.{sid}")
                                        if delete_err:
                                            st.error(delete_err)
                                        else:
                                            st.session_state.teacher_delete_pending = ""
                                            st.rerun()
                                else:
                                    if da.button("🗑️ DELETE", key=f"delete_d_{sid}", use_container_width=True):
                                        st.session_state.teacher_delete_pending = sid
                                        st.rerun()
                            if pending == sid:
                                st.caption(f"Confirm deletion of {name} ({sid})? This permanently removes the saved learner record.")

                    # Mobile/table view — compact rows, not cards.
                    with st.container(key="teacher_mobile_table"):
                        st.markdown("**Learner · Score · Progress · Actions**")
                        for r in filtered_rows:
                            sid = str(r.get("student_id", ""))
                            name = str(r.get("learner_name", ""))
                            score = int(r.get("score", 0) or 0)
                            completed = len(r.get("completed") or [])
                            with st.container(key=f"mobile_learner_{sid}"):
                                c1, c2, c3 = st.columns([1.35, 0.75, 2.0])
                                with c1:
                                    st.markdown(f"**{name}**")
                                    st.caption(sid)
                                with c2:
                                    st.markdown(f"**{score}/1600**")
                                    st.caption(f"{completed}/16")
                                with c3:
                                    ra, da = st.columns(2)
                                    pdf = build_progress_pdf_for_row(r)
                                    ra.download_button("REPORT", data=pdf or b"", file_name=f"Virtual_CyberLab_{sid}_Report.pdf", mime="application/pdf", key=f"teacher_report_m_{sid}", disabled=pdf is None, use_container_width=True)
                                    if pending == sid:
                                        if da.button("CONFIRM", key=f"confirm_delete_m_{sid}", use_container_width=True):
                                            _, delete_err = _supabase_request("DELETE", "vcl_learners", f"student_id=eq.{sid}")
                                            if delete_err:
                                                st.error(delete_err)
                                            else:
                                                st.session_state.teacher_delete_pending = ""
                                                st.rerun()
                                    else:
                                        if da.button("DELETE", key=f"delete_m_{sid}", use_container_width=True):
                                            st.session_state.teacher_delete_pending = sid
                                            st.rerun()
                                if pending == sid:
                                    st.caption(f"Confirm deletion of {name} ({sid})? This permanently removes the saved learner record.")
                else:
                    st.info("No learner records found.")
    if st.session_state.get("teacher_authenticated", False):
        if st.button("🚪 LOG OUT", key="teacher_logout", use_container_width=True):
            st.session_state.teacher_authenticated = False
            st.session_state.pop("teacher_password", None)
            go("home")
    else:
        if st.button("← BACK TO HOME", key="teacher_back", use_container_width=True):
            go("home")

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
    st.markdown("# 🎣 Mission 01 — The Suspicious Invoice")
    st.caption("PHISHING LAB • Investigation simulation • Briefing → Evidence → Decision → Consequence → Explanation")

    st.html(textwrap.dedent("""
    <div class="mission">
      <div style="color:#e16af0;font-size:11px;font-weight:800;letter-spacing:.8px;">CASE FILE 01</div>
      <h2>THE SUSPICIOUS INVOICE</h2>
      <p>A teacher reports an urgent invoice email. Your job is to investigate the evidence before deciding what to do.</p>
      <p><b>Objective:</b> Identify the warning signs, verify the message safely, and choose an appropriate response.</p>
    </div>
    """))

    st.markdown("### 🔎 Investigation Briefing")
    st.info("Do not interact with the attachment. This is a simulated case. Use the evidence provided in the lab.")

    st.markdown("### 📩 Evidence 1 — Email")
    st.html(textwrap.dedent("""
    <div class="evidence">
      <b>From:</b> finance@school-payments.co<br>
      <b>Subject:</b> ACTION REQUIRED — Outstanding Invoice<br>
      <b>To:</b> teacher@school.edu<br>
      <b>Message:</b> Your payment is overdue. Review the attached invoice immediately to avoid account suspension.<br>
      <b>Attachment:</b> Invoice_September.html
    </div>
    """))

    st.markdown("### 🧪 Evidence 2 — Sender & Attachment Check")
    sender_check = st.radio(
        "What should you verify before trusting the message?",
        [
            "The sender domain and whether the request matches a known school process.",
            "Only the sender's display name.",
            "Whether the email looks professional.",
            "Whether the attachment opens successfully."
        ],
        key="m1_sender_check"
    )

    attachment_check = st.multiselect(
        "Which observations are meaningful warning signs? Select all that apply.",
        [
            "Urgent language",
            "Unfamiliar sender domain",
            "HTML attachment",
            "Pressure to act immediately",
            "The message contains a normal greeting"
        ],
        key="m1_clues"
    )

    st.markdown("### 🧭 Decision Point")
    decision = st.radio(
        "What should you do first?",
        [
            "Open the attachment to verify the invoice.",
            "Forward it to colleagues so they can check it.",
            "Report the message and verify the request through a trusted channel.",
            "Reply asking the sender to confirm the password."
        ],
        key="m1_decision"
    )

    st.markdown("### ⚠️ Simulated Consequence")
    consequence = st.radio(
        "If you receive an unexpected attachment from an unfamiliar domain, what is the safest next step?",
        [
            "Avoid opening it and use an independent trusted channel to verify the request.",
            "Open it on a different device.",
            "Rename the file before opening it.",
            "Ask another person to open it for you."
        ],
        key="m1_consequence"
    )

    if st.button("SUBMIT INVESTIGATION", type="primary"):
        record_attempt("m1")
        correct_clues = {"Urgent language", "Unfamiliar sender domain", "HTML attachment", "Pressure to act immediately"}
        clue_ok = set(attachment_check) == correct_clues
        sender_ok = sender_check.startswith("The sender domain")
        decision_ok = decision.startswith("Report")
        consequence_ok = consequence.startswith("Avoid")

        # Four independent scoring components prevent double-counting and allow partial learning credit.
        awarded = 0
        if sender_ok and not st.session_state.get("m1_sender_awarded", False):
            st.session_state.m1_sender_awarded = True
            awarded += 20
        if clue_ok and not st.session_state.get("m1_clues_awarded", False):
            st.session_state.m1_clues_awarded = True
            awarded += 40
        if decision_ok and not st.session_state.get("m1_decision_awarded", False):
            st.session_state.m1_decision_awarded = True
            awarded += 25
        if consequence_ok and not st.session_state.get("m1_consequence_awarded", False):
            st.session_state.m1_consequence_awarded = True
            awarded += 15

        if awarded:
            st.session_state.score += awarded

        current = sum([
            20 if st.session_state.get("m1_sender_awarded", False) else 0,
            40 if st.session_state.get("m1_clues_awarded", False) else 0,
            25 if st.session_state.get("m1_decision_awarded", False) else 0,
            15 if st.session_state.get("m1_consequence_awarded", False) else 0,
        ])

        if current == 100 and "m1" not in st.session_state.completed:
            st.session_state.completed.add("m1")
            st.success("MISSION COMPLETE — 100/100 🛡️")
        elif awarded:
            st.info(f"Partial score recorded: +{awarded} points. Current mission score: {current}/100.")
        else:
            st.warning(f"No new points on this attempt. Current mission score: {current}/100.")

        st.markdown("### 🧠 Explanation")
        st.html("""
        <div class="evidence">
          <b>Sender:</b> A domain that does not match the expected organization should be verified independently.<br>
          <b>Urgency:</b> Pressure to act immediately is a common social-engineering signal.<br>
          <b>Attachment:</b> An unexpected HTML attachment can lead to a malicious or deceptive page and should not be opened just to investigate.<br>
          <b>Response:</b> Report the message and verify the request using a trusted channel rather than replying to the suspicious email.<br>
          <b>Key lesson:</b> Investigate the evidence first. A professional-looking message can still be malicious.
        </div>
        """)

    mission_feedback("m1")
    if st.button("← BACK TO PHISHING LAB"): go("phishing")

# ---------- M2 ----------
elif st.session_state.page == "m2":
    st.markdown("# 🎣 Mission 02 — Fake Microsoft 365 Login")
    st.caption("PHISHING LAB • Digital investigation: inspect the sender, destination and request before acting.")

    st.html('<div class="mission"><h2>CASE FILE</h2><p>A student receives an email claiming that her Microsoft 365 session will expire in 10 minutes. The message urges her to click “Keep My Account Active.” Your task is to determine whether the sign-in request is legitimate.</p></div>')

    st.html(textwrap.dedent("""
    <div class="evidence">
      <b>Evidence A — Sender:</b> microsoft-security@micr0soft-support.com<br>
      <b>Evidence B — Button URL preview:</b> https://microsoft-account.verify-login.example<br>
      <b>Evidence C — Message:</b> “Immediate action required. Sign in now to avoid losing access.”<br>
      <b>Evidence D — Requested data:</b> Microsoft 365 username, password and MFA code
    </div>
    """))

    st.markdown("### 🔎 Investigation Step 1 — Inspect the evidence")
    findings=st.multiselect(
        "Which observations are strong indicators of phishing? Select all that apply.",
        [
            "Look-alike sender domain",
            "Urgent deadline",
            "Unexpected sign-in request",
            "URL does not use the organization's trusted domain",
            "The message contains a greeting"
        ],
        key="m2_findings"
    )

    st.markdown("### 🧭 Investigation Step 2 — Assess the credential request")
    credential_assessment=st.radio(
        "The page asks for a password and MFA code. What does this tell you?",
        [
            "It is normal because Microsoft uses MFA.",
            "The request is high-risk and should be verified through an official channel before any credentials are entered.",
            "It is safe if the page looks professional.",
            "The MFA code can be shared if the sender appears familiar."
        ],
        key="m2_credential_assessment"
    )

    st.markdown("### 🛡️ Investigation Step 3 — Make the decision")
    action=st.radio(
        "What is the safest next step?",
        [
            "Click the button and inspect the page.",
            "Enter credentials but do not save them.",
            "Use the official Microsoft 365 portal/bookmark instead of the email link and report the message.",
            "Forward the email to a friend."
        ],
        key="m2_action"
    )

    if st.button("SUBMIT INVESTIGATION",type="primary"):
        record_attempt("m2")
        correct={"Look-alike sender domain","Urgent deadline","Unexpected sign-in request","URL does not use the organization's trusted domain"}
        findings_ok = set(findings)==correct
        credential_ok = credential_assessment.startswith("The request is high-risk")
        action_ok = action.startswith("Use the official")

        awarded = 0
        if findings_ok and not st.session_state.get("m2_findings_awarded", False):
            st.session_state.m2_findings_awarded = True
            awarded += 40
        if credential_ok and not st.session_state.get("m2_credential_awarded", False):
            st.session_state.m2_credential_awarded = True
            awarded += 30
        if action_ok and not st.session_state.get("m2_action_awarded", False):
            st.session_state.m2_action_awarded = True
            awarded += 30

        if awarded:
            st.session_state.score += awarded

        current = (
            40 if st.session_state.get("m2_findings_awarded", False) else 0
        ) + (
            30 if st.session_state.get("m2_credential_awarded", False) else 0
        ) + (
            30 if st.session_state.get("m2_action_awarded", False) else 0
        )

        if current == 100 and "m2" not in st.session_state.completed:
            st.session_state.completed.add("m2")
            st.success("MISSION COMPLETE — 100/100 🛡️")
            st.info("Investigation result: the sender uses a look-alike domain, the message creates urgency, the destination is not a trusted Microsoft 365 domain, and the page requests sensitive credentials. Verify independently through the official portal.")
        elif awarded:
            st.info(f"Partial score recorded: +{awarded} points. Current mission score: {current}/100.")
            if not findings_ok:
                st.warning("Re-check the sender domain, urgency, unexpected sign-in request and destination URL.")
            elif not credential_ok:
                st.warning("A familiar brand and MFA do not make an unexpected credential request trustworthy.")
            elif not action_ok:
                st.warning("Use a trusted bookmark or official portal instead of the email link, then report the message.")
        else:
            st.warning(f"No new points on this attempt. Current mission score: {current}/100.")

    mission_feedback("m2")
    if st.button("← BACK TO PHISHING LAB"): go("phishing")

# ---------- M3 ----------
elif st.session_state.page == "m3":
    st.markdown("# 🎣 Mission 03 — QR Code Phishing")
    st.caption("PHISHING LAB • Investigate the QR destination before trusting the request.")
    st.html('<div class="mission"><h2>MISSION BRIEFING</h2><p>A poster in a hallway says: “Scan to confirm your student account before Friday.” You scan the QR code and see a login page asking for a school username, password and verification code.</p></div>')

    st.markdown("### 🔎 Investigation Step 1 — Inspect the Evidence")
    st.html('<div class="evidence"><b>Poster:</b> “Confirm your student account before Friday.”<br><b>QR destination:</b> <span style="color:#ffcf5a;">account-confirmation-login.com</span><br><b>Page requests:</b> School username • Password • MFA verification code<br><b>Context:</b> The poster was not announced through the school\'s normal communication channel.</div>')
    findings = st.multiselect(
        "Which findings are meaningful warning signs? Select all that apply.",
        [
            "The QR code hides the destination until it is scanned",
            "The destination is not the school's official portal",
            "The page requests a password",
            "The page requests an MFA verification code",
            "The request creates deadline pressure",
            "The poster uses the school logo"
        ],
        key="m3_findings"
    )

    st.markdown("### 🧭 Investigation Step 2 — Assess the Request")
    assessment = st.radio(
        "Which assessment is most appropriate?",
        [
            "The logo makes the page trustworthy.",
            "A QR code is safe because it is not a normal link.",
            "The destination and credential request should be treated as suspicious and verified independently.",
            "Entering the MFA code will prove that the page is official."
        ],
        key="m3_assessment"
    )

    st.markdown("### 🛡️ Investigation Step 3 — Make the Decision")
    action = st.radio(
        "What should you do next?",
        [
            "Enter the requested information quickly before the deadline.",
            "Use the official school portal directly, avoid the QR page, and report the suspicious poster/link.",
            "Share the QR code with classmates to see if they get the same page.",
            "Disable MFA so the page can work without the verification code."
        ],
        key="m3_action"
    )

    st.markdown("### ⚠️ Simulated Consequence")
    consequence = st.radio(
        "If credentials were entered into the suspicious page, what would be the appropriate immediate response?",
        [
            "Secure the account through the official process and report the suspected credential exposure.",
            "Continue using the same password because MFA is enabled.",
            "Delete the browser history and ignore the event.",
            "Send the password to the school team by email."
        ],
        key="m3_consequence"
    )

    if st.button("SUBMIT INVESTIGATION", type="primary"):
        record_attempt("m3")
        correct_findings = {
            "The QR code hides the destination until it is scanned",
            "The destination is not the school's official portal",
            "The page requests a password",
            "The page requests an MFA verification code",
            "The request creates deadline pressure"
        }
        findings_ok = set(findings) == correct_findings
        assessment_ok = assessment.startswith("The destination")
        action_ok = action.startswith("Use the official")
        consequence_ok = consequence.startswith("Secure the account")

        awarded = 0
        if findings_ok and not st.session_state.get("m3_findings_awarded", False):
            st.session_state.m3_findings_awarded = True
            awarded += 40
        if assessment_ok and not st.session_state.get("m3_assessment_awarded", False):
            st.session_state.m3_assessment_awarded = True
            awarded += 20
        if action_ok and not st.session_state.get("m3_action_awarded", False):
            st.session_state.m3_action_awarded = True
            awarded += 30
        if consequence_ok and not st.session_state.get("m3_consequence_awarded", False):
            st.session_state.m3_consequence_awarded = True
            awarded += 10

        if awarded:
            st.session_state.score += awarded
            current = (40 if st.session_state.get("m3_findings_awarded", False) else 0) + (20 if st.session_state.get("m3_assessment_awarded", False) else 0) + (30 if st.session_state.get("m3_action_awarded", False) else 0) + (10 if st.session_state.get("m3_consequence_awarded", False) else 0)
            if current == 100 and "m3" not in st.session_state.completed:
                st.session_state.completed.add("m3")
                st.success("MISSION COMPLETE — 100/100 🛡️")
                st.info("Investigation result: the QR code leads to an untrusted destination and the page requests sensitive credentials. Verify through the official school portal instead of trusting the QR code.")
            else:
                st.info(f"Partial score recorded: +{awarded} points. Current mission score: {current}/100.")
                if not findings_ok:
                    st.warning("Re-check the destination, credential requests and deadline pressure. A familiar logo does not prove authenticity.")
                elif not assessment_ok:
                    st.warning("A QR code is simply a delivery method for a link. Assess the destination and the information being requested.")
                elif not action_ok:
                    st.warning("Use a trusted official portal instead of the QR destination, then report the suspicious content.")
                elif not consequence_ok:
                    st.warning("If credentials may have been exposed, use the official account-security process and report the event promptly.")
        else:
            current = (40 if st.session_state.get("m3_findings_awarded", False) else 0) + (20 if st.session_state.get("m3_assessment_awarded", False) else 0) + (30 if st.session_state.get("m3_action_awarded", False) else 0) + (10 if st.session_state.get("m3_consequence_awarded", False) else 0)
            st.warning(f"No new points on this attempt. Current mission score: {current}/100. Review the evidence and try again.")

    mission_feedback("m3")
    if st.button("← BACK TO PHISHING LAB"): go("phishing")

# ---------- M4 ----------
elif st.session_state.page == "m4":
    st.markdown("# 🎣 Mission 04 — Social Engineering Message")
    st.caption("PHISHING LAB • Investigate the pressure, verify independently, and protect the organization.")

    st.html(textwrap.dedent("""
    <div class="mission">
      <div style="color:#e16af0;font-size:11px;font-weight:800;letter-spacing:.8px;">CASE BRIEFING</div>
      <h2>SOCIAL ENGINEERING ALERT</h2>
      <p>A message appears to come from a senior staff member. The sender says they are in a meeting and urgently asks you to buy three gift cards and send the codes. They specifically tell you not to call because they cannot talk.</p>
      <p><b>Your role:</b> You are assisting the school with a suspicious-message investigation. Your task is to identify the manipulation techniques, assess the request, choose a safe verification method, and predict the consequence of your decision.</p>
    </div>
    """))

    st.markdown("### 🔎 STEP 1 — Inspect the Message")
    st.html(textwrap.dedent("""
    <div class="evidence">
      <b>From:</b> Senior Staff Member<br>
      <b>Message:</b> “I am in a meeting. Buy three gift cards immediately and send me the codes. Do not call—I cannot talk.”<br>
      <b>Request:</b> Purchase gift cards and provide the redemption codes.<br>
      <b>Communication:</b> The sender asks you to bypass normal voice verification.
    </div>
    """))
    redflags=st.multiselect(
        "Which indicators should you flag? Select all that apply.",
        [
            "Authority pressure",
            "Urgency",
            "Request to bypass normal communication",
            "Request for gift-card codes",
            "Instruction not to verify",
            "A normal routine request"
        ],
        key="m4_flags"
    )

    st.markdown("### 🧭 STEP 2 — Assess the Request")
    risk=st.radio(
        "What is the strongest reason to treat this request as suspicious?",
        [
            "The sender uses a familiar job title, so the request is safe.",
            "The request combines urgency, authority, a financial demand and pressure to avoid independent verification.",
            "Gift cards are always prohibited in every workplace.",
            "The message is short, so it must be automated."
        ],
        key="m4_risk"
    )

    st.markdown("### 🛡️ STEP 3 — Make the Decision")
    response=st.radio(
        "What should you do before taking any action?",
        [
            "Complete the request immediately.",
            "Verify the request through a known phone number or official channel before taking action.",
            "Ask the sender for a different gift-card brand.",
            "Post the request in a public group."
        ],
        key="m4_response"
    )

    st.markdown("### ⚠️ STEP 4 — Predict the Consequence")
    consequence=st.radio(
        "If you follow the message without verification, what is the most likely security consequence?",
        [
            "The gift-card codes may be transferred to an unauthorized person and the loss may be difficult to recover.",
            "The account automatically becomes more secure.",
            "The school system will automatically verify the sender.",
            "Nothing can happen because the message came from a senior staff member."
        ],
        key="m4_consequence"
    )

    if st.button("SUBMIT INVESTIGATION",type="primary"):
        record_attempt("m4")
        correct_flags={"Authority pressure","Urgency","Request to bypass normal communication","Request for gift-card codes","Instruction not to verify"}
        flags_ok = set(redflags)==correct_flags
        risk_ok = risk.startswith("The request combines")
        response_ok = response.startswith("Verify")
        consequence_ok = consequence.startswith("The gift-card codes")

        awarded=0
        feedback=[]
        if flags_ok and not st.session_state.get("m4_flags_awarded",False):
            st.session_state.m4_flags_awarded=True
            awarded += 40
        elif not flags_ok:
            feedback.append("Review the authority, urgency, financial request and pressure to avoid verification.")

        if risk_ok and not st.session_state.get("m4_risk_awarded",False):
            st.session_state.m4_risk_awarded=True
            awarded += 20
        elif not risk_ok:
            feedback.append("A convincing title does not prove identity. The combination of pressure and a financial request is the key warning pattern.")

        if response_ok and not st.session_state.get("m4_response_awarded",False):
            st.session_state.m4_response_awarded=True
            awarded += 30
        elif not response_ok:
            feedback.append("Use an independently known contact method or official channel instead of replying to the suspicious request.")

        if consequence_ok and not st.session_state.get("m4_consequence_awarded",False):
            st.session_state.m4_consequence_awarded=True
            awarded += 10
        elif not consequence_ok:
            feedback.append("Gift-card codes function like value that can be transferred. Once shared, recovery may be difficult.")

        if awarded:
            st.session_state.score += awarded

        current=(40 if st.session_state.get("m4_flags_awarded",False) else 0)+(20 if st.session_state.get("m4_risk_awarded",False) else 0)+(30 if st.session_state.get("m4_response_awarded",False) else 0)+(10 if st.session_state.get("m4_consequence_awarded",False) else 0)

        if current==100 and "m4" not in st.session_state.completed:
            st.session_state.completed.add("m4")
            st.success("MISSION COMPLETE — 100/100 🛡️")
            st.info("Excellent investigation. Social engineering often combines authority, urgency and isolation. Independent verification breaks the attacker's advantage.")
        elif awarded:
            st.info(f"Partial score recorded: +{awarded} points. Current mission score: {current}/100.")
            if feedback:
                for item in feedback: st.warning(item)
        else:
            st.warning(f"No new points on this attempt. Current mission score: {current}/100.")
            if feedback:
                for item in feedback: st.warning(item)

    mission_feedback("m4")
    if st.button("← BACK TO PHISHING LAB"): go("phishing")

# ---------- IDENTITY HUB ----------
elif st.session_state.page == "identity":
    st.markdown("# 🔐 Password & Identity Lab")
    st.caption("LAB 02 • Four missions • Protect credentials, identity and account access.")
    ids=[("m5","05","The Reused Password","Investigate password reuse after an external breach."),("m6","06","MFA Alert","Respond to an unexpected multi-factor authentication prompt."),("m7","07","Account Takeover","Contain a compromised account and preserve evidence."),("m8","08","Credential Security Investigation","Investigate exposed credentials and choose a safe recovery path.")]
    cols=st.columns(2)
    for i,(mid,num,title,desc) in enumerate(ids):
        with cols[i%2]:
            done="✓ COMPLETED" if mid in st.session_state.completed else "MISSION READY"
            st.html(f'<div class="mission"><div style="color:#2be0ec;font-size:11px;font-weight:800;">MISSION {num}</div><h3>{title}</h3><p>{desc}</p><div style="color:#2be0ec;font-size:11px;font-weight:700;">{done}</div></div>')
            if st.button("START MISSION  →",key=f"start_{mid}",use_container_width=True): go(mid)
    if st.button("← BACK TO CYBERLAB"): go("home")

# ---------- M5 ----------
elif st.session_state.page == "m5":
    st.markdown("# 🔐 Mission 05 — The Reused Password")
    st.caption("PASSWORD & IDENTITY • Credential investigation")
    st.html('<div class="mission"><h2>CASE FILE</h2><p>A student receives a breach notice from an unrelated website. She remembers that the same password has been used on the school portal for two years.</p></div>')
    st.html('<div class="evidence"><b>External Website:</b> breach notification received<br><b>School Portal:</b> same password reused for 2 years<br><b>MFA:</b> enabled on the school portal<br><b>Unknown:</b> whether the school password was exposed</div>')

    findings = st.multiselect("STEP 1 — Identify the security risks.",[
        "Password reuse connects two accounts","The school account may be exposed if the password was reused","MFA removes the need to change the password","The breach notice should be ignored because it is from another website","The password has been used for a long time"
    ],key="m5_findings")
    finding_correct={"Password reuse connects two accounts","The school account may be exposed if the password was reused","The password has been used for a long time"}

    priority = st.radio("STEP 2 — What should be prioritized?",[
        "Keep the password until there is proof of compromise.",
        "Secure the affected accounts by changing reused credentials through official services.",
        "Use the same password on another account so it is easier to remember.",
        "Disable MFA before changing the password."
    ],key="m5_priority")

    actions = st.multiselect("STEP 3 — Select the appropriate protective actions.",[
        "Create a unique password for the school account",
        "Change the reused password on the affected service(s)",
        "Review recent account activity where available",
        "Keep the old password as a backup",
        "Ignore the breach because MFA is enabled"
    ],key="m5_actions")
    action_correct={"Create a unique password for the school account","Change the reused password on the affected service(s)","Review recent account activity where available"}

    consequence = st.radio("STEP 4 — What is the safest lesson from this case?",[
        "A password can be reused safely if it is difficult to guess.",
        "Unique passwords reduce the impact of a breach on another service.",
        "MFA means password hygiene is no longer important.",
        "Changing passwords should only happen after an account is taken over."
    ],key="m5_consequence")

    if st.button("SUBMIT INVESTIGATION",type="primary"):
        record_attempt("m5")
        awarded=0; feedback=[]
        if set(findings)==finding_correct and not st.session_state.get("m5_findings_awarded",False):
            st.session_state.m5_findings_awarded=True; awarded+=30
        elif set(findings)!=finding_correct: feedback.append("Re-check the relationship between password reuse, the external breach and the school account.")
        if priority.startswith("Secure") and not st.session_state.get("m5_priority_awarded",False):
            st.session_state.m5_priority_awarded=True; awarded+=25
        elif not priority.startswith("Secure"): feedback.append("The safer response is to secure reused credentials through official account services.")
        if set(actions)==action_correct and not st.session_state.get("m5_actions_awarded",False):
            st.session_state.m5_actions_awarded=True; awarded+=30
        elif set(actions)!=action_correct: feedback.append("Focus on unique credentials, changing reused passwords and reviewing activity where available.")
        if consequence.startswith("Unique") and not st.session_state.get("m5_consequence_awarded",False):
            st.session_state.m5_consequence_awarded=True; awarded+=15
        elif not consequence.startswith("Unique"): feedback.append("The key lesson is to avoid letting one breached password expose multiple accounts.")
        if awarded:
            st.session_state.score += awarded
        current=sum(30 if st.session_state.get("m5_findings_awarded",False) else 0 for _ in [0])+sum(25 if st.session_state.get("m5_priority_awarded",False) else 0 for _ in [0])+sum(30 if st.session_state.get("m5_actions_awarded",False) else 0 for _ in [0])+sum(15 if st.session_state.get("m5_consequence_awarded",False) else 0 for _ in [0])
        if current==100 and "m5" not in st.session_state.completed:
            st.session_state.completed.add("m5"); st.success("MISSION COMPLETE — 100/100 🛡️"); st.info("Unique passwords limit the spread of credential compromise. MFA is an additional layer, not a replacement for password hygiene.")
        elif awarded:
            st.info(f"Partial score recorded: +{awarded} points. Current mission score: {current}/100.")
        else: st.warning(f"No new points on this attempt. Current mission score: {current}/100.")
        for item in feedback: st.warning(item)
    mission_feedback("m5")
    if st.button("← BACK TO IDENTITY LAB"): go("identity")

# ---------- M6 ----------
elif st.session_state.page == "m6":
    st.markdown("# 🔐 Mission 06 — MFA Alert")
    st.caption("PASSWORD & IDENTITY • Authentication investigation")
    st.html('<div class="mission"><h2>CASE FILE</h2><p>While doing homework, a student receives three MFA approval prompts even though she did not attempt to sign in.</p></div>')
    st.html('<div class="evidence"><b>Event:</b> three unexpected MFA prompts<br><b>User:</b> did not initiate a sign-in<br><b>Known:</b> the account uses MFA<br><b>Risk:</b> an attacker may be attempting to authenticate</div>')

    observations=st.multiselect("STEP 1 — What does the evidence suggest?",[
        "The prompts are unexpected","Someone may know the account password","The user should approve one prompt to identify the source","The event deserves investigation","MFA prompts are always harmless"
    ],key="m6_observations")
    obs_correct={"The prompts are unexpected","Someone may know the account password","The event deserves investigation"}

    immediate=st.multiselect("STEP 2 — Select the immediate safe actions.",[
        "Deny the unexpected prompts","Approve a prompt to make the notifications stop","Do not share any verification code","Report the event through the approved school channel","Send the code to a friend for help"
    ],key="m6_immediate")
    immediate_correct={"Deny the unexpected prompts","Do not share any verification code","Report the event through the approved school channel"}

    next_step=st.radio("STEP 3 — What should happen next?",[
        "Change the password through the official account service and review account activity.",
        "Continue approving prompts until they stop.",
        "Disable MFA permanently.",
        "Ignore the event because MFA blocked the sign-in."
    ],key="m6_next")

    lesson=st.radio("STEP 4 — Which security principle applies?",[
        "An MFA prompt is proof that the requester is trusted.",
        "Authentication requests should be approved only when the user initiated them.",
        "MFA codes can be shared if the sender claims to be support.",
        "Unexpected prompts should be accepted quickly to avoid account lockout."
    ],key="m6_lesson")

    if st.button("SUBMIT INVESTIGATION",type="primary"):
        record_attempt("m6")
        awarded=0; feedback=[]
        if set(observations)==obs_correct and not st.session_state.get("m6_obs_awarded",False): st.session_state.m6_obs_awarded=True; awarded+=25
        elif set(observations)!=obs_correct: feedback.append("Treat unexpected MFA prompts as a security signal, not as harmless notifications.")
        if set(immediate)==immediate_correct and not st.session_state.get("m6_immediate_awarded",False): st.session_state.m6_immediate_awarded=True; awarded+=30
        elif set(immediate)!=immediate_correct: feedback.append("Never approve an unexpected prompt or share a verification code.")
        if next_step.startswith("Change") and not st.session_state.get("m6_next_awarded",False): st.session_state.m6_next_awarded=True; awarded+=30
        elif not next_step.startswith("Change"): feedback.append("Use the official account service to secure the credentials and review activity.")
        if lesson.startswith("Authentication") and not st.session_state.get("m6_lesson_awarded",False): st.session_state.m6_lesson_awarded=True; awarded+=15
        elif not lesson.startswith("Authentication"): feedback.append("Only approve authentication requests that you initiated yourself.")
        if awarded: st.session_state.score += awarded
        current=(25 if st.session_state.get("m6_obs_awarded",False) else 0)+(30 if st.session_state.get("m6_immediate_awarded",False) else 0)+(30 if st.session_state.get("m6_next_awarded",False) else 0)+(15 if st.session_state.get("m6_lesson_awarded",False) else 0)
        if current==100 and "m6" not in st.session_state.completed:
            st.session_state.completed.add("m6"); st.success("MISSION COMPLETE — 100/100 🛡️"); st.info("MFA is strongest when the user approves only authentication requests they actually initiated.")
        elif awarded: st.info(f"Partial score recorded: +{awarded} points. Current mission score: {current}/100.")
        else: st.warning(f"No new points on this attempt. Current mission score: {current}/100.")
        for item in feedback: st.warning(item)
    mission_feedback("m6")
    if st.button("← BACK TO IDENTITY LAB"): go("identity")

# ---------- M7 ----------
elif st.session_state.page == "m7":
    st.markdown("# 🔐 Mission 07 — Account Takeover")
    st.caption("PASSWORD & IDENTITY • Containment and recovery investigation")
    st.html('<div class="mission"><h2>CASE FILE</h2><p>A student reports that her profile photo and recovery email changed without permission. Messages were also sent from her account.</p></div>')
    st.html('<div class="evidence"><b>Evidence A:</b> profile photo changed<br><b>Evidence B:</b> recovery email changed<br><b>Evidence C:</b> messages sent without the student action<br><b>Risk:</b> the attacker may still control account access</div>')

    indicators=st.multiselect("STEP 1 — Identify signs of account compromise.",[
        "Recovery information changed without permission","Messages were sent without the user's action","Profile information changed unexpectedly","The user remembers her old password","The account is definitely safe because it has a recovery email"
    ],key="m7_indicators")
    ind_correct={"Recovery information changed without permission","Messages were sent without the user's action","Profile information changed unexpectedly"}

    containment=st.multiselect("STEP 2 — Select appropriate containment actions.",[
        "Use the official account-recovery process","Notify the responsible school/team","Preserve relevant alerts and messages as evidence","Use an unfamiliar recovery link sent by a stranger","Tell classmates to reuse the same recovery link"
    ],key="m7_containment")
    containment_correct={"Use the official account-recovery process","Notify the responsible school/team","Preserve relevant alerts and messages as evidence"}

    recovery=st.radio("STEP 3 — After securing recovery access, what should the user do?",[
        "Change the compromised credentials through the official service and review account activity.",
        "Restore the attacker's recovery email so the account remains accessible.",
        "Delete all security alerts and messages.",
        "Share the new password with classmates for backup."
    ],key="m7_recovery")

    evidence=st.multiselect("STEP 4 — Which evidence should be preserved when available?",[
        "Security alerts and notification messages","Relevant account activity or login records","Timestamps of unauthorized changes","The compromised password in a public document","Unverified rumors about who caused the incident"
    ],key="m7_evidence")
    evidence_correct={"Security alerts and notification messages","Relevant account activity or login records","Timestamps of unauthorized changes"}

    if st.button("SUBMIT INVESTIGATION",type="primary"):
        record_attempt("m7")
        awarded=0; feedback=[]
        if set(indicators)==ind_correct and not st.session_state.get("m7_ind_awarded",False): st.session_state.m7_ind_awarded=True; awarded+=25
        elif set(indicators)!=ind_correct: feedback.append("Look for unauthorized changes and actions that the account owner did not initiate.")
        if set(containment)==containment_correct and not st.session_state.get("m7_contain_awarded",False): st.session_state.m7_contain_awarded=True; awarded+=30
        elif set(containment)!=containment_correct: feedback.append("Use official recovery channels, notify the responsible team and preserve relevant evidence.")
        if recovery.startswith("Change") and not st.session_state.get("m7_recovery_awarded",False): st.session_state.m7_recovery_awarded=True; awarded+=25
        elif not recovery.startswith("Change"): feedback.append("After recovery access is secured, change compromised credentials through the official service and review activity.")
        if set(evidence)==evidence_correct and not st.session_state.get("m7_evidence_awarded",False): st.session_state.m7_evidence_awarded=True; awarded+=20
        elif set(evidence)!=evidence_correct: feedback.append("Preserve alerts, relevant account activity and timestamps; avoid publishing sensitive credentials.")
        if awarded: st.session_state.score += awarded
        current=(25 if st.session_state.get("m7_ind_awarded",False) else 0)+(30 if st.session_state.get("m7_contain_awarded",False) else 0)+(25 if st.session_state.get("m7_recovery_awarded",False) else 0)+(20 if st.session_state.get("m7_evidence_awarded",False) else 0)
        if current==100 and "m7" not in st.session_state.completed:
            st.session_state.completed.add("m7"); st.success("MISSION COMPLETE — 100/100 🛡️"); st.info("Account takeover response combines containment, official recovery, credential protection and evidence preservation.")
        elif awarded: st.info(f"Partial score recorded: +{awarded} points. Current mission score: {current}/100.")
        else: st.warning(f"No new points on this attempt. Current mission score: {current}/100.")
        for item in feedback: st.warning(item)
    mission_feedback("m7")
    if st.button("← BACK TO IDENTITY LAB"): go("identity")

# ---------- M8 ----------
elif st.session_state.page == "m8":
    st.markdown("# 🔐 Mission 08 — Credential Security Investigation")
    st.caption("PASSWORD & IDENTITY • Credential exposure and recovery")
    st.html('<div class="mission"><h2>CASE FILE</h2><p>A student receives a notice that an online service used outside school has suffered a credential breach. The student previously reused a similar password on another service and is unsure whether the school account is affected.</p></div>')
    st.html('<div class="evidence"><b>Evidence A:</b> external service reports a credential breach<br><b>Evidence B:</b> password reuse may connect accounts<br><b>Evidence C:</b> school account uses MFA<br><b>Unknown:</b> whether the school credential was exposed</div>')
    for flag in ["m8_assess_awarded","m8_contain_awarded","m8_verify_awarded","m8_recover_awarded"]:
        if flag not in st.session_state: st.session_state[flag]=False

    st.markdown("### STEP 1 — Identify the credential risks.")
    risks=st.multiselect("Select all relevant concerns.",["Password reuse may expose another account","The external breach should be investigated as a possible warning signal","MFA reduces risk but does not make password reuse safe","The student should share the password with the teacher for checking","The breach can be ignored because it happened on another website"],key="m8_risks")

    st.markdown("### STEP 2 — Choose the immediate protection.")
    contain=st.radio("What should the student do?",["Continue using the reused password until an attack is confirmed.","Change the reused credential through the official service and secure other affected accounts without sharing the password.","Send the password to a classmate for advice.","Disable MFA to make recovery easier."],key="m8_contain")

    st.markdown("### STEP 3 — Verify the situation safely.")
    verify=st.multiselect("Select appropriate verification steps.",["Review official breach/account notifications","Check recent sign-in activity for unfamiliar events","Use the service's official account-security page","Click an unsolicited recovery link from the breach email","Ask someone else to log in using the student's credentials"],key="m8_verify")

    st.markdown("### STEP 4 — Complete the recovery plan.")
    recovery=st.radio("What is the safest long-term action?",["Create a unique credential for each important account, keep MFA enabled, and report confirmed compromise through the approved process.","Reuse the new password on several accounts so it is easier to remember.","Turn off MFA after changing the password.","Share the new password with the teacher so it can be stored."],key="m8_recovery")

    if st.button("SUBMIT INVESTIGATION",key="m8_submit"):
        record_attempt("m8")
        awarded=0
        correct_risks={"Password reuse may expose another account","The external breach should be investigated as a possible warning signal","MFA reduces risk but does not make password reuse safe"}
        if set(risks)==correct_risks and not st.session_state.m8_assess_awarded:
            st.session_state.score += 25; st.session_state.m8_assess_awarded=True; awarded+=25
        elif set(risks)!=correct_risks:
            st.warning("Step 1: Look for the risks created by reuse and remember that MFA is an additional control, not a reason to reuse passwords.")

        if contain.startswith("Change the reused") and not st.session_state.m8_contain_awarded:
            st.session_state.score += 25; st.session_state.m8_contain_awarded=True; awarded+=25
        elif not contain.startswith("Change the reused"):
            st.warning("Step 2: Use official recovery controls and never disclose a password to another person.")

        correct_verify={"Review official breach/account notifications","Check recent sign-in activity for unfamiliar events","Use the service's official account-security page"}
        if set(verify)==correct_verify and not st.session_state.m8_verify_awarded:
            st.session_state.score += 25; st.session_state.m8_verify_awarded=True; awarded+=25
        elif set(verify)!=correct_verify:
            st.warning("Step 3: Verify through trusted channels and official account pages, not through unsolicited links.")

        if recovery.startswith("Create a unique") and not st.session_state.m8_recover_awarded:
            st.session_state.score += 25; st.session_state.m8_recover_awarded=True; awarded+=25
        elif not recovery.startswith("Create a unique"):
            st.warning("Step 4: Good credential hygiene combines unique credentials, MFA and approved reporting.")

        if awarded:
            st.success(f"INVESTIGATION SUBMITTED • +{awarded} points")

    mission_feedback("m8")
    if all(st.session_state.get(x) for x in ["m8_assess_awarded","m8_contain_awarded","m8_verify_awarded","m8_recover_awarded"]):
        st.session_state.completed.add("m8")
        st.success("MISSION COMPLETE — 100/100 🛡️")
        st.info("You connected credential exposure, safe verification and account recovery without disclosing passwords.")
    if st.button("← BACK TO IDENTITY LAB",key="back_m13"): go("identity")

# ---------- INCIDENT HUB ----------
elif st.session_state.page == "incident":
    st.markdown("# 🚨 Incident Response Lab")
    st.caption("LAB 03 • Four case-based missions • Detect, contain, investigate and recover.")
    st.html('<div class="mission"><h2>INCIDENT RESPONSE PROTOCOL</h2><p>Read the evidence, decide what should happen next, preserve useful information, and communicate through approved channels.</p></div>')
    incs=[("m9","09","Suspicious Login","Investigate an unfamiliar login and decide how to contain the account risk."),("m10","10","Malware Alert","Triage a malware alert, contain the device and preserve evidence."),("m11","11","Lost Device","Respond to a missing school device and protect accounts and data."),("m12","12","Ransomware Incident","Contain a file-encryption incident and coordinate a safe response.")]
    cols=st.columns(2)
    for i,(mid,num,title,desc) in enumerate(incs):
        with cols[i%2]:
            done="✓ COMPLETED" if mid in st.session_state.completed else "MISSION READY"
            st.html(f'<div class="mission"><div style="color:#4aa9ff;font-size:11px;font-weight:800;">MISSION {num}</div><h3>{title}</h3><p>{desc}</p><div style="color:#2be0ec;font-size:11px;font-weight:700;">{done}</div></div>')
            if st.button("START MISSION  →",key=f"start_{mid}",use_container_width=True): go(mid)
    if st.button("← BACK TO CYBERLAB"): go("home")

# ---------- M9 ----------
elif st.session_state.page == "m9":
    st.markdown("# 🚨 Mission 09 — Suspicious Login")
    st.caption("INCIDENT RESPONSE • Investigate, contain and communicate")
    st.html('<div class="mission"><h2>CASE BRIEF</h2><p>At 02:14 AM, a student account records a login from an unfamiliar location. The device has never been registered. MFA was approved, but the student says they were asleep at the time.</p></div>')
    st.html('<div class="evidence"><b>02:14 AM</b> — unfamiliar location<br><b>Device</b> — not previously registered<br><b>MFA</b> — authentication approved<br><b>User statement</b> — denies initiating the login</div>')
    if "m9_assess_awarded" not in st.session_state: st.session_state.m9_assess_awarded=False
    if "m9_contain_awarded" not in st.session_state: st.session_state.m9_contain_awarded=False
    if "m9_investigate_awarded" not in st.session_state: st.session_state.m9_investigate_awarded=False
    if "m9_communicate_awarded" not in st.session_state: st.session_state.m9_communicate_awarded=False

    st.markdown("### STEP 1 — Identify the strongest warning signals.")
    findings=st.multiselect("Select all relevant evidence.",["Login at an unusual time","Unfamiliar location","Previously unregistered device","User denies the activity","The account has a profile picture"],key="m9_findings")

    st.markdown("### STEP 2 — What should happen first?")
    action=st.radio("Choose the safest immediate response.",["Ignore the event until another alert appears.","Secure and contain the account through the approved school process while preserving evidence.","Post the login details in a public group.","Delete the login alert so the user is not worried."],key="m9_action")

    st.markdown("### STEP 3 — What should be investigated next?")
    checks=st.multiselect("Select appropriate investigation steps.",["Review recent authentication and account activity","Check whether other unfamiliar devices or sessions exist","Preserve relevant timestamps and security logs","Ask the user to share their password for verification","Delete the suspicious session history"],key="m9_checks")

    st.markdown("### STEP 4 — How should the incident be communicated?")
    comm=st.radio("Choose the appropriate approach.",["Share the incident publicly so others can investigate it.","Use approved school/security channels and provide only the information needed by responsible people.","Send the user's login details to classmates.","Do not document the event if the account is secured."],key="m9_comm")

    if st.button("SUBMIT INVESTIGATION", type="primary", key="submit_m9"):
        record_attempt("m9")
        if set(findings)=={"Login at an unusual time","Unfamiliar location","Previously unregistered device","User denies the activity"}:
            if not st.session_state.get("m9_assess_awarded", False):
                st.session_state.score += 25
                st.session_state.m9_assess_awarded=True
        else:
            st.warning("Review this step and select the safest documented response.")
        if action=="Secure and contain the account through the approved school process while preserving evidence.":
            if not st.session_state.get("m9_contain_awarded", False):
                st.session_state.score += 25
                st.session_state.m9_contain_awarded=True
        else:
            st.warning("Review this step and select the safest documented response.")
        if set(checks)=={"Review recent authentication and account activity","Check whether other unfamiliar devices or sessions exist","Preserve relevant timestamps and security logs"}:
            if not st.session_state.get("m9_investigate_awarded", False):
                st.session_state.score += 25
                st.session_state.m9_investigate_awarded=True
        else:
            st.warning("Review this step and select the safest documented response.")
        if comm=="Use approved school/security channels and provide only the information needed by responsible people.":
            if not st.session_state.get("m9_communicate_awarded", False):
                st.session_state.score += 25
                st.session_state.m9_communicate_awarded=True
        else:
            st.warning("Review this step and select the safest documented response.")

    mission_feedback("m9")
    if st.session_state.get("m9_assess_awarded") and st.session_state.get("m9_contain_awarded") and st.session_state.get("m9_investigate_awarded") and st.session_state.get("m9_communicate_awarded"):
        if "m9" not in st.session_state.completed:
            st.session_state.completed.add("m9")
        st.success("MISSION COMPLETE — 100/100 🛡️")
        st.info("A suspicious login requires evidence-based investigation, safe containment and controlled communication.")
    if st.button("← BACK TO INCIDENT LAB",key="back_m8"): go("incident")

# ---------- M10 ----------
elif st.session_state.page == "m10":
    st.markdown("# 🚨 Mission 10 — Malware Alert")
    st.caption("INCIDENT RESPONSE • Triage, containment and evidence")
    st.html('<div class="mission"><h2>CASE BRIEF</h2><p>An endpoint protection system detects that a downloaded file attempted to launch a suspicious process on a school computer. The alert is still open and the user is waiting for instructions.</p></div>')
    st.html('<div class="evidence"><b>Alert</b> — suspicious process detected<br><b>Source</b> — recently downloaded file<br><b>Status</b> — alert open<br><b>Risk</b> — possible continued activity on the device</div>')
    for flag in ["m10_triage_awarded","m10_contain_awarded","m10_evidence_awarded","m10_escalate_awarded"]:
        if flag not in st.session_state: st.session_state[flag]=False

    st.markdown("### STEP 1 — Triage the alert.")
    triage=st.multiselect("Which observations matter during initial triage?",["Identify the affected device and user","Record the alert time and detection details","Determine what file/process triggered the alert","Open the suspicious file again to reproduce the alert","Delete the alert immediately"],key="m10_triage")

    st.markdown("### STEP 2 — Contain the risk.")
    contain=st.multiselect("Select the safest containment actions.",["Follow the school's approved isolation/containment procedure","Disconnect or isolate the device when authorized by procedure","Ask the user to keep opening the file until it works","Allow unrestricted network access while investigating","Notify the responsible technical/security team"],key="m10_contain")

    st.markdown("### STEP 3 — Preserve evidence.")
    evidence=st.multiselect("What should be preserved for analysis?",["The security alert and detection details","Relevant timestamps and system logs","The suspicious file only if handled by an authorized process","All evidence should be deleted after isolation","A screenshot or record of the reported indicators when appropriate"],key="m10_evidence")

    st.markdown("### STEP 4 — Escalate and recover safely.")
    next_action=st.radio("What is the appropriate next step after initial containment?",["Declare the device safe without further review.","Escalate through the responsible security/technical process, document the incident, and restore the device only after it is cleared.","Delete all logs to protect privacy.","Send the suspicious file to students for analysis."],key="m10_next")

    if st.button("SUBMIT INVESTIGATION", type="primary", key="submit_m10"):
        record_attempt("m10")
        if set(triage)=={"Identify the affected device and user","Record the alert time and detection details","Determine what file/process triggered the alert"}:
            if not st.session_state.get("m10_triage_awarded", False):
                st.session_state.score += 25
                st.session_state.m10_triage_awarded=True
        else:
            st.warning("Review this step and select the safest documented response.")
        if set(contain)=={"Follow the school's approved isolation/containment procedure","Disconnect or isolate the device when authorized by procedure","Notify the responsible technical/security team"}:
            if not st.session_state.get("m10_contain_awarded", False):
                st.session_state.score += 25
                st.session_state.m10_contain_awarded=True
        else:
            st.warning("Review this step and select the safest documented response.")
        if set(evidence)=={"The security alert and detection details","Relevant timestamps and system logs","The suspicious file only if handled by an authorized process","A screenshot or record of the reported indicators when appropriate"}:
            if not st.session_state.get("m10_evidence_awarded", False):
                st.session_state.score += 25
                st.session_state.m10_evidence_awarded=True
        else:
            st.warning("Review this step and select the safest documented response.")
        if next_action=="Escalate through the responsible security/technical process, document the incident, and restore the device only after it is cleared.":
            if not st.session_state.get("m10_escalate_awarded", False):
                st.session_state.score += 25
                st.session_state.m10_escalate_awarded=True
        else:
            st.warning("Review this step and select the safest documented response.")

    mission_feedback("m10")
    if all(st.session_state.get(x) for x in ["m10_triage_awarded","m10_contain_awarded","m10_evidence_awarded","m10_escalate_awarded"]):
        if "m10" not in st.session_state.completed:
            st.session_state.completed.add("m10")
        st.success("MISSION COMPLETE — 100/100 🛡️")
        st.info("Safe malware response combines triage, containment, evidence preservation, escalation and controlled recovery.")
    if st.button("← BACK TO INCIDENT LAB",key="back_m9"): go("incident")

# ---------- M11 ----------
elif st.session_state.page == "m11":
    st.markdown("# 🚨 Mission 11 — Lost Device")
    st.caption("INCIDENT RESPONSE • Protect accounts, data and users")
    st.html('<div class="mission"><h2>CASE BRIEF</h2><p>A school laptop is reported missing after a classroom activity. It may contain locally stored school files and an active browser session. The last known location is not confirmed.</p></div>')
    st.html('<div class="evidence"><b>Asset</b> — school laptop<br><b>Possible exposure</b> — local files and active sessions<br><b>Status</b> — missing<br><b>Unknown</b> — who may have physical access to the device</div>')
    for flag in ["m11_report_awarded","m11_protect_awarded","m11_assess_awarded","m11_communicate_awarded"]:
        if flag not in st.session_state: st.session_state[flag]=False

    st.markdown("### STEP 1 — Make the initial report.")
    report=st.multiselect("Which information should be captured promptly?",["Report that the device is missing through school procedure","Record the device identifier or asset information if available","Record when and where it was last known to be present","Wait a week in case the device is returned","Post the device details publicly"],key="m11_report")

    st.markdown("### STEP 2 — Protect the device and accounts.")
    protect=st.multiselect("Select appropriate protective actions.",["Request remote lock/wipe if supported and authorized","Review and secure affected accounts and active sessions","Follow the school's approved device-management process","Share account passwords with the person searching for the laptop","Ignore active sessions until the device is found"],key="m11_protect")

    st.markdown("### STEP 3 — Assess the possible impact.")
    impact=st.multiselect("What should be assessed?",["What school data may have been stored locally","Which accounts or browser sessions may have remained active","Whether encryption or device-management controls were enabled","Assume there is no risk because the laptop has a password","Ignore the possibility of data exposure"],key="m11_impact")

    st.markdown("### STEP 4 — Communicate the incident.")
    comm=st.radio("Choose the safest communication approach.",["Publish the incident and device details on social media.","Use approved school/security channels, document actions taken, and share only necessary information.","Send account details to classmates so they can help.","Avoid documenting the incident to protect the school's reputation."],key="m11_comm")

    if st.button("SUBMIT INVESTIGATION", type="primary", key="submit_m11"):
        record_attempt("m11")
        if set(report)=={"Report that the device is missing through school procedure","Record the device identifier or asset information if available","Record when and where it was last known to be present"}:
            if not st.session_state.get("m11_report_awarded", False):
                st.session_state.score += 25
                st.session_state.m11_report_awarded=True
        else:
            st.warning("Review this step and select the safest documented response.")
        if set(protect)=={"Request remote lock/wipe if supported and authorized","Review and secure affected accounts and active sessions","Follow the school's approved device-management process"}:
            if not st.session_state.get("m11_protect_awarded", False):
                st.session_state.score += 25
                st.session_state.m11_protect_awarded=True
        else:
            st.warning("Review this step and select the safest documented response.")
        if set(impact)=={"What school data may have been stored locally","Which accounts or browser sessions may have remained active","Whether encryption or device-management controls were enabled"}:
            if not st.session_state.get("m11_assess_awarded", False):
                st.session_state.score += 25
                st.session_state.m11_assess_awarded=True
        else:
            st.warning("Review this step and select the safest documented response.")
        if comm=="Use approved school/security channels, document actions taken, and share only necessary information.":
            if not st.session_state.get("m11_communicate_awarded", False):
                st.session_state.score += 25
                st.session_state.m11_communicate_awarded=True
        else:
            st.warning("Review this step and select the safest documented response.")

    mission_feedback("m11")
    if all(st.session_state.get(x) for x in ["m11_report_awarded","m11_protect_awarded","m11_assess_awarded","m11_communicate_awarded"]):
        if "m11" not in st.session_state.completed:
            st.session_state.completed.add("m11")
        st.success("MISSION COMPLETE — 100/100 🛡️")
        st.info("A lost device is an incident: report quickly, apply authorized controls, assess exposure and communicate appropriately.")
    if st.button("← BACK TO INCIDENT LAB",key="back_m10"): go("incident")


# ---------- M12 ----------
elif st.session_state.page == "m12":
    st.markdown("# 🚨 Mission 12 — Ransomware Incident")
    st.caption("INCIDENT RESPONSE • Contain, preserve and escalate")
    st.html('<div class="mission"><h2>CASE BRIEF</h2><p>Several files on a school computer suddenly become unreadable and receive a new extension. A note appears asking for payment. Another nearby device is still operating normally.</p></div>')
    st.html('<div class="evidence"><b>Signal A:</b> multiple files changed unexpectedly<br><b>Signal B:</b> unfamiliar file extension<br><b>Signal C:</b> payment demand displayed<br><b>Signal D:</b> other devices may not yet be affected</div>')
    for flag in ["m12_detect_awarded","m12_contain_awarded","m12_evidence_awarded","m12_escalate_awarded"]:
        if flag not in st.session_state: st.session_state[flag]=False

    st.markdown("### STEP 1 — Recognize the incident indicators.")
    indicators=st.multiselect("Select the strongest indicators.",["Unexpected mass file changes","Unfamiliar file extension on affected files","Payment demand or ransom note","The computer is in a classroom","The incident can be ignored if other devices still work"],key="m12_indicators")

    st.markdown("### STEP 2 — Contain the spread.")
    contain=st.multiselect("Select appropriate containment actions.",["Follow the school's approved isolation/containment procedure","Isolate the affected device when authorized","Disconnect or restrict affected network access according to procedure","Open the ransom note repeatedly on other computers to test it","Connect backup drives to the affected computer immediately"],key="m12_contain")

    st.markdown("### STEP 3 — Preserve evidence.")
    evidence=st.multiselect("What should be preserved or documented?",["Security alerts and timestamps","Relevant system/network logs when available","Screenshots or records of the indicators when appropriate","Delete the ransom note and logs immediately","Run unknown recovery tools downloaded from the internet"],key="m12_evidence")

    st.markdown("### STEP 4 — Escalate and recover safely.")
    response=st.radio("What should happen next?",["Pay the demand immediately without documenting the incident.","Escalate through the responsible security/technical process, assess backups and recovery options, and document the response.","Ask students to copy the affected files to other devices.","Reconnect the device to the network to see whether the problem disappears."],key="m12_response")

    if st.button("SUBMIT INVESTIGATION", type="primary", key="submit_m12"):
        record_attempt("m12")
        if set(indicators)=={"Unexpected mass file changes","Unfamiliar file extension on affected files","Payment demand or ransom note"}:
            if not st.session_state.get("m12_detect_awarded", False):
                st.session_state.score += 25
                st.session_state.m12_detect_awarded=True
        else:
            st.warning("Review this step and select the safest documented response.")
        if set(contain)=={"Follow the school's approved isolation/containment procedure","Isolate the affected device when authorized","Disconnect or restrict affected network access according to procedure"}:
            if not st.session_state.get("m12_contain_awarded", False):
                st.session_state.score += 25
                st.session_state.m12_contain_awarded=True
        else:
            st.warning("Review this step and select the safest documented response.")
        if set(evidence)=={"Security alerts and timestamps","Relevant system/network logs when available","Screenshots or records of the indicators when appropriate"}:
            if not st.session_state.get("m12_evidence_awarded", False):
                st.session_state.score += 25
                st.session_state.m12_evidence_awarded=True
        else:
            st.warning("Review this step and select the safest documented response.")
        if response.startswith("Escalate through"):
            if not st.session_state.get("m12_escalate_awarded", False):
                st.session_state.score += 25
                st.session_state.m12_escalate_awarded=True
        else:
            st.warning("Review this step and select the safest documented response.")

    mission_feedback("m12")
    if all(st.session_state.get(x) for x in ["m12_detect_awarded","m12_contain_awarded","m12_evidence_awarded","m12_escalate_awarded"]):
        if "m12" not in st.session_state.completed:
            st.session_state.completed.add("m12")
        st.success("MISSION COMPLETE — 100/100 🛡️")
        st.info("You recognized the incident, contained the affected environment, preserved evidence and planned controlled recovery.")
    if st.button("← BACK TO INCIDENT LAB",key="back_m14"): go("incident")

# ---------- FINAL HUB ----------
elif st.session_state.page == "final":
    st.markdown("# 🏆 Final Cyber Challenge")
    st.caption("FINAL LAB • Four advanced case-based missions combining the skills from Labs 01–03.")
    st.html('<div class="mission"><h3>FINAL LAB PROTOCOL</h3><p>Work through the evidence, make decisions, predict consequences, and explain the security principle behind your response.</p></div>')
    finals=[("m13","13","Data Leakage Investigation","Investigate an accidentally shared school folder, contain the exposure and assess its impact."),("m14","14","Account Compromise Investigation","Connect identity, phishing and incident evidence into one complete incident-response case."),("m15","15","Digital Evidence Case","Build an evidence timeline and decide how to preserve, analyze and communicate findings."),("m16","16","Cyber Defender: Final Mission","Complete a full cross-lab cyber incident from detection to recovery.")]
    cols=st.columns(2)
    for i,(mid,num,title,desc) in enumerate(finals):
        with cols[i%2]:
            done="✓ COMPLETED" if mid in st.session_state.completed else "MISSION READY"
            st.html(f'<div class="mission"><div style="color:#ffc12b;font-size:11px;font-weight:800;">MISSION {num}</div><h3>{title}</h3><p>{desc}</p><div style="color:#2be0ec;font-size:11px;font-weight:700;">{done}</div></div>')
            if st.button("START MISSION  →",key=f"start_{mid}",use_container_width=True): go(mid)
    if st.button("← BACK TO CYBERLAB"): go("home")

# ---------- M13 ----------
elif st.session_state.page == "m13":
    st.markdown("# 🏆 Mission 13 — Data Leakage Investigation")
    st.caption("FINAL CHALLENGE • Investigation, containment and impact assessment")
    st.html('<div class="mission"><h2>CASE BRIEF</h2><p>A shared school folder containing student project files is discovered to be accessible to people outside the organization. A public link may have been active for several hours.</p></div>')
    st.html('<div class="evidence"><b>Access:</b> “Anyone with the link”<br><b>Content:</b> student project files<br><b>Discovery:</b> reported by a teacher<br><b>Unknown:</b> who accessed the files and whether copies were made</div>')

    m13_scope=st.multiselect("STEP 1 — Identify the security concerns.",["The folder uses public link access","The files contain student project information","The exposure duration is known to be several hours","The access history is currently unknown","The folder is automatically safe because it is inside the school drive","No investigation is needed if nobody reports misuse"],key="m13_scope")
    m13_contain=st.radio("STEP 2 — What should happen first?",["Ignore it until someone reports a problem.","Preserve relevant information, restrict inappropriate access, and notify the responsible team.","Delete the entire folder immediately.","Share the link with more users to test it."],key="m13_contain")
    m13_follow=st.multiselect("STEP 3 — Which follow-up actions are appropriate?",["Review sharing/access logs if available","Document what was discovered and when","Restore the intended access settings","Publicly name suspected users","Assess whether affected users need notification"],key="m13_follow")
    m13_consequence=st.radio("STEP 4 — What is the main reason to preserve evidence before making unnecessary changes?",["Evidence can help determine scope and support the response.","Evidence should always be shared publicly.","Evidence is only useful if the attacker is known.","Evidence should be deleted to reduce storage."],key="m13_consequence")

    if st.button("SUBMIT INVESTIGATION",type="primary"):
        record_attempt("m13")
        scope_correct={"The folder uses public link access","The files contain student project information","The access history is currently unknown"}
        follow_correct={"Review sharing/access logs if available","Document what was discovered and when","Restore the intended access settings","Assess whether affected users need notification"}
        awarded=0
        if set(m13_scope)==scope_correct and not st.session_state.get("m13_scope_awarded",False):
            st.session_state.m13_scope_awarded=True; awarded+=25
        if m13_contain.startswith("Preserve") and not st.session_state.get("m13_contain_awarded",False):
            st.session_state.m13_contain_awarded=True; awarded+=30
        if set(m13_follow)==follow_correct and not st.session_state.get("m13_follow_awarded",False):
            st.session_state.m13_follow_awarded=True; awarded+=30
        if m13_consequence.startswith("Evidence can help") and not st.session_state.get("m13_consequence_awarded",False):
            st.session_state.m13_consequence_awarded=True; awarded+=15
        if awarded:
            st.session_state.score += awarded
        current=(25 if st.session_state.get("m13_scope_awarded",False) else 0)+(30 if st.session_state.get("m13_contain_awarded",False) else 0)+(30 if st.session_state.get("m13_follow_awarded",False) else 0)+(15 if st.session_state.get("m13_consequence_awarded",False) else 0)
        if current==100 and "m13" not in st.session_state.completed:
            st.session_state.completed.add("m13")
            st.success("MISSION COMPLETE — 100/100 🛡️")
            st.info("You identified the exposure, contained it, preserved evidence and considered impact.")
        elif awarded:
            st.info(f"Partial score recorded: +{awarded} points. Current mission score: {current}/100.")
        else:
            st.warning(f"No new points on this attempt. Current mission score: {current}/100.")
        if current<100:
            st.caption("Review the case evidence and complete the missing investigation stages.")
    mission_feedback("m13")
    if st.button("← BACK TO FINAL CHALLENGE"): go("final")

# ---------- M14 ----------
elif st.session_state.page == "m14":
    st.markdown("# 🏆 Mission 14 — Account Compromise Investigation")
    st.caption("FINAL CHALLENGE • Complete incident-response investigation")
    st.html('<div class="mission"><h2>CASE FILE</h2><p>At 08:10 AM, a teacher reports an unexpected MFA prompt. At 08:16 AM, an email from the same account sends a link to a “shared document.” At 08:20 AM, the security dashboard records a new device login.</p></div>')
    st.html('<div class="evidence"><b>Evidence A:</b> unexpected MFA prompt<br><b>Evidence B:</b> suspicious link sent from the account<br><b>Evidence C:</b> unfamiliar device login<br><b>Evidence D:</b> user denies initiating any of these actions</div>')

    m14_chain=st.multiselect("STEP 1 — Build the evidence chain.",["Unexpected MFA prompt","Suspicious link sent from the account","Unfamiliar device login","User denies initiating the activity","The event happened during school hours"],key="m14_chain")
    m14_priority=st.radio("STEP 2 — What is your first priority?",["Ask the user to approve the next MFA prompt.","Contain and secure the account through the approved process while preserving evidence.","Delete the suspicious email and close the case.","Send the suspicious link to other users for testing."],key="m14_priority")
    m14_actions=st.multiselect("STEP 3 — After containment, select the appropriate actions.",["Document relevant evidence and timestamps","Review account activity and authentication events","Escalate through the appropriate school/security process","Publish the incident details publicly","Delete all logs to protect privacy"],key="m14_actions")
    m14_reason=st.radio("STEP 4 — Why should the events be considered together?",["Multiple independent signals can indicate a connected account-compromise incident.","MFA makes every other security signal irrelevant.","A suspicious link is harmless when it comes from a known account.","Only the device login matters."],key="m14_reason")
    m14_communication=st.radio("STEP 5 — What is the safest communication approach?",["Use approved channels and share only the information needed by responsible people.","Forward the suspicious link to everyone so they can inspect it.","Post the user's account details publicly.","Ask students to investigate the account themselves."],key="m14_communication")

    if st.button("SUBMIT INVESTIGATION",type="primary", key="submit_m14"):
        record_attempt("m14")
        chain_correct={"Unexpected MFA prompt","Suspicious link sent from the account","Unfamiliar device login","User denies initiating the activity"}
        actions_correct={"Document relevant evidence and timestamps","Review account activity and authentication events","Escalate through the appropriate school/security process"}
        awarded=0
        if set(m14_chain)==chain_correct and not st.session_state.get("m14_chain_awarded",False):
            st.session_state.m14_chain_awarded=True; awarded+=25
        if m14_priority.startswith("Contain") and not st.session_state.get("m14_priority_awarded",False):
            st.session_state.m14_priority_awarded=True; awarded+=25
        if set(m14_actions)==actions_correct and not st.session_state.get("m14_actions_awarded",False):
            st.session_state.m14_actions_awarded=True; awarded+=20
        if m14_reason.startswith("Multiple independent") and not st.session_state.get("m14_reason_awarded",False):
            st.session_state.m14_reason_awarded=True; awarded+=15
        if m14_communication.startswith("Use approved") and not st.session_state.get("m14_communication_awarded",False):
            st.session_state.m14_communication_awarded=True; awarded+=15
        if awarded:
            st.session_state.score += awarded
        current=(25 if st.session_state.get("m14_chain_awarded",False) else 0)+(25 if st.session_state.get("m14_priority_awarded",False) else 0)+(20 if st.session_state.get("m14_actions_awarded",False) else 0)+(15 if st.session_state.get("m14_reason_awarded",False) else 0)+(15 if st.session_state.get("m14_communication_awarded",False) else 0)
        if current==100 and "m14" not in st.session_state.completed:
            st.session_state.completed.add("m14")
            st.success("MISSION COMPLETE — 100/100 🛡️")
            st.info("You connected identity signals, phishing evidence and the account activity into one incident-response decision.")
        elif awarded:
            st.info(f"Partial score recorded: +{awarded} points. Current mission score: {current}/100.")
        else:
            st.warning(f"No new points on this attempt. Current mission score: {current}/100.")
        if current<100:
            st.caption("Re-check the evidence chain and prioritize containment, preservation, escalation and controlled communication.")
    mission_feedback("m14")
    if st.button("← BACK TO FINAL CHALLENGE"): go("final")

# ---------- M15 ----------
elif st.session_state.page == "m15":
    st.markdown("# 🏆 Mission 15 — Digital Evidence Case")
    st.caption("FINAL CHALLENGE • Build an evidence timeline and protect investigative integrity")
    st.html('<div class="mission"><h2>CASE FILE</h2><p>A school account may have been used to send a suspicious message. You have four pieces of evidence from different systems and must build a defensible timeline before deciding what to communicate.</p></div>')
    st.html('<div class="evidence"><b>09:02</b> — unusual sign-in recorded<br><b>09:05</b> — message sent from the account<br><b>09:07</b> — user reports the activity was not theirs<br><b>09:10</b> — security team preserves authentication logs</div>')
    for flag in ["m15_timeline_awarded","m15_integrity_awarded","m15_analysis_awarded","m15_communication_awarded"]:
        if flag not in st.session_state: st.session_state[flag]=False

    st.markdown("### STEP 1 — Build the evidence chain.")
    timeline=st.multiselect("Select the events that belong in the incident timeline.",["09:02 unusual sign-in","09:05 message sent","09:07 user denies activity","09:10 authentication logs preserved","A future event that has not happened yet"],key="m15_timeline")

    st.markdown("### STEP 2 — Protect evidence integrity.")
    integrity=st.multiselect("Select appropriate evidence-handling practices.",["Preserve original logs where possible","Record timestamps and source of evidence","Document actions taken during the investigation","Edit the original logs to make them easier to read","Delete inconvenient evidence"],key="m15_integrity")

    st.markdown("### STEP 3 — Analyze before concluding.")
    analysis=st.radio("What is the most defensible conclusion at this stage?",["The account is definitely compromised and no further review is needed.","The events form a suspicious sequence that warrants investigation and containment while evidence is preserved.","The user must be blamed because the message came from their account.","The incident can be ignored because the logs were preserved."],key="m15_analysis")

    st.markdown("### STEP 4 — Communicate the findings.")
    communication=st.radio("How should the findings be shared?",["Use approved channels, summarize verified facts and identify what remains unknown.","Publish all account and log details publicly.","Share raw credentials to prove the account was involved.","Remove uncertain information and present assumptions as facts."],key="m15_communication")

    if st.button("SUBMIT INVESTIGATION", type="primary", key="submit_m15"):
        record_attempt("m15")
        if set(timeline)=={"09:02 unusual sign-in","09:05 message sent","09:07 user denies activity","09:10 authentication logs preserved"}:
            if not st.session_state.get("m15_timeline_awarded", False):
                complete("m15",25)
                st.session_state.m15_timeline_awarded=True
        else:
            st.warning("Review this step and select the safest documented response.")
        if set(integrity)=={"Preserve original logs where possible","Record timestamps and source of evidence","Document actions taken during the investigation"}:
            if not st.session_state.get("m15_integrity_awarded", False):
                complete("m15",25)
                st.session_state.m15_integrity_awarded=True
        else:
            st.warning("Review this step and select the safest documented response.")
        if analysis.startswith("The events form"):
            if not st.session_state.get("m15_analysis_awarded", False):
                complete("m15",25)
                st.session_state.m15_analysis_awarded=True
        else:
            st.warning("Review this step and select the safest documented response.")
        if communication.startswith("Use approved channels"):
            if not st.session_state.get("m15_communication_awarded", False):
                complete("m15",25)
                st.session_state.m15_communication_awarded=True
        else:
            st.warning("Review this step and select the safest documented response.")

    mission_feedback("m15")
    if all(st.session_state.get(x) for x in ["m15_timeline_awarded","m15_integrity_awarded","m15_analysis_awarded","m15_communication_awarded"]):
        st.session_state.completed.add("m15")
        st.success("MISSION COMPLETE — 100/100 🛡️")
        st.info("You built a defensible evidence chain and communicated findings without overstating what the evidence proves.")
    if st.button("← BACK TO FINAL CHALLENGE",key="back_m15"): go("final")

# ---------- M16 ----------
elif st.session_state.page == "m16":
    st.markdown("# 🏆 Mission 16 — Cyber Defender: Final Mission")
    st.caption("FINAL CHALLENGE • Full cross-lab incident investigation")
    st.html('<div class="mission"><h2>FINAL CASE</h2><p>A staff account receives an unexpected MFA prompt. Minutes later, a suspicious link is sent from that account. A new device appears in the sign-in record, and one shared folder shows an unexpected access event.</p></div>')
    st.html('<div class="evidence"><b>Signal A:</b> unexpected MFA prompt<br><b>Signal B:</b> suspicious message from the account<br><b>Signal C:</b> unfamiliar device login<br><b>Signal D:</b> unusual shared-folder access<br><b>Unknown:</b> whether files were copied or credentials were exposed</div>')
    for flag in ["m16_detect_awarded","m16_contain_awarded","m16_investigate_awarded","m16_impact_awarded"]:
        if flag not in st.session_state: st.session_state[flag]=False

    st.markdown("### STEP 1 — Detect the connected signals.")
    detect=st.multiselect("Select all signals that should be investigated together.",["Unexpected MFA prompt","Suspicious message sent from the account","Unfamiliar device login","Unexpected shared-folder access","The user's job title"],key="m16_detect")

    st.markdown("### STEP 2 — Contain the account and exposure.")
    contain=st.multiselect("Select the safest immediate actions.",["Secure the account through the approved process","Preserve authentication and access evidence","Restrict inappropriate sharing/access where authorized","Forward the suspicious link to students for testing","Delete all evidence before changing access"],key="m16_contain")

    st.markdown("### STEP 3 — Investigate the scope.")
    investigate=st.multiselect("Which follow-up checks are appropriate?",["Review authentication and account activity","Review relevant sharing/access logs","Determine which messages or links were sent","Assume every file was copied without checking evidence","Ask the user to provide their password"],key="m16_investigate")

    st.markdown("### STEP 4 — Assess impact and close the response loop.")
    impact=st.radio("What is the most appropriate final approach?",["Document verified findings, assess affected data/users, escalate through the approved process, and communicate only what responsible people need to know.","Declare the incident solved as soon as the password changes.","Publish the suspected user's information so others can investigate.","Delete the evidence once the account is secured."],key="m16_impact")

    if st.button("SUBMIT FINAL MISSION", type="primary", key="submit_m16"):
        record_attempt("m16")
        if set(detect)=={"Unexpected MFA prompt","Suspicious message sent from the account","Unfamiliar device login","Unexpected shared-folder access"}:
            if not st.session_state.get("m16_detect_awarded", False):
                complete("m16",25)
                st.session_state.m16_detect_awarded=True
        else:
            st.warning("Review this step and select the safest documented response.")
        if set(contain)=={"Secure the account through the approved process","Preserve authentication and access evidence","Restrict inappropriate sharing/access where authorized"}:
            if not st.session_state.get("m16_contain_awarded", False):
                complete("m16",25)
                st.session_state.m16_contain_awarded=True
        else:
            st.warning("Review this step and select the safest documented response.")
        if set(investigate)=={"Review authentication and account activity","Review relevant sharing/access logs","Determine which messages or links were sent"}:
            if not st.session_state.get("m16_investigate_awarded", False):
                complete("m16",25)
                st.session_state.m16_investigate_awarded=True
        else:
            st.warning("Review this step and select the safest documented response.")
        if impact.startswith("Document verified"):
            if not st.session_state.get("m16_impact_awarded", False):
                complete("m16",25)
                st.session_state.m16_impact_awarded=True
        else:
            st.warning("Review this step and select the safest documented response.")

    mission_feedback("m16")
    m16_complete_now = all(st.session_state.get(x) for x in ["m16_detect_awarded","m16_contain_awarded","m16_investigate_awarded","m16_impact_awarded"])
    if m16_complete_now:
        was_completed = "m16" in st.session_state.completed
        st.session_state.completed.add("m16")
        st.success("🏆 CYBER DEFENDER — 100/100 🛡️")
        st.info("You completed the full Virtual CyberLab cycle: detect → contain → investigate → assess impact → communicate safely.")
        if not was_completed:
            st.balloons()
    if st.button("← BACK TO FINAL CHALLENGE",key="back_m16"): go("final")

# Persist learner state after each completed interaction.
if (st.session_state.get("learner_id") and st.session_state.get("db_ready")
        and st.session_state.get("page") != "teacher"
        and st.session_state.get("progress_dirty", False)):
    save_progress()
    st.session_state.progress_dirty = False
