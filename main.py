import pandas as pd
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():
    df = pd.DataFrame(
        columns=[
            "Month",
            "Principle Amount",
            "Starting Balance",
            "Interest Amount",
            "End Balance",
        ]
    )
    if request.method == "POST":
        p = float(request.form.get("principle_amount"))  # 1_000 Principal Amount of SIP
        sb = p  # Starting Balance (Calculation purpose)
        I = float(float(request.form.get("interest_rate")) / 100)  # Rate of interest
        I_amount = 0  # Interest Amount (Calculation purpose)
        eb = 0  # Estimate Balance (Calculation purpose)
        tt = int(request.form.get("tenure")) * 12  # Tenure (Year)
        for i in range(1, tt + 1):
            sb = p * i + I_amount
            I_amount = sb * I
            eb = sb + I_amount
            # a=[f'{p*i:,.2f}' , f'{sb:,.2f}' , f'{I_amount:,.2f}' , f'{eb:,.2f}']
            # df=df.append([ f'{p*i:,.2f}' , f'{sb:,.2f}' , f'{I_amount:,.2f}' , f'{eb:,.2f}'])
            a = {
                df.columns[1]: f"{p*i:,.2f}",
                df.columns[2]: f"{sb:,.2f}",
                df.columns[3]: f"{I_amount:,.2f}",
                df.columns[4]: f"{eb:,.2f}",
            }
            # df = df.append(a, ignore_index=True)
            df.loc[len(df.index)] = a
            df["Month"] = df.index + 1
    return render_template(
        "index.html",
        data=df.to_html(classes="container mt-5 table table-bordered", index=False),
        dl=len(df),
    )


if __name__ == "__main__":
    app.run()
