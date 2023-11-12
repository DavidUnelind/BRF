import plotly.graph_objects as go

def generateGraphs(x):
    fig1 = go.Figure(go.Waterfall(
        name = "20", orientation = "v",
        measure = ["relative", "relative", "total", "relative", "relative", "total"],
        x = ["Sales", "Consulting", "Net revenue", "Purchases", "Other expenses", "Profit before tax"],
        textposition = "outside",
        text = [x*4, x*5, "", x*3, x*2, "Total"],
        y = [x*4, x*5, 0, -x*3, -x*2, 0],
        connector = {"line":{"color":"rgb(63, 63, 63)"}},
    ))

    fig1.update_layout(
            title = "Profit and loss statement 2018",
            showlegend = True
    )
    fig1.write_image("static/images/fig1.png")

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