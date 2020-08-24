"""
@author: jcachaldora
views.py - Defines urls with /table/ base 
"""
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from .models import Spectrum
from .forms import FilterForm
from .forms import SearchIDForm
from.forms import SearchCoordForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from astropy.coordinates import SkyCoord
from astropy import units as u
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components
from bokeh.models import HoverTool
import pyfits
from os import path


#Spectra Index Table View
def IndexView(request):
    spectra_list = Spectrum.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(spectra_list, 50)
    
    try:
        spectra = paginator.page(page)
    except PageNotAnInteger:
        spectra = paginator.page(1)
    except EmptyPage:
        spectra = paginator.page(paginator.num_pages)
        
    context = {'spectra' : spectra}
        
    return render(request, "table.html", context)

#Filter Form View
def FilterView(request):
    if request.method == 'POST':
        form = FilterForm(request.POST)
        if form.is_valid():
            #Store min/max form data
            request.session['ra_min'] = form.cleaned_data['ra_min']
            request.session['ra_max'] = form.cleaned_data['ra_max']
            request.session['dec_min'] = form.cleaned_data['dec_min']
            request.session['dec_max'] = form.cleaned_data['dec_max']
            request.session['vel_calib_min'] = form.cleaned_data['vel_calib_min']
            request.session['vel_calib_max'] = form.cleaned_data['vel_calib_max']            
            request.session['vel_calib_std_min'] = form.cleaned_data['vel_calib_std_min']
            request.session['vel_calib_std_max'] = form.cleaned_data['vel_calib_std_max']
            request.session['feh50_min'] = form.cleaned_data['feh50_min']
            request.session['feh50_max'] = form.cleaned_data['feh50_max']
            request.session['logg50_min'] = form.cleaned_data['logg50_min']
            request.session['logg50_max'] = form.cleaned_data['logg50_max']
            request.session['teff50_min'] = form.cleaned_data['teff50_min']
            request.session['teff50_max'] = form.cleaned_data['teff50_max']
            request.session['sn_1700d_min'] = form.cleaned_data['sn_1700d_min']
            request.session['sn_1700d_max'] = form.cleaned_data['sn_1700d_max']
            request.session['utmjd_min'] = form.cleaned_data['utmjd_min']
            request.session['utmjd_max'] = form.cleaned_data['utmjd_max']
            request.session['parallax_min'] = form.cleaned_data['parallax_min']
            request.session['parallax_max'] = form.cleaned_data['parallax_max']
            request.session['phot_g_mean_mag_min'] = form.cleaned_data['phot_g_mean_mag_min']
            request.session['phot_g_mean_mag_max'] = form.cleaned_data['phot_g_mean_mag_max']
            request.session['pmra_min'] = form.cleaned_data['pmra_min']
            request.session['pmra_max'] = form.cleaned_data['pmra_max']
            request.session['pmdec_min'] = form.cleaned_data['pmdec_min']
            request.session['pmdec_max'] = form.cleaned_data['pmdec_max']
            request.session['starhorse_dist50_min'] = form.cleaned_data['starhorse_dist50_min']
            request.session['starhorse_dist50_max'] = form.cleaned_data['starhorse_dist50_max']
            request.session['decam_g_min'] = form.cleaned_data['decam_g_min']
            request.session['decam_g_max'] = form.cleaned_data['decam_g_max']
            request.session['decam_r_min'] = form.cleaned_data['decam_r_min']
            request.session['decam_r_max'] = form.cleaned_data['decam_r_max']
            request.session['priority_min'] = form.cleaned_data['priority_min']
            request.session['priority_max'] = form.cleaned_data['priority_max']
            request.session['qso_flag_wise'] = form.cleaned_data['qso_flag_wise']
            request.session['primary'] = form.cleaned_data['primary']
            request.session['good_star_pb_min'] = form.cleaned_data['good_star_pb_min']
            request.session['good_star_pb_max'] = form.cleaned_data['good_star_pb_max']
            
            #Store boolean 'Use' form data
            request.session['use_ra'] = form.cleaned_data['use_ra']
            request.session['use_dec'] = form.cleaned_data['use_dec']
            request.session['use_vel_calib'] = form.cleaned_data['use_vel_calib']
            request.session['use_vel_calib_std'] = form.cleaned_data['use_vel_calib_std']
            request.session['use_feh50'] = form.cleaned_data['use_feh50']
            request.session['use_logg50'] = form.cleaned_data['use_logg50']
            request.session['use_teff50'] = form.cleaned_data['use_teff50']
            request.session['use_sn_1700d'] = form.cleaned_data['use_sn_1700d']
            request.session['use_utmjd'] = form.cleaned_data['use_utmjd']
            request.session['use_parallax'] = form.cleaned_data['use_parallax']
            request.session['use_phot_g_mean_mag'] = form.cleaned_data['use_phot_g_mean_mag']
            request.session['use_pmra'] = form.cleaned_data['use_pmra']
            request.session['use_pmdec'] = form.cleaned_data['use_pmdec']
            request.session['use_starhorse_dist50'] = form.cleaned_data['use_starhorse_dist50']
            request.session['use_decam_g'] = form.cleaned_data['use_decam_g']
            request.session['use_decam_r'] = form.cleaned_data['use_decam_r']
            request.session['use_priority'] = form.cleaned_data['use_priority']
            request.session['use_good_star_pb'] = form.cleaned_data['use_good_star_pb']
        
            #Store Customization Data
            request.session['numresults'] = form.cleaned_data['numresults']
            request.session['displayplots'] = form.cleaned_data['displayplots']
            return HttpResponseRedirect('/table/results/')
    else:
        form = FilterForm()
    
        return render(request, "spectrumfilter.html", {'form' : form})

