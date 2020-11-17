#!/usr/bin/env python
# coding: utf-8

# In[9]:


from flask import Flask, request, render_template
import pickle
app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))


# In[10]:


@app.route("/")
def home():
    return render_template('index.html')


# In[11]:


@app.route("/", methods = ["POST"])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    import numpy as np
    int_features = [int(x) for x in request.form.values()]
    if int_features[-1]==7011:
        int_features.append(1)
        int_features.append(0)
        int_features.append(0)
        int_features.append(0)
        int_features.append(0)
        final_features = [np.array(int_features)]
        prediction = model.predict(final_features)
        if prediction==0:
            output='no colar rápido'
        elif prediction==1:
            output='colar rapido'
    elif int_features[-1]==7023:
        int_features.append(0)
        int_features.append(1)
        int_features.append(0)
        int_features.append(0)
        int_features.append(0)
        final_features = [np.array(int_features)]
        prediction = model.predict(final_features)
        if prediction==0:
            output='no colar rápido'
        elif prediction==1:
            output='colar rapido'
    elif int_features[-1]==7026:
        int_features.append(0)
        int_features.append(0)
        int_features.append(1)
        int_features.append(0)
        int_features.append(0)
        final_features = [np.array(int_features)]
        prediction = model.predict(final_features)
        if prediction==0:
            output='no colar rápido'
        elif prediction==1:
            output='colar rapido'
    elif int_features[-1]==7907:
        int_features.append(0)
        int_features.append(0)
        int_features.append(0)
        int_features.append(1)
        int_features.append(0)
        final_features = [np.array(int_features)]
        prediction = model.predict(final_features)
        if prediction==0:
            output='no colar rápido'
        elif prediction==1:
            output='colar rapido'
    elif int_features[-1]==7910:
        int_features.append(0)
        int_features.append(0)
        int_features.append(0)
        int_features.append(0)
        int_features.append(1) 
        final_features = [np.array(int_features)]
        prediction = model.predict(final_features)
        if prediction==0:
            output='no colar rápido'
        elif prediction==1:
            output='colar rapido'
    else:
        output='no colar rapido. Grado no permitido para colado rapido'
    return render_template('index.html', prediction_text='Debería {}'.format(output))


# In[ ]:


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)


# In[ ]:




