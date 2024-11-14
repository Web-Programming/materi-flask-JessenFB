from flask import Flask, render_tempalet,request,redirect,url_for
app=Flask(__name__)

@app.route('/contact',method={'GET','POST'})
def contact():
    if request.method == 'POST':
        name=request.form['name']
        email=request.form['email']
        message=request.form['message']
        print(f"Name :{name},Email :{email},Message {message}")
        return redirect(url_for('contact'))
    
    title = "Contact Page"
    return render_tempalet('contacts.html',title-title)




if __name__ =='__main__':
    app.run(debug=True)   