#ID Search View        
def SearchView(request):
 if request.method == 'POST':
        form = SearchIDForm(request.POST)
        if form.is_valid():
            idlist = (form.cleaned_data['source_id_search']).split()
            request.session['idlist'] = idlist
            request.session['numresults'] = form.cleaned_data['numresults']
            request.session['displayplots'] = form.cleaned_data['displayplots']
            return HttpResponseRedirect('/table/searchresults/')
    
 else:
    form = SearchIDForm()
    return render(request, "searchby.html", {'form' : form})

#Coordinate Search View
def SearchCoordView(request):
    if request.method == 'POST':
        form = SearchCoordForm(request.POST)
        if form.is_valid():
            data = list(Spectrum.objects.values_list('ra','dec'))
            radata, decdata = zip(*data)
            iddata = list(Spectrum.objects.values_list('source_id'))
            coordlist = (form.cleaned_data['coord_search']).split()
            request.session['numresults'] = form.cleaned_data['numresults']
            request.session['displayplots'] = form.cleaned_data['displayplots']
            rainputlist = []
            decinputlist = []
            isRA=True
            for coord in coordlist:
                if(isRA):
                    rainputlist.append(float(coord))
                    isRA=False
                else:
                    decinputlist.append(float(coord))
                    isRA=True
            coordinput = SkyCoord(ra=rainputlist*u.degree, dec=decinputlist*u.degree)
            coorddata = SkyCoord(ra=radata*u.degree, dec=decdata*u.degree)      
            match, d2d, d3d = coordinput.match_to_catalog_sky(coorddata)
            
            idlist = []
            for i in range (0,len(match)):
                if (d2d[i] < 1*u.arcsec):
                        idlist.append(iddata[match[i]][0])
            request.session['idlist'] = idlist
            return HttpResponseRedirect('/table/searchresults/')
    else:
         form = SearchCoordForm()
         return render(request, "searchbycoord.html", {'form' : form})
                
#ID Search/Coordinate Search results view
def SearchResultsView(request):
 idlist = request.session['idlist']
 spectra = []
 for ID in idlist:
     if(Spectrum.objects.filter(source_id=ID).count() != 0):
         for spectrum in Spectrum.objects.filter(source_id=ID):
            if(spectrum not in spectra):
             spectra.append(spectrum)
 
 page = request.GET.get('page', 1)
 if(request.session['numresults'] == None):
     request.session['numresults'] = 10 
 paginator = Paginator(spectra, request.session['numresults'])
 spectra = list(spectra)
 try:
        spectra_result = paginator.page(page)
 except PageNotAnInteger:
        spectra_result = paginator.page(1)
 except EmptyPage:
        spectra_result = paginator.page(paginator.num_pages)
 context = {'spectra_result' : spectra_result}
 context["size"] = len(spectra)
 if(request.session['displayplots']==True):
     return render(request, "results.html", context)
 else:
     return render(request, "plotlessresults.html", context)     

