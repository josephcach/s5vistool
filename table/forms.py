"""
@author: jcachaldora
forms.py - forms for searches
"""
from django import forms

#Filter by ranges form
class FilterForm(forms.Form):
        #min/max entries
        source_id = forms.CharField(required=False, widget=forms.TextInput(attrs={'class' : 'myfieldclass'}))
        ra_min = forms.FloatField(required=False)
        ra_max = forms.FloatField(required=False)
        dec_min = forms.FloatField(required=False)
        dec_max = forms.FloatField(required=False)
        vel_calib_min = forms.FloatField(required=False)
        vel_calib_max = forms.FloatField(required=False)
        vel_calib_std_min = forms.FloatField(required=False)
        vel_calib_std_max = forms.FloatField(required=False)
        feh50_min = forms.FloatField(required=False)
        feh50_max = forms.FloatField(required=False)
        logg50_min = forms.FloatField(required=False)
        logg50_max = forms.FloatField(required=False)
        teff50_min = forms.FloatField(required=False)
        teff50_max = forms.FloatField(required=False)
        sn_1700d_min = forms.FloatField(required=False)
        sn_1700d_max = forms.FloatField(required=False)
        utmjd_min = forms.FloatField(required=False)
        utmjd_max = forms.FloatField(required=False)
        parallax_min = forms.FloatField(required=False)
        parallax_max = forms.FloatField(required=False)
        phot_g_mean_mag_min = forms.FloatField(required=False)
        phot_g_mean_mag_max = forms.FloatField(required=False)
        pmra_min = forms.FloatField(required=False)
        pmra_max = forms.FloatField(required=False)
        pmdec_min = forms.FloatField(required=False)
        pmdec_max = forms.FloatField(required=False)
        starhorse_dist50_min = forms.FloatField(required=False)
        starhorse_dist50_max = forms.FloatField(required=False)
        decam_g_min = forms.FloatField(required=False)
        decam_g_max = forms.FloatField(required=False)
        decam_r_min = forms.FloatField(required=False)
        decam_r_max = forms.FloatField(required=False)
        priority_min = forms.IntegerField(required=False)
        priority_max = forms.IntegerField(required=False)
        qso_flag_wise = forms.IntegerField(required = False)
        primary = forms.BooleanField(required=False, widget = forms.CheckboxInput())
        good_star_pb_min = forms.FloatField(required=False)
        good_star_pb_max = forms.FloatField(required=False)
        
        #Results customization entries
        numresults = forms.IntegerField(required=False, initial = 10)
        displayplots = forms.BooleanField(required=False, widget=forms.CheckboxInput(), initial = True)
        
        #'use' entries
        use_ra = forms.BooleanField(required=False, widget=forms.CheckboxInput())
        use_dec = forms.BooleanField(required=False, widget=forms.CheckboxInput())
        use_vel_calib = forms.BooleanField(required=False, widget=forms.CheckboxInput())
        use_vel_calib_std = forms.BooleanField(required=False, widget=forms.CheckboxInput())
        use_feh50 = forms.BooleanField(required=False, widget=forms.CheckboxInput())
        use_logg50 = forms.BooleanField(required=False, widget=forms.CheckboxInput())
        use_teff50 = forms.BooleanField(required=False, widget=forms.CheckboxInput())
        use_sn_1700d = forms.BooleanField(required=False, widget=forms.CheckboxInput())
        use_utmjd = forms.BooleanField(required=False, widget=forms.CheckboxInput())
        use_parallax = forms.BooleanField(required=False, widget=forms.CheckboxInput())
        use_phot_g_mean_mag = forms.BooleanField(required=False, widget=forms.CheckboxInput())
        use_pmra = forms.BooleanField(required=False, widget=forms.CheckboxInput())
        use_pmdec = forms.BooleanField(required=False, widget=forms.CheckboxInput())
        use_starhorse_dist50 = forms.BooleanField(required=False, widget=forms.CheckboxInput())
        use_decam_g = forms.BooleanField(required=False, widget=forms.CheckboxInput())
        use_decam_r = forms.BooleanField(required=False, widget=forms.CheckboxInput())
        use_priority = forms.BooleanField(required=False, widget=forms.CheckboxInput())
        use_qso_flag_wise = forms.BooleanField(required=False, widget=forms.CheckboxInput())
        use_good_star_pb = forms.BooleanField(required=False, widget=forms.CheckboxInput())

#Search by ID form        
class SearchIDForm(forms.Form):
        source_id_search = forms.CharField(required=False, widget=forms.Textarea(attrs={"rows":30,"cols":50}))
        primary = forms.BooleanField(required=False, widget = forms.CheckboxInput())
        numresults = forms.IntegerField(required=False, initial = 10)
        displayplots = forms.BooleanField(required=False, widget=forms.CheckboxInput(), initial = True)

#Search by coordinates form
class SearchCoordForm(forms.Form):
        coord_search = forms.CharField(required=False, widget=forms.Textarea(attrs={"rows":30,"cols":50}))
        primary = forms.BooleanField(required=False, widget = forms.CheckboxInput())
        numresults = forms.IntegerField(required=False, initial = 10)
        displayplots = forms.BooleanField(required=False, widget=forms.CheckboxInput(), initial = True)