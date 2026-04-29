FROM python:3.12-alpine
RUN pip install contourpy==1.1.0 & 
  pip install cycler==0.12.1 & 
  pip install et-xmlfile==1.1.0 & 
  pip install fonttools>=4.43.0 & 
  pip install graphviz==0.20.1 & 
  pip install Jinja2>=3.1.3 & 
  pip install kiwisolver==1.4.5 &
  pip install MarkupSafe==2.1.3 &
  pip install matplotlib==3.7.2 &
  pip install numpy==1.26.0 &
  pip install openpyxl==3.1.2 &
  pip install packaging==23.2 &
  pip install pandas==2.1.1 &
  pip install Pillow>=10.2.0 &
  pip install pyparsing<3.1.0and>=2.3.1 &
  pip install python-dateutil==2.8.2 &
  pip install pytz==2023.3 &
  pip install PyYAML==6.0.1 &
  pip install six==1.16.0