#Filter Form results view
def ResultsView(request):
 spectra = Spectrum.objects.all()
 if(request.session['use_ra']):
    if(request.session['ra_min'] != None):
        spectra = spectra.filter(ra__gte = request.session['ra_min'] )
    if(request.session['ra_max'] != None):
        spectra = spectra.filter(ra__lte = request.session['ra_max'])
 if(request.session['use_dec']):
    if(request.session['dec_min'] != None):
        spectra =  spectra.filter(dec__gte = request.session['dec_min'])
    if(request.session['dec_max'] != None):
        spectra = spectra.filter(dec__lte =  request.session['dec_max'])
 if(request.session['use_vel_calib']):
    if(request.session['vel_calib_min'] != None):
        spectra = spectra.filter(vel_calib__gte = request.session['vel_calib_min'])
    if(request.session['vel_calib_max'] != None):
        spectra = spectra.filter(vel_calib__lte = request.session['vel_calib_max'])
 if(request.session['use_vel_calib_std']):
    if(request.session['vel_calib_std_min'] != None):
        spectra = spectra.filter(vel_calib_std__gte = request.session['vel_calib_std_min'])
    if(request.session['vel_calib_std_max'] != None):
        spectra = spectra.filter(vel_calib_std__lte = request.session['vel_calib_std_max'])
 if(request.session['use_feh50']):
    if(request.session['feh50_min'] != None):
        spectra = spectra.filter(feh50__gte = request.session['feh50_min'])
    if(request.session['feh50_max'] != None):
        spectra = spectra.filter(feh50__lte = request.session['feh50_max'])
 if(request.session['use_logg50']):
    if(request.session['logg50_min'] != None):
        spectra = spectra.filter(logg50_gte = request.session['logg50_min'])
    if(request.session['logg50_max'] != None):
        spectra = spectra.filter(logg50_lte = request.session['logg50_max'])
 if(request.session['use_teff50']):
    if(request.session['teff50_min'] != None):
        spectra = spectra.filter(teff50_gte = request.session['teff50_min'])
    if(request.session['teff50_max'] != None):
        spectra = spectra.filter(teff50_lte = request.session['teff50_max'])
 if(request.session['use_sn_1700d']):
    if(request.session['sn_1700d_min'] != None):
        spectra = spectra.filter(sn_1700d__gte = request.session['sn_1700d_min'])
    if(request.session['sn_1700d_max'] != None):
        spectra = spectra.filter(sn_1700d__lte = request.session['sn_1700d_max'])
 if(request.session['use_utmjd']):
    if(request.session['utmjd_min'] != None):
        spectra = spectra.filter(utmjd__gte = request.session['utmjd_min'])
    if(request.session['utmjd_max'] != None):
        spectra = spectra.filter(utmjd__lte = request.session['umtjd_max'])
 if(request.session['use_parallax']):
    if(request.session['parallax_min'] != None):
        spectra = spectra.filter(parallax__gte = request.session['parallax_min'])
    if(request.session['parallax_max'] != None):
        spectra = spectra.filter(parallax__lte = request.session['parallax_max'])
 if(request.session['use_phot_g_mean_mag']):
    if(request.session['phot_g_mean_mag_min'] != None):
        spectra = spectra.filter(phot_g_mean_mag__gte = request.session['phot_g_mean_mag_min'])
    if(request.session['phot_g_mean_mag_max'] != None):
        spectra = spectra.filter(phot_g_mean_mag__lte = request.session['phot_g_mean_mag_max'])
 if(request.session['use_pmra']):
    if(request.session['pmra_min'] != None):
        spectra = spectra.filter(pmra__gte = request.session['pmra_min'])
    if(request.session['pmra_max'] != None):
        spectra = spectra.filter(pmra__lte = request.session['pmra_max'])
 if(request.session['use_pmdec']):
    if(request.session['pmdec_min'] != None):
        spectra = spectra.filter(pmdec__gte = request.session['pmdec_min'])
    if(request.session['pmdec_max'] != None):
        spectra = spectra.filter(pmdec__lte = request.session['pmdec_max'])
 if(request.session['use_starhorse_dist50']):
    if(request.session['starhorse_dist50_min'] != None):
        spectra = spectra.filter(starhorse_dist50__gte = request.session['starhorse_dist50_min'])
    if(request.session['starhorse_dist50_max'] != None):
        spectra = spectra.filter(starhorse_dist50__lte = request.session['starhorse_dist50_max'])
 if(request.session['use_decam_g']):
    if(request.session['decam_g_min'] != None):
        spectra = spectra.filter(decam_g__gte = request.session['decam_g_min'])
    if(request.session['decam_g_max'] != None):
        spectra = spectra.filter(decam_g__lte = request.session['decam_g_max'])
 if(request.session['use_decam_r']):
    if(request.session['decam_r_min'] != None):
        spectra = spectra.filter(decam_r__gte = request.session['decam_r_min'])
    if(request.session['decam_r_max'] != None):
        spectra = spectra.filter(decam_r__lte = request.session['decam_r_max'])
 if(request.session['use_priority']):
    if(request.session['priority_min'] != None):
        spectra = spectra.filter(priority__gte = request.session['priority_min'])
    if(request.session['priority_max'] != None):
        spectra = spectra.filter(priority__lte = request.session['priority_max'])
 if(request.session['use_good_star_pb']):
    if(request.session['good_star_pb_min'] != None):
        spectra = spectra.filter(good_star_pb__gte = request.session['good_star_pb_min'])
    if(request.session['good_star_pb_max'] != None):
        spectra = spectra.filter(good_star_pb__lte = request.session['good_star_pb_max'])
 if(request.session['primary'] == True):
    spectra = spectra.filter(primary = True)
 page = request.GET.get('page', 1)
 if(request.session['numresults'] == None):
     request.session['numresults'] = 10 
 paginator = Paginator(spectra, request.session['numresults'])
 spectra = list(spectra)
    
 try:
        spectra_result = paginator.page(page)
 except PageNotAnInteger:
        spectra_result = paginator.page(1)
 except EmptyPage:
        spectra_result = paginator.page(paginator.num_pages)
 context = {'spectra_result' : spectra_result}
 context['size'] = len(spectra)
 if(request.session['displayplots']==True):
     return render(request, "results.html", context)
 else:
     return render(request, "plotlessresults.html", context)

