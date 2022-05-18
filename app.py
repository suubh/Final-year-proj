import streamlit as st
st.set_page_config(layout="wide")
import streamlit.components.v1 as components
import os
from PIL import Image
import numpy as np
from keras.models import load_model

classes = { 0:'Speed limit (20km/h)',
            1:'Speed limit (30km/h)',
            2:'Speed limit (50km/h)',
            3:'Speed limit (60km/h)',
            4:'Speed limit (70km/h)',
            5:'Speed limit (80km/h)',
            6:'End of speed limit (80km/h)',
            7:'Speed limit (100km/h)',
            8:'Speed limit (120km/h)',
            9:'No passing',
            10:'No passing veh over 3.5 tons',
            11:'Right-of-way at intersection',
            12:'Priority road',
            13:'Yield',
            14:'Stop',
            15:'No vehicles',
            16:'Vehicle > 3.5 tons prohibited',
            17:'No entry',
            18:'General caution',
            19:'Dangerous curve left',
            20:'Dangerous curve right',
            21:'Double curve',
            22:'Bumpy road',
            23:'Slippery road',
            24:'Road narrows on the right',
            25:'Road work',
            26:'Traffic signals',
            27:'Pedestrians',
            28:'Children crossing',
            29:'Bicycles crossing',
            30:'Beware of ice/snow',
            31:'Wild animals crossing',
            32:'End speed + passing limits',
            33:'Turn right ahead',
            34:'Turn left ahead',
            35:'Ahead only',
            36:'Go straight or right',
            37:'Go straight or left',
            38:'Keep right',
            39:'Keep left',
            40:'Roundabout mandatory',
            41:'End of no passing',
            42:'End no passing vehicle > 3.5 tons' }

def image_processing(img):
    pass
    model = load_model('temp\\model\\TSR.h5')
    data=[]
    image = img.resize((30,30))
    data.append(np.array(image))
    Xtest = np.array(data)
    Ypred = model.predict_classes(Xtest)
    return Ypred


st.title('🚦Indian Traffic Sign Classification')
components.html(
    """
  <style>
    .intro{
      color:white;
      text-align:center;
      background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
      background-size: cover;
      padding-top: 200px;
      padding-bottom: 200px;  
      border-radius: 10px;
    }
  </style>
  <div class="intro">
    <p style="font-family:courier;"> <b>Traffic sign classification is the process of automatically recognizing traffic signs 
      along the road, including speed limit signs, yield signs, merge signs, etc. Being able to automatically recognize traffic
       signs enables us to build “smarter cars”.</b></p>
  </div>
    """,
    height=520
)

uploaded_file = st.file_uploader("Choose an Image", type=["png", "jpg", "jpeg"])
if uploaded_file is not None:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file)
    with open(os.path.join("uploads/",uploaded_file.name),"wb") as f: 
        f.write(uploaded_file.getbuffer())
    image = Image.open("uploads/"+uploaded_file.name)
    pred = image_processing(image)
    s = [str(i) for i in pred]
    a = int("".join(s))
    result = "Predicted Traffic🚦Sign is: " +classes[a]
    st.image(image, caption= result)

