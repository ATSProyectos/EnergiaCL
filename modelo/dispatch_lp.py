"""
Despacho optimo FV + BESS + conexion, por programacion lineal (horizonte semanal,
SOC explicito => matriz bandeada). Minimiza el costo economico de servir el consumo
de SQM valorando cada MWh a su costo de oportunidad horario.
"""
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix

def solve(pv, load, cmg, bess_mwh, bess_mw, tolls=18.0,
          inj_limit=40.0, imp_limit=60.0, rte=0.88, dod=0.94,
          horizon=168, grid_charge=True):
    n = len(pv)
    eta = np.sqrt(rte)
    usable = bess_mwh * dod
    out = {k: np.zeros(n) for k in ("ch","dis","imp","exp","curt","soc")}

    for s in range(0, n, horizon):
        e = min(s+horizon, n); T = e-s
        p, l, c = pv[s:e], load[s:e], cmg[s:e]
        # indices: ch[0:T] dis[T:2T] imp[2T:3T] exp[3T:4T] curt[4T:5T] soc[5T:6T]
        NV = 6*T
        CH, DI, IM, EX, CU, SO = (np.arange(T)+k*T for k in range(6))

        obj = np.zeros(NV)
        obj[IM] = c + tolls
        obj[EX] = -c
        obj[CH] = 1e-4; obj[DI] = 1e-4

        rows, cols, vals, beq = [], [], [], []
        req = 0
        # (1) balance horario: dis + imp - ch - exp - curt = load - pv
        for t in range(T):
            for idx, v in ((DI[t],1.0),(IM[t],1.0),(CH[t],-1.0),(EX[t],-1.0),(CU[t],-1.0)):
                rows.append(req); cols.append(idx); vals.append(v)
            beq.append(l[t]-p[t]); req += 1
        # (2) dinamica del SOC: soc_t - soc_{t-1} - eta*ch_t + dis_t/eta = 0
        for t in range(T):
            rows += [req, req]; cols += [SO[t], CH[t]]; vals += [1.0, -eta]
            rows.append(req); cols.append(DI[t]); vals.append(1.0/eta)
            if t == 0:
                beq.append(usable/2.0)          # SOC inicial de la semana
            else:
                rows.append(req); cols.append(SO[t-1]); vals.append(-1.0)
                beq.append(0.0)
            req += 1
        # (3) cierre ciclico: soc_final = usable/2
        rows.append(req); cols.append(SO[T-1]); vals.append(1.0); beq.append(usable/2.0); req += 1

        Aeq = coo_matrix((vals,(rows,cols)), shape=(req,NV)).tocsr()

        lb = np.zeros(NV); ub = np.zeros(NV)
        ub[CH] = bess_mw; ub[DI] = bess_mw
        ub[IM] = imp_limit; ub[EX] = inj_limit
        ub[CU] = np.maximum(p,0)+1e-6
        ub[SO] = usable
        if bess_mwh <= 0:
            ub[CH] = 0; ub[DI] = 0
        if not grid_charge:
            ub[CH] = np.minimum(bess_mw, np.maximum(p-l, 0))

        r = linprog(obj, A_eq=Aeq, b_eq=np.array(beq),
                    bounds=np.column_stack([lb,ub]), method="highs")
        if not r.success:
            raise RuntimeError(f"LP infactible en h={s}: {r.message}")
        x = r.x
        out["ch"][s:e]=x[CH]; out["dis"][s:e]=x[DI]; out["imp"][s:e]=x[IM]
        out["exp"][s:e]=x[EX]; out["curt"][s:e]=x[CU]; out["soc"][s:e]=x[SO]

    out["served_local"] = load - out["imp"]
    out["cycles"] = out["dis"].sum()/max(usable,1e-9)
    return out