#Spectra Profile View
def DetailView(request, source_id):
    spectrum = Spectrum.objects.filter(primary=True).get(source_id=source_id)
    if (path.exists('table/plotdata/specs_r_'+source_id+'.fits')):
        dd = pyfits.open('table/plotdata/specs_r_'+source_id+'.fits')[0].data
        TOOLTIPS = [
            ("(x,y)", "($x, $y)")]
        p = figure(plot_width=900, plot_height=550, tools="hover,pan,xwheel_zoom,reset,save,box_zoom", toolbar_location="below", title=spectrum.field+" - "+source_id, tooltips=TOOLTIPS)
        p.title.align="center"
        p.title.text_font_size='18pt'
        p.xaxis.axis_label="Wavelength"
        p.yaxis.axis_label="Flux"
        p.line(dd[0], dd[1], line_width=2)
        p.line(dd[0], dd[3], line_width=2, line_color="red")
        script, div = components(p)
        context = {
        "spectrum":spectrum, "script":script, "div":div
        }
        return render(request, "detail.html", context)
    else:
        return render(request, "detail.html", {"spectrum":spectrum})

def TestView(request):
    dd = pyfits.open('table/plotdata/specs_r_5017995357763954944.fits')[0].data
    p = figure(plot_width=900, plot_height=650)
    p.line(dd[0], dd[1], line_width=2)
    p.line(dd[0], dd[3], line_width=2, line_color="red")
    script, div = components(p)
    return render(request, 'test.html', {'script':script,'div':div})