components.html(
    """
    <!DOCTYPE html>
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <title>Final Year Project</title>
    <link href="https://cdn.bootcss.com/bootstrap/4.0.0/css/bootstrap.min.css" rel="stylesheet"/>
    <style>
      body{
    /* background-image: url("../background1.jpg"); */
    font-family:courier;
    background-color: #0e1117;
    color:white;
  }
  .upload{
    padding-top: 10%;
    padding-bottom:10%;
    margin-top: 5%;
    margin-bottom: 5%;
    text-align: center;
    background-image: url('../slide_1.jpg');
    border-radius: 10px;
  }
  h2{
    font-size: 50px;
  }
  h1{
    text-align: center;
  }
  .service-6 {
font-family: "Montserrat", sans-serif;
color: #8d97ad;
font-weight: 300;
}

.service-6 h1, .service-6 h2, .service-6 h3, .service-6 h4, .service-6 h5, .service-6 h6 {
color: #3e4555;
}

.service-6 .font-weight-medium {
font-weight: 500;
}

.service-6 .subtitle {
color: #8d97ad;
line-height: 24px;
}

.service-6 a {
text-decoration: none;	
}

.service-6 .wrap-service6-box {
-webkit-transition: 0.2s ease-in;
-o-transition: 0.2s ease-in;
transition: 0.2s ease-in;
}

.service-6 .wrap-service6-box .card-body {
padding: 30px;
}

.service-6 .wrap-service6-box .card-body .linking {
color: #ffffff;
}

.service-6 .wrap-service6-box .card-body .linking:hover {
color: #263238;
}

.service-6 .wrap-service6-box .card-body p {
opacity: 0.8;
}

.service-6 .wrap-service6-box:hover {
-webkit-transform: scale(1.1);
-ms-transform: scale(1.1);
transform: scale(1.1);
}

.service-6 .bg-danger-gradiant {
  background: #ff4d7e;
background: -webkit-linear-gradient(legacy-direction(to right), #ff4d7e 0%, #ff6a5b 100%);
background: -webkit-gradient(linear, left top, right top, from(#ff4d7e), to(#ff6a5b));
background: -webkit-linear-gradient(left, #ff4d7e 0%, #ff6a5b 100%);
background: -o-linear-gradient(left, #ff4d7e 0%, #ff6a5b 100%);
background: linear-gradient(to right, #ff4d7e 0%, #ff6a5b 100%);
}

.service-6 .bg-info-gradiant {
    background: #188ef4;
background: -webkit-linear-gradient(legacy-direction(to right), #188ef4 0%, #316ce8 100%);
background: -webkit-gradient(linear, left top, right top, from(#188ef4), to(#316ce8));
background: -webkit-linear-gradient(left, #188ef4 0%, #316ce8 100%);
background: -o-linear-gradient(left, #188ef4 0%, #316ce8 100%);
background: linear-gradient(to right, #188ef4 0%, #316ce8 100%);
}

.service-6 .bg-success-gradiant {
  background: #2cdd9b;
background: -webkit-linear-gradient(legacy-direction(to right), #2cdd9b 0%, #1dc8cc 100%);
background: -webkit-gradient(linear, left top, right top, from(#2cdd9b), to(#1dc8cc));
background: -webkit-linear-gradient(left, #2cdd9b 0%, #1dc8cc 100%);
background: -o-linear-gradient(left, #2cdd9b 0%, #1dc8cc 100%);
background: linear-gradient(to right, #2cdd9b 0%, #1dc8cc 100%);
}

.service-6 .btn-outline-success {
    color: #2cdd9b !important;
background-color: transparent;
border-color: #2cdd9b !important;
}

.service-6 .btn-outline-success:hover {
  background: #2cdd9b;
border-color: #2cdd9b;
color: #ffffff !important;
}

.service-6 .btn-md {
padding: 15px 45px;
font-size: 16px;
}
.intro{
    margin: 0%;
    padding:0%;
    background-image: url('../slide_2.jpg');
    background-size: cover;
    text-align: center;
}
.intro p{
    /* margin: 10%; */
    padding:20%;
}
h5{
  color:white;
}
    </style>
  </head>

  <body>
    
        <h1>Scope and Upcoming Features</h1>
        <div class="py-5 service-6">
          <div class="container">
              <!-- Row  -->
              <div class="row">
                  <!-- Column -->
                  <div class="col-md-4 wrap-service6-box">
                      <div class="card border-0 bg-success-gradiant text-white mb-4">
                          <div class="card-body">
                              <h6 class="font-weight-medium text-white">ADAS</h6>
                              <p class="mt-3">Being able to automatically recognize traffic signs enables us to build “smarter cars”. Self-driving cars need traffic sign recognition in order to properly parse and understand the roadway</p>
                              <a href="#f4" class="linking">Learn More</a>
                          </div>
                      </div>
                  </div>
                  <!-- Column -->
                  <!-- Column -->
                  <div class="col-md-4 wrap-service6-box">
                      <div class="card border-0 bg-info-gradiant text-white mb-4">
                          <div class="card-body">
                              <h6 class="font-weight-medium text-white">Driver Alert</h6>
                              <p class="mt-3">Being able to automatically recognize traffic signs enables us to build “smarter cars”. Self-driving cars need traffic sign recognition in order to properly parse and understand the roadway</p>
                              <a href="#f4" class="linking">Learn More</a>
                          </div>
                      </div>
                  </div>
                  <!-- Column -->
                  <!-- Column -->
                  <div class="col-md-4 wrap-service6-box">
                      <div class="card border-0 bg-danger-gradiant text-white mb-4">
                          <div class="card-body">
                              <h6 class="font-weight-medium text-white">Real Time Detection</h6>
                              <p class="mt-3">Being able to automatically recognize traffic signs enables us to build “smarter cars”. Self-driving cars need traffic sign recognition in order to properly parse and understand the roadway</p>
                              <a href="#f4" class="linking">Learn More</a>
                          </div>
                      </div>
                  </div>
                  <!-- Column -->
                  <div class="col-md-12 mt-3 text-center">
                      <a class="btn btn-outline-success btn-md"><span>View Details</span></a>
                  </div>
              </div>
          </div>
      </div>
      <div id="team">
        <h1>Team Members</h1>

        <div class="container">
          <div class="row text-center">
      
              <!-- Team item -->
              <div class="col-xl-3 col-sm-6 mb-5">
                  <div class="bg-black rounded shadow-sm py-5 px-4"><img src="https://media-exp1.licdn.com/dms/image/C4D03AQGgsHstTUJ49g/profile-displayphoto-shrink_400_400/0/1609398956433?e=1656547200&v=beta&t=SWrdSj-9OLbOdVUhLak8w6Jf2b6HaOknTFnRKURqQxA" alt="" width="100" class="img-fluid rounded-circle mb-3 img-thumbnail shadow-sm">
                      <h5 class="mb-0">Anurag Anand</h5><span class="small text-uppercase text-muted">CSE/18/27</span>
                      
                  </div>
              </div><!-- End -->
      
              <!-- Team item -->
              <div class="col-xl-3 col-sm-6 mb-5">
                  <div class="bg-black rounded shadow-sm py-5 px-4"><img src="https://media-exp1.licdn.com/dms/image/C5603AQEhdnVlUyhX4g/profile-displayphoto-shrink_400_400/0/1651610938884?e=1658361600&v=beta&t=pZoYr5YDSxuj8ubyAQbpwkdNXyMOnFiC5FOfAIj9bYQ" alt="" width="100" class="img-fluid rounded-circle mb-3 img-thumbnail shadow-sm">
                      <h5 class="mb-0">Sarthak Gupta</h5><span class="small text-uppercase text-muted">CSE/18/28</span>
                      
                  </div>
              </div><!-- End -->
      
              <!-- Team item -->
              <div class="col-xl-3 col-sm-6 mb-5">
                  <div class="bg-black rounded shadow-sm py-5 px-4"><img src="https://media-exp1.licdn.com/dms/image/C4E03AQHVi0VqQf9JsA/profile-displayphoto-shrink_400_400/0/1597560844744?e=1656547200&v=beta&t=3cPNizzj-tjDmwKHIzcdVqi0W6Age1pHECNbpEj9hRo" alt="" width="100" class="img-fluid rounded-circle mb-3 img-thumbnail shadow-sm">
                      <h5 class="mb-0">Shubham Singh</h5><span class="small text-uppercase text-muted">CSE/18/29</span>
                     
                  </div>
              </div><!-- End -->
      
              <!-- Team item -->
              <div class="col-xl-3 col-sm-6 mb-5">
                  <div class="bg-black rounded shadow-sm py-5 px-4"><img src="https://media-exp1.licdn.com/dms/image/C4E03AQEPAEzQCEy96g/profile-displayphoto-shrink_400_400/0/1596619182270?e=1656547200&v=beta&t=A8oeGHvx2tF4SrGSosZszXrVgKCkFZytLx7wW4vbmMA" alt="" width="100" class="img-fluid rounded-circle mb-3 img-thumbnail shadow-sm">
                      <h5 class="mb-0">Dhiren Sorathiya</h5><span class="small text-uppercase text-muted">CSE/18/30</span>
                      
                  </div>
              </div><!-- End -->
          </div>
      </div>
      </div>
    </div>
  </body>
  </html>
    """,
    height=2500,
)