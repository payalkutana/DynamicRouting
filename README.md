# DjangoDynamicUrlHandling

This project demonstrates dynamic URL handling based on region detection using GeoIP2. Follow the steps below to set up and run the project.

Installation and Setup

1. Install Python Libraries

Make sure you have all required Python libraries installed:

pip install -r requirements.txt

2. GDAL and GEOS Installation

Django's GeoIP2 depends on external libraries like GDAL and GEOS. Install them according to your operating system:

macOS:

brew install gdal

Ubuntu/Debian:

sudo apt-get install gdal-bin libgdal-dev

Running the Django Project

3. Start the Django Project

Navigate to the project directory:

cd DjangoDynamicUrlHandling

Run the development server:

python manage.py runserver

Accessing the Application

4. View the Home Page

Use the following URLs to access the home page based on region:

Region INDIA: http://localhost:8000/in/home

Region US: http://localhost:8000/us/home

Region UK: http://localhost:8000/uk/home

5. View the About Page

Use the following URLs to access the about page based on region:

Region INDIA: http://localhost:8000/in/about

Region US: http://localhost:8000/us/about

Region UK: http://localhost:8000/uk/about

Important Notes

6. Region Detection Logic

If the region code is not provided in the URL route, the middleware detects the user's region based on their IP address. The behavior is as follows:

If the detected region is us, uk, or in, the user is redirected to the corresponding region's route.

For all other regions, the user is redirected to the US site by default.

To test this functionality:

Use a VPN to simulate different IPs.

Alternatively, manually define an IP address in middleware.py for testing.

7. Assumptions

The region code must consist of 2 lowercase letters (e.g., in, us, uk).
