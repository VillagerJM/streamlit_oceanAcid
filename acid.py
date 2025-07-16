import streamlit as st

def calc_dpH(fe, dic0, depth, eff): #철, 초기 DIC, 유효깊이, 효율계수
    
    chl = fe * 1.5 * eff #철분농도 x 계수 x 1.5 = 클로로필 증가량   
    cmd = chl * 20 * (depth / 50) #클로로필 증가량으로 DIC 변화량 계산 (기준 깊이 50m)    
    dpH = 0.15 * (cmd / dic0)**0.8 #DIC 초기값과 변화량 기반 pH 변화량 계산 (지수 연산으로 완충력 반영)
    return round(dpH, 3)


def get_pH0(dic0):
    return round(8.3 - 0.001 * (dic0 - 2000), 3)  #pH 변화량에서 pH 결과값 유도를 위한 pH 초기값 계산. (일차식으로 단순화)

st.title("🌊 해양 철분 살포 시뮬레이터")

st.markdown("### 🧪 **철분 증가량 (Fe)**")
fe = st.slider("Fe 농도 증가량 (nM)", 0.0, 5.0, 2.0, 0.1)
st.caption("💡 일반 해역 철분 농도는 약 0.1-0.6 nM. 기존 철분살포 실험에서는 대체로 2-3nM 증가.")

st.markdown("### 🫧 **초기 DIC (용존 무기탄소)**")
dic0 = st.slider("초기 DIC (μmol/kg)", 1800, 2400, 2100, 10)
st.caption("💡 일반 해양 표층의 DIC는 1950-2150 μmol/kg. 높을수록 pH 완충력이 큼.")

st.markdown("### 🌞 **유효 광합성 깊이**")
depth = st.slider("유효 깊이 (m)", 10, 100, 50, 5)
st.caption("💡 일반적으로 여름은 20-40m, 겨울/극지는 60-80m. 깊을수록 더 많은 DIC 소비 가능.")

st.markdown("### 🌿 **환경 효율 계수**")
eff = st.slider("환경 효율 (0 = 불리함, 1 = 이상적)", 0.0, 1.0, 0.8, 0.05)
st.caption("💡 광량, 규산, 질소, 수온 등 조건의 종합 점수. SEEDS I = 1.0, LOHAFEX ≈ 0.1")

if st.button("시뮬레이션 실행"):
    dpH = calc_dpH(fe, dic0, depth, eff)
    pH0 = get_pH0(dic0)
    pH1 = round(pH0 + dpH, 3)
    st.success(f"📈 예상 pH 변화: **{pH0} → {pH1}** (ΔpH = +{dpH})")

st.markdown("---")
st.markdown("💡 예시: SEEDS I, 2001 → Fe=2, DIC=2100, 깊이=30m, 효율계수 1.0")  최종