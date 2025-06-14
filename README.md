Rent House system 

if  want  to use the pdf function need to follow this step

You can just go to the payment page to try the pdf function
example: http://127.0.0.1/Login/payment/

make sure to follow your own urls this is just my own example


PDF Export Feature – Requirements & Setup
To enable the PDF export functionality for the receipt in this Django project, follow these steps:

1. Install wkhtmltopdf
Download from the official site:
https://wkhtmltopdf.org/downloads.html

Choose the Windows 64-bit installer (MSVC) version.

Install it to the default path (C:\Program Files\wkhtmltopdf).

2. Add wkhtmltopdf to Windows PATH
To allow Django to access wkhtmltopdf:

Open Start > search for "Environment Variables" > open "Edit the system environment variables"

Click "Environment Variables…"

Under System Variables, find Path, and click Edit

Click New and add:

makefile

C:\Program Files\wkhtmltopdf\bin
Click OK on all dialogs

Restart your terminal or IDE

3. Install pdfkit Python library
In your Django environment, run:

pip install pdfkit
4. Install Jinja2 template support (optional but recommended)
If you encounter template issues, also run:

pip install Jinja2
5. Verify Setup
Test in CMD or terminal:

wkhtmltopdf --version
If it returns a version number (like wkhtmltopdf 0.12.6), it's working.

6. Ready to Use
Now you can use the Export as PDF function in your Django app.

Make sure your views.py includes logic that uses pdfkit.from_string(...) and a valid HTML template.

