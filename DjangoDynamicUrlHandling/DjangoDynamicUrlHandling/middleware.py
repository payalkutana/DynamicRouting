from django.http import HttpResponseRedirect
from django.contrib.gis.geoip2 import GeoIP2


class HandleRouteMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        resolver_match = request.resolver_match
        if resolver_match:
            # Extract route variables (kwargs)
            region = resolver_match.kwargs.get('region')
            
            # If region is not provided, detect based on IP and redirect
            if region is None:
                region_prefix = self.detect_region_from_ip(request)
                if 'home' in resolver_match.route:
                    redirect_path = f'/{region_prefix}/home'
                elif 'about' in resolver_match.route:
                    redirect_path = f'/{region_prefix}/about'
                else:
                    redirect_path = None
                if redirect_path:
                    return HttpResponseRedirect(redirect_path)

    def detect_region_from_ip(self, request):
        """Detect user's region based on IP address."""
        ip_address = self.get_client_ip(request)
        geoip = GeoIP2()
        default_region = 'us'
        country_region_map = {
            'United States': 'us',
            'United Kingdom': 'uk',
            'India': 'in',
        }
        try:
            country = geoip.country(ip_address).get('country_name', '')
            return country_region_map.get(country, default_region)
        except Exception as e:
            print("GeoIP Error:", str(e))
            return default_region

    @staticmethod
    def get_client_ip(request):
        """Retrieve the client IP address from the request."""
        if request.META.get('HTTP_X_FORWARDED_FOR'):
            ip = request.META.get('HTTP_X_FORWARDED_FOR').split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

        # Sample IP Address
        # ip = '14.96.0.0' #India IP
        # ip = '51.141.28.0' #UK IP
        # ip = '103.255.255.0 #Hong Kong IP