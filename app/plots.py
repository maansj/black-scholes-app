import numpy as np
import plotly.graph_objects as go
from .bs_model import black_scholes_price

def intraday_plot(intraday_data, ticker):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=intraday_data.index,
        y=intraday_data['Close'],
        mode='lines+markers',
        name=f'{ticker} Intraday'
    ))
    fig.update_layout(title=f"Intraday Price Curve for {ticker}",
                      xaxis_title="Time", yaxis_title="Price")
    return fig

def sensitivity_rate(S, K, sigma, T, r_current):
    r_range = np.linspace(0, 0.1, 50)
    calls, puts = zip(*[black_scholes_price(S, K, r, sigma, T) for r in r_range])

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=r_range, y=calls, name="Call"))
    fig.add_trace(go.Scatter(x=r_range, y=puts, name="Put"))
    fig.add_vline(x=r_current, line=dict(color="red", dash="dash"))
    fig.update_layout(title="Option Price vs Interest Rate",
                      xaxis_title="Risk-free Rate",
                      yaxis_title="Price")
    return fig

def sensitivity_volatility(S, K, r, T, sigma_current):
    sigma_range = np.linspace(0.01, 1.0, 50)
    calls, puts = zip(*[
        black_scholes_price(S, K, r, sigma, T) for sigma in sigma_range
    ])

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=sigma_range, y=calls, name="Call"))
    fig.add_trace(go.Scatter(x=sigma_range, y=puts, name="Put"))
    fig.add_vline(x=sigma_current, line=dict(color="red", dash="dash"))
    fig.update_layout(title="Option Price vs Volatility",
                      xaxis_title="Volatility",
                      yaxis_title="Price")
    return fig

def sensitivity_maturity(S, K, r, sigma, T_current):
    T_range = np.linspace(0.01, 5.0, 50)
    calls, puts = zip(*[
        black_scholes_price(S, K, r, sigma, t) for t in T_range
    ])

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=T_range, y=calls, name="Call"))
    fig.add_trace(go.Scatter(x=T_range, y=puts, name="Put"))
    fig.add_vline(x=T_current, line=dict(color="red", dash="dash"))
    fig.update_layout(title="Option Price vs Time to Maturity",
                      xaxis_title="Years",
                      yaxis_title="Price")
    return fig
