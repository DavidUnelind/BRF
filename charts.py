import plotly.graph_objects as go

def generateWaterfall(totalKostnad, 
                          resultat, 
                          finansiellaKostnader, 
                          jämförelsestörande,
                          avskrivning,
                          amortering,
                          avsättning):
    intäkter = totalKostnad + resultat
    resultEfterFinansella = resultat - finansiellaKostnader
    likviditet = resultEfterFinansella - jämförelsestörande + avskrivning - amortering
    referensAvgiftsUttag = likviditet - avsättning
    waterfall = go.Figure(go.Waterfall(
        name = "Tusentals kronor", orientation = "v",
        measure = ["relative", #Relative (delta) eller total
                   "relative", 
                   "total", 
                   "relative", 
                   "total", 
                   "relative",
                   "relative",
                   "relative",
                   "total",
                   "relative",
                   "total"],
        x = ["Intäkter", #Texten under
             "Totala kostnader", 
             "Resultat, exklusive finansiella kostnader", 
             "Finansiella kostnader", 
             "Resultat efter finansiella kostnader", 
             "Jämförelsestörande kostnader",
             "Avskrivning",
             "Amortering",
             "Likviditet",
             "Avsättning till underhållsplan",
             "Referens avgiftsuttag"],
        textposition = "outside",
        text = [int(intäkter), #Värdet som står ovanför/under
                int(-totalKostnad), 
                int(resultat), 
                int(-finansiellaKostnader), 
                int(resultEfterFinansella), 
                int(jämförelsestörande), 
                int(avskrivning), 
                int(-amortering), 
                int(likviditet), 
                int(-avsättning), 
                int(referensAvgiftsUttag)], 
        y = [intäkter, #Värdet
             -totalKostnad, 
             0, 
             -finansiellaKostnader, 
             0, 
             -jämförelsestörande, 
             avskrivning, 
             -amortering, 
             0, 
             -avsättning, 
             0],
        connector = {"line":{"color":"rgb(63, 63, 63)"}},
    ))

    waterfall.update_layout(
            title = "Analys ekonomi BRF ",
            showlegend = True,
            margin=dict(l=30, r=30, t=30, b=30)
    )
    waterfall.write_image("static/images/waterfall.png")

