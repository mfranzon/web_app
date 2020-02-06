from flask import Flask, request, render_template, send_file
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/', methods=['GET','POST'])
def my_form_post():
    if request.method == 'POST':

        if (request.form.get('caso')=='1'):
            src = 'static/img/bias_exhaustive.png'
            return render_template('home.html', src=src)
        if (request.form.get('caso')=='2'):
            src = 'static/img/bias_not_info.png'
            return render_template('home.html', src=src)
        if (request.form.get('caso')=='3'):
            src = 'static/img/bias_info.png'
            return render_template('home.html', src=src)
        if (request.form.get('caso')=='4'):
            src = 'static/img/undersampling.png'
            return render_template('home.html', src=src)
        if (request.form.get('caso')=='5'):
            src = 'static/img/swap.png'
            return render_template('home.html', src=src)
        if (request.form.get('caso')=='6'):
            src = 'static/img/swap_1.png'
            return render_template('home.html', src=src)
        if (request.form.get('caso')=='7'):
            src = 'static/img/L1_L2.png'
            return render_template('home.html', src=src)
        if (request.form.get('caso')=='8'):
            src = 'static/img/L1_L2_sep_noise.png'
            return render_template('home.html', src=src)
        if (request.form.get('caso')=='9'):
            src = 'static/img/increase_non_info0.png'
            return render_template('home.html', src=src)
        if (request.form.get('caso')=='10'):
            src = 'static/img/increase_non_info1.png'
            return render_template('home.html', src=src)
        if (request.form.get('caso')=='12'):
            src = 'static/img/hiddenFalse0.png'
            return render_template('home.html', src=src)
        if (request.form.get('caso')=='13'):
            src = 'static/img/hiddenFalse1.png'
            return render_template('home.html', src=src)
        if (request.form.get('caso')=='14'):
            src = 'static/img/hiddenTrue0.png'
            return render_template('home.html', src=src)

    return ''


if __name__ == '__main__':
    app.run(debug=True)
