from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

model = joblib.load("psycometric.sav")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def result():
    a = float(request.form['a'])
    b = float(request.form['b'])
    c = float(request.form['c'])
    d = float(request.form['d'])
    e = float(request.form['e'])
    f = float(request.form['f'])
    g = float(request.form['g'])
    h = float(request.form['h'])
    i = float(request.form['i'])
    j = float(request.form['j'])
    k = float(request.form['k'])
    l = float(request.form['l'])
    m = float(request.form['m'])
    n = float(request.form['n'])
    o = float(request.form['o'])
    p = float(request.form['p'])
    q = float(request.form['q'])
    r = float(request.form['r'])
    s = float(request.form['s'])
    t = float(request.form['t'])
    u = float(request.form['u'])
    v = float(request.form['v'])
    w = float(request.form['w'])
    x = float(request.form['x'])
    y = float(request.form['y'])
    z = float(request.form['z'])
    A = float(request.form['A'])
    B = float(request.form['B'])
    C = float(request.form['C'])
    D = float(request.form['D'])
    E = float(request.form['E'])
    F = float(request.form['F'])
    G = float(request.form['G'])
    H = float(request.form['H'])
    I = float(request.form['I'])
    J = float(request.form['J'])
    K = float(request.form['K'])
    L = float(request.form['L'])
    M = float(request.form['M'])
    N = float(request.form['N'])
    O = float(request.form['O'])
    P = float(request.form['P'])
    Q = float(request.form['Q'])
    R = float(request.form['R'])
    S = float(request.form['S'])
    T = float(request.form['T'])
    U = float(request.form['U'])
    V = float(request.form['V'])
    W = float(request.form['W'])
    X = float(request.form['X'])
    
    pred = model.predict([[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X]])
    
    
    return render_template("index.html", result = pred[0])
   
    
    
    

if __name__ == '__main__':
    app.run()