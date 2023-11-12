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
    waterfall.write_image("static/images/fig1.png")

def test():
    fig = go.Figure(go.Waterfall(
        name = "20", orientation = "v",
        measure = ["relative", "relative", "total", "relative", "relative", "total"],
        x = ["Sales", "Consulting", "Net revenue", "Purchases", "Other expenses", "Profit before tax"],
        textposition = "outside",
        text = ["+60", "+80", "", "-40", "-20", "Total"],
        y = [60, 80, 0, -40, -20, 0],
        connector = {"line":{"color":"rgb(63, 63, 63)"}},
    ))

    fig.update_layout(
            title = "Profit and loss statement 2018",
            showlegend = True
    )

    fig.show()


    fig1 = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = 270,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Speed"}))

    fig1.show()

    fig2 = go.Figure(
        data=[go.Bar(y=[2, 1, 3])],
        layout_title_text="A Figure Displayed with the 'svg' Renderer"
    )
    fig2.show(renderer="svg")