def generateNyckelTal(totalLån, 
                          totalYta, 
                          boarea, 
                          intäkt,
                          underhållsutrymme,
                          driftskostnad,
                          amortering,
                          finansiellaKostnader):
    
    lånPerkvmTotalYta = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = totalLån * 1000 / totalYta,
        domain = {"x": [0, 1], "y": [0, 1]},
        number = {
            "valueformat": ".0f"
        },
        gauge = {
        "axis": {"range": [0, 15000], "tickwidth": 1, "tickcolor": "darkblue"},
        'bar': {'color': "black", "thickness" : 0.1},
        "bgcolor": "white",
        "borderwidth": 2,
        "bordercolor": "gray",
        "steps": [
            {"range": [0, 5000], "color": "green"},
            {"range": [5000, 10000], "color": "yellow"},
            {"range": [10000, 15000], "color": "red"}]},
        title = {"text": "Lån per kvm totalyta (kr/kvm)"}))
    lånPerkvmTotalYta.write_image("static/images/lånPerkvmTotalYta.png")

    totalYtaToBoareaFactor = totalYta / boarea
    lånPerkvmBoarea = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = totalLån * 1000 / boarea,
        domain = {"x": [0, 1], "y": [0, 1]},
        number = {
            "valueformat": ".0f"
        },
        gauge = {
        "axis": {"range": [0, 15000 * totalYtaToBoareaFactor], "tickwidth": 1, "tickcolor": "darkblue"},
        'bar': {'color': "black", "thickness" : 0.1},
        "bgcolor": "white",
        "borderwidth": 2,
        "bordercolor": "gray",
        "steps": [
            {"range": [0, 5000 * totalYtaToBoareaFactor], "color": "green"},
            {"range": [5000 * totalYtaToBoareaFactor, 10000 * totalYtaToBoareaFactor], "color": "yellow"},
            {"range": [10000 * totalYtaToBoareaFactor, 15000 * totalYtaToBoareaFactor], "color": "red"}]},
        title = {"text": "Lån per kvm boarea (kr/kvm)"}))
    lånPerkvmBoarea.write_image("static/images/lånPerkvmBoarea.png")

    skuldkvot = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = totalLån / intäkt,
        domain = {"x": [0, 1], "y": [0, 1]},
        number = {
            "valueformat": ".1f"
        },
        gauge = {
        "axis": {"range": [0, 25], "tickwidth": 1, "tickcolor": "darkblue"},
        'bar': {'color': "black", "thickness" : 0.1},
        "bgcolor": "white",
        "borderwidth": 2,
        "bordercolor": "gray",
        "steps": [
            {"range": [0, 10], "color": "green"},
            {"range": [10, 20], "color": "yellow"},
            {"range": [20, 25], "color": "red"}]},
        title = {"text": "Skuldkvot (lån/intäkt)"}))
    skuldkvot.write_image("static/images/skuldkvot.png")

    UHutrymmeProcent = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = underhållsutrymme / intäkt,
        domain = {"x": [0, 1], "y": [0, 1]},
        number = {
            "valueformat": ".0%"
        },
        gauge = {
        "axis": {"range": [0, 0.75], "tickwidth": 1, "tickcolor": "darkblue", "tickformat": ".0%"},
        'bar': {'color': "black", "thickness" : 0.1},
        "bgcolor": "white",
        "borderwidth": 2,
        "bordercolor": "gray",
        "steps": [
            {"range": [0, 0.25], "color": "red"},
            {"range": [0.25, 0.50], "color": "yellow"},
            {"range": [0.50, 0.75], "color": "green"}]},
        title = {"text": "Underhålls & amorteringsutrymme i % av intäkt"}))
    UHutrymmeProcent.write_image("static/images/UHutrymmeProcent.png")

    UHutrymmePerTotalYta = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = underhållsutrymme * 1000 / totalYta,
        domain = {"x": [0, 1], "y": [0, 1]},
        number = {
            "valueformat": ".0f"
        },
        gauge = {
        "axis": {"range": [0, 500], "tickwidth": 1, "tickcolor": "darkblue"},
        'bar': {'color': "black", "thickness" : 0.1},
        "bgcolor": "white",
        "borderwidth": 2,
        "bordercolor": "gray",
        "steps": [
            {"range": [0, 150], "color": "red"},
            {"range": [150, 250], "color": "yellow"},
            {"range": [250, 500], "color": "green"}]},
        title = {"text": "Underhålls & amorteringsutrymme per kvm totalyta (kr/kvm)"}))
    UHutrymmePerTotalYta.write_image("static/images/UHutrymmePerTotalYta.png")

    driftskostnadPerKvm = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = driftskostnad * 1000 / boarea,
        domain = {"x": [0, 1], "y": [0, 1]},
        number = {
            "valueformat": ".0f"
        },
        gauge = {
        "axis": {"range": [0, 700], "tickwidth": 1, "tickcolor": "darkblue"},
        'bar': {'color': "black", "thickness" : 0.1},
        "bgcolor": "white",
        "borderwidth": 2,
        "bordercolor": "gray",
        "steps": [
            {"range": [0, 375], "color": "green"},
            {"range": [375, 550], "color": "yellow"},
            {"range": [550, 700], "color": "red"}]},
        title = {"text": "Driftskostnad per boarea (kr/kvm)"}))
    driftskostnadPerKvm.write_image("static/images/driftskostnadPerKvm.png")

    finansiellUtgift = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = (amortering + finansiellaKostnader) / totalLån,
        domain = {"x": [0, 1], "y": [0, 1]},
        number = {
            "valueformat": ".0%"
        },
        gauge = {
        "axis": {"range": [0, 0.12], "tickwidth": 1, "tickcolor": "darkblue", "tickformat": ".0%"},
        'bar': {'color': "black", "thickness" : 0.1},
        "bgcolor": "white",
        "borderwidth": 2,
        "bordercolor": "gray",
        "steps": [
            {"range": [0, 0.04], "color": "red"},
            {"range": [0.04, 0.05], "color": "yellow"},
            {"range": [0.05, 0.07], "color": "green"},
            {"range": [0.07, 0.08], "color": "yellow"},
            {"range": [0.08, 0.12], "color": "red"}]},
        title = {"text": "Finansiell utgift i % av lån"}))
    finansiellUtgift.write_image("static/images/finansiellUtgift.png")

    räntekostnadProcent = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = finansiellaKostnader / intäkt,
        domain = {"x": [0, 1], "y": [0, 1]},
        number = {
            "valueformat": ".0%"
        },
        gauge = {
        "axis": {"range": [0, 0.75], "tickwidth": 1, "tickcolor": "darkblue", "tickformat": ".0%"},
        'bar': {'color': "black", "thickness" : 0.1},
        "bgcolor": "white",
        "borderwidth": 2,
        "bordercolor": "gray",
        "steps": [
            {"range": [0, 0.25], "color": "green"},
            {"range": [0.25, 0.5], "color": "yellow"},
            {"range": [0.5, 0.75], "color": "red"}]},
        title = {"text": "Räntekostnad i % av intäkt"}))
    räntekostnadProcent.write_image("static/images/räntekostnadProcent.png")