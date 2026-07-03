import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# --- 1. INTERFACE AM ANFANG ---
st.title("🎓 Student Data Analysis Dashboard")
st.write("Willkommen! Bitte lade zuerst deine CSV-Datei hoch, um mit der Analyse zu starten.")

# Datei-Uploader erstellen
uploaded_file = st.file_uploader("Wähle deine CSV-Datei aus", type=["csv"])

# --- 2. WENN DIE DATEI HOCHGELADEN WURDE ---
if uploaded_file is not None:
    
    # Daten einlesen (Semikolon als Trennzeichen)
    df = pd.read_csv(uploaded_file, sep=";")
    df.columns = df.columns.str.strip()
    
    # Jahre extrahieren
    years = df.iloc[2:, 0]
    
    # --- 3. DIE VISUELLE SUCHMASKE (CONTAINER) ---
    with st.container(border=True):
        st.subheader("🔍 Daten-Suchmaske")
        st.write("Tippe den Namen der Gruppe ein oder wähle einen Plot aus:")
        
        # Eindeutige Selectbox (keine Duplikate mehr!)
        plot_selection = st.selectbox(
            "Diagramm-Typ auswählen:",
            [
                "Gesamtübersicht: Bestanden vs. Nicht bestanden (2 Achsen)",
                "Deutsche Männer: Bestanden",
                "Deutsche Frauen: Bestanden",
                "Ausländische Männer: Bestanden",
                "Ausländische Frauen: Bestanden",
                "Deutsche Männer: Nicht bestanden",
                "Deutsche Frauen: Nicht bestanden",
                "Ausländische Männer: Nicht bestanden",
                "Ausländische Frauen: Nicht bestanden",
                "Vergleich: Alle Bestandenen zusammen",
                "Vergleich: Alle Durchgefallenen zusammen"
            ],
            index=0,
            help="Du kannst hier auch Text eintippen, um die Liste schnell zu durchsuchen!",
            key="suchmaske_plot_auswahl"
        )
        
        # Der Search-Button (farblich hervorgehoben)
        search_clicked = st.button("Diagramm generieren", type="primary")

    # --- 4. PLOTS AUSFÜHREN ERST NACH KLICK AUF GENERIEREN ---
    if search_clicked:
        fig, ax = plt.subplots(figsize=(10, 5))
        
        # A) EINZELNE PLOTS FÜR BESTANDEN
        if plot_selection == "Deutsche Männer: Bestanden":
            data = df.iloc[2:, 1].astype(int)
            ax.plot(years, data, marker="o", color="royalblue", linewidth=2, label=f"Gesamt: {data.sum():,}".replace(",", "."))
            ax.set_title("Deutsche Männer - Bestandene Prüfungen")
            
        elif plot_selection == "Deutsche Frauen: Bestanden":
            data = df.iloc[2:, 5].astype(int)
            ax.plot(years, data, marker="o", color="darkorange", linewidth=2, label=f"Gesamt: {data.sum():,}".replace(",", "."))
            ax.set_title("Deutsche Frauen - Bestandene Prüfungen")
            
        elif plot_selection == "Ausländische Männer: Bestanden":
            data = df.iloc[2:, 9].astype(int)
            ax.plot(years, data, marker="o", color="forestgreen", linewidth=2, label=f"Gesamt: {data.sum():,}".replace(",", "."))
            ax.set_title("Ausländische Männer - Bestandene Prüfungen")
            
        elif plot_selection == "Ausländische Frauen: Bestanden":
            data = df.iloc[2:, 13].astype(int)
            ax.plot(years, data, marker="o", color="orchid", linewidth=2, label=f"Gesamt: {data.sum():,}".replace(",", "."))
            ax.set_title("Ausländische Frauen - Bestandene Prüfungen")
            
        # B) EINZELNE PLOTS FÜR NICHT BESTANDEN
        elif plot_selection == "Deutsche Männer: Nicht bestanden":
            data = df.iloc[2:, 3].astype(int)
            ax.plot(years, data, marker="o", color="blue", linewidth=2, label=f"Gesamt: {data.sum():,}".replace(",", "."))
            ax.set_title("Deutsche Männer - Nicht bestandene Prüfungen")
            
        elif plot_selection == "Deutsche Frauen: Nicht bestanden":
            data = df.iloc[2:, 7].astype(int)
            ax.plot(years, data, marker="o", color="orange", linewidth=2, label=f"Gesamt: {data.sum():,}".replace(",", "."))
            ax.set_title("Deutsche Frauen - Nicht bestandene Prüfungen")
            
        elif plot_selection == "Ausländische Männer: Nicht bestanden":
            data = df.iloc[2:, 11].astype(int)
            ax.plot(years, data, marker="o", color="firebrick", linewidth=2, label=f"Gesamt: {data.sum():,}".replace(",", "."))
            ax.set_title("Ausländische Männer - Nicht bestandene Prüfungen")
            
        elif plot_selection == "Ausländische Frauen: Nicht bestanden":
            data = df.iloc[2:, 15].astype(int)
            ax.plot(years, data, marker="o", color="darkmagenta", linewidth=2, label=f"Gesamt: {data.sum():,}".replace(",", "."))
            ax.set_title("Ausländische Frauen - Nicht bestandene Prüfungen")
            
        # C) VERGLEICHS-PLOTS ALLER GRUPPEN
        elif plot_selection == "Vergleich: Alle Bestandenen zusammen":
            ax.plot(years, df.iloc[2:, 1].astype(int), marker="o", color="royalblue", label="DE Männer")
            ax.plot(years, df.iloc[2:, 5].astype(int), marker="o", color="darkorange", label="DE Frauen")
            ax.plot(years, df.iloc[2:, 9].astype(int), marker="o", color="forestgreen", label="Ausl. Männer")
            ax.plot(years, df.iloc[2:, 13].astype(int), marker="o", color="orchid", label="Ausl. Frauen")
            ax.set_title("Vergleich: Bestandene Prüfungen aller Gruppen")
            
        elif plot_selection == "Vergleich: Alle Durchgefallenen zusammen":
            ax.plot(years, df.iloc[2:, 3].astype(int), marker="o", color="blue", label="DE Männer")
            ax.plot(years, df.iloc[2:, 7].astype(int), marker="o", color="orange", label="DE Frauen")
            ax.plot(years, df.iloc[2:, 11].astype(int), marker="o", color="firebrick", label="Ausl. Männer")
            ax.plot(years, df.iloc[2:, 15].astype(int), marker="o", color="darkmagenta", label="Ausl. Frauen")
            ax.set_title("Vergleich: Nicht bestandene Prüfungen aller Gruppen")
            
        # D) SPEZIALFALL: GESAMTÜBERSICHT MIT 2 ACHSEN
        elif plot_selection == "Gesamtübersicht: Bestanden vs. Nicht bestanden (2 Achsen)":
            plt.close(fig) # Schließe Standard-Figur
            fig, ax1 = plt.subplots(figsize=(10, 5))
            
            total_passed = df.iloc[2:, [1, 5, 9, 13]].astype(int).sum(axis=1)
            total_failed = df.iloc[2:, [3, 7, 11, 15]].astype(int).sum(axis=1)
            
            line1 = ax1.plot(years, total_passed, marker="o", color="seagreen", label="Gesamt: Bestanden", linewidth=2.5)
            ax1.set_xlabel("Jahr")
            ax1.set_ylabel("Anzahl: Bestanden (links)", color="seagreen")
            ax1.tick_params(axis='y', labelcolor="seagreen")
            
            ax2 = ax1.twinx()
            line2 = ax2.plot(years, total_failed, marker="x", color="crimson", label="Gesamt: Nicht bestanden", linewidth=2.5, linestyle="--")
            ax2.set_ylabel("Anzahl: Nicht bestanden (rechts)", color="crimson")
            ax2.tick_params(axis='y', labelcolor="crimson")
            
            lines = line1 + line2
            labels = [l.get_label() for l in lines]
            ax1.legend(lines, labels, loc="upper left")
            ax1.set_title("Gesamtvergleich: Bestanden vs. Nicht bestanden")

        # Allgemeines Styling für die Diagramme (außer bei den 2 Achsen)
        if plot_selection != "Gesamtübersicht: Bestanden vs. Nicht bestanden (2 Achsen)":
            ax.set_xlabel("Jahr")
            ax.set_ylabel("Anzahl")
            ax.grid(True, linestyle="--", alpha=0.6)
            ax.legend()

        # Diagramm anzeigen
        st.pyplot(fig)
        st.success("Diagramm erfolgreich generiert!")
        
else:
    # Infotext, solange keine Datei da ist
    st.info("Bitte lade eine CSV-Datei hoch, um das Suchfenster zu aktivieren.")