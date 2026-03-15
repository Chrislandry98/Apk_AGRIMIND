# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 23:05:29 2026

@author: Chris Landry
"""

# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
from datetime import datetime
import numpy as np
import plotly.express as px
# --------------------------
# CONFIG PAGE
# --------------------------
st.set_page_config(page_title="AgriMind Dashboard", page_icon="📊", layout="wide")

# --------------------------
# SESSION INIT
# --------------------------
if 'user_role' not in st.session_state:
    st.session_state['user_role'] = None
if 'user_name' not in st.session_state:
    st.session_state['user_name'] = None
if 'alertes' not in st.session_state:
    st.session_state['alertes'] = [{"Date":datetime.now().strftime("%Y-%m-%d %H:%M"),
                                    "Récolte":"Maïs", "Statut":"⚠️ VIGILANCE", "Action":"Arrosage préventif"}]
if 'orders' not in st.session_state:
    st.session_state['orders'] = []

# --------------------------
# LOGIN SIMPLE
# --------------------------
def login():
    st.title("🔐 Connexion AgriMind")
    username = st.text_input("Nom d'utilisateur")
    password = st.text_input("Mot de passe", type="password")
    if st.button("Se connecter"):
        if username.lower() == "admin" and password == "admin123":
            st.session_state['user_role'] = "admin"
            st.session_state['user_name'] = "Admin"
        else:
            st.session_state['user_role'] = "client"
            st.session_state['user_name'] = username
        # Au lieu de st.experimental_rerun(), on recharge la page avec st.experimental_set_query_params
        st.session_state['login_done'] = True
        st.stop()  # stoppe l'exécution pour rafraîchir et passer au contenu

if st.session_state['user_role'] is None:
    login()
    st.stop()  # stop ici pour ne pas exécuter le dashboard tant que login pas fait

# --------------------------
# CONTENU ADMIN (TON CODE COLLE)
# --------------------------
if st.session_state['user_role']=="admin":
    # === INSERER ICI TON CODE COMPLET Figma / KPI / ENT / ACTIVITE / TABLE ===
    # Je vais juste mettre ton code précédent tel quel
    st.title("🌍 AgriMind Global Expert")

    st.markdown(
    """
    <div class="main-header">
    🌾 AGRIMIND - Intelligent Agriculture Analytics & Crop Monitoring
    <br>
    Plateforme IA pour Agriculture Intelligente
    </div>
    """,
    unsafe_allow_html=True
    )

    # ... ici tu colles tout ton code complet des KPI, activité, tableau, pagination etc. ...
    # Configuration de la page
    st.set_page_config(
        page_title="Dashboard Visiteurs",
        page_icon="📊",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # CSS personnalisé pour reproduire le design Figma
    st.markdown("""
    <style>
        /* Fond sombre global */
        .stApp {
            background-color: #0f1219;
        }
        
        /* Sidebar */
        [data-testid="stSidebar"] {
            background-color: #131825;
            border-right: 1px solid #2a3344;
        }
        
        [data-testid="stSidebar"] .stMarkdown {
            color: #94a3b8;
        }
        
        /* Cartes KPI */
        .kpi-card {
            background-color: #1a1f2e;
            border-radius: 12px;
            padding: 20px;
            border: 1px solid #2a3344;
        }
        
        .kpi-value {
            font-size: 2.5rem;
            font-weight: 700;
            color: #e2e8f0;
            margin: 10px 0;
        }
        
        .kpi-label {
            font-size: 0.75rem;
            color: #64748b;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }
        
        .kpi-trend-up {
            color: #22c55e;
            font-size: 0.875rem;
        }
        
        .kpi-trend-down {
            color: #ef4444;
            font-size: 0.875rem;
        }
        
        /* Cards génériques */
        .dashboard-card {
            background-color: #1a1f2e;
            border-radius: 12px;
            padding: 24px;
            border: 1px solid #2a3344;
            margin-bottom: 20px;
        }
        
        .card-title {
            font-size: 1.25rem;
            font-weight: 600;
            color: #e2e8f0;
            margin-bottom: 8px;
        }
        
        .card-subtitle {
            font-size: 0.875rem;
            color: #64748b;
            margin-bottom: 20px;
        }
        
        /* Barres de progression */
        .funnel-bar {
            height: 40px;
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-weight: 600;
            margin-bottom: 16px;
        }
        
        /* Activité récente */
        .activity-item {
            display: flex;
            align-items: center;
            padding: 12px 0;
            border-bottom: 1px solid #2a3344;
        }
        
        .activity-avatar {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-weight: 600;
            margin-right: 12px;
        }
        
        /* Badges */
        .badge {
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.75rem;
            font-weight: 500;
        }
        
        .badge-premium { background-color: #22c55e; color: white; }
        .badge-actif { background-color: #22c55e; color: white; }
        .badge-inactif { background-color: #374151; color: white; }
        .badge-ads { background-color: #3b82f6; color: white; }
        .badge-organic { background-color: #22c55e; color: white; }
        .badge-social { background-color: #a855f7; color: white; }
        .badge-linkedin { background-color: #0077b5; color: white; }
        
        /* Table */
        .dataframe {
            background-color: #1a1f2e !important;
        }
        
        .dataframe th {
            background-color: #1a1f2e !important;
            color: #64748b !important;
            text-transform: uppercase;
            font-size: 0.75rem;
            letter-spacing: 0.05em;
        }
        
        .dataframe td {
            background-color: #1a1f2e !important;
            color: #e2e8f0 !important;
            border-color: #2a3344 !important;
        }
        
        /* Texte global */
        h1, h2, h3, h4, h5, h6, p, span, div {
            color: #e2e8f0;
        }
        
        /* Navigation sidebar */
        .nav-item {
            padding: 12px 16px;
            border-radius: 8px;
            margin-bottom: 4px;
            cursor: pointer;
            transition: background-color 0.2s;
        }
        
        .nav-item:hover {
            background-color: #1e2433;
        }
        
        .nav-item.active {
            background-color: #3b82f6;
            color: white;
        }
    </style>
    """, unsafe_allow_html=True)

    # ============ SIDEBAR ============
    with st.sidebar:
        st.markdown("### NAVIGATION")
        st.markdown("---")
        
        # Menu de navigation
        menu_items = [
            ("📊", "Dashboard", True),
            ("👥", "Utilisateurs", False),
            ("🔽", "Entonnoir", False),
            ("💳", "Abonnements", False),
            ("📢", "Campagnes", False),
            ("📅", "Calendrier", False),
            ("⚙️", "Paramètres", False),
        ]
        
        for icon, label, is_active in menu_items:
            if is_active:
                st.markdown(f"""
                    <div style="background-color: #3b82f6; padding: 12px 16px; border-radius: 8px; margin-bottom: 8px; display: flex; align-items: center; gap: 12px;">
                        <span>{icon}</span>
                        <span style="color: white; font-weight: 500;">{label}</span>
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                    <div style="padding: 12px 16px; border-radius: 8px; margin-bottom: 8px; display: flex; align-items: center; gap: 12px; cursor: pointer;">
                        <span>{icon}</span>
                        <span style="color: #94a3b8;">{label}</span>
                    </div>
                """, unsafe_allow_html=True)

    # ============ CONTENU PRINCIPAL ============

    # KPI Cards
    st.markdown("## Dashboard")
    st.markdown("---")

    kpi_data = [
        {"icon": "👥", "color": "#3b82f6", "label": "UTILISATEURS", "value": "1 200", "trend": "+12%", "trend_label": "vs mois dernier", "up": True},
        {"icon": "⬇️", "color": "#22c55e", "label": "TÉLÉCHARGEMENTS", "value": "200", "trend": "+16.6%", "trend_label": "Conversion", "up": True},
        {"icon": "👤", "color": "#f97316", "label": "COMPTES", "value": "80", "trend": "↓40%", "trend_label": "Conversion", "up": False},
        {"icon": "📈", "color": "#22c55e", "label": "ACTIFS", "value": "35", "trend": "+43.7%", "trend_label": "Conversion", "up": True},
        {"icon": "⭐", "color": "#eab308", "label": "PREMIUM", "value": "12", "trend": "+34.3%", "trend_label": "Conversion", "up": True},
    ]

    cols = st.columns(5)
    for i, kpi in enumerate(kpi_data):
        with cols[i]:
            trend_color = "#22c55e" if kpi["up"] else "#ef4444"
            trend_icon = "↗" if kpi["up"] else "↘"
            st.markdown(f"""
                <div class="dashboard-card">
                    <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 12px;">
                        <div style="background-color: {kpi['color']}; width: 40px; height: 40px; border-radius: 8px; display: flex; align-items: center; justify-content: center; font-size: 1.25rem;">
                            {kpi['icon']}
                        </div>
                        <span class="kpi-label">{kpi['label']}</span>
                    </div>
                    <div class="kpi-value">{kpi['value']}</div>
                    <div style="color: {trend_color}; font-size: 0.875rem;">
                        {trend_icon} {kpi['trend']} <span style="color: #64748b;">{kpi['trend_label']}</span>
                    </div>
                </div>
            """, unsafe_allow_html=True)

    # Deux colonnes: Entonnoir et Activité
    col1, col2 = st.columns([2, 1])

    # ============ VISUALISATION ENTONNOIR ============
    with col1:
        st.markdown("""
            <div class="dashboard-card">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <span class="card-title">Visualisation de l'Entonnoir</span>
                    <a href="#" style="color: #3b82f6; text-decoration: none; font-size: 0.875rem;">Voir détails →</a>
                </div>
                <div class="card-subtitle">Taux de Conversion par Étape</div>
            </div>
        """, unsafe_allow_html=True)
        
        funnel_data = [
            {"label": "Visiteurs LP", "value": 1200, "percent": 100, "color": "#3b82f6"},
            {"label": "Agriculteurs Touchés", "value": 1000, "percent": 83, "color": "#3b82f6"},
            {"label": "Téléchargements", "value": 500, "percent": 42, "color": "#a855f7"},
            {"label": "Comptes Créés", "value": 200, "percent": 17, "color": "#f97316"},
            {"label": "Abonnements", "value": 50, "percent": 4, "color": "#ef4444"},
        ]
        
        for item in funnel_data:
            col_label, col_bar = st.columns([1, 3])
            with col_label:
                st.markdown(f"""
                    <div style="display: flex; justify-content: space-between; align-items: center; height: 45px;">
                        <span style="color: #e2e8f0; font-size: 0.875rem;">{item['label']}</span>
                        <span style="color: #64748b; font-size: 0.875rem;">{item['value']:,} ({item['percent']}%)</span>
                    </div>
                """, unsafe_allow_html=True)
            with col_bar:
                st.markdown(f"""
                    <div style="width: {item['percent']}%; background-color: {item['color']}; height: 40px; border-radius: 8px; display: flex; align-items: center; justify-content: center; color: white; font-weight: 600;">
                        {item['percent']}%
                    </div>
                """, unsafe_allow_html=True)

    # ============ ACTIVITÉ RÉCENTE ============
    with col2:
        st.markdown("""
            <div class="card-title">Activité Récente</div>
        """, unsafe_allow_html=True)
        
        activities = [
            {"icon": "⭐", "color": "#eab308", "title": "Nouvel abonnement Premium", "user": "Jean Dupont • Ferme du Soleil", "time": "Il y a 5 min"},
            {"icon": "💰", "color": "#22c55e", "title": "Agriculteur devenu actif", "user": "Marie Martin", "time": "Il y a 12 min"},
            {"icon": "👤", "color": "#a855f7", "title": "Nouveau téléchargement", "user": "Pierre Durand", "time": "Il y a 23 min"},
            {"icon": "✓", "color": "#3b82f6", "title": "Compte créé", "user": "Sophie Leroy", "time": "Il y a 34 min"},
            {"icon": "🔴", "color": "#ef4444", "title": "Pic de visites", "user": "+45 visiteurs en 1h", "time": "Il y a 1h"},
        ]
        
        for activity in activities:
            st.markdown(f"""
                <div style="display: flex; align-items: center; padding: 16px 0; border-bottom: 1px solid #2a3344;">
                    <div style="background-color: {activity['color']}; width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-right: 12px;">
                        {activity['icon']}
                    </div>
                    <div>
                        <div style="color: #e2e8f0; font-weight: 500; font-size: 0.875rem;">{activity['title']}</div>
                        <div style="color: #64748b; font-size: 0.75rem;">{activity['user']}</div>
                        <div style="color: #475569; font-size: 0.75rem;">{activity['time']}</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

    # ============ TABLEAU DES CONVERSIONS ============
    st.markdown("---")
    st.markdown("""
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
            <span class="card-title">Détails des Conversions</span>
        </div>
    """, unsafe_allow_html=True)

    # Filtre statut
    status_filter = st.selectbox(
        "Filtrer par statut",
        ["Tous les statuts", "Premium", "Actif", "Inactif"],
        label_visibility="collapsed"
    )

    # Données du tableau
    users_data = [
        {"initials": "JD", "color": "#3b82f6", "name": "Jean Dupont", "email": "jean.dupont@email.com", "date": "12 Mar 2024", "source": "Ads", "source_color": "#3b82f6", "status": "Premium", "status_color": "#22c55e", "activity": 85},
        {"initials": "MM", "color": "#22c55e", "name": "Marie Martin", "email": "marie.martin@email.com", "date": "10 Mar 2024", "source": "Organic", "source_color": "#22c55e", "status": "Actif", "status_color": "#22c55e", "activity": 60},
        {"initials": "PD", "color": "#a855f7", "name": "Pierre Durand", "email": "pierre.durand@email.com", "date": "08 Mar 2024", "source": "Social", "source_color": "#a855f7", "status": "Inactif", "status_color": "#374151", "activity": 10},
        {"initials": "SL", "color": "#f97316", "name": "Sophie Leroy", "email": "sophie.leroy@email.com", "date": "05 Mar 2024", "source": "LinkedIn", "source_color": "#0077b5", "status": "Actif", "status_color": "#22c55e", "activity": 45},
    ]

    # Entêtes du tableau
    header_cols = st.columns([2, 1.5, 1, 1, 1, 0.5])
    headers = ["UTILISATEUR", "DATE D'INSCRIPTION", "SOURCE", "STATUT", "ACTIVITÉ", "ACTION"]
    for i, header in enumerate(headers):
        with header_cols[i]:
            st.markdown(f"<span style='color: #64748b; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.05em;'>{header}</span>", unsafe_allow_html=True)

    st.markdown("<div style='border-bottom: 1px solid #2a3344; margin: 8px 0;'></div>", unsafe_allow_html=True)

    # Lignes du tableau
    for user in users_data:
        cols = st.columns([2, 1.5, 1, 1, 1, 0.5])
        
        with cols[0]:
            st.markdown(f"""
                <div style="display: flex; align-items: center; gap: 12px;">
                    <div style="background-color: {user['color']}; width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-weight: 600;">
                        {user['initials']}
                    </div>
                    <div>
                        <div style="color: #e2e8f0; font-weight: 500;">{user['name']}</div>
                        <div style="color: #64748b; font-size: 0.75rem;">{user['email']}</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
        
        with cols[1]:
            st.markdown(f"<span style='color: #e2e8f0;'>{user['date']}</span>", unsafe_allow_html=True)
        
        with cols[2]:
            st.markdown(f"""
                <span style="background-color: {user['source_color']}; padding: 4px 12px; border-radius: 20px; font-size: 0.75rem; color: white;">
                    {user['source']}
                </span>
            """, unsafe_allow_html=True)
        
        with cols[3]:
            st.markdown(f"""
                <span style="background-color: {user['status_color']}; padding: 4px 12px; border-radius: 20px; font-size: 0.75rem; color: white; display: inline-flex; align-items: center; gap: 4px;">
                    ⭐ {user['status']}
                </span>
            """, unsafe_allow_html=True)
        
        with cols[4]:
            activity_color = "#22c55e" if user['activity'] > 50 else "#f97316" if user['activity'] > 20 else "#ef4444"
            st.markdown(f"""
                <div style="display: flex; align-items: center; gap: 8px;">
                    <div style="flex: 1; height: 8px; background-color: #2a3344; border-radius: 4px; overflow: hidden;">
                        <div style="width: {user['activity']}%; height: 100%; background-color: {activity_color}; border-radius: 4px;"></div>
                    </div>
                    <span style="color: #e2e8f0; font-size: 0.875rem;">{user['activity']}%</span>
                </div>
            """, unsafe_allow_html=True)
        
        with cols[5]:
            st.markdown("⋮", unsafe_allow_html=True)
        
        st.markdown("<div style='border-bottom: 1px solid #2a3344; margin: 12px 0;'></div>", unsafe_allow_html=True)

    # Pagination
    st.markdown("---")
    pagination_cols = st.columns([3, 1])
    with pagination_cols[0]:
        st.markdown("<span style='color: #64748b;'>Affichage 1-4 sur 52 résultats</span>", unsafe_allow_html=True)
    with pagination_cols[1]:
        page_cols = st.columns(7)
        pages = ["<", "1", "2", "3", "...", "13", ">"]
        for i, page in enumerate(pages):
            with page_cols[i]:
                if page == "1":
                    st.markdown(f"<div style='background-color: #3b82f6; color: white; width: 32px; height: 32px; border-radius: 8px; display: flex; align-items: center; justify-content: center; cursor: pointer;'>{page}</div>", unsafe_allow_html=True)
                else:
                    st.markdown(f"<div style='color: #64748b; width: 32px; height: 32px; display: flex; align-items: center; justify-content: center; cursor: pointer;'>{page}</div>", unsafe_allow_html=True)

# --------------------------
# CONTENU CLIENT (CODE DETAILLE)
# --------------------------
else:
    st.set_page_config(page_title="AgriMind Client Dashboard", layout="wide")
    
    # --- HEADER ---
    col1,col2 = st.columns([8,2])
    with col1:
        st.title("🌾 AgriMind Agriculture Analytics")
    with col2:
        st.write("👤 Client Portal")
    st.divider()
    
    # --- KPI CARDS: Total production, stock, commandes, clients ---
    c1,c2,c3,c4 = st.columns(4)
    kpis = [
        ("Production totale", "124 T"),
        ("Stock total", "52 T"),
        ("Commandes", "36"),
        ("Clients", "18")
    ]
    for i,(title,value) in enumerate(kpis):
        with [c1,c2,c3,c4][i]:
            st.markdown(f"""
            <div style="background:#1e293b; padding:20px; border-radius:12px; text-align:center; color:white;">
                <div style="font-size:14px; color:#94a3b8;">{title}</div>
                <div style="font-size:28px; font-weight:bold;">{value}</div>
            </div>
            """, unsafe_allow_html=True)
    
    # --- GRAPHIQUE DE PRODUCTION PAR JOUR ---
    st.markdown('<div style="font-size:20px; font-weight:bold; color:white; margin-top:20px;">📈 Production quotidienne & prévisions</div>', unsafe_allow_html=True)
    dates = pd.date_range(start="2026-03-01", periods=30)
    production = np.random.randint(10,40,30)
    prevision = production + np.random.randint(5,15,30)
    df_prod = pd.DataFrame({"date":dates, "production":production, "prévision":prevision})
    fig = px.line(df_prod, x="date", y=["production","prévision"], labels={"value":"Quantité (T)", "variable":"Type"}, markers=True)
    st.plotly_chart(fig,use_container_width=True)
    
    # --- REPARTITION PAR CULTURE ---
    st.markdown('<div style="font-size:20px; font-weight:bold; color:white; margin-top:20px;">🌾 Répartition des cultures</div>', unsafe_allow_html=True)
    crops = pd.DataFrame({
        "culture":["Myrtille","Maïs","Riz","Sorgho"],
        "production":[45,60,30,20],
        "prévision":[50,65,35,25]
    })
    fig2 = px.bar(crops, x="culture", y=["production","prévision"], barmode="group", labels={"value":"Quantité (T)","variable":"Type"})
    st.plotly_chart(fig2,use_container_width=True)
    
    # --- STOCK PAR SILO ---
    st.markdown('<div style="font-size:20px; font-weight:bold; color:white; margin-top:20px;">📦 Stock par silo</div>', unsafe_allow_html=True)
    col1,col2 = st.columns(2)
    silos = {"Myrtille":80,"Maïs":65,"Riz":45,"Sorgho":30}
    for c in col1, col2:
        for culture, val in list(silos.items())[:2]:
            c.progress(val)
            c.write(f"{culture} silo")
        silos = dict(list(silos.items())[2:])
    
    # --- COMMANDES RÉCENTES ---
    st.markdown('<div style="font-size:20px; font-weight:bold; color:white; margin-top:20px;">🛒 Commandes récentes</div>', unsafe_allow_html=True)
    orders = pd.DataFrame({
        "Client":["Restaurant A","Supermarché B","Exportateur C","Grossiste D"],
        "Produit":["Myrtille","Maïs","Riz","Sorgho"],
        "Quantité":["2T","5T","3T","4T"],
        "Statut":["Livré","En cours","Préparation","Livré"]
    })
    st.dataframe(orders,use_container_width=True)
    
    # --- TOP CLIENTS ---
    col1,col2 = st.columns(2)
    with col1:
        st.markdown('<div style="font-size:20px; font-weight:bold; color:white; margin-top:20px;">👥 Top Clients</div>', unsafe_allow_html=True)
        clients = pd.DataFrame({"Client":["Supermarché A","Restaurant B","Exportateur C"],"Volume":[12,8,18]})
        st.dataframe(clients,use_container_width=True)
    with col2:
        st.markdown('<div style="font-size:20px; font-weight:bold; color:white; margin-top:20px;">🚨 Alerts</div>', unsafe_allow_html=True)
        alerts = pd.DataFrame({
            "Type":["ROUGE","VIGILANCE"],
            "Message":["Température silo élevée","Production faible"],
            "Date":["2026-03-14","2026-03-13"]
        })
        st.dataframe(alerts,use_container_width=True)
    
    # --- LOGISTIQUE ---
    st.markdown('<div style="font-size:20px; font-weight:bold; color:white; margin-top:20px;">🚛 Logistique</div>', unsafe_allow_html=True)
    log = pd.DataFrame({
        "Commande":["CMD1023","CMD1024","CMD1025"],
        "Destination":["Montréal","Toronto","Québec"],
        "Statut":["En transit","Préparation","Livré"]
    })
    st.dataframe(log,use_container_width=True)